from django import forms
from .models import UserDetail, Blog, QuizQuestion

class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ['name', 'employee_id', 'department']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['employee_id'].widget.attrs['placeholder'] = 'Employee ID'
        self.fields['employee_id'].label = ''

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'volume', 'part', 'content', 'published_date', 'week', 'image']

class QuizQuestionForm(forms.ModelForm):
    class Meta:
        model = QuizQuestion
        fields = ['question_text', 'option1', 'option2', 'option3', 'option4', 'correct_option']
