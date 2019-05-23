from django.db import models
from django.db.models import Avg
from .round import Round

class Currency(models.Model):
    class Meta:
        db_table = 'currency'
        constraints = [models.UniqueConstraint(fields=['name'], name='name_unique_constraint')]
    name = models.CharField(max_length=5)
    def __str__(self):
        return self.name

class Rate(models.Model):
    class Meta:
        db_table = 'rate'
    currency_id = models.ForeignKey(Currency, on_delete=models.CASCADE)
    date = models.DateField()
    rate = models.DecimalField(max_digits=20, decimal_places=8)
    volume = models.DecimalField(max_digits=20, decimal_places=8)
    def __str__(self):
        return '%s %s'%(self.currency_id.name, str(self.date))

    @staticmethod
    def get_rate_data(needed_date, curr_id):
        data = Rate.objects \
            .filter(currency_id=curr_id, date__gte=needed_date) \
            .aggregate(avg_volume=Round(Avg('volume')))
        data['last_rate'] = Rate.objects.filter(currency_id=curr_id).order_by('-id')[:1].get().rate
        return data