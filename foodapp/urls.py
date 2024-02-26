from .views import OrganizationView ,ItemView,PricingView,DeliveryPriceView,product_selection
from django.urls import path  
  
urlpatterns = [  
    path('Organization/', OrganizationView.as_view()),  
    path('Item/', ItemView.as_view()),  
    path('Pricing/', PricingView.as_view()),  
    path('DeliveryPricing/', DeliveryPriceView.as_view()),  
    path('product-selection/', product_selection, name='product_selection'),
    path('process-selection/', product_selection, name='process_selection'),

]  