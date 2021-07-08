from django.urls import path

from accountapp.urls import urlpatterns
from profileapp.views import ProfileCreateView

app_name = 'profileapp'

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),
]