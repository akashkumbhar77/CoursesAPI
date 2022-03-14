from rest_framework import serializers
from .models import CoursesModel,Product

class CoursesSerializers(serializers.ModelSerializer):
    class Meta:
        model = CoursesModel
        fields = '__all__'
    def create(self, validated_data):
        return CoursesModel.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.url = validated_data.get('url',instance.url)
        instance.isPaid = validated_data.get('isPaid',instance.isPaid)
        instance.price = validated_data.get('price',instance.price)
        instance.numSubscribers = validated_data.get('numSubscribers',instance.numSubscribers)
        instance.numReveiws = validated_data.get('numReveiws',instance.numReveiws)
        instance.instructionalLevel = validated_data.get('instructionalLevel',instance.instructionalLevel)
        instance.contentInfo = validated_data.get('contentInfo', instance.contentInfo)
        instance.publishedTime = validated_data.get('publishedTime', instance.publishedTime)
        instance.save()
        return instance


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self,validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.prod_name = validated_data.get('prod_name',instance.prod_name)
        instance.prod_owner = validated_data.get('prod_owner',instance.prod_owner)
        instance.prod_price = validated_data.get('prod_price',instance.prod_price)
        instance.prod_source = validated_data.get('prod_source',instance.prod_source)
        instance.save()
        return instance