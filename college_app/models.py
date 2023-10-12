from django.db import models



# Create your models here.

class Department(models.Model):
    dept_id=models.CharField(max_length=259,blank=True)
    dept_name=models.CharField(max_length=259)
    class Meta:
        db_table='Department'
        ordering=['dept_id']
    def __str__(self):
        return '{}'.format(self.dept_name)

class Purpose(models.Model):
    purpose_id=models.CharField(max_length=259,blank=True)
    purpose_name=models.CharField(max_length=259)
    class Meta:
        db_table='Purpose'
        ordering=['purpose_id']
    def __str__(self):
        return '{}'.format(self.purpose_name)

class Course(models.Model):
    course_id=models.CharField(max_length=259,blank=True)
    dept_id= models.ForeignKey(Department, on_delete=models.CASCADE)
    course_name=models.CharField(max_length=259)
    class Meta:
        db_table='Course'
        ordering=['course_id']
    def __str__(self):
        return '{}'.format(self.course_name)

class Register(models.Model):
    name = models.CharField(max_length=259, blank=True)
    dob = models.DateField()
    age = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    mail_id = models.EmailField()
    address = models.TextField(blank=True)
    course= models.ForeignKey(Course, on_delete=models.CASCADE)
    purpose=models.ForeignKey(Purpose, on_delete=models.CASCADE)
    material=models.TextField()
    dept_name=models.ForeignKey(Department, on_delete=models.CASCADE)
    class Meta:
        db_table = 'Register'

    def __str__(self):
        return '{}'.format(self.name)