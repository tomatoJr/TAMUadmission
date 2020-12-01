from django.db import models
# import django_filters
# Create your models here.

# class Test(models.Model):
#     name = models.CharField(max_length=50)


class Applicant(models.Model):
    App_Seq_No = models.AutoField(primary_key=True)
    Application_ID = models.CharField(max_length=10)
    Average_Review_Score = models.FloatField()
    Applied_Degree = models.CharField(max_length=50)
    Nationality = models.CharField(max_length=100)
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Research_Interest = models.CharField(max_length=500)
    Potential_Faculty = models.CharField(max_length=500)
    BS_University_and_GPA = models.CharField(max_length=500)
    MS_University_and_GPA = models.CharField(max_length=500)
    GRE_Score = models.IntegerField()
    TOEFL_Score = models.IntegerField()
    Gender = models.CharField(max_length=50)
    Ethnicity = models.CharField(max_length=50)
    Residency = models.CharField(max_length=50)
    Citizenship = models.CharField(max_length=50)
    Faculty_Contact = models.CharField(max_length=50)
    Faculty_giving_GANT_GAT = models.CharField(max_length=50)
    Faculty_giving_GAR = models.CharField(max_length=50)

    def __str__(self):
        return self.Name+" "+str(self.App_Seq_No)

    class Meta:
        ordering = ['App_Seq_No']


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    faculty = models.CharField(max_length=50)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)

    score = models.IntegerField()
    faculty_decision = models.CharField(max_length=50)
    assistantship_decision = models.CharField(max_length=50)
    nomination = models.CharField(max_length=50)
    comments = models.CharField(max_length=50000)

    def __str__(self):
        return self.faculty+" "+self.comments
