from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.db import connection

from tracks.models import Track
from userTracks.models import UserTrack
from shoppingcarts.models import ShoppingCart, CartItem
from customers.models import Customer
from invoiceLines.models import InvoiceLine
from invoices.models import Invoice

from reportlab.pdfgen import canvas
from io import BytesIO

# Create your views here.

@login_required
def index(request):
    user = request.user
    shoppingCart = ShoppingCart.objects.filter(user = user.id).first()
    if (shoppingCart):
        cartItems = custom_sql_dictfetchall(
            """
                SELECT track.id, track.name, track.composer, track.milliseconds/60000 as duracion, track.unitprice
                FROM cartitem JOIN track
                    ON track.id = cartitem.item_id
                WHERE cart_id = {cart_id}
            """.format(cart_id=shoppingCart.id)
        )
        return render(
            request,
            'shoppingcart.html', 
            {
                'user': user,
                'tracks': cartItems
            }
        )
    else:
        return redirect('tracks:index')

@login_required
def delete(request, id):
    user = request.user
    try:
        shoppingCart = ShoppingCart.objects.filter(user = user.id).first()
        track = Track.objects.get(pk = id)
        cartitem = CartItem.objects.filter(item = track, cart = shoppingCart).first()
        shoppingCart.total -= track.unitprice
        shoppingCart.save()
        cartitem.delete()
        if (len(shoppingCart.cartitem_set.all()) == 0):
            shoppingCart.delete()
            return redirect('tracks:index')
    except Track.DoesNotExist:
        raise Http404("Track does not exist")
    return redirect('shoppingcarts:index')

@login_required
def buy(request):
    user = request.user
    try:
        cart = confirm_shopping_cart(user, None)
        response=HttpResponse(content_type='application/pdf')
        response['status_code'] = 200
        response['Content-Disposition'] = 'attachment; filename=Factura.pdf'
        buffer = BytesIO()
        c = canvas.Canvas(buffer)
        contador = 600
        for cartitem in cart:
            track = cartitem.item
            c.drawString(200, 770, "FACTURA")
            c.drawString(100, 700, "Canciones" )
            c.drawString(340, 700, "Precio" )
            c.drawString(50, contador, str(track))
            c.drawString(350, contador, str(track.unitprice))
            contador -= 20
           # c.drawString(50,450,"hola")
        c.showPage()
        c.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
    except ShoppingCart.DoesNotExist:
        raise Http404("Shopping does not exist")
    return response

def confirm_shopping_cart(user, date):
    shoppingCart = ShoppingCart.objects.filter(user = user.id).first()
    customer = Customer.objects.filter(user = user).first()
    if (not customer):
        customer = Customer.objects.create(
            id = Customer.objects.all().last().id + 1,
            user = user,
            firstname = user.username
        )
    invoice = Invoice.objects.create(
        id = Invoice.objects.all().last().id + 1,
        total = shoppingCart.total,
        customer = customer,
        invoicedate = date
    )
    cartItems = shoppingCart.cartitem_set.all()
        
    for cartitem in cartItems:
        track = cartitem.item
        print(track)
        InvoiceLine.objects.create(
            id = InvoiceLine.objects.all().last().id + 1,
            unitprice = track.unitprice,
            quantity = 1,
            invoice = invoice,
            track = track
        )
    shoppingCart.delete()
    return cartItems

def custom_sql_dictfetchall(query):
    "Return all rows from a cursor as a dict"
    with connection.cursor() as cursor:
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
