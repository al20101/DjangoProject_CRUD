from django import forms
from crud_student.models import Students

class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = "__all__"