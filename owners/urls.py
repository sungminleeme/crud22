from django.urls    import path

from .views import OwnerListView, DogListView

urlpatterns = [
    path('/owners', OwnerListView.as_view()),
    path('/dogs', DogListView.as_view())
]