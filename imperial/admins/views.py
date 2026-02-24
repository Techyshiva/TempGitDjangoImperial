from django.shortcuts import render, redirect, get_object_or_404
from .models import Portfolio, Gallery
from .forms import PortfolioForm, GalleryForm

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