# School Management System

A modern, full-stack school management application built with Django REST Framework and Flutter. This system provides an intuitive dashboard for managing student data with real-time analytics and visualizations.

## Features

### Dashboard Analytics
- **Real-time Statistics**: Live updates of student data with auto-refresh functionality
- **Gender Distribution**: Interactive pie chart showing male/female student ratios
- **Age Distribution**: Bar chart displaying student age demographics
- **Grade Distribution**: Progress bars showing percentage of students in each grade
- **Average Age per Grade**: Line chart tracking age trends across grades
- **Total Students Counter**: Dynamic counter with animated updates

### Student Management
- **Comprehensive Student List**: 
  - Searchable student directory
  - Detailed student profiles
  - Quick access to student information
- **Student Details**:
  - Personal information
  - Academic records
  - Contact details
  - Parent/Guardian information

### Data Visualization
- **Interactive Charts**:
  - Gender distribution pie chart
  - Age distribution bar chart
  - Grade distribution progress bars
  - Average age per grade line chart
- **Real-time Updates**:
  - Automatic data refresh every 30 seconds
  - Manual refresh option
  - Last update timestamp display

### User Interface
- **Modern Design**:
  - Material Design 3 components
  - Responsive layout
  - Dark/Light theme support
- **Navigation**:
  - Tabbed interface (Dashboard/Students)
  - Intuitive search and filtering
  - Smooth animations and transitions

## Technical Stack

### Backend
- **Framework**: Django 5.0.2
- **API**: Django REST Framework
- **Documentation**: Swagger/OpenAPI
- **Database**: SQLite (default)

### Frontend
- **Framework**: Flutter
- **State Management**: Provider
- **Charts**: fl_chart
- **HTTP Client**: Built-in HTTP package
- **Date Formatting**: intl package

## Setup

### Backend Setup
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup
1. Install Flutter dependencies:
   ```bash
   flutter pub get
   ```

2. Run the application:
   ```bash
   flutter run
   ```

## API Endpoints

- `GET /api/students/`: List all students
- `POST /api/students/`: Create a new student
- `GET /api/students/{id}/`: Retrieve a specific student
- `PUT /api/students/{id}/`: Update a student
- `DELETE /api/students/{id}/`: Delete a student

## Project Structure

```
school_management_app/
├── lib/
│   ├── models/
│   │   └── student.dart
│   ├── providers/
│   │   └── student_provider.dart
│   ├── screens/
│   │   └── dashboard_screen.dart
│   └── main.dart
├── pubspec.yaml
└── README.md
```

## Features in Development

- Student attendance tracking
- Grade management system
- Teacher dashboard
- Parent portal
- Report generation
- File upload for student documents
- Email notifications
- Mobile responsive design improvements

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Flutter team for the amazing framework
- Django team for the robust backend framework
- Chart library contributors
- All contributors who have helped shape this project

## Support

For support, please open an issue in the GitHub repository or contact the development team.

## Screenshots

[Add screenshots of your application here] 