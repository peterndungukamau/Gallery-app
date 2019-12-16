from django.db import models

class Image (models.Model):
    image_name = models.CharField(max_length=50)
    image_desc = models.CharField(max_length=50)
    img_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.image_name

    
    def save_image(self):
        self.save()

class location(models.Model):
    place = models.CharField(max_length=50)

    def __str__(self):
        return self.place

class Category(models.Model):
    category = models.CharField(max_length=60)
    post = models.TextField()
    image = models.ForeignKey(Image)
    location = models.ManyToManyField(location)
    article_image = models.ImageField(upload_to = 'category/')

    @classmethod
    def dis_name(cls):
        pics = cls.objects.all()
        return pics

    
    @classmethod
    def search_by_category(cls,search_term):
        pics = cls.objects.filter(category__icontains=search_term)
        return pics


    def __str__(self):
        return self.category