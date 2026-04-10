# Flask MongoDB Application - Git Workflow Documentation

**GitHub Repository:** https://github.com/NaveenKumarRB/Test-Tute.git

## Overview

This document details the complete Git workflow implementation for a Flask MongoDB application, including branch management, feature development, merging, rebasing, and version control best practices.

---

## Part 1: SSH Configuration & Repository Setup

### Step 1: SSH Key Generation

SSH keys were generated for secure GitHub authentication:

```powershell
ssh-keygen -t rsa -b 4096 -f "$env:USERPROFILE\.ssh\id_rsa" -P '""'
```

**Output:**
```
Generating public/private rsa key pair.
Your identification has been saved in C:\Users\navee\.ssh\id_rsa
Your public key has been saved in C:\Users\navee\.ssh\id_rsa.pub
The key fingerprint is:
SHA256:MONQHKf7IF0sswGg9vCVxsL+a9WkJnl1I58kitNfRTo navee@Naveen_Gowda
```

**SSH Public Key:**
```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCU/JG0eGYPnloDb4HZJQDjrUo...
```

### Step 2: Git Configuration

```powershell
git config --global user.name "Naveen"
git config --global user.email "naveen@example.com"
```

### Step 3: Remote Setup

```powershell
git remote set-url origin git@github.com:NaveenKumarRB/Test-Tute.git
```

---

## Part 2: Feature Branch Workflow

### Step 2-3: Creating and Merging Naveen Branch

**Branch Creation:**
```powershell
git checkout -b Naveen
```

**Added README.md with project documentation**

**Commit & Merge:**
```powershell
git add README.md
git commit -m "Add comprehensive README documentation"
git checkout main
git merge Naveen
```

**Result:** README successfully merged to main branch

---

## Part 3: JSON Data Updates in Naveen_new Branch

**Branch Creation:**
```powershell
git checkout -b Naveen_new
```

**Updated data.json** - Added 3 new employee records:
- Naveen Kumar (DevOps Engineer)
- Sophia Chen (Backend Developer)
- Amit Singh (Frontend Developer)

**Files Modified:** `data.json` (added 21 lines)

**Commit & Merge:**
```powershell
git add data.json
git commit -m "Update data.json with new employee records"
git checkout main
git merge Naveen_new
```

---

## Part 4: Parallel Development - master_1 & master_2 Branches

### Master_1: Frontend To-Do Form Development

**Branch Creation:**
```powershell
git checkout -b master_1
```

**Created templates/todo.html** with:
- Responsive UI design
- Initial form fields: Item Name, Item Description

**Commit:**
```powershell
git add templates/todo.html
git commit -m "Add To-Do form template with Item Name and Item Description fields"
```

### Master_2: Backend API Development

**Branch Creation:**
```powershell
git checkout -b master_2
```

**Added `/submittodoitem` route** in app.py:
- Accepts POST requests with itemName and itemDescription
- Stores data in MongoDB database
- Returns JSON responses with status and item ID
- Handles connection and operation errors

**Commit:**
```powershell
git add app.py
git commit -m "Add /submittodoitem route to accept and store To-Do items in MongoDB"
```

---

## Part 5: Merging Parallel Branches

### Merge Master_1 to Main

```powershell
git checkout main
git merge master_1
```

**Result:** Fast-forward merge of To-Do form

### Merge Master_2 to Main

```powershell
git merge master_2
```

**Result:** Successfully merged /submittodoitem route

---

## Part 6: Sequential Field Additions in master_1

### First Commit: Add Item ID Field

```powershell
git checkout master_1
# Modified templates/todo.html
git add templates/todo.html
git commit -m "Add Item ID field to To-Do form"
```

**Commit Hash:** 6f48315

### Second Commit: Add Item UUID Field

```powershell
# Modified templates/todo.html
git add templates/todo.html
git commit -m "Add Item UUID field to To-Do form"
```

**Commit Hash:** b6c88d1

### Third Commit: Add Item Hash Field

```powershell
# Modified templates/todo.html
git add templates/todo.html
git commit -m "Add Item Hash field to To-Do form"
```

**Commit Hash:** 1a59589

**Commit History:**
```
1a59589 Add Item Hash field to To-Do form
b6c88d1 Add Item UUID field to To-Do form
6f48315 Add Item ID field to To-Do form
f74f8ab Add To-Do form template with Item Name and Item Description fields
```

---

## Part 7: Git Reset and Re-commit

### Reset to Item ID State

```powershell
git checkout main
git merge master_1  # Brings in all 3 field commits

# Reset to Item ID commit using --soft flag
git reset --soft 6f48315
```

**Output:**
```
On branch main
Changes to be committed:
  modified:   app.py
  modified:   templates/todo.html
```

### Unstage and Re-commit

```powershell
git reset
git add -A
git commit -m "Restate form with Item ID, UUID, and Hash fields updated"
```

**Result:** New consolidated commit containing all changes

---

## Part 8: Rebase Operation

### Rebase master_1 onto Updated main

```powershell
git rebase main master_1
```

**Conflict Resolution:** Resolved merge conflict in templates/todo.html by accepting both UUID and Hash fields

```powershell
git add templates/todo.html
git rebase --continue
```

**Result:** Successfully rebased with one commit automatically dropped due to already being upstream

---

## Complete Commit History

```
2e74d63 (main, master_1) Restate form with Item ID, UUID, and Hash fields updated
6f48315 Add Item ID field to To-Do form
f74f8ab Add To-Do form template with Item Name and Item Description fields
9092bfa (Naveen_new) Update data.json with new employee records
e813993 (Naveen) Add comprehensive README documentation
c473d0c (origin/main) updated file
a208c29 Flask + MongoDB Atlas app
```

---

## Branch Summary

| Branch | Purpose | Status |
|--------|---------|--------|
| main | Primary development branch | ✓ All feature merged |
| master_1 | Frontend To-Do form | ✓ Features added with 3 commits |
| master_2 | Backend /submittodoitem route | ✓ API implemented |
| Naveen | Initial project setup | ✓ Merged to main |
| Naveen_new | JSON data updates | ✓ Merged to main |

---

## Pushed to GitHub

```powershell
git push origin main master_1 master_2 Naveen Naveen_new
```

**Result:** All branches successfully pushed to remote repository

**Branches pushed:**
- main → main (updated)
- master_1 → master_1 (new branch)
- master_2 → master_2 (new branch)  
- Naveen → Naveen (new branch)
- Naveen_new → Naveen_new (new branch)

---

## Repository Statistics

- **Total Commits:** 10+
- **Total Branches:** 5 feature branches + main
- **Files Modified:** app.py, templates/todo.html, data.json
- **Lines Added:** 200+
- **Merge Conflicts Resolved:** 1 (during rebase)

---

## Key Git Commands Used

1. **Branch Creation:** `git checkout -b <branch-name>`
2. **Merging:** `git merge <branch-name>`
3. **Reset with Soft Flag:** `git reset --soft <commit-hash>`
4. **Rebasing:** `git rebase main master_1`
5. **Conflict Resolution:** `git add`, `git rebase --continue`
6. **Remote Operations:** `git push origin <branches>`

---

## Best Practices Demonstrated

✓ Clear commit messages  
✓ Sequential feature development  
✓ Proper branch naming conventions  
✓ Merge conflict resolution  
✓ Git reset for history management  
✓ Rebase for maintaining clean commit history  
✓ SSH authentication setup  
✓ Remote repository management  

---

## Repository Link

**GitHub:** https://github.com/NaveenKumarRB/Test-Tute.git

All work has been successfully completed and pushed to the GitHub repository.

