# task_manager/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from tasks_app.views import TaskListCreate, TaskUpdate, TaskDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),  # GET e POST
    path('tasks/<int:pk>/update/', TaskUpdate.as_view(), name='task-update'),  # PUT
    path('tasks/<int:pk>/delete/', TaskDelete.as_view(), name='task-delete'),  # DELETE
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
