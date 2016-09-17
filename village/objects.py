import attr


@attr.s
class Street(object):
    name = attr.ib()

    def __str__(self):
        return self.name


@attr.s
class House(object):
    street = attr.ib()
    number = attr.ib()

    def __str__(self):
        return '%s %s' % (self.number, self.street)


@attr.s
class Person(object):
    name = attr.ib()
    family = attr.ib()
    residence = attr.ib()
    parents = attr.ib(default=attr.Factory(list), cmp=False, repr=False)
    spouse = attr.ib(default=None, cmp=False, repr=False)

    def __str__(self):
        return '%s %s' % (self.name, self.family_name)

    def begat(self, name):
        other = Person(name=name, family=self.family, residence=self.residence)
        other.parents.append(self)
        if self.spouse:
            other.parents.append(self.spouse)
        return other

    def married(self, other):
        self.spouse = other
        other.spouse = self
        other.family = self.family
        other.residence = self.residence

    def moved(self, residence):
        self.residence = residence
