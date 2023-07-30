# flask_blogs


Flask Blog is a simple Flask-based blog application with user registration, login, and basic CRUD functionality for posts. It uses SQLite as the database to store user information and blog posts.

## Requirements

- Python 3.x
- Flask
- Flask-Login

## Getting Started

1. Clone the repository to your local machine.
2. Create a virtual environment (optional but recommended):

  ```
python -m venv venv
  ```

3. Activate the virtual environment:

- On Windows:

  ```
  venv\Scripts\activate
  ```

- On macOS and Linux:

  ```
  source venv/bin/activate
  ```


4. Create the SQLite database:

  ```
    python init_db.py
  ```


5. Start the development server:

 ```
    python app.py
  ```


6. Open your web browser and go to http://localhost:5000 to access the blog.

## Features

- User Registration and Login: Users can register with their name, email, and password. Registered users can log in to access their profiles and create, edit, and delete blog posts.

- Password Hashing: User passwords are hashed using the `generate_password_hash` function from `werkzeug.security` to ensure security.

- Flask-Login: The application uses Flask-Login to manage user sessions and authentication.

- CRUD for Posts: Logged-in users can create, view, update, and delete their blog posts.

- User Profile: Users can view and update their profile, including uploading an avatar image.

## Project Structure

- `app.py`: This file contains the main Flask application and routes for different pages.
- `FDataBase.py`: This file defines the `FDataBase` class, which handles database interactions.
- `UserLogin.py`: This file defines the `UserLogin` class, which represents a logged-in user.
- `admin/admin.py`: This file contains the routes and views for the admin section of the blog (optional).
- `forms.py`: This file defines the Flask-WTF forms for user login and registration.
- `sq_db.sql`: This file contains the SQL script to create the initial database schema.
- `static/`: This directory contains static files such as CSS and images.
- `templates/`: This directory contains HTML templates for the blog.

## Contributing

If you find any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue on the GitHub repository.

## License

This is free and unencumbered software released into the public domain.





