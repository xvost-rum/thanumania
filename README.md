# Thanumania Project

A small self-hosted project by two developers. Built for learning, deployed for real.

## Table of Contents
- [Requirements](#requirements)
- [Running Locally](#running-locally)
- [Environment Setup](#environment-setup)
- [Running the Project](#running-the-project)

## Requirements

Before you begin, make sure you have the following installed:
- [Python](https://www.python.org/downloads/)
- [Git](https://git-scm.com/install/windows)

## Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/xvost-rum/thanumania.git
cd thanumania
```

### 2. Create a virtual environment

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Environment Setup

Create a `.env` file in the project root directory and add the following variables:

```env
SECRET_KEY=django-insecure-local-dev-key
DEBUG=True
ALLOWED_HOSTS=localhost,game.localhost,127.0.0.1
```

## Running the Project

### 1. Apply migrations

```bash
python manage.py migrate
```

### 2. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 3. Start the development server

```bash
python manage.py runserver
```

Done! 🎉 The project is available at: [http://localhost:8000](http://localhost:8000)
