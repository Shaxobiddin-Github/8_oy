from django.db import models

# Create your models here.


class FoodType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100)
    food_type = models.ForeignKey(FoodType,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(default=1)  # 1 dan 5 gacha reyting
    text = models.TextField(blank=True, null=True)  # Fikr
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.food.name} - {self.rating} by {self.author}"