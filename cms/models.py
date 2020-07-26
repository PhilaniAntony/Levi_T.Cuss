from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Customer model
class Customer(models.Model) :
    user = models.OneToOneField(User, null=True,blank= True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null =  True)
    phone = models.CharField(max_length=200, null =  True)
    email= models.CharField(max_length=200, null =  True)
    date_created = models.DateTimeField(auto_now_add = True, null =  True)
    image = models.ImageField( null=True, blank= True)
    
    
    
    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
#Adress Model   
class Address(models.Model):
    name = models.CharField(max_length=200, null =  True)
    block = models.CharField(max_length=200, null =  True)
    city = models.CharField(max_length=200, null =  True)
    state = models.CharField(max_length=200, null =  True)
    country = models.CharField(max_length=200, null =  True)
    zipcode = models.CharField(max_length=10, null =  True)
    
    def __str__(self):
        return self.block
    
#Shiiping Adress    
class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, null=True,  on_delete=models.SET_NULL)
	address = models.ForeignKey(Address, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.address    
 
 
#Collection model
class Collection(models.Model) :
    STATUS =(
        ('Active', 'Active'),
        ('Deactived', 'Deactived'),
    )
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=450, null=True)
    status = models.CharField(max_length=200, null =  True, choices = STATUS)
    image = models.ImageField( null=True, blank= True)
    
    def __str__(self):
        return self.name
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 
    
  
#Category model
class Category(models.Model) :
    STATUS =(
        ('Active', 'Active'),
        ('Deactived', 'Deactived'),
    )
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=450, null=True)
    status = models.CharField(max_length=200, null =  True, choices = STATUS)
    image = models.ImageField( null=True, blank= True)
    
    def __str__(self):
        return self.name
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    

#Tags
class Tag(models.Model) :
    name = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name
    
class Paymentmethod(models.Model) :
    name = models.CharField(max_length= 200, null = False)
    value = models.FloatField(null= True)
    date_added = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length= 200, null = False)
    
    def __str__(self):
        return self.name    

#Product Model
class Product(models.Model):
    STATUS =(
        ('Active', 'Active'),
        ('Deactived', 'Deactived'),
    )
    SIZE =(
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
        
    )
    name = models.CharField(max_length=200, null =  True)
    vendor = models.CharField(max_length=200, null =  True)
    productType = models.CharField(max_length=200, null =  True)
    description = models.CharField(max_length=400, null =  True, blank = True)
    quantity = models.IntegerField(default=0)
    hs = models.CharField(max_length=200, null =  True)
    date_created = models.DateTimeField(auto_now_add = True, null =  True)
    digital = models.BooleanField(default=False,null=True, blank=True)
    status = models.CharField(max_length=200, null =  True, choices = STATUS)
    size = models.CharField(max_length=200, null =  True, choices = SIZE)
    color = models.CharField(max_length=200, null =  True)
    note = models.CharField(max_length=450, blank = True )
    unitPrice = models.FloatField(null= True)
    discount = models.FloatField(null= True)
    image = models.ImageField(null=True, blank=True)
    category = models.ManyToManyField(Category)
    collection = models.ManyToManyField(Collection)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    @property
    def productPrice(self):
        if self.discount :
            price = self.productPrice - self.discount
            return price
        
#Supliers
class Supplier(models.Model):
    STATUS =(
        ('Active', 'Active'),
        ('Deactived', 'Deactived'),
    )
    product = models.ManyToManyField(Product)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    paymentmethod = models.ForeignKey(Paymentmethod, null = True, on_delete= models.SET_NULL) 
    name = models.CharField(max_length=200, null=False)
    email = models.EmailField(max_length=200, null=False)
    phone = models.CharField(max_length=200, null=False)
    url = models.CharField(max_length=200, null =  True)
    handler = models.CharField(max_length=200, null=False)
    image = models.ImageField( null=True, blank= True)
    status = models.CharField(max_length=200, null =  True, choices = STATUS)
    note = models.CharField(max_length=200, null =  True) 
    paymentMethod = models.CharField(max_length=200, null =  True)
    
    def __str__(self):
        return self.name
    
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 
    
        

     
#Order items    
class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

#Orders Model
class Order (models.Model) :
    STATUS =(
        ('Pending', '   Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'delivered'),
    )
    orderItems = models.ForeignKey(OrderItem, null = True, on_delete= models.SET_NULL)
    customer = models.ForeignKey(Customer, null = True, on_delete= models.SET_NULL)
    paymentmethod = models.ForeignKey(Paymentmethod, null = True, on_delete= models.SET_NULL)
    
    date_created = models.DateTimeField(auto_now_add = True, null =  True)
    status = models.CharField(max_length=200, null =  True, choices = STATUS)
    note = models.CharField(max_length=1000, null =  True)
    address = models.ForeignKey(ShippingAddress, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.product.name
    
    @property
    def shipping(self):
        shipping = False
        orderitems =  self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
    

    
#Shippers
class Shippers(models.Model):
    STATUS =(
        ('Active', 'Active'),
        ('Deactived', 'Deactived'),
    )
    
    Order = models.ManyToManyField(Order)
    address = models.ForeignKey(Address, null=True, on_delete=models.CASCADE)
    paymentmethod = models.ForeignKey(Paymentmethod, null = True, on_delete=models.SET_NULL)
    
    name = models.CharField(max_length=200, null=False)
    email = models.EmailField(max_length=200, null=False)
    phone = models.CharField(max_length=200, null=False)
    url = models.CharField(max_length=200, null =  True)
    handler = models.CharField(max_length=200, null=False)
    image = models.ImageField( null=True, blank= True)
    status = models.CharField(max_length=200, null =  True, choices = STATUS)
    
    
    note = models.CharField(max_length=200, null =  True) 
    paymentMethod = models.CharField(max_length=200, null =  True)
    
    def __str__(self):
        return self.name
    
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
 
    
    




        
    




    
		






 


    
