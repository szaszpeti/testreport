from django.forms import ModelForm
from django import forms

from .models import *
from pyuploadcare.dj.forms import ImageField






class OperationForm(forms.ModelForm):
	class Meta:
		model = Operation
		fields = '__all__'
		exclude = ['user']

class InspectionForm(forms.ModelForm):
	image_1 = ImageField(label='image')
	class Meta:
		model = Inspection
		fields = '__all__'

class BladeForm(forms.ModelForm):
	class Meta:
		model = Blade
		fields = '__all__'
