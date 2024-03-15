from django.contrib import admin
from django.urls import include, path
from my_app import views as my_app_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_app.urls'))
]
