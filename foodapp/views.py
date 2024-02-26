from django.shortcuts import render  
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from rest_framework import generics
from .models import Organization,Item,Pricing  
from .serializers import OrganizationSerializer,ItemSerializer,PricingSerializer  
# Create your views here.  
  
class OrganizationView(APIView):  
  
    def get(self, request, *args, **kwargs):  
        result = Organization.objects.all()  
        serializers = OrganizationSerializer(result, many=True)  
        return Response({'status': 'success', "Organization":serializers.data}, status=200)  
  
    def post(self, request):  
        serializer = OrganizationSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  

class ItemView(APIView):  
  
    def get(self, request, *args, **kwargs):  
        result = Item.objects.all()  
        serializers = ItemSerializer(result, many=True)  
        return Response({'status': 'success', "Item":serializers.data}, status=200)  
  
    def post(self, request):  
        serializer = ItemSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  

class PricingView(APIView):  
  
    def get(self, request, *args, **kwargs):  
        result = Pricing.objects.all()  
        serializers = PricingSerializer(result, many=True)  
        return Response({'status': 'success', "Pricing":serializers.data}, status=200)  
  
    def post(self, request):  
        serializer = PricingSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  

class DeliveryPriceView(APIView):
    def post(self, request):
        total_delivery_price=0.0
        zone=request.data.get('zone') 
        orgId=request.data.get('organization_id') 
        total_distance=request.data.get('total_distance') 
        itemType=request.data.get('item_type') 

      
        if zone == None: # The variable
            print('It is None')
            return Response({"status": "error", "Error message": "Zone field is mandatory"}, status=status.HTTP_400_BAD_REQUEST)

        elif orgId == None: 
            print('It is None')
            return Response({"status": "error", "Error message": "Organization_id field is mandatory"}, status=status.HTTP_400_BAD_REQUEST)
        elif total_distance== None:
             return Response({"status": "error", "Error message": "toatl_distance field is mandatory"}, status=status.HTTP_400_BAD_REQUEST)
        elif itemType== None:
             return Response({"status": "error", "Error message": "item_type field is mandatory"}, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            print ("It is defined and has a value")
            print(total_distance)
            print(itemType)
            itemIdVal=Item.objects.values()
            print(itemIdVal)
            itemId=Item.objects.filter(type=itemType).values('id').first().get('id')
            print(itemId)
            deliveryPriceList = Pricing.objects.filter(organization_id=orgId,item_id=itemId,zone=zone).values('base_distance_in_km','km_price','fix_price').first()
            print(deliveryPriceList.get('base_distance_in_km'))
            print(deliveryPriceList.get('km_price'))
            print(deliveryPriceList.get('fix_price'))

            print(total_distance==deliveryPriceList.get('base_distance_in_km'))
            print(total_distance < deliveryPriceList.get('base_distance_in_km'))
            print(type(total_distance))
            print(type(deliveryPriceList.get('base_distance_in_km')))

            if float(total_distance)==float(deliveryPriceList.get('base_distance_in_km')) or   float(total_distance) < float(deliveryPriceList.get('base_distance_in_km')):
                total_delivery_price=deliveryPriceList.get('fix_price')
            else :
                rem_dis=float(total_distance)-float(deliveryPriceList.get('base_distance_in_km'))
                total_delivery_price =float(deliveryPriceList.get('fix_price'))+(rem_dis*float(deliveryPriceList.get('km_price')))

            return Response({"status": "success", "Total_delivery_price": total_delivery_price}, status=status.HTTP_200_OK) 
        
              
        


        # mydata = Member.objects.filter(lastname='Refsnes', id=2).values()
        # template = loader.get_template('template.html')
        # context = {
        #     'mymembers': mydata,
        # }



def product_selection(request):

    items = Item.objects.all()
    return render(request, 'F:\Food-delivery-app/foodapp/templates/foodapp/test.html', {'items': items})

    if request.method == 'POST':
        selected_items = request.POST.getlist('selected_items')
        # Process the selected items as needed, e.g., add to cart, etc.
        # Redirect to a success page or render a template
        return redirect('success_page')

    # Handle other cases, if needed
   

    # elif request.method == 'GET':
    #     items = Item.objects.all()
    #     return render(request, 'F:\Food-delivery-app/foodapp/templates/foodapp/productus.html', {'items': items})

    return render(request, 'Failure')



    
