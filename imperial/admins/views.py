from django.shortcuts import render, redirect, get_object_or_404
from .models import Portfolio, Gallery, FeaturedEvent, Testimonial
from main.models import EventBooking

from .forms import PortfolioForm, GalleryForm, FeaturedEventForm, TestimonialForm

# Create your views here.
def admin_home(request):
    return render(request, "admin_home.html")

def admin_portfolio(request, pk=None):

    portfolios = Portfolio.objects.all().order_by('-created_at')

    if pk:
        portfolio = get_object_or_404(Portfolio, pk=pk)
    else:
        portfolio = None

    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('admin_portfolio')
    else:
        form = PortfolioForm(instance=portfolio)

    context = {
        'form': form,
        'portfolios': portfolios,
        'edit_mode': True if pk else False
    }

    return render(request, 'portfolio_admin.html', context)

def delete_portfolio(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk)
    portfolio.delete()
    return redirect('admin_portfolio')


# Gallery

def admin_gallery(request, pk=None):

    images = Gallery.objects.all().order_by('-created_at')

    if pk:
        image_obj = get_object_or_404(Gallery, pk=pk)
    else:
        image_obj = None

    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES, instance=image_obj)
        if form.is_valid():
            form.save()
            return redirect('admin_gallery')
    else:
        form = GalleryForm(instance=image_obj)

    return render(request, 'gallery_admin.html', {
        'form': form,
        'images': images,
        'edit_mode': True if pk else False
    })
    
def delete_gallery(request, pk):
    image = get_object_or_404(Gallery, pk=pk)
    image.delete()
    return redirect('admin_gallery')

# Featured events From Home page

def manage_featured(request, pk=None):

    events = FeaturedEvent.objects.all().order_by('-created_at')

    if pk:
        event_obj = get_object_or_404(FeaturedEvent, pk=pk)
    else:
        event_obj = None

    if request.method == "POST":
        form = FeaturedEventForm(request.POST, request.FILES, instance=event_obj)
        if form.is_valid():
            event = form.save(commit=False)

            if event.category != "custom":
                event.custom_category = None

            event.save()
            return redirect("manage_featured")
    else:
        form = FeaturedEventForm(instance=event_obj)

    return render(request, "featured_admin.html", {
        "form": form,
        "events": events,
        "edit_mode": True if pk else False
    })
    
    
def delete_featured(request, pk):
    event = get_object_or_404(FeaturedEvent, pk=pk)
    event.delete()
    return redirect("manage_featured")


# Testimonial

def admin_testimonials(request, pk=None):
    testimonials = Testimonial.objects.all().order_by('-created_at')

    if pk:
        obj = get_object_or_404(Testimonial, pk=pk)
    else:
        obj = None

    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('admin_testimonials')
    else:
        form = TestimonialForm(instance=obj)

    return render(request, 'testimonials_admin.html', {
        'form': form,
        'testimonials': testimonials,
        'edit_mode': True if pk else False
    })

def delete_testimonial(request, pk):
    obj = get_object_or_404(Testimonial, pk=pk)
    obj.delete()
    return redirect('admin_testimonials')


# main/views.py
def admin_bookings(request):
    bookings = EventBooking.objects.all().order_by('-created_at')
    return render(request, 'admin_bookings.html', {'bookings': bookings})

# 3. DELETE: Remove a booking and refresh the page
def delete_booking(request, pk):
    booking = get_object_or_404(EventBooking, pk=pk)
    booking.delete()
    # Optional: messages.error(request, 'Booking deleted.')
    return redirect('admin_bookings')