from django.shortcuts import render
from admins.models import Portfolio, Gallery, TeamMember, JobOpening,Facility,Blog,FAQ,Term,PrivacyPolicy
# Create your views here.
def home(request):
    return render(request, "main/index.html")

def about(request):
    team_members = TeamMember.objects.filter(is_active=True).order_by('-created_at')

    return render(request, "main/about.html", {
        'team_members': team_members
    })

def blog(request):
    posts = Blog.objects.all().order_by('-date')
    return render(request, "main/blog.html", {'posts': posts})


def career_page(request):
    jobs = JobOpening.objects.all().order_by('-created_at')
    return render(request, 'main/carrer.html', {'jobs': jobs})
    
    


def contact(request):
    return render(request, "main/contact.html")

def corporate(request):
    return render(request, "main/corporate.html")

def entertainment(request):
    return render(request, "main/entertainment.html")

def exhibition(request):
    return render(request, "main/exhibition.html")

def facilities(request):
    facilities_list = Facility.objects.all().order_by('-created_at')
    return render(request, "main/facilities.html", {'facilities': facilities_list})

def faq(request):
    faqs = FAQ.objects.all().order_by('created_at') # Or '-created_at' for newest first
    return render(request, "main/FAQ.html", {'faqs': faqs})

def gallery(request):
    images = Gallery.objects.all().order_by('-created_at')
    return render(request, "main/gallery.html", {'images': images})

def plan_event(request):
    return render(request, "main/plan-event.html")

def privacy(request):
    policies = PrivacyPolicy.objects.all().order_by('order')
    return render(request, "main/privacy.html", {'policies': policies})

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
    terms_list = Term.objects.all().order_by('-order')
    return render(request, "main/terms.html", {'terms_list': terms_list})

def themes(request):
    return render(request, "main/themes.html")

def wedding(request):
    return render(request, "main/wedding.html")
