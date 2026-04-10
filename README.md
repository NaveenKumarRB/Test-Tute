# Flask MongoDB Application

A complete Flask application demonstrating CRUD operations with MongoDB Atlas integration.

## Features

- **Form Submission**: Web form to submit name, email, and message
- **API Route**: `/api` endpoint returns JSON data from data.json
- **MongoDB Integration**: Stores form submissions in MongoDB Atlas
- **Responsive Design**: Beautiful and responsive UI

## Project Structure

```
flask-mongodb-app/
├── app.py                    # Main Flask application
├── data.json                 # Sample JSON data for /api route
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (MONGO_URI, SECRET_KEY)
└── templates/
    ├── form.html            # Contact form template
    └── success.html         # Success page template
```

## Installation

1. Clone the repository:
```bash
git clone git@github.com:NaveenKumarRB/Test-Tute.git
cd flask-mongodb-app
```

2. Create a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables in `.env`:
```
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/flask_demo
SECRET_KEY=your-secret-key
FLASK_DEBUG=False
```

5. Run the application:
```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

## API Routes

- `GET /` - Display submission form
- `POST /` - Submit form data to MongoDB
- `GET /api` - Get JSON data from data.json
- `GET /success` - Display success message

## Technologies

- Flask
- MongoDB Atlas
- Python-dotenv
- Jinja2 Templates
- HTML5 & CSS3

## Author

Naveen Kumar
