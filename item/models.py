from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})
    
class item(models.Model):
        category = models.ForeignKey(Category , related_name = 'items' , on_delete = models.CASCADE)
        name = models.CharField(max_length=255)
        description = models.TextField(blank = True , null=True)
        price = models.FloatField()
        is_sold = models.BooleanField(default=False)
        image = models.ImageField(upload_to ='item_images' , blank=True , null=True)
        created_by = models.ForeignKey(User , related_name = 'items' , on_delete = models.CASCADE)
        created_at = models.DateField(auto_now_add = True)
        

