from django import forms
from .models import reservations,menu
TIME_CHOICES = [
    ('12:00', '12:00 PM'),
    ('13:00', '1:00 PM'),
    ('14:00', '2:00 PM'),
    ('14:00', '3:00 PM'),
    ('14:00', '4:00 PM'),
    ('14:00', '5:00 PM'),
    # Add more time slots as needed
]
class reservation_form(forms.ModelForm):
    time = forms.ChoiceField(choices=TIME_CHOICES)
    class Meta:
        model = reservations
        fields = ['name', 'reservation_slot', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
class MenuItemForm(forms.ModelForm):
    class Meta:
        model = menu
        fields = ['name', 'description', 'price']