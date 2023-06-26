from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create_listing, name="create"),
    path("displayCategory", views.displayCategory, name="display_category"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("add/<int:id>", views.add, name="add"),
    path("remove/<int:id>", views.remove, name="remove"),
    path("watchlist/", views.watchlist, name="watchlist"),
    path("comment/<int:id>", views.addComment, name="comment"),
    path("place_bid/<int:id>", views.placeBid, name="place_bid"),
    path("closeAuction/<int:id>", views.closeAuction, name="closeAuction"),
    path("categories/", views.categories, name="categories"),
    path("category/<int:id>", views.category, name="category"),
]
