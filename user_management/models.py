from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    # Define role choices
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Project Manager', 'Project Manager'),
        ('Site Engineer', 'Site Engineer'),
        ('Croxx', 'Croxx'),
        ('Stronger', 'Stronger'),
        ('ROW Coordinator', 'ROW Coordinator'),
        ('Quality Inspector', 'Quality Inspector'),
        ('User', 'User'),
        ('Viewer', 'Viewer'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Ensure unique email addresses
    phone = models.CharField(max_length=20)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)  # Dropdown field for roles
    password = models.CharField(max_length=128)  # Stores hashed password

    def __str__(self):
        return self.full_name

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

# from django.conf import settings
# from datetime import datetime
# class Task(models.Model):
#     TASK_STATUS_CHOICES = [
#         ('Pending', 'Pending'),
#         ('In Progress', 'In Progress'),
#         ('Completed', 'Completed'),
#         ('On Hold', 'On Hold'),
#     ]
    
#     business_area_choices = [
#         ('IT', 'IT'),
#         ('HR', 'HR'),
#         ('Finance', 'Finance'),
#         ('Marketing', 'Marketing'),
#         ('Operations', 'Operations'),
#     ]
#     milestone_choices = [
#         ('select Milestone', 'select Milestone'),
#         ('Desktop Survey Design', 'Desktop Survey Design'),
#         ('Design/Network Health Checkup', 'Design/Network Health Checkup'),
#         ('HOTO-Existing', 'HOTO-Existing'),
#         ('Detailed Design', 'Detailed Design'),
#         ('ROW(Right of way)', 'ROW(Right of way)'),
#         ('IFC(Issued For Construction)', 'IFC(Issued For Construction)'),
#         ('IC(Initial Construction)', 'IC(Initial Construction)'),
#         ('As-Built', 'As-Built'),
#         ('HOTO(Final)', 'HOTO(Final)'),
#     ]
#     STATE_CHOICES = [
#         ('AP', 'Andhra Pradesh'),
#         ('TS', 'Telangana'),
#         ('KA', 'Karnataka'),
#         ('TN', 'Tamil Nadu'),
#         ('MH', 'Maharashtra'),
#         ('OD', 'Odisha'),
#         ('RJ', 'Rajasthan'),
#         ('GJ', 'Gujarat'),
#         ('WB', 'West Bengal'),
#         ('UP', 'Uttar Pradesh'),
#     ]

#     STATE_DISTRICT_CHOICES = {
#         'AP': [('EG', 'East Godavari'), ('WG', 'West Godavari'), ('VSP', 'Visakhapatnam')],
#         'TS': [('HYD', 'Hyderabad'), ('RRS', 'Ranga Reddy'), ('KHM', 'Khammam')],
#         'KA': [('BLR', 'Bangalore'), ('MYS', 'Mysuru'), ('HBL', 'Hubballi')],
#         'TN': [('CHN', 'Chennai'), ('CBE', 'Coimbatore'), ('MDU', 'Madurai')],
#         'MH': [('MUM', 'Mumbai'), ('PUN', 'Pune'), ('NGP', 'Nagpur')],
#         'OD': [('BBS', 'Bhubaneswar'), ('CTC', 'Cuttack'), ('RKL', 'Rourkela')],
#         'RJ': [('JPR', 'Jaipur'), ('JOD', 'Jodhpur'), ('UDA', 'Udaipur')],
#         'GJ': [('AMD', 'Ahmedabad'), ('RJT', 'Rajkot'), ('VAD', 'Vadodara')],
#         'WB': [('KOL', 'Kolkata'), ('HWH', 'Howrah'), ('SLG', 'Siliguri')],
#         'UP': [('LKO', 'Lucknow'), ('VNS', 'Varanasi'), ('AGC', 'Agra')],
#     }

