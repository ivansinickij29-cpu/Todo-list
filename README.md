# Todo List

A web application built with Python and Django
for managing daily tasks.

## Features

- Create new tasks
- Edit existing tasks
- Delete tasks
- Mark tasks as completed or incomplete
- Organize tasks using tags
- View incomplete and completed tasks

## Installation

1. Clone the repository:

   git clone https://github.com/ivansinickij29-cpu/Todo-list.git

2. Navigate to the project directory:

   cd Todo-list

3. Create a virtual environment:

   python -m venv .venv


4. Activate the virtual environment:

   .venv\Scripts\activate


5. Install dependencies:

  pip install -r requirements.txt


6. Create a `.env` file based on `.env.example` and set the environment variables.

7. Apply database migrations:

   python manage.py migrate

8. Run the development server:

   python manage.py runserver