from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        
        # ارسال ایمیل (اختیاری)
        send_mail(
            f"پیام جدید از {name}",
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],  # ایمیل گیرنده
            fail_silently=True,
        )
        
        return HttpResponseRedirect("/contact/?success=True")
    
    return render(request, "contact/contact.html")
