from django.shortcuts import render
from admins.models import Portfolio, Gallery
# Create your views here.
def home(request):
    return render(request, "main/index.html")

def about(request):
    return render(request, "main/about.html")

def blog(request):
    return render(request, "main/blog.html")

def career(request):
    return render(request, "main/carrer.html")

def contact(request):
    return render(request, "main/contact.html")

def corporate(request):
    return render(request, "main/corporate.html")

def entertainment(request):
    return render(request, "main/entertainment.html")

def exhibition(request):
    return render(request, "main/exhibition.html")

def facilities(request):
    return render(request, "main/facilities.html")

def faq(request):
    return render(request, "main/FAQ.html")

def gallery(request):
    images = Gallery.objects.all().order_by('-created_at')
    return render(request, "main/gallery.html", {'images': images})

def plan_event(request):
    return render(request, "main/plan-event.html")

def privacy(request):
    return render(request, "main/privacy.html")

def product_launch(request):
    return render(request, "main/product_launch.html")

def portfolio(request):
    portfolios = Portfolio.objects.all().order_by('-created_at')
    return render(request, "main/portfolio.html", {'portfolios': portfolios})

def services(request):
    return render(request, "main/services.html")

def social_events(request):
    return render(request, "main/social_events.html")

def terms(request):
    return render(request, "main/terms.html")

def themes(request):
    return render(request, "main/themes.html")

def wedding(request):
    return render(request, "main/wedding.html")