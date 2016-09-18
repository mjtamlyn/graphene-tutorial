from django.db import models


class Street(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class House(models.Model):
    street = models.ForeignKey(Street)
    number = models.IntegerField()

    def __str__(self):
        return '%s %s' % (self.number, self.street)


class Person(models.Model):
    name = models.CharField(max_length=255)
    family = models.CharField(max_length=255)
    residence = models.ForeignKey(House)
    parents = models.ManyToManyField('self', blank=True)
    spouse = models.ForeignKey('self', blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.name, self.family)

    class Meta:
        verbose_name_plural = 'people'

    def begat(self, name):
        other = Person.objects.create(name=name, family=self.family, residence=self.residence)
        other.parents.add(self)
        if self.spouse:
            other.parents.add(self.spouse)
        return other

    def married(self, other):
        self.spouse = other
        other.spouse = self
        other.family = self.family
        other.residence = self.residence
        self.save()
        other.save()

    def moved(self, residence):
        self.residence = residence
        self.save()
