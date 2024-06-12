# Team Projects for Fundamentals of Software Engineering

## Overview
This repository contains various projects developed by our team. Each project demonstrates different aspects of web development and database management using various technologies. Below are the details of the included projects.

## Projects

### CA01 - Creative Programming Assignment - Prompt Engineering
**Description**: This project focuses on creating a web app using Flask which uses prompt engineering to generate useful responses to specific user queries.

**Technologies**: Python, Flask, OpenAI API

**Features**:
- Designed and implemented a web app for prompt engineering
- Each team member contributed a specific prompt method
- About page explaining the purpose and functionality of the app
- Team page with bios and roles of each member
- Individual pages for each member with specific prompt forms
- Short demonstration videos by each team member

**Steps**:
1. Created a repository and structured it with necessary folders and files.
2. Implemented methods in `gpt.py` to handle different prompts.
3. Enhanced `gptwebapp.py` with additional routes and pages.
4. Documented the project with an about page and team bios.
5. Created demonstration videos for individual contributions.

### PA03 - Persistence with SQL
**Description**: A web application that utilizes SQL databases for data persistence, demonstrating CRUD operations and automated testing.

**Technologies**: Python, SQLite, pytest, pylint

**Features**:
- CRUD operations using SQL
- Python class `Transaction` to handle database interactions
- User interface for managing financial transactions
- Automated tests using pytest
- Code linting with pylint for style compliance

**Steps**:
1. Developed a Python class `Transaction` to manage database operations.
2. Created a user interface in `tracker.py` for various transaction operations.
3. Implemented automated tests in `test_transaction.py`.
4. Ensured code quality with pylint.
5. Documented the project with usage instructions and a demonstration transcript.

### PA04 - Transaction App in Express/Mongoose/EJS
**Description**: This project involves recreating the PA03 app as an Express.js application using MongoDB (through Mongoose) as the database.

**Technologies**: Node.js, Express.js, MongoDB, Mongoose, EJS

**Features**:
- View, add, edit, and delete transactions
- Sort transactions by any column (date, amount, description, category)
- Group transactions by category
- Responsive and interactive UI with EJS templates

**Steps**:
1. Recreated the SQL-based app using Express and MongoDB.
2. Implemented transaction features with Mongoose.
3. Designed views with EJS for dynamic content rendering.
4. Enhanced user experience with sorting and grouping functionalities.

### CA02 - Creative Express App with chatGPT
**Description**: This project involves creating an innovative Express app that integrates with OpenAI's chatGPT. The app provides an interactive chat interface that leverages AI to respond to user queries.

**Technologies**: Node.js, Express.js, MongoDB, Mongoose, EJS, OpenAI API

**Features**:
- Interactive chat interface
- Integration with chatGPT for AI responses
- Authentication system with username/password
- Storage of user queries and responses in the database
- Informative about and team pages
- Individual prompt pages for each team member

**Steps**:
1. Created a team repository and structured it with necessary folders and files.
2. Developed individual routes invoking chatGPT for different tasks.
3. Implemented authentication and user session management.
4. Enhanced the app with about, team, and individual prompt pages.
5. Created demonstration videos for individual contributions.

## Getting Started

### Prerequisites
- Node.js
- MongoDB (for PA04 and CA02)
- SQL Database (for PA03)
- Python (for CA01 and PA03)

### Installation
1. Clone the repository:
    ```sh
    git clone <repository-url>
    ```
2. Navigate to the project directory of your choice (e.g., PA04):
    ```sh
    cd <project-directory>
    ```
3. Install dependencies:
    ```sh
    npm install
    ```

### Running the Projects
1. For PA03 and PA04, start your SQL or MongoDB server.
2. Start the application server:
    ```sh
    npm start
    ```
3. Open your browser and navigate to `http://localhost:3000` (or the specified port).

## Contributors
- Madina Nasriddinova
- Defne Coban
- Zev Ross
- Eliora Kruman
