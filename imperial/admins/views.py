from django.shortcuts import render, redirect, get_object_or_404
from .models import Portfolio, Gallery,TeamMember,JobOpening,Facility ,Blog, FAQ
from .forms import PortfolioForm, GalleryForm, TeamMemberForm, JobOpeningForm, FacilityForm, BlogForm, FAQForm

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



def team_admin(request):
    members = TeamMember.objects.all().order_by('-created_at')

    if request.method == "POST":
        form = TeamMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('team_admin')
    else:
        form = TeamMemberForm()

    context = {
        'form': form,
        'members': members
    }
    return render(request, 'admin_team.html', context)


def edit_team(request, pk):
    member = get_object_or_404(TeamMember, pk=pk)
    members = TeamMember.objects.all()

    if request.method == "POST":
        form = TeamMemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return redirect('team_admin')
    else:
        form = TeamMemberForm(instance=member)

    context = {
        'form': form,
        'members': members,
        'edit_mode': True
    }
    return render(request, 'admin_team.html', context)


def delete_team(request, pk):
    member = get_object_or_404(TeamMember, pk=pk)
    member.delete()
    return redirect('team_admin')


def about(request):
    team_members = TeamMember.objects.filter(is_active=True)

    return render(request, 'about.html', {
        'team_members': team_members
    })
    
    
def admin_careers(request, pk=None):
    jobs = JobOpening.objects.all().order_by('-created_at')
    
    if pk:
        job_obj = get_object_or_404(JobOpening, pk=pk)
    else:
        job_obj = None

    if request.method == 'POST':
        form = JobOpeningForm(request.POST, instance=job_obj)
        if form.is_valid():
            form.save()
            return redirect('admin_careers')
    else:
        form = JobOpeningForm(instance=job_obj)

    return render(request, 'careers_admin.html', {
        'form': form,
        'jobs': jobs,
        'edit_mode': True if pk else False
    })

def delete_job(request, pk):
    job = get_object_or_404(JobOpening, pk=pk)
    job.delete()
    return redirect('admin_careers')


def admin_facilities(request, pk=None):
    facilities = Facility.objects.all().order_by('-created_at')
    facility_obj = get_object_or_404(Facility, pk=pk) if pk else None

    if request.method == 'POST':
        form = FacilityForm(request.POST, instance=facility_obj)
        if form.is_valid():
            form.save()
            return redirect('admin_facilities')
    else:
        form = FacilityForm(instance=facility_obj)

    return render(request, 'facilities_admin.html', {
        'form': form,
        'facilities': facilities,
        'edit_mode': True if pk else False
    })

def delete_facility(request, pk):
    facility = get_object_or_404(Facility, pk=pk)
    facility.delete()
    return redirect('admin_facilities')

def admin_blog(request, pk=None):
    posts = Blog.objects.all().order_by('-created_at')
    blog_obj = get_object_or_404(Blog, pk=pk) if pk else None

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog_obj)
        if form.is_valid():
            form.save()
            return redirect('admin_blog')
    else:
        form = BlogForm(instance=blog_obj)

    return render(request, 'blog_admin.html', {
        'form': form,
        'posts': posts,
        'edit_mode': True if pk else False
    })

def delete_blog(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect('admin_blog')

def admin_faq(request, pk=None):
    faqs = FAQ.objects.all().order_by('-created_at')
    faq_obj = get_object_or_404(FAQ, pk=pk) if pk else None

    if request.method == 'POST':
        form = FAQForm(request.POST, instance=faq_obj)
        if form.is_valid():
            form.save()
            return redirect('admin_faq')
    else:
        form = FAQForm(instance=faq_obj)

    return render(request, 'faq_admin.html', {
        'form': form,
        'faqs': faqs,
        'edit_mode': True if pk else False
    })

def delete_faq(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)
    faq.delete()
    return redirect('admin_faq')