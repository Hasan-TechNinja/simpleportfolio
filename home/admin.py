from django.contrib import admin
from . models import home,homess,introduction,about,cart,review,cv,number,sent
# Register your models here.
@admin.register(home)
class homeModelAdmin(admin.ModelAdmin):
    list_display=['id','name','title','discrption','c_img']


@admin.register(homess)
class homeModelAdmin(admin.ModelAdmin):
    list_display=['id','name','title','discrption','c_img','cetagorys']

@admin.register(introduction)

class introductionModelAdmin(admin.ModelAdmin):
    list_display=['id','title','say','host_img']

@admin.register(about)

class adoutModelAdmin(admin.ModelAdmin):
    list_display=['id','title','discription','img']

@admin .register(cart)

class cartModelAdmin(admin.ModelAdmin):
    list_display=['id','title','discription']

@admin.register(review)

class reviewModelAdmin(admin.ModelAdmin):
    list_display=['id','name','discription','img']

@admin.register(cv)

class cvModelAdmin(admin.ModelAdmin):
    list_display=['id','cvt']

@admin.register(number)
class numberModelAdmin(admin.ModelAdmin):
    list_display=['id','contract']

@admin.register(sent)

class sentModelAdmin(admin.ModelAdmin):
    list_display=['id','name','email','subject']