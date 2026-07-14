# 📝 Online Complaint Management System

Online Complaint Management System is a Django-based web application that enables users to register complaints, upload supporting documents, track complaint status, and provide feedback. The system streamlines complaint handling and improves communication between users and administrators.

## 🚀 Features

### 👤 User Features

* User registration and login
* Secure authentication
* Submit complaints with file attachments
* View complaint history
* Track complaint status
* Submit feedback after complaint resolution

### 📋 Complaint Management

* Register complaints with relevant details
* Upload supporting documents or images
* View all submitted complaints
* Complaint status tracking

### 🛠 Admin Features

* Admin login
* View and manage complaints
* Update complaint status
* Monitor user complaints
* Review user feedback

## 🧰 Technologies Used

* Python
* Django
* SQLite
* HTML
* CSS
* Bootstrap
* JavaScript

## 📂 Project Structure

```text
online-complaint-management-system/
│
├── complaint_app/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/
│   └── static/
│
├── manage.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/ASKANIPRAVEEN/online-complaint-management-system.git
cd online-complaint-management-system
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## 👨‍💻 Author

**Praveen Askani**

* GitHub: https://github.com/ASKANIPRAVEEN
* LinkedIn: https://www.linkedin.com/in/praveen-askani
