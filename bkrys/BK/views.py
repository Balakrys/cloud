from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.contrib import auth,messages
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.sessions.models import Session
from django import forms
from django.conf import settings
from django.core.mail import send_mail


# from captcha.fields import ReCaptchaField

# 
# from django.contrib.auth import logout
# from django.shortcuts import redirect

# def logout_view(request):
#     logout(request)
#     return redirect('real')
# def home(request):
# 	text = """<h1>welcome to my app !</h1>"""
# 	

# Create your views here.
from django.shortcuts import render
from BK.forms import realform
from BK.models import real

@login_required(login_url='/accounts/login/')
def hello(request):
	if request.method=="POST":
		form=realform(request.POST)
		if form.is_valid():
			
			username=request.POST.get('username','')
			password=request.POST.get('password','')
			message=request.POST.get('message','')
			real_obj=real(username=username,password=password,message=message)
			real_obj.save()
			request.session['username'] = username
			request.session['password'] = password
			print message
			# session_key = request.COOKIES["sessionid"]
			# session = Session.objects.get(session_key=session_key)

			# remaining_seconds = session.get_expiry_age()
			# response= render_to_response(request, "form.html",context_instance = RequestContext(request))
			# response.set_cookie('last_connection', datetime.datetime.now())
			# response.set_cookie('username', datetime.datetime.now())
			subject="hey whatssup"
			message=request.POST.get('message','')
			from_email=settings.EMAIL_HOST_USER
			to_list=["shbakrys@gmail.com"]
			send_mail(subject,message,from_email,to_list,fail_silently=True)
			return render(request,"form.html",locals())
   			# return response
			# user = authenticate(userusername='john', password='password')
		
			# return HttpResponse("hi")
			obj=real.objects.all()
			# send_mail(sub,msg,fromemail,to,fail_silently=true)
			
			# return render(request,"hello.html",{"obj": obj})	
	else:
		form=realform()


	# return HttpResponse("hey")

	return render(request, "form.html", {'form':form})
# @logout_required(logout_url='/accounts/logout/')
def search(request):
	obj=real.objects.all()
	
	return render(request,"hello.html",{"obj": obj})	
def logout(request):
	return HttpResponse("logged out")

# @login_required(login_url='/accounts/login/')
# def login(request):

# 	c={}
# 	c.update(csrf(request))
# 	print c
# 	return render('form.html',c)
# def auth(request):
# 	if request.method=="POST":
# 		username =request.POST.get('username','')
# 		password =request.POST.get('password','')
# 		user=auth.authenticate(username=username,password=password)

# 		if user is not None:
# 			auth.login(request,user)
# 			text="valid"
# 			print "valid"
# 			obj=real.objects.all()
	
# 			return render(request,"hello.html",{"obj": obj})
	
# 		else:
# 			text="inavlid"
# 			obj=real.objects.all()
	
# 			return render(request,"hello.html",{"obj": obj})
# def login(request):
#    username = 'not logged in'
   
#    if request.method == 'POST':
#       MyLoginForm = LoginForm(request.POST)
      
#       if MyLoginForm.is_valid():
#          username = MyLoginForm.cleaned_data['username']
#          request.session['username'] = username
#       else:
#          MyLoginForm = LoginForm()
			
#    return render(request, 'loggedin.html', {"username" : username}
def formView(request):
	if request.session.has_key('username') and request.session.has_key('password'):
		username = request.session['username']
		password=request.session['password']
		print password
		return HttpResponse("hey you are logged in"+' '+username+" " + password)
		# return render(request, 'loggedin.html', {"username" : username})
	else:
		return render(request, 'login.html', {})
def formcook(request):
	if 'username' in request.COOKIES and 'last_connection' in request.COOKIES:
		username = request.COOKIES['username']
		last_connection = request.COOKIES['last_connection']
      	last_connection_time = datetime.datetime.strptime(last_connection[:-7], 
         "%Y-%m-%d %H:%M:%S")
      	if (datetime.datetime.now() - last_connection_time).seconds < 10:
      		print username
        	return render(request, 'loggedin.html', {"username" : username})
      	else:
        	return render(request, 'login.html', {})
    # else:
   	# 	return render(request, 'login.html', {})    