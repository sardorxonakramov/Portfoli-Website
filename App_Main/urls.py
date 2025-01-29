from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView, name="home"),
    path("about/", views.AboutView, name="about"),
    path("resume/", views.ResumeView, name="resume"),
    path("rervice/", views.ServiceView, name="service"),
    path("portfolio/", views.PortfolioList.as_view(), name="portfolio"),
    path('portfolio-detail/<int:portfolio_id>/', views.PortfolioDetailView.as_view(), name='portfolio_detail'),
]
