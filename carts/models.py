from django.db import models
from store.models import Product, Variation
from account.models import Account


# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True, verbose_name= 'Panier ID')
    date_added = models.DateField(auto_now_add=True, verbose_name= 'Date d\'ajout')

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Produits')
    variations = models.ManyToManyField(Variation, blank=True)
    cart    = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Produits du panier')
    quantity = models.IntegerField('quantité')
    is_active = models.BooleanField('Est actif ?',default=True)

    def sub_total(self):
        return self.product.price * self.quantity

    def __unicode__(self):
        return self.product
