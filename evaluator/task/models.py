from django.db import models


month = [
    ('Jan', 'January'),
    ('Feb', 'February'),
    ('Mar', 'March'),
    ('Apr', 'April'),
    ('May', 'May'),
    ('Jun', 'June'),
    ('Jul', 'July'),
    ('Aug', 'August'),
    ('Sep', 'September'),
    ('Oct', 'October'),
    ('Nov', 'November'),
    ('Dec', 'December'),
]


class Companie(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Information(models.Model):
    name = models.ForeignKey(Companie, on_delete=models.CASCADE)
    year = models.IntegerField(default=2019)
    month = models.TextField(max_length=3, choices=month)
    score = models.IntegerField()

    def __str__(self):
        return self.month
