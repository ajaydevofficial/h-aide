from django.shortcuts import render,redirect
from .forms import loginForm,registerForm,add_details,applicationForm,schemeForm
from django.contrib.auth import get_user_model,authenticate,login
from user.models import Details,scheme,application
from django.views.generic import ListView


def view_page(request):
	details = Details.objects.all()
	return render(request,"view_details.html")

def success_page(request):
	return render(request,"success.html")

def no_details(request):
	return render(request,"no_details.html")	

def no_schemes(request):
	return render(request,"no_schemes.html")

def home_page(request):
	return render(request,"home.html")

def login_page(request):
	myform = loginForm(request.POST or None) 
	context = {"form":myform}
	if myform.is_valid():
		username = myform.cleaned_data.get('username')
		password = myform.cleaned_data.get('password')
		print(myform.cleaned_data)
		user = authenticate(username=username,password=password)
		if not user==None:
			login(request,user)
			print(request.user.is_authenticated())
			return redirect(home_page)
		else:
			print("Login Failed")
			return render(request,"login.html",{"form":myform,"invalid":True})
	return render(request,"login.html",context)

User = get_user_model()
def register_page(request):
	regform = registerForm(request.POST or None)  
	context = {"form":regform}
	try:
		if regform.is_valid():
			username = regform.cleaned_data.get('username')
			password = regform.cleaned_data.get('password')
			email = regform.cleaned_data.get('email')
			newuser = User.objects.create_user(username,email,password)
			return redirect(home_page)
	except Exception as e:
		pass
	return render(request,"register.html",context)

def details_page(request):
	detailform = add_details(request.POST or None)
	context ={"form" : detailform}		
	if detailform.is_valid():
		try:
			if Details.objects.get(user_id=request.user.username):
				return render(request,"add_details.html",{"form":detailform,"invalid":True})
		except Exception as e:
			first_name = detailform.cleaned_data.get('first_name')
			last_name = detailform.cleaned_data.get('last_name')
			address = detailform.cleaned_data.get('address')
			age = detailform.cleaned_data.get('age')
			aadhar_id = detailform.cleaned_data.get('aadhar_id')
			disablity = detailform.cleaned_data.get('disablity')
			category = detailform.cleaned_data.get('category')
			percentage_disabliity = detailform.cleaned_data.get('percentage_disabliity')
			ward = detailform.cleaned_data.get('ward')
			house = detailform.cleaned_data.get('house')
			village = detailform.cleaned_data.get('village')
			education = detailform.cleaned_data.get('education')
			job = detailform.cleaned_data.get('job')
			income = detailform.cleaned_data.get('income')
			user_id = request.user.username
			Details.objects.create(fname=first_name,lname=last_name,address=address,age=age,aadhar_id=aadhar_id,disability=disablity,category=category,percentage_disabliity=percentage_disabliity,ward_number=ward,house_number=house,village=village,educational_qualification=education,job=job,income=income,user_id=user_id)
			return redirect(home_page)
		
	return render(request,"add_details.html",context)	
