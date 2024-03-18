from django.db import models

# Create your models here.
class home(models.Model):
    title=models.CharField(max_length=50)
    name=models.CharField( max_length=50)
    discrption=models.TextField()
    c_img=models.ImageField( upload_to='cimg', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return str(self.id)


    
CETAGORY_c=[
    ('M','Men'),
    ('W','Women')
]
class homess(models.Model):
    title=models.CharField(max_length=50)
    name=models.CharField( max_length=50)
    discrption=models.TextField()
    cetagorys=models.CharField(choices=CETAGORY_c, max_length=2)
    c_img=models.ImageField( upload_to='cimg', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return str(self.id)
    
class introduction(models.Model):
    host_img=models.ImageField( upload_to='cimg', height_field=None, width_field=None, max_length=None)
    title=models.CharField( max_length=50)
    say=models.TextField()

class about(models.Model):
    title=models.CharField( max_length=50)
    discription=models.CharField( max_length=200)
    img=models.ImageField(upload_to='cimg', height_field=None, width_field=None, max_length=None)

class cart(models.Model):
    title=models.CharField( max_length=50)
    discription=models.TextField()

class review(models.Model):
    name=models.CharField(max_length=50) 
    discription=models.CharField( max_length=220)
    img=models.ImageField( upload_to='cimg', height_field=None, width_field=None, max_length=None) 

class cv(models.Model):
    cvt=models.FileField( upload_to='cimg', max_length=100) 

class number(models.Model):
    contract=models.CharField( max_length=50)

class sent(models.Model):
    name=models.CharField( max_length=200)
    email=models.EmailField()
    subject=models.TextField()

    def __str__(self):
        return self.name
    