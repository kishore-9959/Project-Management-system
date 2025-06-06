from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User, Task
from .forms import UserForm, TaskForm
from .models import User, Task
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User, Task
from .forms import UserForm, TaskForm
from django.contrib.auth import authenticate, login, logout

from .models import User, Task # Ensure Milestone is defined in models.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Task
from .forms import TaskForm

# ------------------------------
# Task List with Filtering
# ------------------------------
from django.shortcuts import render
from django.http import JsonResponse
from .models import Task  # Ensure to import the Task model




# @login_required
# def admin_dashboard(request):
#     # Get all the tasks
#     tasks = Task.objects.all()
    
#     # Milestone names based on your MILESTONE_CHOICES
#     milestone_names = [
#         "Desktop Survey Design",
#         "Design/Network Health Checkup",
#         "HOTO-Existing",
#         "Detailed Design",
#         "ROW(Right of way)",
#         "IFC(Issued For Construction)",
#         "IC(Initial Construction)",
#         "As-Built",
#         "HOTO(Final)",
#     ]

#     # List to hold milestone data and status counts
#     milestone_data = []

#     # Loop through each milestone and count the task statuses
#     for milestone in milestone_names:
#         milestone_tasks = tasks.filter(milestone=milestone)

#         # Count tasks for each status
#         nil_count = milestone_tasks.filter(status="Pending").count()
#         inprogress_count = milestone_tasks.filter(status="In Progress").count()
#         completed_count = milestone_tasks.filter(status="Completed").count()
#         onhold_count = milestone_tasks.filter(status="On Hold").count()

#         # Only add milestone data if there are tasks with any status
#         if nil_count > 0 or inprogress_count > 0 or completed_count > 0 or onhold_count > 0:
#             milestone_data.append({
#                 'name': milestone,
#                 'nil_count': nil_count,
#                 'inprogress_count': inprogress_count,
#                 'completed_count': completed_count,
#                 'onhold_count': onhold_count,
#             })

#     # Pass the tasks and milestone data to the template
#     return render(request, 'admin_dashboard.html', {
#         'tasks': tasks,
#         'milestone_data': milestone_data
#     })


# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Task

@login_required
def admin_dashboard(request):
    # Get all the tasks from the database
    tasks = Task.objects.all()
    
    # Milestone names based on your MILESTONE_CHOICES
    milestone_names = [
        "Desktop Survey Design",
        "Design/Network Health Checkup",
        "HOTO-Existing",
        "Detailed Design",
        "ROW(Right of way)",
        "IFC(Issued For Construction)",
        "IC(Initial Construction)",
        "As-Built",
        "HOTO(Final)",
    ]

    # List to hold milestone data and status counts
    milestone_data = []

    for milestone in milestone_names:
        milestone_tasks = tasks.filter(milestone=milestone)
        nil_count = milestone_tasks.filter(status="Pending").count()
        inprogress_count = milestone_tasks.filter(status="In Progress").count()
        completed_count = milestone_tasks.filter(status="Completed").count()
        onhold_count = milestone_tasks.filter(status="On Hold").count()

        if nil_count > 0 or inprogress_count > 0 or completed_count > 0 or onhold_count > 0:
            milestone_data.append({
                'name': milestone,
                'nil_count': nil_count,
                'inprogress_count': inprogress_count,
                'completed_count': completed_count,
                'onhold_count': onhold_count,
            })

    # Static Gantt Chart Tasks (for Timeline Chart)
    gantt_tasks = [
        {
            "task": "Network Access Control Setup",
            "start": "2025-01-15",
            "end": "2025-02-15",
            "color": "red",
        },
        {
            "task": "Network Checkup",
            "start": "2025-01-20",
            "end": "2025-03-01",
            "color": "yellow",
        },
        {
            "task": "Signal Strength Test",
            "start": "2025-01-10",
            "end": "2025-02-28",
            "color": "red",
        },
        {
            "task": "Junction Box Maintenance",
            "start": "2025-02-01",
            "end": "2025-04-15",
            "color": "red",
        },
        {
            "task": "Power Supply Check",
            "start": "2025-02-10",
            "end": "2025-03-15",
            "color": "red",
        },
        {
            "task": "Network Connectivity Check",
            "start": "2025-02-05",
            "end": "2025-04-01",
            "color": "red",
        },
        {
            "task": "Port Forwarding Setup",
            "start": "2025-01-05",
            "end": "2025-08-20",
            "color": "red",
        },
        {
            "task": "Firewall Configuration Audit",
            "start": "2025-03-10",
            "end": "2025-09-25",
            "color": "red",
        },
        {
            "task": "Telephony Port Testing",
            "start": "2025-01-15",
            "end": "2025-06-30",
            "color": "red",
        },
        {
            "task": "Test Surveillance Camera Line",
            "start": "2025-01-20",
            "end": "2025-05-10",
            "color": "red",
        },
        {
            "task": "Check the Cable in Sultanganj Block",
            "start": "2025-03-01",
            "end": "2025-08-01",
            "color": "red",
        },
        {
            "task": "Network Health Monitoring",
            "start": "2025-03-15",
            "end": "2025-11-15",
            "color": "yellow",
        },
        {
            "task": "Outdoor Line Repair",
            "start": "2025-03-01",
            "end": "2025-07-01",
            "color": "yellow",
        },
        {
            "task": "Cable Checkup",
            "start": "2025-04-01",
            "end": "2025-08-30",
            "color": "green",
        },
    ]

    # Pass both milestone and gantt task data to the template
    return render(request, 'admin_dashboard.html', {
        'tasks': tasks,
        'milestone_data': milestone_data,
        'gantt_tasks': gantt_tasks,
    })