def apply(request):
	username = request.user.username
	context={}
	name =[]
	try:
		for_category = Details.objects.get(user_id=username).aadhar_id
		category = Details.objects.get(user_id=username).category
		scheme_list = scheme.objects.filter(for_category=category).values('scheme_name')
		context = {"object":for_category,"scheme":name}
		for i in scheme_list:
			name.append(i['scheme_name'])
		if request.method == "POST":
			scheme_name = request.POST['scheme']
			scheme_id = scheme.objects.get(scheme_name=scheme_name).scheme_id
			username = request.user.username
			aadhar_id = Details.objects.get(user_id=username).aadhar_id
			
			if application.objects.filter(aadhar_id=aadhar_id,scheme_id=scheme_id):
				context = {"object":for_category,"scheme":name,"flag":True}
				print(context)
				return render(request,"apply.html",context)
			fname = Details.objects.get(aadhar_id=aadhar_id).fname
			lname = Details.objects.get(aadhar_id=aadhar_id).lname
			age = Details.objects.get(aadhar_id=aadhar_id).age
			category = Details.objects.get(aadhar_id=aadhar_id).category
			income = Details.objects.get(aadhar_id=aadhar_id).income
			percentage = Details.objects.get(aadhar_id=aadhar_id).percentage_disabliity
			qualification = Details.objects.get(aadhar_id=aadhar_id).educational_qualification
			ward_number = Details.objects.get(aadhar_id=aadhar_id).ward_number
			house_number = Details.objects.get(aadhar_id=aadhar_id).house_number
			village = Details.objects.get(aadhar_id=aadhar_id).village
			for_category = scheme.objects.get(scheme_id=scheme_id).for_category
			income_criteria = scheme.objects.get(scheme_id=scheme_id).income_criteria
			percentage_criteria = scheme.objects.get(scheme_id=scheme_id).percentage_criteria
			grant_amount = scheme.objects.get(scheme_id=scheme_id).grant_amount
			application.objects.create(fname=fname,lname=lname,age=age,aadhar_id=aadhar_id,category=category,income=income,percentage=percentage,qualification=qualification,ward_number=ward_number,house_number=house_number,village=village,scheme_name=scheme_name,scheme_id=scheme_id,for_category=for_category,income_criteria=income_criteria,percentage_criteria=percentage_criteria,grant_amount=grant_amount)
			return redirect(success_page)

	except Exception as e:
		fname = Details.objects.get(aadhar_id=aadhar_id).fname
		lname = Details.objects.get(aadhar_id=aadhar_id).lname
		age = Details.objects.get(aadhar_id=aadhar_id).age
		category = Details.objects.get(aadhar_id=aadhar_id).category
		income = Details.objects.get(aadhar_id=aadhar_id).income
		percentage = Details.objects.get(aadhar_id=aadhar_id).percentage_disabliity
		qualification = Details.objects.get(aadhar_id=aadhar_id).educational_qualification
		ward_number = Details.objects.get(aadhar_id=aadhar_id).ward_number
		house_number = Details.objects.get(aadhar_id=aadhar_id).house_number
		village = Details.objects.get(aadhar_id=aadhar_id).village
		for_category = scheme.objects.get(scheme_id=scheme_id).for_category
		income_criteria = scheme.objects.get(scheme_id=scheme_id).income_criteria
		percentage_criteria = scheme.objects.get(scheme_id=scheme_id).percentage_criteria
		grant_amount = scheme.objects.get(scheme_id=scheme_id).grant_amount
		application.objects.create(fname=fname,lname=lname,age=age,aadhar_id=aadhar_id,category=category,income=income,percentage=percentage,qualification=qualification,ward_number=ward_number,house_number=house_number,village=village,scheme_name=scheme_name,scheme_id=scheme_id,for_category=for_category,income_criteria=income_criteria,percentage_criteria=percentage_criteria,grant_amount=grant_amount)
		return redirect(success_page)
		print(e)
	return render(request,"apply.html",context)
	
def scheme_page(request):
	schemeform = schemeForm(request.POST or None)
	context ={"form" : schemeform}		
	if schemeform.is_valid():
		scheme_name = schemeform.cleaned_data.get('scheme_name')
		scheme_id = schemeform.cleaned_data.get('scheme_id')
		for_category  = schemeform.cleaned_data.get('for_category')
		income_criteria = schemeform.cleaned_data.get('income_criteria')
		percentage_criteria = schemeform.cleaned_data.get('percentage_criteria')
		grant_amount = schemeform.cleaned_data.get('grant_amount')
		scheme.objects.create(scheme_name=scheme_name,scheme_id=scheme_id,for_category=for_category,income_criteria=income_criteria,percentage_criteria=percentage_criteria,grant_amount=grant_amount)
		return redirect(success_page)
	return render(request,"add_schemes.html",context)				