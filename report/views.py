from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import Group
from django.urls import reverse

from datetime import timedelta, date, time
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
import csv
from .doctest import report
# Create your views here.
from .models import *
from .forms import *
#from .filters import InspectionFilter



# Create your views here.
def home(request):

	operation = Operation.objects.all()
	inspection = Inspection.objects.all()


	context = {'operation':operation, 'inspection':inspection}

	return render(request, 'report/home.html', context)


def prework(request):

	return render(request, 'report/prework.html')


def inspectionDetail(request, pk):
	blade = Blade.objects.get(id=pk)

	inspection = blade.inspection_set.all()

	#report(operation, inspection)

	

	context = {'blade':blade, 'inspection':inspection}
	return render(request, 'report/inspection_detail.html', context)

def bladeDetail(request, pk):
	operation = Operation.objects.get(id=pk)

	blades = operation.blade_set.all()

	#report(operation, inspection)

	

	context = {'operation':operation, 'blades':blades}
	return render(request, 'report/blade_detail.html', context)

def createOperation(request):
	form = OperationForm()

	if request.method == 'POST':
		form = OperationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
			
	context = {'form':form}
	return render(request, 'report/operation_form.html', context)

def createBlade(request, pk):
	BladeFormset = inlineformset_factory(Operation, Blade, fields='__all__', extra=3)
	operation = Operation.objects.get(id=pk)
	formset = BladeFormset(queryset=Blade.objects.none(), instance=operation)

	if request.method == 'POST':
		form = BladeForm(request.POST)
		formset = BladeFormset(request.POST, instance=operation)

		if formset.is_valid():
			formset.save()
			return redirect('/')
			
	context = {'form':formset}
	return render(request, 'report/blade_form.html', context)


def createInspection(request, pk):
	InspectionFormSet = inlineformset_factory(Blade, Inspection, fields='__all__', extra=3)      
	blade = Blade.objects.get(id=pk)
	formset = InspectionFormSet(queryset=Inspection.objects.none(), instance=blade)
	#form = InspectionForm()

	if request.method == 'POST':
		form = InspectionForm(request.POST)
		formset = InspectionFormSet(request.POST, instance=blade)
		if formset.is_valid():
			formset.save()
			return redirect('/')

		# if form.is_valid():
		# 	form.save()
		# 	return redirect('/')

	context = {'form':formset}
	return render(request, 'report/inspection_form.html', context)


def updateOperation(request, pk):
	operation = Operation.objects.get(id=pk)
	form = OperationForm(instance=operation)

	if request.method == 'POST':

		form = OperationForm(request.POST, instance=operation)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'report/operation_form.html', context)

def updateBlade(request, pk):
	blade = Blade.objects.get(id=pk)
	form = BladeForm(instance=blade)

	if request.method == 'POST':

		form = BladeForm(request.POST, instance=blade)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'report/blade_update_form.html', context)

def updateInspection(request, pk):
	inspection = Inspection.objects.get(id=pk)
	form = InspectionForm(instance=inspection)

	if request.method == 'POST':

		form = InspectionForm(request.POST, instance=inspection)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'report/inspection_update_form.html', context)

def deleteOperation(request, pk):
	operation = Operation.objects.get(id=pk)
	if request.method == "POST":
		operation.delete()
		reverse('/')

	context = {'item':operation}
	return render(request, 'report/delete_operation.html', context)

def deleteBlade(request, pk):
	blade = Blade.objects.get(id=pk)
	if request.method == "POST":
		blade.delete()
		return redirect('/')

	context = {'item':blade}
	return render(request, 'report/delete_blade.html', context)

def deleteInspection(request, pk):
	inspection = Inspection.objects.get(id=pk)
	bladeid = inspection.blade
	print(bladeid)
	if request.method == "POST":
		inspection.delete()
		return redirect('/')

	context = {'item':inspection}
	return render(request, 'report/delete_inspection.html', context)