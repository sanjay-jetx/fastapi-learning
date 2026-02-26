# 🚀 FastAPI Learning Project

This repository contains my practice and learning projects using **FastAPI** and **Pydantic**.
It demonstrates how to build simple and structured REST APIs using modern Python backend tools.

---

## 📌 Features

* ✅ FastAPI project setup
* ✅ GET API implementation
* ✅ Pydantic model usage
* ✅ Returning JSON responses
* ✅ Project folder structure
* ✅ API testing using browser and Swagger UI

---

## 🧠 Technologies Used

* Python 3.13
* FastAPI
* Pydantic
* Uvicorn
* Git & GitHub

---

## 📁 Project Structure

```
FastApi/
│
├── Products_to_display/
│   ├── main.py
│   └── products.py
│
├── customer.py
├── Signup.py
├── main.py
│
├── venv/
└── README.md
```

---

## ⚙️ Installation and Setup

### Step 1: Clone the repository

```
git clone https://github.com/sanjay-jetx/fastapi-learning.git
```

### Step 2: Navigate to project folder

```
cd fastapi-learning
```

### Step 3: Create virtual environment

```
python -m venv venv
```

### Step 4: Activate virtual environment

Windows:

```
venv\Scripts\activate
```

### Step 5: Install dependencies

```
pip install fastapi uvicorn pydantic
```

---

## ▶️ Run the FastAPI Server

```
uvicorn main:app --reload
```

---

## 🌐 Open in Browser

API root:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 📷 Example API Response

```
GET /product
```

Response:

```json
{
  "id": 101,
  "name": "sanjay"
}
```

---

## 🎯 Learning Goals

This project is part of my journey to become:

* AI Automation Engineer
* Backend Developer
* FastAPI Developer

---

## 👨‍💻 Author

**Sanjay Kumar**

GitHub:
https://github.com/sanjay-jetx

---

## ⭐ Future Improvements

* POST API
* PUT API
* DELETE API
* Database Integration
* Authentication

---

## 🙌 Thank You

This repository is created for learning and practice purposes.
