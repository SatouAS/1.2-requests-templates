from django.urls import path

from calculator.views import omlet, pasta, buter


urlpatterns = [
    path('omlet/', omlet),
    path('pasta/', pasta),
    path('buter/', buter),
]
