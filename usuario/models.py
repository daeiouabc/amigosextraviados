from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UsuarioManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        print("crear")
        if not email:
            raise ValueError('El email debe ingresarse')
        email = self.normalize_email(email)
        user = self.model(email=email, is_active=True, is_staff=is_staff, is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        print("create_user")
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self,  email, password, **extra_fields):
        print("create_superuser")
        return self._create_user(email, password, True, True, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=55)
    apellido = models.CharField(max_length=55, blank=True)
    direccion = models.CharField(max_length=50, blank=True)
    telefono = models.CharField(max_length=15, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    #campo login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']

    #class Meta:
    #    verbose_name = "Usuario"
    #    verbose_name_plural = "Usuarios"

    def get_short_name(self):
        return u'%s %s' % (self.nombre, self.apellido)

    def __str__(self):
        return u'%s - %s' % (self.id, self.nombre)

    def save(self, *args, **kwargs):
        if not self.is_superuser:
            self.set_password(self.password)
        super(Usuario, self).save(*args, **kwargs)
