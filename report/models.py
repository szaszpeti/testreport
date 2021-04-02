from django.db import models

# Create your models here.
from django.db import models
import sys
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from pyuploadcare.dj.models import ImageField


# Create your models here.

class Technician(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Operation(models.Model):
	location = models.CharField(max_length=50, null=True)
	wtg_number = models.CharField(max_length=200, null=True)
	wtg_id = models.CharField(max_length=200, null=True)
	set_nummber = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	name_1 = models.CharField(max_length=200, null=True)
	company_1 = models.CharField(max_length=200, null=True)
	name_2 = models.CharField(max_length=200, null=True)
	company_2 = models.CharField(max_length=200, null=True)
	name_3 = models.CharField(max_length=200, null=True, blank=True)
	company_3 = models.CharField(max_length=200, null=True, blank=True)
	name_4 = models.CharField(max_length=200, null=True, blank=True)
	company_4 = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return f'{self.location + " - " + self.wtg_id}'

class Blade(models.Model):
	operation = models.ForeignKey(Operation, default=None, null=True, on_delete= models.SET_NULL)
	
	A = 'A'
	B = 'B'
	C = 'C'

	CODE = [(A, 'A'),
	(B, 'B'),
	(C, 'C'),
	]

	blade_code = models.CharField(choices=CODE, max_length=200, null=True)
	blade_number = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return f'{self.blade_code + " - " + self.blade_number}'

class Inspection(models.Model):

	blade = models.ForeignKey(Blade, default=None, null=True, on_delete= models.SET_NULL)
	damage_id = models.CharField(max_length=50, null=True)
	

	LE = 'Leading Edge'
	TE = 'Trailing Edge'
	PS = 'Preassure Side'
	SS = 'Suction Side'


	AREA = [(LE, 'Leading Edge'),
			(TE, 'Trailing Edge'),
			(PS, 'Preassure Side'),
			(SS, 'Suction Side') ]

	area = models.CharField(choices=AREA, max_length=15, null=True)
	
	ROOT_COATING = 'Root Coating'
	DEFECT_ON_VORTEX_GENERATORS = 'Defect on Vortex Generators'
	PINHOLE = 'Pinhole'
	TRANSPORT_DAMAGE = 'Transport Damage'
	CHIPPED_PAINT = 'Chipped Paint'
	SUPERFICIAL_CRACK = 'Superficial Crack'
	EROSION = 'Erosion'
	EROSION_WITH_EXPOSED_LAMINATE = 'Erosion with Exposed Laminate'
	LIGTHNING_STRIKE = 'Ligthning Strike'
	DAMAGED_RECEPTRO = 'Damaged Receptor'
	DRAINHOLE = 'Drainhole'

	DESCRIPTION = [(ROOT_COATING, 'Root Coating'),
				(DEFECT_ON_VORTEX_GENERATORS, 'Defect on Vortex Generators'),
				(PINHOLE, 'Pinhole'),
				(TRANSPORT_DAMAGE, 'Transport Damage'),
				(CHIPPED_PAINT, 'Chipped Paint'),
				(SUPERFICIAL_CRACK, 'Superficial Crack'),
				(EROSION, 'Erosion'),
				(EROSION_WITH_EXPOSED_LAMINATE, 'Erosion with Exposed Laminate'),
				(LIGTHNING_STRIKE, 'Ligthning Strike'),
				(DAMAGED_RECEPTRO, 'Damaged Receptor'),
				(DRAINHOLE, 'Drainhole'),
				]

	description = models.CharField(choices=DESCRIPTION, max_length=30, null=True)
	category = models.CharField(max_length=15, null=True)
	comments = models.CharField(max_length=100, null=True)
	image_1 = ImageField(manual_crop="", blank=True)
	image_2 = ImageField(manual_crop="", blank=True)



	def get_absolute_url(self):
		return reverse('inspection_details', kwargs={'pk': self.pk})

	def __str__(self):
		return f'{self.blade.blade_number + " - " + self.damage_id}'
