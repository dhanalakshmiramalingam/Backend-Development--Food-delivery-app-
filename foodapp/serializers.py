from rest_framework import serializers  
from .models import Organization, Item, Pricing
  
  
class OrganizationSerializer(serializers.ModelSerializer):  
    id = serializers.CharField(max_length=200, required=True)  
    name = serializers.CharField(max_length=200, required=True)  

  
    class Meta:  
        model = Organization  
        fields = ('__all__')  
    
    def create(self, validated_data):  
        """ 
        Create and return a new `Students` instance, given the validated data. 
        """  
        return Organization.objects.create(**validated_data)  
  
    def update(self, instance, validated_data):  
        """ 
        Update and return an existing `Students` instance, given the validated data. 
        """  
        instance.id = validated_data.get('id', instance.id)  
        instance.name = validated_data.get('name', instance.name)  
  
        instance.save()  
        return instance  

class ItemSerializer(serializers.ModelSerializer):  
    id = serializers.CharField(max_length=200, required=True)  
    type = serializers.CharField(max_length=200, required=True)  
    description = serializers.CharField(max_length=200, required=True)
    item_price_per_pack = serializers.CharField(max_length=200)

  
    class Meta:  
        model = Item  
        fields = ('__all__')  

    def create(self, validated_data):  
        """ 
        Create and return a new `Students` instance, given the validated data. 
        """  
        return Item.objects.create(**validated_data)  
  
    def update(self, instance, validated_data):  
        """ 
        Update and return an existing `Students` instance, given the validated data. 
        """  
        instance.id = validated_data.get('id', instance.id)  
        instance.type = validated_data.get('type', instance.type)  
        instance.description = validated_data.get('description', instance.description) 
  
        instance.save()  
        return instance  

class PricingSerializer(serializers.ModelSerializer):  
    pricing_id = serializers.CharField(max_length=200, required=True)  
    organization_id = serializers.CharField(max_length=200)
    item_id = serializers.CharField(max_length=200)
    zone = serializers.CharField(max_length=200)
    base_distance_in_km = serializers.CharField(max_length=200)
    item_price_per_pack = serializers.CharField(max_length=200)
    km_price = serializers.FloatField()  # Variable cost per kilometer
    fix_price = serializers.FloatField()  # Fixed cost
    #total_delivery_price=models.FloatField()

  
    class Meta:  
        model = Pricing  
        fields = ('__all__')  

    def create(self, validated_data):  
        """ 
        Create and return a new `Students` instance, given the validated data. 
        """  
        return Pricing.objects.create(**validated_data)  
  
    def update(self, instance, validated_data):  
        """ 
        Update and return an existing `Students` instance, given the validated data. 
        """  
        instance.pricing_id = validated_data.get('pricing_id', instance.pricing_id)  
        instance.organization_id = validated_data.get('organization_id', instance.organization_id)  
        instance.item_id = validated_data.get('item_id', instance.item_id) 
        instance.zone = validated_data.get('zone', instance.zone) 
        instance.base_distance_in_km = validated_data.get('base_distance_in_km', instance.base_distance_in_km) 
        instance.item_price_per_pack = validated_data.get('item_price_per_pack', instance.item_price_per_pack) 
        instance.km_price = validated_data.get('km_price', instance.km_price)
        instance.fix_price = validated_data.get('fix_price', instance.fix_price) 
 
  
        instance.save()  
        return instance  

# class DeliveryPricingSerializer(serializers.ModelSerializer):  
#     zone = serializers.CharField(max_length=200, required=True)  
#     organization_id = serializers.CharField(max_length=200)
#     total_distance = serializers.CharField(max_length=200)
#     item_type = serializers.CharField(max_length=200)
#     total_delivery_price=models.FloatField()

  
#     class Meta:  
#         model = Pricing  
#         fields = ('__all__') 