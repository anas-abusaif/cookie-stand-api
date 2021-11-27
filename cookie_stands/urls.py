from django.urls import path
from .views import Cookie_standsList, Cookie_standDetail

urlpatterns = [
    path("", Cookie_standsList.as_view(), name="cookiie_stands_list"),
    path("<int:pk>/", Cookie_standDetail.as_view(), name="cookie_stand_detail"),
]
