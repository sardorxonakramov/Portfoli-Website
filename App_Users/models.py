from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import MyUserManager


class Users(AbstractUser):
    email = models.EmailField(unique=True)  # Email maydonini noyob qilib qo'yamiz
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = None  # `username` maydonini o'chirib tashlaymiz
    phone = models.CharField(max_length=13, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    nationalty = models.CharField(max_length=50, blank=True, null=True)    
    image = models.ImageField(
        upload_to="users_img/", default="users_img/default-user.png"
    )

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",
        blank=True,
    )

    objects = MyUserManager()

    USERNAME_FIELD = "email"  # `email` maydoni asosiy identifikator bo'ladi
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
    ]  # Email bilan birga kerak bo'lgan maydonlar

    def __str__(self):
        return self.fullname
    

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def positions(self):
        return f"{self.position}"

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"

    def set_fullname(self, value):
        names = value.split()
        if names:
            self.first_name, self.last_name = names[0], " ".join(names[1:])
        else:
            self.first_name, self.last_name = 'User', 'User'

    fullname = property(get_fullname, set_fullname)



class Comments(models.Model):
    # Tizimga kirgan foydalanuvchilar uchun
    owner = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name="comments", blank=True, null=True
    )
    # Tizimga kirmagan foydalanuvchilar uchun
    email = models.EmailField(blank=True, null=True)  # Email talab qilinadi
    full_name = models.CharField(max_length=150, blank=True, null=True)  # To'liq ism talab qilinadi

    subject = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    is_comment = models.BooleanField(default=False)
    is_summary = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created"]  # Kommentlar eng yangi ma'lumot birinchi chiqadi

    def __str__(self):
        if self.owner:
            return f"{self.subject} - {self.owner.email}"  # Tizimga kirgan foydalanuvchi
        return f"{self.subject} - {self.email}"  # Tizimga kirmagan foydalanuvchi
