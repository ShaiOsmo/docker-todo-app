# 🐳 Docker Todo App

A command-line Task Manager application built with **Python** to demonstrate **Docker Containers**, **Docker Volumes**, and persistent data storage.

This project was developed as part of my DevOps learning journey and focuses on understanding how Docker manages containers and persistent storage.

---

## ✨ Features

* ➕ Add new tasks
* 📋 View all tasks
* ✏️ Edit existing tasks
* 🗑 Delete tasks
* ✅ Mark tasks as completed
* 🔴 Priority levels (Low / Medium / High)
* 📅 Due date validation
* 🔁 Recurring tasks

  * One-time
  * Daily
  * Weekly
  * Monthly
* 📊 Statistics Dashboard
* 💾 JSON-based data persistence

---

## 🛠 Technologies

* Python 3
* Docker
* Docker Volumes
* JSON

---

## 📂 Project Structure

```text
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

## 🚀 Build the Docker Image

```bash
docker build -t todo-app .
```

---

## ▶️ Run the Application

```bash
docker run -it --name todo todo-app
```

---

## 💾 Run with Docker Volume

Create a Docker Volume:

```bash
docker volume create todo-data
```

Run the application with persistent storage:

```bash
docker run -it --name todo \
-v todo-data:/app/app/data \
todo-app
```

---

## 🧪 Docker Volume Demonstration

### Without Docker Volume

```
Container
    │
tasks.json
```

Deleting the container also deletes the stored tasks.

### With Docker Volume

```
Container
     │
Docker Volume
     │
tasks.json
```

Deleting the container **does not** delete the stored tasks.

---

## 📚 What I Learned

During this project I practiced:

* Creating Docker Images
* Writing Dockerfiles
* Running and managing Docker Containers
* Understanding the difference between Images and Containers
* Using Docker Volumes for persistent storage
* CRUD operations in Python
* JSON file handling
* Input validation
* Date validation
* Building a command-line application

---

## 🔮 Future Improvements

* Docker Compose
* Flask Web Interface
* SQLite Database
* REST API
* User Authentication
* Categories & Search
* Task Filtering

---

## 👩‍💻 Author

**Shai Osmo**

Software Engineering Graduate | Python | Docker | DevOps Learning Journey
