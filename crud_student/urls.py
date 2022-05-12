from django.urls import path, include
from crud_student import views


urlpatterns = [
    path('',views.initial),
    path('student_add',views.student_add),
    path('show',views.show),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delete)

]
