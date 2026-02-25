from django.shortcuts import render, redirect
from admins.models import Portfolio, Gallery, FeaturedEvent, Testimonial
from main.models import EventBooking
# Create your views here.
def home(request):
    featured_events = FeaturedEvent.objects.filter(is_active=True).order_by('-created_at')
    testimonials = Testimonial.objects.all().order_by('-created_at')

    return render(request, "main/index.html", {
        "featured_events": featured_events,
        "testimonials": testimonials,
    })
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
    if request.method == "POST":
        print("\n🟢 ------------- FORM SUBMITTED ------------- 🟢")
        print(request.POST) # This prints the raw data to your terminal
        
        try:
            EventBooking.objects.create(
                event_type=request.POST.get('event_type'),
                event_date=request.POST.get('event_date'),
                event_city=request.POST.get('event_city'),
                expected_guests=request.POST.get('expected_guests'),
                event_budget=request.POST.get('event_budget'),
                full_name=request.POST.get('full_name'),
                email=request.POST.get('email'),
                mobile_number=request.POST.get('mobile_number'),
                additional_info=request.POST.get('additional_info')
            )
            print("🟢 DATABASE SAVE SUCCESSFUL!")
            messages.success(request, "Success! Your event details have been sent.")
            return redirect('plan_event') 
            
        except Exception as e:
            print(f"🔴 DATABASE ERROR: {e}")
            messages.error(request, "Something went wrong saving your data.")
            return redirect('plan_event')

    return render(request, 'main/plan-event.html')

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




from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import EventBooking

