from resume.admin import LanguageAdmin
from django.shortcuts import redirect, render
from .models import Languages, Profile, Project, Contact, ContactMe

# Create your views here.

def profile(request):
    if request.method == "GET":
        p = Profile.objects.get(id=1)
        lang = Languages.objects.all()
        project = Project.objects.all().order_by("-id")
        contact = Contact.objects.get(id=1)
        return render(request,"index.html",{"p":p,"lang":lang,"project":project,"contact":contact})
    else:
        obj = ContactMe()
        obj.name = request.POST["name"]
        obj.email = request.POST["email"]
        obj.subject = request.POST["subject"]
        obj.message = request.POST["message"]
        obj.save()
        return redirect(profile)