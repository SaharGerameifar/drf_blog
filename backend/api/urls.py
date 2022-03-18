from django.urls import path, include
from .views import ArticleViewSet, UserViewSet
from rest_framework import routers
# from .views import ArticleList, ArticleDetail, UserList, UserDetail

app_name = "api"

router = routers.SimpleRouter()
router.register('users', UserViewSet, basename="users")
router.register('articles', ArticleViewSet, basename="articles")

urlpatterns = [
    path("",include(router.urls)),
    # path("author/<int:pk>/",AuthorRetrieve.as_view(), name="author-detail"),
]

# urlpatterns = [
#     path('articles/', ArticleList.as_view(), name= "article-list"),
#     path('articles/<slug:slug>/', ArticleDetail.as_view(), name= "article-detail"),
#     path('users/', UserList.as_view(), name= "user-list"),
#     path('users/<int:pk>/', UserDetail.as_view(), name= "user-detail"),
# ]