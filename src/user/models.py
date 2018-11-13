from django.db import models

# Create your models here.
class Details(models.Model):

	# Personal Details
	fname = models.CharField(max_length=50)
	lname = models.CharField(max_length=50)
	address = models.TextField()
	age = models.DecimalField(default=0,max_digits=20,decimal_places=0)
	aadhar_id = models.DecimalField(default=0,max_digits=20,decimal_places=0)

	# Disability Details
	disability = models.CharField(max_length=50,null=True)
	category = models.CharField(max_length=50,null=True)
	percentage_disabliity = models.DecimalField(default=0,max_digits=4,decimal_places=2)

	# Ward Detials
	ward_number = models.DecimalField(default=0,max_digits=3,decimal_places=0)
	house_number = models.DecimalField(default=0,max_digits=3,decimal_places=0)
	village = models.CharField(max_length=50,null=True)

    # Educational Details
	educational_qualification = models.CharField(max_length=50,null=True)

    # Job and Income
	job = models.CharField(max_length=50,null=True)
	income = models.DecimalField(default =0,max_digits=50,decimal_places=2)

    # Alloted scheme
	scheme_name = models.CharField(max_length=50,null=True)
	scheme_id = models.DecimalField(default =0,max_digits=5,decimal_places=0)

	# Owner ID
	user_id = models.CharField(max_length=20,null=True)

	def __str__(self):
		return self.fname

	def __unicode__(self):
		return self.fname

class scheme(models.Model):
	
	scheme_name = models.CharField(max_length=50)
	scheme_id = models.DecimalField(default =0,max_digits=5,decimal_places=0)
	for_category  = models.CharField(max_length=20)
	income_criteria = models.DecimalField(default=50000,max_digits=20,decimal_places=2)
	percentage_criteria = models.DecimalField(default=0,max_digits=4,decimal_places=2)
	grant_amount = models.DecimalField(default=0,max_digits=20,decimal_places=0)

	def __str__(self):
		return self.scheme_name

	def __unicode__(self):
		return self.scheme_name

class application(models.Model):
	
	fname = models.CharField(max_length=50)
	lname = models.CharField(max_length=50)
	age = models.DecimalField(default=0,max_digits=20,decimal_places=0)
	aadhar_id = models.DecimalField(default=0,max_digits=20,decimal_places=0)
	category  = models.CharField(max_length=20)
	income = models.DecimalField(default=50000,max_digits=20,decimal_places=2)
	percentage = models.DecimalField(default=0,max_digits=4,decimal_places=2)
	qualification = models.CharField(max_length=50,null=True)
	ward_number = models.DecimalField(default=0,max_digits=3,decimal_places=0)
	house_number = models.DecimalField(default=0,max_digits=3,decimal_places=0)
	village = models.CharField(max_length=50,null=True)
	scheme_name = models.CharField(max_length=50)
	scheme_id = models.DecimalField(default =0,max_digits=5,decimal_places=0)
	for_category  = models.CharField(max_length=20,null=True)
	income_criteria = models.DecimalField(default=50000,max_digits=20,decimal_places=2)
	percentage_criteria = models.DecimalField(default=0,max_digits=4,decimal_places=2)
	grant_amount = models.DecimalField(default=0,max_digits=20,decimal_places=0)

	def __str__(self):
		return self.scheme_name

	def __unicode__(self):
		return self.scheme_name