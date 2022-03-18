from rest_framework import serializers
from article.models import Article
from django.contrib.auth import get_user_model
from drf_dynamic_fields import DynamicFieldsMixin


# class AuthorSerializers(serializers.ModelSerializer):
    
#     class Meta:
#         model = get_user_model()
#         fields = ["id", "username", "first_name"]


# class AuthorUsernameField(serializers.RelatedField):
#     def to_representation(self, value):
#         return value.username


class ArticleSerializers(DynamicFieldsMixin, serializers.ModelSerializer):
    # author = serializers.HyperlinkedIdentityField(view_name="api:author-detail")
    # author = AuthorUsernameField(read_only=True)
    # author = serializers.CharField(source="author.username", read_only=True)

    def get_author(self, obj):
        return obj.author.username

    author = serializers.SerializerMethodField("get_author")


    class Meta:
        model = Article
        # fields = "__all__"
        exclude = ("created", "updated")

    # def validate_title(self, value):
    #     filter_list = ["hi", "hello"]
    #     for i in filter_list:
    #         if i in value:
    #             raise serializers.ValidationError("dont hello")   
    #     return value    


class UserSerializers(DynamicFieldsMixin, serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = "__all__"
       
