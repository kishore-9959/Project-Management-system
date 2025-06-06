
# from django import forms
# from .models import User  # your User model

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super(UserForm, self).__init__(*args, **kwargs)
#         if 'password' in self.fields:
#             self.fields['password'].widget = forms.PasswordInput()




from django import forms
from .models import User  # Your custom User model

class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        required=False,  # Make password optional on update
        help_text="Leave blank to keep the current password."
    )

    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        # Optional: Hide password in form if needed
        if 'instance' in kwargs and kwargs['instance']:
            self.fields['password'].required = False

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password and self.instance.pk:
            # Keep existing password if none provided
            return self.instance.password
        return password




        
     



# from django import forms
# from .models import Task
# from django.contrib.auth.models import User

# class TaskForm(forms.ModelForm):
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

#     state = forms.ChoiceField(choices=Task.STATE_CHOICES)
#     district = forms.ChoiceField(choices=[], required=False)

#     class Meta:
#         model = Task
#         fields = [
#             'task_name', 'subtasks', 'milestone', 'assign_to', 
#             'state', 'district', 'business_area', 'block',
#             'start_date', 'end_date', 'status'
#         ]
#         widgets = {
#             'district': forms.Select(attrs={'class': 'form-control'}),
#             'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
#             'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
#         }

#     def __init__(self, *args, **kwargs):
#         super(TaskForm, self).__init__(*args, **kwargs)

#         self.fields['assign_to'].queryset = User.objects.filter(is_staff=True)
#         self.fields['state'].choices = Task.STATE_CHOICES
#         self.fields['district'].choices = [('', 'Select District')]

#         # Case 1: when user is submitting the form
#         if 'state' in self.data:
#             state = self.data.get('state')
#             if state in self.STATE_DISTRICT_CHOICES:
#                 self.fields['district'].choices += self.STATE_DISTRICT_CHOICES[state]

#         # Case 2: when editing existing task but not changing state
#         elif self.instance and self.instance.pk:
#             state = self.instance.state
#             district = self.instance.district
#             if state in self.STATE_DISTRICT_CHOICES:
#                 self.fields['district'].choices += self.STATE_DISTRICT_CHOICES[state]
#             self.initial['district'] = district

#         # Optional: make dates not required in update mode
#         if self.instance and self.instance.pk:
#             self.fields['start_date'].required = False
#             self.fields['end_date'].required = False

#     def clean(self):
#         cleaned_data = super().clean()
#         state = cleaned_data.get('state')
#         district = cleaned_data.get('district')

#         if district and state and state in self.STATE_DISTRICT_CHOICES:
#             valid_districts = dict(self.STATE_DISTRICT_CHOICES[state])
#             if district not in valid_districts:
#                 raise forms.ValidationError("Invalid district selected.")

#         return cleaned_data



from django import forms
from .models import Task
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
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

    state = forms.ChoiceField(choices=Task.STATE_CHOICES)
    district = forms.ChoiceField(choices=[], required=False)

    class Meta:
        model = Task
        fields = [
            'task_name', 'subtasks', 'milestone', 'assign_to', 
            'state', 'district', 'business_area', 'block',
            'start_date', 'end_date', 'status'
        ]
        # fields = '__all__'
        widgets = {
            'district': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)

        self.fields['assign_to'].queryset = User.objects.filter(is_staff=True)
        self.fields['state'].choices = Task.STATE_CHOICES
        self.fields['district'].choices = [('', 'Select District')]

        # If POST data is present (form is submitted)
        if 'state' in self.data:
            state = self.data.get('state')
            if state in self.STATE_DISTRICT_CHOICES:
                self.fields['district'].choices += self.STATE_DISTRICT_CHOICES[state]

        # Else: Form is in edit mode
        elif self.instance and self.instance.pk:
            state = self.instance.state
            district = self.instance.district
            if state in self.STATE_DISTRICT_CHOICES:
                self.fields['district'].choices += self.STATE_DISTRICT_CHOICES[state]
            self.initial['district'] = district

        # Optional: make dates not required in update mode
        if self.instance and self.instance.pk:
            self.fields['start_date'].required = False
            self.fields['end_date'].required = False

    def clean(self):
        cleaned_data = super().clean()
        state = cleaned_data.get('state')
        district = cleaned_data.get('district')

        if district and state and state in self.STATE_DISTRICT_CHOICES:
            valid_districts = dict(self.STATE_DISTRICT_CHOICES[state])
            if district not in valid_districts:
                raise forms.ValidationError("Invalid district selected.")

        return cleaned_data


