from django.urls import path

from .views import registerUser, loginUser, logoutUser, dashboard, userIndex

app_name = "user"

urlpatterns = [
    path('', userIndex),
    path('register/', registerUser, name="register"),
    path('login/', loginUser, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('dashboard/', dashboard, name="dashboard")
]