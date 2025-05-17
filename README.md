# Todo List Application

A feature-rich todo list application built with Django that helps you manage your tasks efficiently.

## Features

- ✨ Create new tasks with titles
- ✅ Mark tasks as complete/incomplete
- 📝 Edit existing tasks
- 🗑️ Delete tasks
- 📅 Automatic timestamp for task creation
- 📱 Responsive web interface
- 🔄 Real-time updates

## Technology Stack

- **Backend Framework:** Django
- **Database:** SQLite
- **Frontend:** Django Templates
- **Styling:** CSS

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd todolist
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
# OR
source venv/bin/activate      # On Unix/MacOS
```

3. Install dependencies:
```bash
pip install django
```

4. Run database migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

6. Open your browser and navigate to `http://localhost:8000`

## Usage

1. **Adding a Task**
   - Enter the task title in the input field
   - Click "Add Task" or press Enter

2. **Completing a Task**
   - Click the checkbox next to the task to mark it as complete/incomplete

3. **Updating a Task**
   - Click the "Update" button next to the task
   - Modify the task details
   - Click "Update Task" to save changes

4. **Deleting a Task**
   - Click the "Delete" button next to the task
   - Confirm deletion in the confirmation page

## Project Structure

```
todolist/
├── tasks/                  # Main application directory
│   ├── migrations/        # Database migrations
│   ├── templates/        # HTML templates
│   ├── admin.py         # Admin configuration
│   ├── forms.py         # Form definitions
│   ├── models.py        # Data models
│   ├── urls.py          # URL routing
│   └── views.py         # View logic
├── todolist/             # Project configuration
├── manage.py            # Django management script
└── db.sqlite3          # SQLite database
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 