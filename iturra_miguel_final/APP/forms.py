from django import forms
from .models import Instituciones, Inscritos

class FormInstitucion(forms.ModelForm):
    class Meta:
        model = Instituciones
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form_control'})
        }

class FormInscritos(forms.ModelForm):
    

    institucion = forms.ModelChoiceField(queryset=Instituciones.objects.all(), widget=forms.Select(attrs={'class': 'form_control'}))

    class Meta:
        model = Inscritos
        fields = '__all__'
        ESTADO_CHOICES = [
        ('Reservado', 'RESERVADO'),
        ('Completada', 'COMPLETADA'),
        ('Anulada', 'ANULADA'),
        ('No asisten', 'NO ASISTEN'),
    ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form_control'}),
            'telefono': forms.TextInput(attrs={'class': 'form_control'}),
            'fechaInscripcion': forms.DateInput(attrs={'type': 'date'}),
            'horaInscripcion': forms.TextInput(attrs={'type': 'time'}),
            'estado': forms.Select(choices=ESTADO_CHOICES, attrs={'class': 'form_control'}),
            'observacion': forms.Textarea(attrs={'class': 'form_control'})
        }