from django.db import models


month = (
    ('January', 'Jan'),
    ('February', 'Feb'),
    ('March', 'Mar'),
    ('April', 'Apr'),
    ('May', 'May'),
    ('June', 'Jun'),
    ('July', 'Jul'),
    ('August', 'Aug'),
    ('September', 'Sep'),
    ('October', 'Oct'),
    ('November', 'Nov'),
    ('December', 'Dec'),
)


class Company(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Information(models.Model):
    name = models.ForeignKey(Company, on_delete=models.CASCADE)
    month = models.CharField(max_length=3, choices=month)
    Score = models.IntegerField()

    def __str__(self):
        return self.name, " - ", self.month
