# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework.generics import RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from article.models import Article
from django.contrib.auth import get_user_model
from .serializers import ArticleSerializers, UserSerializers
from .permissions import IsSuperUser, IsAuthorOrReadOnly, IsStaffOrReadOnly, IsSuperUserOrStaffReadOnly
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    lookup_field = "slug"
    filterset_fields = ["status", "author"]
    search_fields = ["title", "author__username", "content"]
    ordering_fields = ["publish", "status"]
    ordering = ["-publish"]

    # def get_queryset(self):
    #     queryset = Article.objects.all()
    #     status = self.request.query_params.get('status')
    #     if status is not None:
    #         queryset = queryset.filter(status=status)
    #     author = self.request.query_params.get('author')
    #     if author is not None:
    #         queryset = queryset.filter(author__username=author)    
    #     return queryset

    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]    
        return [permission() for permission in permission_classes]


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializers
    permission_classes = (IsSuperUserOrStaffReadOnly, )


# class AuthorRetrieve(RetrieveAPIView):
#     queryset = get_user_model().objects.filter(is_staff=True)
#     serializer_class = AuthorSerializers
    

# class ArticleList(ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializers


# class ArticleDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializers 
#     lookup_field = "slug"   
#     permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)


# class UserList(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializers
#     permission_classes = (IsSuperUserOrStaffReadOnly, )
 

# class UserDetail(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializers 
#     permission_classes = (IsSuperUserOrStaffReadOnly, )       


# class RevokeToken(APIView):    
#     permission_classes = (IsAuthenticated, )

#     def delete(self, request):
#         request.auth.delete()
#         return Response(status=204)