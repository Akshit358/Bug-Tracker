# 🐛 BugTracker+ — Flask-based Bug Tracking System

> A clean, modular, and fully functional bug tracking web application built using Python and Flask. Perfect for solo developers and small teams to report, track, and manage bugs in a software development environment.

![Flask](https://img.shields.io/badge/Built%20With-Flask-blue) ![Python](https://img.shields.io/badge/Python-3.10%2B-yellow) ![Status](https://img.shields.io/badge/Project-Active-green) ![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📸 Overview

**BugTracker+** allows users to report software bugs via a web interface and store them securely in a SQLite database. Users can also view a historical log of all submitted bugs. It includes form validation, a responsive UI layout, modular structure, and test coverage — all set up for further expansion.

---

## ✨ Features

- 📝 **Bug Reporting Form** — Simple, intuitive interface for submitting bugs.
- 📂 **Bug History** — View all submitted bugs with details like title, description, and priority.
- 💾 **Persistent Storage** — SQLite database using SQLAlchemy ORM.
- ✅ **Input Validation** — Secure and clean forms with Flask-WTF.
- 🔍 **Modular Flask Structure** — Easy to scale and maintain.
- 🧪 **Unit Tests** — Pre-written tests for validating bug submission logic.
- 🔐 **Security** — CSRF protection enabled via Flask-WTF.

---

## 📂 Project Structure

```
BugTracker/
│
├── app/                         # Main Flask app package
│   └── __init__.py              # Initializes app and extensions
│
├── instance/
│   └── bugs.db                  # SQLite database (runtime generated)
│
├── static/
│   └── style.css                # Custom styling
│
├── templates/                   # HTML templates (Jinja2)
│   ├── bug_history.html         # Bug history page
│   ├── form.html                # Optional base form template
│   ├── report_bug.html          # Bug submission form
│   └── submit_bug.html          # Confirmation after bug submission
│
├── tests/
│   └── test_bug_submission.py   # Unit tests
│
├── venv/                        # Virtual environment (not pushed to Git)
│
├── app.py                       # Entry point
├── bugtracker.db                # Optional legacy DB (dev only)
├── extensions.py                # DB and form extension setup
├── forms.py                     # WTForms definitions
├── models.py                    # SQLAlchemy models
├── route.py                     # Main routing and views
└── README.md                    # You’re here!
```

---

## 🌐 Application URLs

| Endpoint | Description |
|----------|-------------|
| `/` | Redirects to the bug report page |
| `/report` | Submit a new bug |
| `/history` | View all submitted bugs |

---

## 🚀 Getting Started

Follow these steps to set up and run the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/BugTrackerPlus.git
cd BugTrackerPlus
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

> If `requirements.txt` doesn’t exist, generate it:
```bash
pip freeze > requirements.txt
```

### 4. Run the Application
```bash
python app.py
```

### 5. Access the App in Your Browser
```txt
http://127.0.0.1:5000/
```

---

## 🧪 Run Unit Tests

This project includes a basic unit test file to ensure core functionality:

```bash
python -m unittest discover tests
```

---

## 🛠️ Dependencies

- Flask
- Flask-WTF
- WTForms
- SQLAlchemy

You can install them all with:

```bash
pip install flask flask-wtf sqlalchemy
```

---

## 🎯 Future Enhancements

Here are some planned and potential features to take this project to the next level:

- [ ] Status field for bugs (e.g., Open, In Progress, Resolved)
- [ ] Edit & Delete functionality for bug reports
- [ ] User Authentication & Role-Based Access
- [ ] Export bug list as CSV or PDF
- [ ] UI upgrade with Tailwind or Bootstrap
- [ ] REST API integration
- [ ] Docker support for deployment
- [ ] Deployment on platforms like Render, Railway, or Heroku


---

## 👨‍💻 Author

**Akshit Singh**  
📧 [akshitsingh0319@gmail.com](mailto:akshitsingh0319@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/akshit-singh-aba4b51a6) | 💡 Passionate about Tech, Psychology & Innovation  

---

## 📄 License

This project is licensed under the MIT License.  
Feel free to use, modify, and share it. Check the [LICENSE](LICENSE) file for full details.

---

## 🌟 Acknowledgements

- Flask Docs — for being incredibly helpful
- Real Python — for tutorials on modular Flask apps
- YouTube Dev Community — for debugging walkthroughs


