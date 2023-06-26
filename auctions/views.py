from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Category, Listing, Comment, Bid



def categories(request):
    categories = Category.objects.all()

    return render(request, "auctions/categories.html", {
        "categories": categories
    })


def category(request, id):
    category = Category.objects.get(pk=id)
    listingsInCategory = Listing.objects.filter(category = category, is_active = True)

    return render(request, "auctions/category.html", {
        "category": category,
        "listingsInCategory": listingsInCategory
    })


def placeBid(request, id):
    placed_bid = int(request.POST["placeBid"])

    current_user = request.user
    current_listing = Listing.objects.get(pk = id)

    if placed_bid > current_listing.price.bid:
        new_bid = Bid(author = current_user, bid = placed_bid)
        new_bid.save() 
        current_listing.price = new_bid
        current_listing.save()
        is_owner = request.user.username == current_listing.owner.username

        return render(request, "auctions/listing.html", {
            "listing": current_listing,
            "message": "Bid has been placed successfully",
            "alert": True,
            "isOwner": is_owner,
        })
    else:
        return render(request, "auctions/listing.html", {
            "listing": current_listing,
            "message": "New bid must be larger",
            "alert": False,
            "isOwner": is_owner,    
        })
    

def create_listing(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, "auctions/create_listing.html", {
            "categories": categories
        })
    else:
        title = request.POST["title"]
        description = request.POST["description"]
        img_url = request.POST["img_url"]
        price = request.POST["price"]
        category = request.POST["category"]

        current_user = request.user

        category_data = Category.objects.get(category_name = category)

        bid = Bid(bid = int(price), author = current_user)
        bid.save()

        new_listing = Listing(
            title = title,
            description = description,
            image_url = img_url,
            price = bid,
            owner = current_user,
            category = category_data
        )

        new_listing.save()

        return HttpResponseRedirect(reverse(index))


def listing(request, id):
    listing_data = Listing.objects.get(pk = id)
    comments = Comment.objects.filter(listing = listing_data)
    inWatchList = request.user in listing_data.watchlist.all()
    is_owner = request.user.username == listing_data.owner.username

    return render(request, "auctions/listing.html", {
        "listing": listing_data,
        "inWatchList": inWatchList,
        "comments": comments,
        "isOwner": is_owner
    })


def closeAuction(request, id):
    listing_data = Listing.objects.get(pk = id)
    listing_data.is_active = False
    listing_data.save()
    is_owner = request.user.username == listing_data.owner.username

    return render(request, "auctions/listing.html", {
        "listing": listing_data,
        "isOwner": is_owner,
        "alert": True,
        "message": "Your auction is closed!"
    })


def addComment(request, id):
    message = request.POST["comment"]
    current_user = request.user
    current_listing = Listing.objects.get(pk = id)
    

    new_comment = Comment(
        author = current_user, 
        listing = current_listing, 
        comment = message
    )
    new_comment.save()

    return HttpResponseRedirect(reverse("listing", args=(id, )))


def watchlist(request):
    current_user = request.user
    watchlist_listings = current_user.watchlist.all()
    return render(request, "auctions/watchlist.html", {
        "watchlist_listings": watchlist_listings
    })


def remove(request, id):
    listing_data = Listing.objects.get(pk = id)
    current_user = request.user
    listing_data.watchlist.remove(current_user)
    return HttpResponseRedirect(reverse(listing, args=(id, )))


def add(request, id):
    listing_data = Listing.objects.get(pk = id)
    current_user = request.user
    listing_data.watchlist.add(current_user)
    return HttpResponseRedirect(reverse(listing, args=(id, )))


def index(request):
    active_listings = Listing.objects.filter(is_active = True)
    categories = Category.objects.all()
    return render(request, "auctions/index.html", {
        "listings": active_listings,
        "categories": categories
    })


def displayCategory(request):
    if request.method == "POST":   
        if request.POST["category"] == "all":
            active_listings = Listing.objects.filter(is_active = True)
            categories = Category.objects.all()
            return render(request, "auctions/index.html", {
                "listings": active_listings,
                "categories": categories
            })
        else:
            category_filter = request.POST["category"]
            category = Category.objects.get(category_name = category_filter)

            active_listings = Listing.objects.filter(is_active = True, category = category)
            categories = Category.objects.all()

            return render(request, "auctions/index.html", {
                "listings": active_listings,
                "categories": categories
            })
           

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
