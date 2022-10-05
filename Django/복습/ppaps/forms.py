from django import forms
from .models import Review

# Ariticle 모델에 있는 모든 Form을 가져다 쓰겠다.
class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['title', 'content']