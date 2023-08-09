from django.shortcuts import render , redirect
from base.emails import send_emali_token
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect , HttpResponse
from .models import Profile
import uuid

# Create your views here.


def register_page(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username= email)
        if user_obj.exists():
            messages.warning(request, "Already exists your Email. Try another..")
            return HttpResponseRedirect(request.path_info)
        user_obj = User.objects.create(first_name = first_name, last_name= last_name, email = email, username = email)
        user_obj.set_password(password)
        p_obj = Profile.objects.create(
            user = user_obj,
            email_token = str(uuid.uuid4())
        )
        send_emali_token(email, p_obj.email_token)
        messages.success(request, "An email has been sent on your mail.")

    context = {}
    return render(request, 'register.html', context=context)


def verify(request, email_token):
    try:
        obj = Profile.objects.get(email_token = email_token)
        obj.is_verified = True
        obj.save()
        messages.success(request, "Congratulations! Your account is verified.")
        return redirect('register')
    except Exception as e:
        messages.warning(request, "Invalid Token!")
        return redirect('register')