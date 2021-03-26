from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status
from mybox.models import BoxItems, MyBox
from products.models import Variety

exclude_fields = ["is_archived", "is_published", "created_date", "modified_date"]


class BoxItemPostSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(required=True)

    class Meta:
        model = BoxItems
        exclude = exclude_fields


class AddBoxItemAPIView(APIView):

    def post(self, request):
        serializer = BoxItemPostSerializer(data=request.data['data'])
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        data = serializer.data

        box = MyBox.objects.filter(owner=request.user.userprofile).first()

        if box:
            quantity = int(data['quantity'])
            variety = Variety.objects.get(id=data["variety"])
            variety_price = variety.product.price
            line_total = variety_price * quantity
            box_items_by_variety = BoxItems.objects.filter(variety=variety, box=box, is_archived=False)

            if not box_items_by_variety:
                box_item = BoxItems(box=box, variety=variety, quantity=quantity,
                                     line_total=line_total, is_archived=False)
                box_item.save()
            else:
                b_item = box_items_by_variety.first()
                b_item.quantity = b_item.quantity + quantity
                b_item.save()
            response = {
                "message": "Item add with success"
            }
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            box = MyBox(owner=request.user.userprofile)
            box.save()

            quantity = int(data['quantity'])
            variety = Variety.objects.get(id=data["variety"])
            variety_price = variety.product.price
            line_total = variety_price * quantity
            box_items_by_variety = BoxItems.objects.filter(variety=variety, box=box, is_archived=False)

            if not box_items_by_variety:
                box_item = BoxItems(box=box, variety=variety, quantity=quantity,
                                    line_total=line_total, is_archived=False)
                box_item.save()
            else:
                b_item = box_items_by_variety.first()
                b_item.quantity = b_item.quantity + quantity
                b_item.save()
            response = {
                "message": "Item add with success"
            }
            return Response(response, status=status.HTTP_201_CREATED)
