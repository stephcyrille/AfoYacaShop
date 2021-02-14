# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from products.apis.utils import get_upload_host
from products.models import Product, Variety

exclude_fields = ["is_archived", "created_by", "modified_by", "created_date", "modified_date"]
one_week_ago = datetime.today() - timedelta(days=7)
one_month_ago = datetime.today() - timedelta(days=30)


class ProductSerializer(serializers.ModelSerializer):
    product_url = serializers.SerializerMethodField()
    pictures = serializers.SerializerMethodField()

    def get_product_url(self, instance):
        product_url = get_upload_host(self.context["request"]) + instance.get_absolute_url()
        return product_url

    def get_pictures(self, instance):
        """
        Get at max 30 pictures for all services composing this pack
        """
        pics = []
        # si le queryset services_of_pack est grand
        v = Variety.objects.filter(product=instance).first()

        if v is not None:
            if v.picture1:
                pics.append(get_upload_host(self.context["request"]) + v.picture1.url)
            if v.picture2:
                pics.append(get_upload_host(self.context["request"]) + v.picture2.url)
            if v.picture3:
                pics.append(get_upload_host(self.context["request"]) + v.picture3.url)
            if v.picture4:
                pics.append(get_upload_host(self.context["request"]) + v.picture4.url)

        return pics

    class Meta:
        model = Product
        fields = ["id", "title", "slug", "price", "pictures", "product_url"]



class ProductFlashSaleAPIView(APIView):
    queryset = Product.objects.none()
    serializer_class = ProductSerializer

    @staticmethod
    def get_queryset():
        #return Product.objects.filter(is_published=True, flash_sale=True)
        return Product.objects.filter(is_published=True)

    def get(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)
