import json
import os
from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "fallback-secret-key")

# ─────────────────────────────────────────────
# MongoDB Atlas Connection
# ─────────────────────────────────────────────
MONGO_URI = os.getenv("MONGO_URI", "")

def get_db():
    """Return MongoDB database instance."""
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    db = client["flask_demo"]
    return db


# ─────────────────────────────────────────────
# Route 1: /api — Read from data.json and return JSON list
# ─────────────────────────────────────────────
@app.route("/api", methods=["GET"])
def get_data():
    """Read data from data.json and return as JSON response."""
    data_file = os.path.join(os.path.dirname(__file__), "data.json")
    try:
        with open(data_file, "r") as f:
            data = json.load(f)
        return jsonify({
            "status": "success",
            "count": len(data),
            "data": data
        }), 200
    except FileNotFoundError:
        return jsonify({"status": "error", "message": "Data file not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"status": "error", "message": "Invalid JSON in data file"}), 500


# ─────────────────────────────────────────────
# Route 2: / — Home page with submission form
# ─────────────────────────────────────────────
@app.route("/", methods=["GET", "POST"])
def index():
    """Display form; on POST insert data into MongoDB Atlas."""
    error = None

    if request.method == "POST":
        name  = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        # Basic validation
        if not name or not email or not message:
            error = "All fields are required. Please fill in every field."
            return render_template("form.html", error=error)

        try:
            db = get_db()
            collection = db["submissions"]
            document = {
                "name": name,
                "email": email,
                "message": message,
                "submitted_at": datetime.utcnow()
            }
            result = collection.insert_one(document)

            if result.inserted_id:
                # Redirect to success page
                return redirect(url_for("success"))
            else:
                error = "Insertion failed: no ID returned from MongoDB."

        except ConnectionFailure:
            error = "Could not connect to MongoDB Atlas. Check your MONGO_URI in .env."
        except OperationFailure as e:
            error = f"MongoDB operation failed: {str(e)}"
        except Exception as e:
            error = f"An unexpected error occurred: {str(e)}"

        return render_template("form.html", error=error)

    # GET request — show empty form
    return render_template("form.html", error=None)


# ─────────────────────────────────────────────
# Route 3: /success — Shown after successful submission
# ─────────────────────────────────────────────
@app.route("/success")
def success():
    """Display success message after form submission."""
    return render_template("success.html")


# ─────────────────────────────────────────────
# Route 4: /submittodoitem — Accept and store To-Do items
# ─────────────────────────────────────────────
@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    """Accept itemName and itemDescription via POST and store in MongoDB."""
    try:
        item_name = request.form.get("itemName", "").strip()
        item_description = request.form.get("itemDescription", "").strip()

        # Basic validation
        if not item_name or not item_description:
            return jsonify({
                "status": "error",
                "message": "Both itemName and itemDescription are required."
            }), 400

        db = get_db()
        collection = db["todo_items"]
        
        document = {
            "itemName": item_name,
            "itemDescription": item_description,
            "created_at": datetime.utcnow(),
            "completed": False
        }
        
        result = collection.insert_one(document)
        
        if result.inserted_id:
            return jsonify({
                "status": "success",
                "message": "To-Do item added successfully",
                "id": str(result.inserted_id)
            }), 201
        else:
            return jsonify({
                "status": "error",
                "message": "Failed to insert item"
            }), 500

    except ConnectionFailure:
        return jsonify({
            "status": "error",
            "message": "Could not connect to MongoDB"
        }), 500
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"An unexpected error occurred: {str(e)}"
        }), 500


if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG", "False") == "True", port=5000)