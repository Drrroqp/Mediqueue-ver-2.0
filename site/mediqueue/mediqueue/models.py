from django.utils import timezone

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Doctors(models.Model):
    title = models.CharField(max_length=45, verbose_name='ФИО врача')
    content = models.TextField(blank=True, verbose_name='Биография')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null = True, verbose_name='Специальность')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Врачи'
        verbose_name_plural = 'Врачи'
        ordering = ['cat', 'title']

class Category(models.Model):
    name = models.TextField(max_length=45, db_index=True, verbose_name='Специальности')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Специальности'
        verbose_name_plural = 'Специальности'
        ordering = ['id', 'name']


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_num, email=None, password=None, years=None, fio=None, **extra_fields):
        if not phone_num:
            raise ValueError('The Phone number must be set')

        email = self.normalize_email(email)
        user = self.model(phone_num=phone_num, email=email, **extra_fields)
        user.years = years
        user.fio = fio
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_num, email=None, password=None, years=None, fio=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone_num, email, password, years, fio, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone_num = models.CharField(max_length=15, unique=True)
    email = models.EmailField(blank=True, null=True)
    years = models.DateField(blank=True, null=True)
    fio = models.CharField(max_length=255, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)  # Добавляем поле is_superuser
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_num'
    EMAIL_FIELD = 'email'

    def __str__(self):
        return self.phone_num