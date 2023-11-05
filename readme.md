# To-Do List Web Application

A simple Flask-based web application for managing your to-do list.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

This web application allows users to create, view, update, search and delete tasks on their to-do list. It provides a user-friendly interface for managing tasks and uses a Flask backend with a MongoDB database to store task data.

## Features

- User registration and login
- Add new tasks to the to-do list
- Edit and update task titles
- Delete tasks from the list
- Search for tasks by title
- User-friendly interface

## Installation

To set up and run this project locally, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/todo-list-web-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd todo-list-web-app
    ```

3. Install the required Python packages:

    ```bash
    pip freeze > requirements.txt
    pip install -r requirements.txt
    ```

4. Make sure you have MongoDB installed and running on your system. You can change the MongoDB connection URI in the Flask app configuration (see `app.config['MONGO_URI']` in `app.py`) to match your MongoDB setup.

5. Start the Flask development server:

    ```bash
    python app.py
    ```

6. Access the web application in your browser at [http://localhost:5000](http://localhost:5000).

## Usage

To use this To-Do List web application, follow these steps:

1. Register for a new account or log in with your existing credentials.
2. Add tasks to your to-do list by entering a task title and clicking "Add to List."
3. Click the "Update" button next to a task to edit its title. Click "Save" to save changes or "Update" to cancel.
4. Click the "Delete" button to remove a task from the list.
5. Use the search bar to filter tasks by title.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature-name`.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your fork: `git push origin feature-name`.
5. Submit a pull request to the main repository.

We appreciate your contributions to make this project even better!
