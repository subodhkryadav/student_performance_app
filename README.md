# 🎓 Student Performance Prediction App

[![Deploy to PythonAnywhere](https://www.PythonAnywhere.com/static/images/deploy/button.svg)]
![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Framework-green)
![Machine Learning](https://img.shields.io/badge/ML-Model-orange)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

> 🚀 A machine learning–powered web app that predicts students' academic performance based on input features.  
> 🧠 Built with **Flask**, deployed on **PythonAnywhere**, and trained using advanced regression models.

---

## 📜 Table of Contents
- [📖 Overview](#-overview)
- [✨ Features](#-features)
- [📂 Project Structure](#-project-structure)
- [⚙️ Installation](#️-installation)
- [🚀 Deployment on PythonAnywhere](#-deployment-on-PythonAnywhere)
- [🖥️ Screenshots](#️-screenshots)
- [🤖 Model Details](#-model-details)
- [🛠️ Technologies Used](#️-technologies-used)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## 📖 Overview
The **Student Performance Prediction App** is a web-based tool designed to help educators, researchers, and students analyze and predict academic outcomes.  
Users can input key factors (like study time, attendance, and previous scores), and the app predicts the student’s final performance using a pre-trained machine learning model.

> 🌟 This project demonstrates the power of **Data Science +  basic Web Development +  Basic Cloud Deployment**.

---

## ✨ Features
✅ Simple and clean **web interface**  
✅ **Real-time predictions** powered by a pre-trained ML model  
✅ **Flask backend** for handling requests and inference  
✅ **Responsive design** with custom CSS  
✅ Easy to **deploy on PythonAnywhere**  
✅ Lightweight & beginner-friendly project structure  

---

## 📂 Project Structure
```
student_performance_app/
├── app.py                        # Main Flask application
├── requirements.txt              # Python dependencies
├── Student_Performance_model.pickle # Pre-trained ML model
├── static/
│   └── style.css                  # Styling for the frontend
└── templates/
    └── index.html                 # Web interface
some other file like procfile 
```

---

## ⚙️ Installation

### 🔹 Prerequisites
- Python 3.8+
- Git
- pip (Python package manager)

### 🔹 Steps
```bash
# 1. Clone the repository
git clone https://github.com/subodhkryadav/student-performance-app.git

# 2. Navigate into the project folder
cd student-performance-app/student_performance_app

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Flask app
python app.py
```

Visit the app at: **http://127.0.0.1:5000/**

---

## 🚀 Deployment on PythonAnywhere
1. Push the repository to GitHub.
2. Create a new **Web Service** on [PythonAnywhere](https://PythonAnywhere.com/).
3. Connect your GitHub repo.
4. Set the **Start Command** as:
   ```bash
   web: gunicorn student_performance_app.app:app --bind :$PORT

   ```
5. Add a `requirements.txt` and `Procfile` if needed:
   ```
   web: gunicorn app:app
   ```
6. Deploy and share your live app 🚀

---

## 🖥️ Screenshots


### 🏠 Home Page
![Home Page](https://github.com/subodhkryadav/student_performance_app/blob/main/templates/home.png)

### 📊 Prediction Result
![Prediction Result](https://github.com/subodhkryadav/student_performance_app/blob/main/templates/output.png)

---

## 🤖 Model Details
- The ML model was trained to predict **student academic performance** based on factors like:
  - Study hours
  - Attendance
  - Past scores
  - Socio-economic and demographic factors (if provided)

- Saved as: `Student_Performance_model.pickle`
- Integrated directly into the Flask app for fast predictions.

---

## 🛠️ Technologies Used
- **Python** (3.8+)
- **Flask** – Backend framework
- **Scikit-Learn / Pickle** – Machine Learning & model storage
- **HTML + CSS** – Frontend
- **Gunicorn** – Production WSGI server
- **PythonAnywhere** – Cloud deployment

---

## 🤝 Contributing
Contributions are welcome!  
Feel free to **fork** this repo and submit a **pull request**.

---

## 📄 License
This project is licensed under the **MIT License** – you are free to use and modify it.

---

⭐ If you like this project, don’t forget to **star ⭐ the repo** on GitHub!
