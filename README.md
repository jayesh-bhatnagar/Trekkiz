# 📍 Trekkiz
A simple Flask based web-application for Trek-Management, developed as a part of **MAD-I project for May 2026 term**. The web-app provides different interfaces for administrators, staff-members (guides), and the users (trekkers) to make the Trek management process easier.

---

## ✨ Features

### 1. Administrators
* Create new Treks and edit them. Assign guides to the Treks.
* Approve or Reject the registration of staff-members.
* Blacklist / Unblacklist staff-members and users (trekkers).
* Can view all the bookings, registered users and trek-staff.

### 2. Staff-Members (Guides)
* Manage the assigned treks.
* View assigned treks.
* View participants for an assigned trek.

### 3. Users (Trekkers)
* Self-register without needing the approval of administrators.
* Book and search for treks.
* View their bookings.
* View their past trek history.
* Update profiles

---

## 🧑🏻‍💻 Tech Stack

*  **Python**
*  **Flask**
*  **SQLAlchemy**
*  **Jinja2**
*  **Bootstrap 5**
*  **HTML and CSS**

---

## 📂 Folder Structure
```text 
├── app.py
├── helpers.py
├── models.py
├── requirements.txt
├── routes.py
├── static
│   ├── css/
│   └── images/
└── templates/
```

---

## 🚗 Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd Trek-Management
```

### 2. Create a virtual environment.

**Linux / macOS**

```bash
python -m venv .venv
```

**Windows**

```bash
python -m venv .venv
```

### 3. Activating the virtual environment

**Linux / macOS**
```bash
source .venv/Scripts/activate
```

**Windows**
```bash
.\.venv\Scripts\activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

The application will be available at: 
```text
http://127.0.01:5000
```

---



---

## About

This project is created for **MAD-I project for May 2026 term**. This project helped me gain knowledge on Role-Based Access Control (RBAC), authentication, CRUD operations, and database relationships.

Link to access project report: 
Link to access video report: 
