from rest_framework import serializers
from .models import Article


# le = serializers.CharField(max_length=100)
#     author = serializers.CharField(max_length=100)
#     email = serializers.EmailField(max_length=100)
#     #date = serializers.DateTimeField(auto_now_add=True)
#     class ArticleSerializer(serializers.Serializer):
#         tit
#     def create(self, validated_data):
#         return Article.objects.create(validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data('title', instance.title)
#         instance.author = validated_data('author', instance.author)
#         instance.email = validated_data('email', instance.email)
#         instance.date = validated_data('date', instance.date)
#         instance.save()
#         return instance

 # model serializers
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
      #  fields = ['id','title','author','email']
        fields ='__all__'



