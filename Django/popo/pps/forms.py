from django import forms
from .models import Article

# Ariticle 모델에 있는 모든 Form을 가져다 쓰겠다.
class PpsForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = '__all__'