#     task_name = models.CharField(max_length=255)
#     subtasks = models.TextField()
#     milestone = models.CharField(max_length=255, choices=milestone_choices)
#     assign_to = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE
#     )
#     state = models.CharField(max_length=50, choices=STATE_CHOICES)
#     business_area = models.CharField(max_length=50, choices=business_area_choices)
#     district = models.CharField(max_length=50)
#     block = models.CharField(max_length=255)
#     start_date = models.DateField(null=True, blank=True)  # <<< ADD THIS
#     end_date = models.DateField(null=True, blank=True)
#     status = models.CharField(max_length=50, choices=TASK_STATUS_CHOICES, default='Pending')

#     def __str__(self):
#         return self.task_name


from django.db import models
from django.conf import settings

class Task(models.Model):
    TASK_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('On Hold', 'On Hold'),
    ]

    BUSINESS_AREA_CHOICES = [
        ('IT', 'IT'),
        ('HR', 'HR'),
        ('Finance', 'Finance'),
        ('Marketing', 'Marketing'),
        ('Operations', 'Operations'),
    ]

    MILESTONE_CHOICES = [
        ('select Milestone', 'select Milestone'),
        ('Desktop Survey Design', 'Desktop Survey Design'),
        ('Design/Network Health Checkup', 'Design/Network Health Checkup'),
        ('HOTO-Existing', 'HOTO-Existing'),
        ('Detailed Design', 'Detailed Design'),
        ('ROW(Right of way)', 'ROW(Right of way)'),
        ('IFC(Issued For Construction)', 'IFC(Issued For Construction)'),
        ('IC(Initial Construction)', 'IC(Initial Construction)'),
        ('As-Built', 'As-Built'),
        ('HOTO(Final)', 'HOTO(Final)'),
    ]

    STATE_CHOICES = [
        ('AP', 'Andhra Pradesh'),
        ('TS', 'Telangana'),
        ('KA', 'Karnataka'),
        ('TN', 'Tamil Nadu'),
        ('MH', 'Maharashtra'),
        ('OD', 'Odisha'),
        ('RJ', 'Rajasthan'),
        ('GJ', 'Gujarat'),
        ('WB', 'West Bengal'),
        ('UP', 'Uttar Pradesh'),
    ]

    STATE_DISTRICT_CHOICES = {
        'AP': [('EG', 'East Godavari'), ('WG', 'West Godavari'), ('VSP', 'Visakhapatnam')],
        'TS': [('HYD', 'Hyderabad'), ('RRS', 'Ranga Reddy'), ('KHM', 'Khammam')],
        'KA': [('BLR', 'Bangalore'), ('MYS', 'Mysuru'), ('HBL', 'Hubballi')],
        'TN': [('CHN', 'Chennai'), ('CBE', 'Coimbatore'), ('MDU', 'Madurai')],
        'MH': [('MUM', 'Mumbai'), ('PUN', 'Pune'), ('NGP', 'Nagpur')],
        'OD': [('BBS', 'Bhubaneswar'), ('CTC', 'Cuttack'), ('RKL', 'Rourkela')],
        'RJ': [('JPR', 'Jaipur'), ('JOD', 'Jodhpur'), ('UDA', 'Udaipur')],
        'GJ': [('AMD', 'Ahmedabad'), ('RJT', 'Rajkot'), ('VAD', 'Vadodara')],
        'WB': [('KOL', 'Kolkata'), ('HWH', 'Howrah'), ('SLG', 'Siliguri')],
        'UP': [('LKO', 'Lucknow'), ('VNS', 'Varanasi'), ('AGC', 'Agra')],
    }

    BLOCK_CHOICES = [
        ('Block1', 'Block1'),
        ('Block2', 'Block2'),
        ('Block3', 'Block3'),
        ('Block4', 'Block4'),
        ('Block5', 'Block5'),
    ]

    task_name = models.CharField(max_length=255)
    subtasks = models.TextField()
    milestone = models.CharField(max_length=255, choices=MILESTONE_CHOICES)
    assign_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    state = models.CharField(max_length=50, choices=STATE_CHOICES)
    business_area = models.CharField(max_length=50, choices=BUSINESS_AREA_CHOICES)
    district = models.CharField(max_length=50)
    block = models.CharField(max_length=50, choices=BLOCK_CHOICES)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=TASK_STATUS_CHOICES, default='Pending')

    def __str__(self):
        return self.task_name

