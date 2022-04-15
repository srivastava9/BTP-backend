from django.urls import path
from .views import *

urlpatterns = [
    path(
        "<str:factory_id>/employees",
        ListEmployeesView.as_view(),
        name="List of Employees",
    )
]
