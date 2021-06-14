from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib import messages

# Create your models here.

class MyAccountManager(BaseUserManager):

	def create_user(self, first_name, last_name, username, email, city, password=None):

		if not email:
			raise ValueError("Vous devez saisir une adresse Email")

		if not username:
			raise ValueError("Le champ nom d'utilisateur est obligatoire")


		user = self.model( 

			   email = self.normalize_email(email),
			   username = username,
			   first_name = first_name,
			   last_name = last_name,
			   city = city,

		)

		user.set_password(password)
		user.save(using=self._db)
		return user


	def create_superuser(self, first_name, last_name, username, email, city, password):

		user = self.create_user( 
			email = self.normalize_email(email), 
			username = username, 
			password = password,
			first_name = first_name, 
			last_name = last_name,
			city = city,
		)

		user.is_superadmin = True
		user.is_admin = True
		user.is_staff = True
		user.is_active = True

		user.save(using=self._db)

		return user


class Account(AbstractBaseUser):
	first_name = models.CharField('Prénom' ,max_length=200)
	last_name = models.CharField('Nom' ,max_length = 200)
	username = models.CharField('Nom d\'utilisateur' ,max_length = 200, unique=True)
	email = models.EmailField('Email' ,max_length = 200, unique = True)
	phone_number = models.CharField('Téléphone' ,max_length = 60)
	city = models.CharField('Ville' ,max_length = 60)


	date_joined = models.DateTimeField('Compte crée' , auto_now_add=True)
	last_login = models.DateTimeField('Dernière connexion' ,auto_now_add = True)
	is_admin = models.BooleanField('Admin ?' ,default=False)
	is_staff = models.BooleanField('Staff ?' ,default=False)
	is_active = models.BooleanField('Actif ?' ,default=False)
	is_superadmin = models.BooleanField('Super Admin ?' ,default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'city']

	objects = MyAccountManager()

	def __str__(self):
		return self.email


	def has_perm(self, perm, obj=None):
		return self.is_admin


	def has_module_perms(self, add_label):
		return True

	class Meta:
		verbose_name = "Compte"
		verbose_name_plural = "Comptes"