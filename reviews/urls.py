from django.urls import path

from . import views


app_name="reviews"

urlpatterns = [
    
    path("", views.index, name="index"),
    path("new-review", views.add_review, name="new_review"),
    path("<username>/<int:post_id>/edit/", views.edit_review, name="edit_review"),
]