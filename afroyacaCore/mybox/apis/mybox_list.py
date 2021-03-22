from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from mybox.models import BoxItems, MyBox
from utils.custom_libs import get_upload_host

exclude_fields = ["is_archived", "created_date", "modified_date", "is_published"]


class MyBoxSerializer(serializers.ModelSerializer):
    box_items = serializers.SerializerMethodField()
    box_price = serializers.SerializerMethodField()
    box_quantity = serializers.SerializerMethodField()

    class Meta:
        model = MyBox
        exclude = exclude_fields

    def get_box_items(self, instance):
        items = []
        box_items = BoxItems.objects.filter(box=instance, is_archived=False)
        for i in box_items:
            item_product_pictures = []
            if i.variety.picture1:
                item_product_pictures.append(get_upload_host(self.context["request"]) + i.variety.picture1.url)
            if i.variety.picture2:
                item_product_pictures.append(get_upload_host(self.context["request"]) + i.variety.picture2.url)
            if i.variety.picture3:
                item_product_pictures.append(get_upload_host(self.context["request"]) + i.variety.picture3.url)
            if i.variety.picture4:
                item_product_pictures.append(get_upload_host(self.context["request"]) + i.variety.picture4.url)

            item = {
                "id": i.id,
                "slug": i.variety.product.slug,
                "title": "%s - %s" % (i.variety.product.title, i.variety.color.title),
                "description": i.variety.product.description,
                "price": i.variety.product.price,
                "color": i.variety.color.title,
                "size": i.variety.size.name,
                "selected_quantity": i.quantity,
                "line_total": (i.variety.product.price * i.quantity),
                "pictures": item_product_pictures
            }
            items.append(item)
        return items

    @staticmethod
    def get_box_price(instance):
        total_price = 0
        box_items = BoxItems.objects.filter(box=instance, is_archived=False)
        for i in box_items:
            quantity = i.quantity
            product_price = i.variety.product.price
            line_total = product_price * quantity
            total_price = total_price + line_total
        instance.total = total_price
        instance.save()
        return total_price

    @staticmethod
    def get_box_quantity(instance):
        total_quantity = 0
        box_items = BoxItems.objects.filter(box=instance, is_archived=False)
        for i in box_items:
            quantity = i.quantity
            total_quantity = total_quantity + quantity
        return total_quantity


class MyBoxAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        box = MyBox.objects.filter(owner=user.userprofile).first()
        return Response(MyBoxSerializer(box, context={"request": request}).data)