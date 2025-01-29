from django.db import models
import datetime


# Create your models here.
class MyPersonal(models.Model):
    first_name = models.CharField(max_length=50, default='Sardorxon')
    last_name = models.CharField(max_length=50, default="Akramov")
    photo_fon = models.ImageField(upload_to='galery/', default='galery/hero-bg.jpg')
    photo_profile = models.ImageField(upload_to='galery/', default='galery/profile-img.jpg')
    birth = models.DateField(default=datetime.date(2001, 9, 18))

    address = models.CharField(max_length=200)
    address_url = models.URLField(blank=True,null=True)
    phone_number = models.CharField(max_length=13, default='+998911888990')

    degree = models.CharField(max_length=30, default='Junior')
    occupation = models.CharField(max_length=100, default='Backend Developer')
    
    personal_description = models.TextField()
    job_description = models.TextField()
    summary_description = models.TextField()

    instgram = models.URLField('Instagram',blank=True,null=True)
    telegram = models.URLField('Telegram', default='https://t.me/Sardorxon_Dev',blank=True,null=True)
    whatsapp = models.URLField('WhatsApp', default='https://wa.me/qr/KXRW4TSCYRGNF1',blank=True,null=True)
    github = models.URLField('GitHub', default='https://github.com/sardorxon18',blank=True,null=True)
    email = models.EmailField('Email',default='sardorxonakramov01@gmail.com', blank=True,null=True)
    linkedin = models.URLField('LinkedIn', default='https://www.linkedin.com/in/sardorxon-akramov-915728285',blank=True,null=True)
    facebook = models.URLField("Facebook",blank=True,null=True)
    website = models.URLField('Website',default='https://sardorxon.uz',blank=True,null=True)
    website_name = models.CharField(max_length=50,default='sardorxon.uz')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Skill(models.Model):
    owner = models.ForeignKey(MyPersonal, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=255,blank=True,null=True)
    degree = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.degree}%)"

class Education(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    finish_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Experience(models.Model):  # Typo correction from Exprience
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    finish_date = models.DateField()

    def __str__(self):
        return self.name

class ExperienceDescription(models.Model):  # Typo correction from Exprience_Description
    experience_id = models.ForeignKey(Experience, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"Description for {self.experience_id.name}"


class Portfolio(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='loyihalar/', default='loyihalar/project-image.jpg')
    client = models.CharField(max_length=100, default="O'zim Uchun")
    project_date_finish = models.DateField()
    project_url = models.URLField('Web site address')
    source_code = models.URLField("Project's GitHub URL")
    bio = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    logo = models.CharField(max_length=50)

