﻿# Uncover Myself App Setup

This repository contains a Django app named "Uncover Myself" that requires a few steps to set up.

## Live Demo
AI-powered quizzes for self-discovery using Google Gemini API. 
URL: https://uncovermyself.com

## Prerequisites

- Python 3.x installed on your system
- Git installed on your system (optional)

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine:

    git clone <repository-url>
    cd app-name

### 2. Create and Activate Virtual Environment

Create a virtual environment for the project:

    # On Windows
    python -m venv venv

    # On macOS and Linux
    python3 -m venv venv

Activate the virtual environment:

    # On Windows
    venv\Scripts\activate

    # On macOS and Linux
    source venv/bin/activate

### 3. Install Dependencies

Install the required Python packages:

    pip install -r requirements.txt

### 4. Configure Environment Variables

Create a `.env` file inside the "dashboard" app directory (if not present) and add your Google API key:

    # .env file
    GOOGLE_API_KEY=your_google_api_key_here

### 5. Run the Django App

Navigate to the Django project directory and start the development server:

    python manage.py runserver

The app should now be running locally at `http://localhost:8000/`.
