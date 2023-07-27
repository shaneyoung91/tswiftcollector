from django.forms import ModelForm
from .models import DatingHistory

class DatingHistoryForm(ModelForm):
    class Meta:
        model = DatingHistory
        fields = ['partner_name', 'start_date', 'end_date']