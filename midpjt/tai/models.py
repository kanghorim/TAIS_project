from django.db import models

# Create your models here.
class TACHART(models.Model):
    occur_yr = models.IntegerField()
    occur_mn = models.IntegerField()
    occur_hr = models.CharField(max_length=26)
    num_death = models.IntegerField()
    num_heavy_injury = models.IntegerField()
    num_middle_injury = models.IntegerField()
    num_light_injury = models.IntegerField()
    occur_city = models.CharField(max_length=26)
    occur_provin = models.CharField(max_length=26)
    occur_dong = models.CharField(max_length=26)
    occur_road_name_yn = models.CharField(max_length=26)
    road_condition = models.CharField(max_length=26)
    weath_info = models.CharField(max_length=26)
    attacker_gender = models.CharField(max_length=26)
    attacker_human_age = models.CharField(max_length=26)
    accident_gender = models.CharField(max_length=26)
    accident_human_age = models.CharField(max_length=26)

    def __str__(self) :
        return self.occur_city