# Task Dashboard View
@login_required
def task_dashboard(request):
    return render(request, 'task_dashboard.html')

# user_management/views.py

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate using the Django auth system
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Login the user
            login(request, user)
            return redirect('admin_dashboard')  # Redirect to the dashboard if login is successful
        else:
            messages.error(request, "Invalid username or password.")  # Show error if login fails

    return render(request, 'login.html')  # Render login template


# Logout View
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

# User Management Views

# User List View for Admin: Display all users
@login_required
def user_list_admin(request):
    # Check if the user is an admin
    if not request.user.is_superuser:
        messages.error(request, "You do not have permission to access this page.")
        return redirect('admin_dashboard')  # Redirect if not admin
    
    users = User.objects.all()
    return render(request, 'user_list_admin.html', {'users': users})

# User List View for Normal User: Display their own details
@login_required
def user_list_user(request):
    # For normal users, show only their own information
    user = request.user
    return render(request, 'user_list_user.html', {'user': user})

# User Create View (Admin Only): Add new user
@login_required
def add_user(request):
    # Admins can add new users
    if not request.user.is_superuser:
        messages.error(request, "You do not have permission to add users.")
        return redirect('admin_dashboard')  # Redirect if not admin

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list_admin')  # Redirect to admin user list
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})

# User Update View (Admin Only): Edit existing user
@login_required
def update_user(request, pk):
    # Admins can update user details
    if not request.user.is_superuser:
        messages.error(request, "You do not have permission to edit users.")
        return redirect('admin_dashboard')  # Redirect if not admin
    
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list_admin')  # Redirect to admin user list
    else:
        form = UserForm(instance=user)
    return render(request, 'user_form.html', {'form': form})

# User Delete View (Admin Only): Remove user
@login_required
def delete_user(request, pk):
    # Admins can delete users
    if not request.user.is_superuser:
        messages.error(request, "You do not have permission to delete users.")
        return redirect('admin_dashboard')  # Redirect if not admin
    
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        messages.success(request, "User deleted successfully.")
        return redirect('user_list_admin')  # Redirect to admin user list
    return render(request, 'user_confirm_delete.html', {'user': user})

# Task Management Views

# # Task List View: Display all tasks
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from .forms import TaskForm
# from .models import Task

# # Task List View: Display all tasks
# @login_required
# def task_list(request):
#     tasks = Task.objects.all()  # Fetch all tasks from the database
#     return render(request, 'task_list.html', {'tasks': tasks})


# # Task Create View: Create a new task
# @login_required
# def create_task(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             task = form.save(commit=False)
#             task.save()
#             messages.success(request, "Task created successfully.")
#             return redirect('task_list')  # Redirect to task list after saving
#         else:
#             # Handle invalid form
#             print(form.errors)  # Print errors to console for debugging
#             messages.error(request, "There was an error creating the task. Please check the form.")
#     else:
#         form = TaskForm()

#     return render(request, 'task_form.html', {'form': form})






# # # Task Update View: Edit existing task
# @login_required
# def update_task(request, id):
#     task = get_object_or_404(Task, pk=id)  # Fetch task by ID or show 404 if not found
#     if request.method == 'POST':
#         form = TaskForm(request.POST, instance=task)  # Bind the form with the existing task instance
#         if form.is_valid():
#             form.save()  # Save the updated task
#             messages.success(request, "Task updated successfully.")
#             return redirect('task_list')  # Redirect to task list after update
#         else:
#             messages.error(request, "There was an error updating the task. Please check the form.")
#     else:
#         form = TaskForm(instance=task)  # Prefill the form with the task data

#     return render(request, 'task_form.html', {'form': form})


# # @login_required
# # def update_task(request, id):
# #     task = get_object_or_404(Task, pk=id)  # Fetch task by ID or show 404 if not found
# #     if request.method == 'POST':
# #         form = TaskForm(request.POST, instance=task)  # Bind the form with the existing task instance
# #         if form.is_valid():
# #             # Save the updated task
# #             form.save()
# #             messages.success(request, "Task updated successfully.")
# #             return redirect('task_list')  # Redirect to task list after update
# #         else:
# #             messages.error(request, "There was an error updating the task. Please check the form.")
# #     else:
# #         form = TaskForm(instance=task)  # Prefill the form with the task data

# #     return render(request, 'task_form.html', {'form': form})




# # Task Delete View: Remove a task from the database
# @login_required
# def delete_task(request, id):
#     task = get_object_or_404(Task, pk=id)  # Fetch task by ID or show 404 if not found
#     task.delete()  # Delete the task from the database
#     messages.success(request, "Task deleted successfully.")
#     return redirect('task_list')  # Redirect to task list after deletion




