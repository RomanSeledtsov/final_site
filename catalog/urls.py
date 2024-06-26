from django.urls import path
from . import views

urlpatterns = [
    path("catalog/", views.InvListView.as_view(), name="inv_list"),
    path("catalog/<int:id>/", views.InvDetailView.as_view(), name="inv_detail"),
    path("catalog/<int:id>/delete/", views.DeleteInvView.as_view(), name="delete_inv"),
    path("catalog/<int:id>/update/", views.EditInvView.as_view(), name="edit_inv"),
    path("create_inv/", views.CreateInvView.as_view(), name="create_inv"),
]
