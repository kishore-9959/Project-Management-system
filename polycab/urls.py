"""
URL configuration for polycab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('users/', include('user_management.urls')),
#     path('', include('user_management.urls')),  # For root URL
    
# ]

# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     # Default Django Admin Panel
#     path('admin/', admin.site.urls),
    
#     # Include your app's URLs only once, for example for 'users/' path
#     path('users/', include('user_management.urls')),
    
#     # Optionally include user_management URLs at the root if needed
#     # path('', include('user_management.urls')),  # Only include if needed for the root path
    
# ]



# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),  # Default Django Admin Panel
#     path('users/', include('user_management.urls')),  # User management URLs
#     path('tasks/', include('user_management.urls')),
# ]


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include your app urls
    path('', include('user_management.urls')),  # 👈 Add this line
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



