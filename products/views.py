from django.shortcuts import render, redirect
from .models import Food, Cart
from account.models import my_user

# Create your views here.


def home(req, *args, **kwargs):
    obj = list(Food.objects.all())
    msg = ""
    if req.POST:
        if str(req.user) != "AnonymousUser":
            curr_user = my_user.objects.get(username=req.user)
            cart_details = {
                "user": curr_user.id,
                "food": req.POST.get("prod_id"),
                "qty": 1,
            }
            Cart.objects.create(**cart_details)
            msg = "Added to cart"
        else:
            return redirect("login")
    return render(req, "home.html", {"obj": obj, "msg": msg})


def cart(req, *args, **kwargs):
    if str(req.user) != "AnonymousUser":

        # Delete
        if req.POST:
            instance = Cart.objects.filter(id=req.POST.get("prod_id"))
            print("id:", req.POST.get("prod_id"))
            instance.delete()

        # Display
        curr_user = my_user.objects.get(username=req.user)
        objs = Cart.objects.filter(user=curr_user.id)

        data = []
        bill_amt = 0

        for i in objs:
            food_item = Food.objects.get(id=i.food)
            food_item_obj = {
                "title": food_item.title,
                "price": food_item.price,
                "image": food_item.image,
                "veg": food_item.veg,
                "id": i.id,
            }
            bill_amt += food_item.price
            data.append(food_item_obj)
    else:
        return redirect("login")
    return render(req, "cart.html", {"data": data, "bill": bill_amt})


def profile(req, *args, **kwargs):
    return render(req, "profile.html")
