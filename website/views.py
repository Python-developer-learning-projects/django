from django.shortcuts import render, redirect
from .models import Member
from .forms import MemberForm
from django.contrib import messages


# Create your views here.
def home(request):
    all_members = Member.objects.all
    return render(request, 'home.html', {'all': all_members})


def join(request):
    if request.method == "POST":
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            fname = request.POST['fname']
            lname = request.POST['lname']
            age = request.POST['age']
            email = request.POST['email']
            messages.success(request, "There was an error! Please try again...")
            return render(request, 'join.html', {
                'fname': fname,
                'lname': lname,
                'age': age,
                'email': email
            })
        messages.success(request, 'Your form has been submit successfully !')
        return redirect('home')

    else:
        return render(request, 'join.html', {})
