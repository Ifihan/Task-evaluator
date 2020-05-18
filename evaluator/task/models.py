from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


MONTH = [
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


# COLOR = [
#     ('red', range(0, 49)),
#     ('green', range(70, 100)),
# ]

COLOR = [
    ('red', 'RED'),
    ('green', 'GREEN'),
]


class Companie(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Information(models.Model):
    name = models.ForeignKey(Companie, on_delete=models.CASCADE)
    year = models.IntegerField(default=2019)
    month = models.TextField(max_length=3, choices=MONTH)
    score = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(100)])

    # @staticmethod
    # def color(self):
    #     if self.filter(score__gt='69'):
    #         return "circle green"
    #
    #     if self.filter(score__lt='70'):
    #         return "circle red"

    def __str__(self):
        return ' %s - %s ' % (self.year, self.month)
