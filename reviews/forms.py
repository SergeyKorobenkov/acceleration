from django import forms
from .models import Review
from django.forms import ModelForm

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('job_status', 'reply', 'replies_from_employer', 'test_tasks', 'offers', 'comment')
        widgets = {
            'text': forms.Textarea,
        }