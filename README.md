# PassionToWander Project Documentation

This is the main documentation for the PassionToWander project. This project is a web app designed to manage travel blog posts.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contribution](#contribution)
- [License](#license)

## Project Structure

The PassionToWander project consists of several Django apps including:

- `users`: Handles user management, authentication and authorization.
- `blog`: Handles blog posts and related models.

The project also includes several key features:

- **Post management**: Users can create, read, update, and delete blog posts.
- **Content management**: Supports various types of content, including text, images, and videos.
- **User registration and authentication**: Users can create accounts and log in.

## Installation

Instructions for setting up a development environment are as follows:

```bash
# Clone the repository
git clone https://github.com/DerGeraetK/passiontowander.git

# Navigate into the project directory
cd passiontowander

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
