from .models import Info
from django.forms import ModelForm, TextInput, Textarea

class InfoForm(ModelForm):
    class Meta:
        model = Info
        fields = ["title_message", "message"]
        widgets = {
            "title_message": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название пожелания'
            }),
            "message": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'введите описание'
            }),
        
        }