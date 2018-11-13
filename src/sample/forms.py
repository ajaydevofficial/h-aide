from django import forms
from django.contrib.auth import get_user_model
from user.models import Details,scheme
User = get_user_model()

class loginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={}))

	def clean_username(self):
		username = self.cleaned_data.get('username')
		qs = User.objects.filter(username=username)
		if not qs.exists():
			raise forms.ValidationError("Username invalid")
		return username

class registerForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={}))
	repassword = forms.CharField(widget=forms.PasswordInput(attrs={}))
	email = forms.CharField(widget=forms.TextInput(attrs={}))
	
	def clean(self):
		password = self.cleaned_data.get('password')
		repassword = self.cleaned_data.get('repassword')
		email = self.cleaned_data.get('email')
		qs = User.objects.filter(email=email)
		username = self.cleaned_data.get('username')
		query = User.objects.filter(username=username)
		flag = False
		if query.exists():
			raise forms.ValidationError("Username already taken!")
		try:		
			if(len(password)<6):
				raise forms.ValidationError("Password must contain atleast 6 characters!")
		except Exception as e:
			pass	
		if not password==repassword:
			raise forms.ValidationError("Passwords must match !")
		if qs.exists():
			raise forms.ValidationError("Email already taken!")
		elif not '@' in list(email):
			raise forms.ValidationError("Enter a valid email!")
		elif not '.' in list(email):
			raise forms.ValidationError("Enter a valid email!")	
		elif 'in' in email.split('.'):
			flag = True
		elif 'com' in email.split('.'):
			flag = True	
		elif flag == False:
			raise forms.ValidationError("Enter a valid email!")
		
	

class add_details(forms.Form):
	first_name = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control"}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control"}))
	address = forms.CharField(widget=forms.Textarea(attrs={"class" : "form-control"}))
	age = forms.IntegerField(widget=forms.NumberInput(attrs={"class" : "form-control"}))
	aadhar_id = forms.IntegerField(widget=forms.NumberInput(attrs={"class" : "form-control"}))
	disablity = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control"}))
	category = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control"}))
	percentage_disabliity = forms.DecimalField(widget=forms.NumberInput(attrs={"class" : "form-control"}))
	ward = forms.IntegerField(widget=forms.NumberInput(attrs={"class" : "form-control"}))
	house = forms.IntegerField(widget=forms.NumberInput(attrs={"class" : "form-control"}))
	village = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control"}))
	education = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control"}))
	job = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control"}))
	income = forms.DecimalField(widget=forms.NumberInput(attrs={"class" : "form-control"}))

	def clean_aadhar_id(self):
		aadhar_id = self.cleaned_data.get('aadhar_id')
		qs = Details.objects.filter(aadhar_id=aadhar_id)
		if qs.exists():
			raise forms.ValidationError("Aadhar ID already registered!")
		return aadhar_id

class applicationForm(forms.Form):
	aadhar_id = forms.IntegerField(widget=forms.NumberInput(attrs={"class" : "form-control"}))
	#scheme_id = forms.IntegerField(widget=forms.NumberInput(attrs={"class" : "form-control"}))

class schemeForm(forms.Form):
	scheme_name = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control"}))
	scheme_id = forms.IntegerField(widget=forms.NumberInput(attrs={"class" : "form-control"}))
	for_category  = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control"}))
	income_criteria = forms.IntegerField(widget=forms.NumberInput(attrs={"class" : "form-control"}))
	percentage_criteria = forms.IntegerField(widget=forms.NumberInput(attrs={"class" : "form-control"}))
	grant_amount = forms.IntegerField(widget=forms.NumberInput(attrs={"class" : "form-control"}))

	def clean_scheme_name(self):
		scheme_name = self.cleaned_data.get('scheme_name')
		qs = scheme.objects.filter(scheme_name=scheme_name)
		if qs.exists():
			raise forms.ValidationError("Scheme already exists!")
		return scheme_name

	def clean_scheme_id(self):
		scheme_id = self.cleaned_data.get('scheme_id')
		qs = scheme.objects.filter(scheme_id=scheme_id)
		if qs.exists():
			raise forms.ValidationError("Scheme ID already exists!")
		return scheme_id	