from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# INSTITUTE
class Institute(models.Model):
    name = models.CharField(max_length=150)
    abbr = models.CharField(max_length=20, null=True, blank=True)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    district = models.ForeignKey('District',on_delete=models.CASCADE)
    state = models.ForeignKey('State',on_delete=models.CASCADE)
    pin = models.IntegerField()

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Email required")
        
        user = self.model(
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)
    institute = models.ForeignKey(Institute, null=True, on_delete=models.SET_NULL) # Remove and add User to Institute
    dob = models.DateField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True



# STATE
class State(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


# DISTRICT
class District(models.Model):
    name = models.CharField(max_length=50, unique=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# BLOCK
class Block(models.Model):
    name = models.CharField(max_length=50, unique=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# ADDRESS
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=255)
    block = models.ForeignKey(Block, on_delete=models.PROTECT)
    district = models.ForeignKey(District, on_delete=models.PROTECT)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    pin = models.PositiveBigIntegerField()
    primary = models.BooleanField(default=False)

    def __str__(self):
        return self.address1
