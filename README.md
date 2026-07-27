# Trekkiz
A simple Flask based web-application for Trek-Management, developed as a part of **MAD-I project for May 2026 term**. The web-app provides different interfaces for administrators, staff-members (guides), and the users (trekkers) to make the Trek management process easier.

## Features

### Administrators
* Create new Treks and edit them. Assign guides to the Treks.
* Approve or Reject the registration of staff-members.
* Blacklist / Unblacklist staff-members and users (trekkers).
* Can view all the bookings, registered users and trek-staff.

### Staff-Members (Guides)
* Manage the assigned treks.
* View assigned treks.
* View participants for an assigned trek.

### Users (Trekkers)
* Self-register without needing the approval of administrators.
* Book and search for treks.
* View their bookings.
* View their past trek history.
* Update profiles

---

## Tech Stack

* **Python**
* **Flask**
* **SQLAlchemy**
* **Jinja2**
* **Bootstrap 5**
* **HTML and CSS**

---

## Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd Trek_Management
```

### 2. Create a virtual environment.

**Linux / macOS**

```bash
python -m venv .venv
source .venv/Scripts/activate
```

**Windows**

```bash
python -m venv .venv
.\.venv\Scripts\activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

The application will be available at: 
```text
http://127.0.01:5000
```

## Screens Included

* Home page: The first page which gets loaded.
* Login and Signup:
    Login: Login for admin, user(trekker), staff(guides)
* Admin Dashboard:
    Dashboard home: Displays the count cards, recent bookings, pending staff approvals, trek catalogue.
    Treks Table: Displays a table of all the treks exisiting in the database, with an add new trek button.
    Staff Table: Displays a table of all the guides, with their username, name, phone number, status, and buttons to reject, approve, or blacklist staff.
    Users Table: Displays a table of all the registered users(trekkers), with their username, name, phone number, status, and buttons to blacklist or unblacklist users.
    Bookings Table: Displays a table of all the bookings made by different users for different treks.
* Staff Dashboard:
    Dashboard home: Displays the count cards, and assigned trek catalogue.
    My Treks: Displays a table of all the treks assigned to a staff, where they can update some trek details and view the bookings done for a particular trek.
    My Profile: Displays the profile details for the guide and gives them freedom to change their name and phone number.
* Users Dashboard:
    Dashboard home: Displays the bookings and available trek catalogue.
    My Bookings: Displays a table of all the bookings done by a trekker.
    My Profile: Displays the profile details for the trekker and gives them freedom to change their name and phone number.
    Trek History: Where a trekker can see a list of all the completed treks.

---

## About

This project is created for **MAD-I project for May 2026 term**. This project helped me gain knowledge on Role-Based Access Control (RBAC), authentication, CRUD operations, and database relationships.

Link to access project report: https://drive.google.com/file/d/1mWESy8G-aMOo2rev2Ebg8HFdDQ97bCf-/view?usp=sharing

Link to access video report: https://drive.google.com/file/d/1NEhOSgupt2WYbfnFHvf9H12c79D-guy0/view?usp=drive_link

---
