# UMB-OATS
## Online Application for Tutoring Scheduling
### University of Massachusetts, Boston

## Project Overview

UMB-OATS is a dynamic scheduling application designed to streamline tutoring services at the University of Massachusetts, Boston. Developed with Django, HTML, and Bootstrap, this user-friendly platform empowers students to efficiently book tutoring sessions and manage their academic schedules.

## Setting Up

To set up the project, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the directory where the `manage.py` file is located.
3. (Optional) Create a virtual environment for the project (recommended).
4. Activate the virtual environment.
5. Install the required packages by running the following command:
   - pip install -r requirements.txt
6. Start the application locally by running the following command:
   - python manage.py runserver


Make sure to replace `python` with the appropriate command for your Python environment.

## Project Structure

The project consists of the following main files:

- `settings.py`: Contains the configuration settings for the Django project.
- `urls.py`: Defines the URL patterns and corresponding views for the application.
- `views.py`: Contains the view functions that handle requests and generate responses.
- `models.py`: Contains the models to represent the structure in the database

## Roles 
There are 3 roles in UMB OATS Application: -
1. Student
2. Admin
3. Tutor

## Features
1. User registration and authentication: 
   - Users can sign up for an account and log in to the application.
2. User roles and permissions: 
   - Different roles such as student and tutor can be assigned to users, granting them specific permissions.
3. Tutor availability management: 
   - Tutors can set their availability for tutoring sessions, specifying the dates and time slots they are available.
4. Session booking: 
   - Students can browse available tutoring sessions and book sessions with tutors based on their availability.
5. Session cancellation: 
   - Both students and tutors can cancel booked sessions, triggering notifications to the affected parties.
6. Semester management: 
   - Administrators can add and manage academic semesters, defining start and end dates for each semester.
7. Password management: 
   - Users can change their passwords through a secure password change form.
8. Session history: 
   - Users can view their session history, including past sessions they have participated in.
9. Email notifications: 
   - Automated email notifications are sent to users for various actions such as session booking, cancellation, and password reset.
10. Error handling: 
    - Custom error pages and handling for 404 (Page Not Found) errors to enhance user experience.

## Impact:

UMB-OATS contributes to a more organized and efficient tutoring system at the University of Massachusetts, Boston. By empowering students with an easy-to-use platform, the project enhances the overall academic support experience, fostering a conducive learning environment.

## Technologies Used:

1. Python
2. Django
2. HTML
3. Bootstrap

## Authors

* **Adnan Ali** - Project Lead & Main Contributor

As a Master's degree holder in Computer Science from UMass Boston, I have utilized my expertise in machine learning and computer vision to spearhead the development of this integrated model system. 
With a keen eye for innovative solutions, I have orchestrated the seamless fusion of posture analysis and logo detection models, showcasing state-of-the-art techniques in the realm of AI.

Connect :
- [GitHub](https://github.com/adi-tsvet)
- [LinkedIn](https://www.linkedin.com/in/adi-tsvet/) 

## References
1. UMB Tutoring Programs - https://www.umb.edu/academics/seas/center-for-academic-excellence/tutoring-programs/
2. Website reference - https://traccloud.umb.edu/

For more details refer this documentation : 
[UMB-OATS User Documentation](UMB_OATS_User_Documentation_Final.pdf)
