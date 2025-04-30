# 🧠 Unix-Inspired Task Manager

A Django + sqlite backend with a custom HTML/CSS/JS frontend that replicates Unix-style task management via a clean web interface. The system supports task lifecycle states, user authentication via JWT, and simulates concurrency in task handling.

## 🚀 Features

- ✅ **User Authentication**
  - Register, login, and manage sessions with JWT (stored in cookies)
- 🛠️ **Task Management**
  - Create, view, update, and delete tasks
  - Each task has a lifecycle: `pending`, `running`, `completed`, or `failed`
- 🔍 **Filter & Pagination**
  - Easily filter tasks or paginate results via query parameters
- ⚙️ **Simulated Concurrency**
  - Tasks can "run" and complete or fail based on simulated logic
- 🔐 **Protected Endpoints**
  - Only authenticated users can access their own tasks

## 🧱 Tech Stack

- **Backend:** Django (DRF), Sqlite, JWT
- **Frontend:** HTML, CSS, JavaScript
- **Database:** Sqlite (Cloud / Local)
- **Containerization (optional):** Docker, Docker Compose


---

## 🏗️ Setup

### 🔧 Prerequisites

- Python 3.9+
- PostgreSQL (or hosted DB)
- Git
- (Optional) Docker

---

### ⚙️ Local Installation

```bash
# Clone the repository
git clone https://github.com/AMANKUMAR22MCA/taskmanager.git
cd taskmanager

# Set up the backend
cd backend
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start the server
python manage.py runserver


Open in browser: http://127.0.0.1:5500/frontend/index.html   ( go live with frontend/index.html )

```

![image](https://github.com/user-attachments/assets/cbffaa63-ada6-497b-9f29-c295747fafd6)  <br>

![image](https://github.com/user-attachments/assets/011a4961-af23-474f-990c-0b03d0fe8273)  <br>

![image](https://github.com/user-attachments/assets/a0bb2592-3d68-4a69-8ac6-4cdffa2614fc)  <br>

![image](https://github.com/user-attachments/assets/d6019d75-11d8-4812-972b-592476d170fb)




