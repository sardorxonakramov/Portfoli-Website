from django.shortcuts import render
from django.views.generic import ListView,DetailView
from App_Users.models import Comments
from django.db.models import Q
from django.http import HttpResponse


from .models import MyPersonal, Skill, Education, Experience, Service,Portfolio
from App_Users.models import Comments

def HomeView(request):
    man = MyPersonal.objects.first()
    context = {"person": man} if man else {"person": None}
    if request.method == 'POST':
        pdf = open(file='cv/SardorxonAkramov(CV).pdf', mode='rb')
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Sardorxon Akramov CV.pdf"'
        return response

    return render(request, "App_Main/index.html", context)


def AboutView(request):
    man = MyPersonal.objects.first()
    skill = Skill.objects.all()
    comment = Comments.objects.filter( ~Q(owner=None) & Q(is_comment=True))

    context = {"person": man, "skills": skill,'comments':comment}

    return render(request, "App_Main/about.html", context)


def ResumeView(request):
    person = MyPersonal.objects.first()

    education = Education.objects.all()
    experience = Experience.objects.all()
    comment = Comments.objects.filter(is_summary=True).first()
    if not comment:
        comment = None

    context = {"educations": education, "experiences": experience, "comment": comment,'person':person}

    return render(request, "App_Main/resume.html", context)


def ServiceView(request):
    person = MyPersonal.objects.first()

    service = Service.objects.all()
    context = {"services": service,'person':person}
    return render(request, "App_Main/services.html", context)


class PortfolioList(ListView):
    model = Portfolio
    template_name = 'App_Main/portfolio.html'
    context_object_name = 'portfolio'

    def get_context_data(self, **kwargs):
        # Asosiy context ma'lumotlarini olish
        context = super().get_context_data(**kwargs)
        
        # person ma'lumotlarini qo'shish
        context['person'] = MyPersonal.objects.first()
        return context
class PortfolioDetailView(DetailView):
    
    model = Portfolio
    pk_url_kwarg = 'portfolio_id'
    context_object_name = 'portfolio'
    template_name = 'App_Main/portfolio-detail.html'

    def get_context_data(self, **kwargs):
        # Asosiy context ma'lumotlarini olish
        context = super().get_context_data(**kwargs)
        
        # person ma'lumotlarini qo'shish
        context['person'] = MyPersonal.objects.first()
        return context

