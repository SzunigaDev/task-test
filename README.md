# To-Do List Application

This is a simple To-Do List web application built with Flask for the backend and Vue.js with Vuetify for the frontend.

## Features

- Create, update, and delete tasks
- Responsive design using Vuetify
- Flask backend with RESTful API

## Technologies Used

- Python (Flask)
- Vue.js
- Vuetify
- MySQL
- Axios
- Flask-Migrate

## Getting Started

### Prerequisites

- Python 3.x
- Node.js and npm
- MySQL

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/todo-app.git
   cd todo-app
   ```

2. Setup tje backend:
   cd backend
   python3 -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt

3. Setup the frontend:
   cd ../frontend
   npm install

4. Create a .env file in the backend directory with your database credentials:
   DB_USERNAME=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=localhost
   DB_NAME=tasks_db

5. Run the backend:
   cd ../backend
   flask run

6. Run the frontend:
   cd ../frontend
   npm run dev

## License

This project is licensed under the MIT License - see the LICENSE file for details.
