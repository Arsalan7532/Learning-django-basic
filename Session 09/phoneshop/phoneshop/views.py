from django.shortcuts import render,redirect
from products.models import Product
from .models import Email
def homepage(request):
    products = Product.objects.all()
    loggedIn = False
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        loggedIn = True
    return render(request, 'home.html', {'products': products, 'loggedIn': loggedIn})
def subscribe (request):
    if request.method == "POST":
        email_value=request.POST.get('email')
        if email_value and not Email.objects.filter(email=email_value).exists():
            email=Email()
            email.email=email_value
            email.save()
            return redirect ('home')
    return render(request, 'home.html', {
        'products': Product.objects.all(),
        'loggedIn': 'user_id' in request.session,
        'error': 'لطفاً ایمیل معتبر وارد کنید یا ایمیل قبلاً ثبت شده است'
    })        