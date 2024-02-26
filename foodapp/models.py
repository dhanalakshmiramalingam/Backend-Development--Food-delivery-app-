from django.db import models

# Create your models here.

from django.urls import reverse  # To generate URLS by reversing URL patterns


class Organization(models.Model):
    """Model representing a organization"""
    id = models.CharField( 
        max_length=200,
        primary_key=True,
        help_text="Enter the organization ID.")
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter the organization name."
    )

    # def get_absolute_url(self):
    #     """Returns the url to access a particular genre instance."""
    #     return reverse('org-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class Item(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    id= models.CharField(primary_key=True,max_length=200)
    type= models.CharField(max_length=200)
    item_price_per_pack = models.CharField(max_length=200)
    # Foreign Key used because book can only have one author, but authors can have multiple books.
    # Author as a string rather than object because it hasn't been declared yet in file.
    description = models.TextField(
        max_length=1000, 
        help_text="Enter a brief description of the food Item")

    """ class Meta:
        ordering = ['id', 'type','description']""" 

    """ def get_absolute_url(self):
        #Returns the url to access a particular book record.
        return reverse('item-detail', args=[str(self.description)])
    """
    def __str__(self):
        """String for representing the Model object."""
        return self.title


import uuid  # Required for unique book instances
from datetime import date

from django.conf import settings  # Required to assign User as a borrower


class Pricing(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    pricing_id=models.CharField(primary_key=True,max_length=200)
    organization_id = models.CharField(max_length=200)
    item_id =models.CharField(max_length=200)
    zone = models.CharField(max_length=200)
    base_distance_in_km = models.CharField(max_length=200)
    item_price_per_pack = models.CharField(max_length=200)
    km_price = models.FloatField()  # Variable cost per kilometer
    fix_price = models.FloatField()  # Fixed cost
    #total_delivery_price=models.FloatField()
    
    """ class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_returned", "Set book as returned"),) """

    """ def get_absolute_url(self):
        #Returns the url to access a particular book instance.
        return reverse('pricinginstance-detail', args=[str(self.pricing_id)]) 
    """

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.organization_id} ({self.item_id})'


class Bill_Per_Item(models.Model):
    """Model representing an author."""
    bill_id_per_item=models.CharField(primary_key=True,max_length=100)
    first_name = models.CharField(max_length=100)
    date_of_purchase = models.DateField(null=True, blank=True)
    item_id = models.ForeignKey('Item', on_delete=models.RESTRICT, null=True)
    quantity=models.CharField(max_length=100)
    organization_id=models.ForeignKey('Organization', on_delete=models.RESTRICT, null=True)
    bill_amt=models.CharField(max_length=100)
    


    """ def get_absolute_url(self):
        #Returns the url to access a particular author instance.
        return reverse('billperitem-detail', args=[str(self.id)]) """

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.bill_id_per_item}, {self.bill_amt}'

class TotalBill(models.Model):
    """Model representing an author."""
    bill_id=models.CharField(primary_key=True,max_length=100)
    bill_id_per_item=models.ForeignKey('Bill_Per_Item', on_delete=models.RESTRICT, null=True)
    first_name = models.CharField(max_length=100)
    date_of_purchase = models.DateField(null=True, blank=True)
    total_bill_amt=models.CharField(max_length=100)
    


    """ def get_absolute_url(self):
        #Returns the url to access a particular author instance.
        return reverse('total-detail', args=[str(self.bill_id)]) """

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.bill_id}, {self.total_bill_amt}'

