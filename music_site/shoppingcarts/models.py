from django.db import models
from tracks.models import Track

# Shopping Cart
class ShoppingCart(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, null=False)
    total = models.DecimalField(decimal_places=2, max_digits=5)

    class Meta:
        db_table = 'shoppingcart'

# Shopping Cart Item
class CartItem(models.Model):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, null=False)
    item = models.ForeignKey(Track, on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'cartitem'
