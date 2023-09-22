from django.contrib import admin
from .models import Category,Post,SignUpModel
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['image_tag','cat_id','title','description','url','add_date']
    search_fields=['title']
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['image','post_id','title','content','url','cat_id','video']
    search_fields=['title']
    list_filter=['cat_id']
    

admin.site.register(SignUpModel)
