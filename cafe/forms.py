from django import forms

from .models import Booking

TIME_CHOICES =     (('Start', '---------'),
                    ('10:00-11:00', '10:00 - 11:00'),
                    ('11:00-12:00', '11:00 - 12:00'),
                    ('12:00-13:00', '12:00 - 13:00'),
                    ('13:00-14:00', '13:00 - 14:00'),
                    ('14:00-15:00', '14:00 - 15:00'),
                    ('15:00-16:00', '15:00 - 16:00'),
                    ('16:00-17:00', '16:00 - 17:00'),
                    ('17:00-18:00', '17:00 - 18:00'),
                    ('18:00-19:00', '18:00 - 19:00'),
                    ('19:00-20:00', '19:00 - 20:00'),
                    ('20:00-21:00', '20:00 - 21:00'),
                    ('21:00-22:00', '21:00 - 22:00'),
                    ('22:00-23:00', '22:00 - 23:00'),)

class Booking_Form(forms.ModelForm):

    date = forms.DateField(label='Дата визита', widget=forms.SelectDateWidget())
    time = forms.ChoiceField(label='Время визита', choices=TIME_CHOICES)

    class Meta:
        model = Booking
        fields = [
            'district',
            'person_name',
            'date',
            'time',
            'person_quantity',
            'phone',
            'comment',
        ]