from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .models import Task

# ------------------------------
# Task List View: Display tasks with status filter
# ------------------------------
# @login_required
# def task_list(request):
#     status_filter = request.GET.get('status')  # Example: /tasks/?status=Pending

#     if status_filter:
#         tasks = Task.objects.filter(status=status_filter)
#     else:
#         tasks = Task.objects.all()
    
#     # Status counts
#     pending_count = Task.objects.filter(status='Pending').count()
#     inprogress_count = Task.objects.filter(status='In Progress').count()
#     completed_count = Task.objects.filter(status='Completed').count()
#     onhold_count = Task.objects.filter(status='On Hold').count()

#     context = {
#         'tasks': tasks,
#         'pending_count': pending_count,
#         'inprogress_count': inprogress_count,
#         'completed_count': completed_count,
#         'onhold_count': onhold_count,
#         'selected_status': status_filter
#     }
#     return render(request, 'task_list.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Task
from .forms import TaskForm

# ------------------------------
# Task List with Filtering
# ------------------------------
from django.shortcuts import render
from django.http import JsonResponse
from .models import Task  # Ensure to import the Task model

def task_list(request):
    tasks = Task.objects.all()  # Get all tasks

    # Handle filters (State and District) if selected
    state = request.GET.get('state')
    district = request.GET.get('district')

    if state:
        tasks = tasks.filter(state=state)

    if district:
        tasks = tasks.filter(district=district)

    # Milestone names based on your MILESTONE_CHOICES (excluding 'select Milestone')
    milestone_names = [
        "Desktop Survey Design",
        "Design/Network Health Checkup",
        "HOTO-Existing",
        "Detailed Design",
        "ROW(Right of way)",
        "IFC(Issued For Construction)",
        "IC(Initial Construction)",
        "As-Built",
        "HOTO(Final)",
    ]

    milestone_data = []  # To store milestone-related data

    for milestone in milestone_names:
        milestone_tasks = tasks.filter(milestone=milestone)

        nil_count = milestone_tasks.filter(status="Pending").count()
        inprogress_count = milestone_tasks.filter(status="In Progress").count()
        completed_count = milestone_tasks.filter(status="Completed").count()

        if nil_count > 0 or inprogress_count > 0 or completed_count > 0:
            milestone_data.append({
                'name': milestone,
                'nil_count': nil_count,
                'inprogress_count': inprogress_count,
                'completed_count': completed_count,
            })

    # Check if the request is an AJAX request
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'milestone_data': milestone_data,
            'selected_state': state,
            'selected_district': district,
        })

    # Return the data to the template context
    context = {
        'tasks': tasks,  # Pass the tasks to the template
        'milestone_data': milestone_data,
        'selected_state': state,
        'selected_district': district,
    }

    return render(request, 'task_dashboard.html', context)


# views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Task

# def task_list(request):
#     return render(request, 'task_list.html')

def get_filtered_milestones(request):
    # Get state and district from query parameters
    state = request.GET.get('state')
    district = request.GET.get('district')

    # Filter tasks based on state and district
    tasks = Task.objects.all()

    if state:
        tasks = tasks.filter(state=state)
    if district:
        tasks = tasks.filter(district=district)

    # Prepare data for milestones
    milestone_data = []
    milestone_names = ["Desktop Survey Design", "Design/Network Health Checkup", 
                       "HOTO-Existing", "Detailed Design", "ROW(Right of way)",
                       "IFC(Issued For Construction)", "IC(Initial Construction)", 
                       "As-Built", "HOTO(Final)"]

    for milestone in milestone_names:
        milestone_tasks = tasks.filter(task_name=milestone)

        nil_count = milestone_tasks.filter(status="Pending").count()
        inprogress_count = milestone_tasks.filter(status="In Progress").count()
        completed_count = milestone_tasks.filter(status="Completed").count()

        if nil_count > 0 or inprogress_count > 0 or completed_count > 0:
            milestone_data.append({
                'name': milestone,
                'nil_count': nil_count,
                'inprogress_count': inprogress_count,
                'completed_count': completed_count,
            })

    return JsonResponse(milestone_data, safe=False)



# ------------------------------
# Task Create View
# ------------------------------
@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.assign_to = request.user  # Optionally auto-assign to current user
            task.save()
            messages.success(request, "Task created successfully.")
            return redirect('task_list')
        else:
            messages.error(request, "There was an error creating the task. Please check the form.")
    else:
        form = TaskForm()

    return render(request, 'task_form.html', {'form': form, 'is_update': False})

# ------------------------------
# Task Update View
# ------------------------------
@login_required
def update_task(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully.")
            return redirect('task_list')
        else:
            messages.error(request, "There was an error updating the task. Please check the form.")
    else:
        form = TaskForm(instance=task)

    return render(request, 'task_form.html', {'form': form, 'is_update': True})

# ------------------------------
# Task Delete View
# ------------------------------
@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    messages.success(request, "Task deleted successfully.")
    return redirect('task_list')
