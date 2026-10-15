from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'content', 'is_completed']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '할 일을 입력하세요 (필수)'}),
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': '세부 내용 (선택)'}),
        }