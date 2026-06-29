# 🐳 Docker Todo App

A command-line Task Manager application built with **Python** to demonstrate **Docker**, **Docker Volumes**, and persistent data storage.

---

# 📖 About

This project was developed as part of my DevOps learning journey.

The application allows users to manage daily tasks while demonstrating how Docker containers work and how Docker Volumes preserve data even after containers are removed.

---

# ✨ Features

* Add new tasks
* Display tasks
* Edit existing tasks
* Delete tasks
* Mark tasks as completed
* Priority levels (Low / Medium / High)
* Due date validation
* One-time and recurring tasks
* Statistics Dashboard
* JSON persistent storage

---

# 🛠 Technologies

* Python 3
* Docker
* Docker Volumes
* JSON

---

# 📂 Project Structure

```
docker-todo-app
│
├── app
│   ├── main.py
│   └── data
│       └── tasks.json
│
├── Dockerfile
├── .dockerignore
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 🚀 Build Docker Image

```bash
docker build -t todo-app .
```

---

# ▶ Run Container

```bash
docker run -it --name todo todo-app
```

---

# 💾 Run With Docker Volume

```bash
docker volume create todo-data

docker run -it --name todo \
-v todo-data:/app/app/data \
todo-app
```

---

# 🧪 What I Learned

During this project I learned:

* Writing Dockerfiles
* Building Docker Images
* Running Containers
* Difference between Images and Containers
* Docker Volumes
* Persistent Storage
* JSON file handling
* CRUD operations in Python
* Input validation
* Working with dates
* Command Line applications

---

# 🐳 Docker Volume Demonstration

Without Docker Volume:

```
Container
    │
tasks.json
```

Deleting the container also deletes the stored tasks.

With Docker Volume:

```
Container
     │
Docker Volume
     │
tasks.json
```

Deleting the container does **NOT** delete the stored tasks.

---

# 🔮 Future Improvements

* Docker Compose
* Flask Web Interface
* SQLite Database
* REST API
* User Authentication
* Categories
* Search & Filtering

---

Developed as a personal DevOps practice project.
