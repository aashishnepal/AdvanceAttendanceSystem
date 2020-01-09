from django.db import models

class student(models.Model):
    full_name = models.CharField(max_length=100)

    email = models.EmailField()
    
    mac_address = models.CharField(max_length=200)

    roll_no = models.CharField(max_length=10, default='0000000000')

    attendence_stat = models.BooleanField(default= False)
    
    

    def __str__(self):
        return self.full_name


class attendance_history(models.Model):
    student = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=10, default='0000000000')
    datetime = models.DateTimeField()
    attendance = models.BooleanField(default= True)

    def __str__(self):
        return self.student


class total_record(models.Model):
    student = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=10, default='0000000000')
    total_days = models.IntegerField(default = 0)

    def __str__(self):
        return self.student
