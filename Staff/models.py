from django.db import models

class LeaveApplication(models.Model):
    DESIGNATION_CHOICES = (
        ('Professor', 'Professor'),
        ('Associate Professor', 'Associate Professor'),
        ('Assistant Professor', 'Assistant Professor'),
        ('Lecturer', 'Lecturer')
    )

    DEPARTMENT_CHOICES = (
        ('CSE', 'Computer Science and Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
        ('EEE', 'Electrical and Electronics Engineering'),
        ('Mech', 'Mechanical Engineering'),
        ('Civil', 'Civil Engineering'),
        ('Physics', 'Physics'),
        ('Chemistry', 'Chemistry'),
        ('Maths', 'Mathematics')
    )

    LEAVE_TYPE_CHOICES = (
        ('Sick', 'Sick'),
        ('Casual', 'Casual'),
        ('Earned', 'Earned')
    )

    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=20, choices=DESIGNATION_CHOICES)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    email = models.EmailField()
    leave_type = models.CharField(max_length=10, choices=LEAVE_TYPE_CHOICES)
    date_from = models.DateField()
    date_to = models.DateField()
    reason = models.TextField()
    is_approved_HOD = models.BooleanField(default=False)
    is_approved_AR = models.BooleanField(default=False)
    is_approved_DIRECTOR = models.BooleanField(default=False)

