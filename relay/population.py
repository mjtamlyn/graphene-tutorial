from .models import House, Person, Street


def create_village():
    afon = Street.objects.create(name='Afon Stryd')
    glyn = Street.objects.create(name='Glyn Stryd')
    ysgol = Street.objects.create(name='Ysgol Stryd')

    afon_1 = House.objects.create(street=afon, number=1)
    afon_2 = House.objects.create(street=afon, number=2)
    afon_3 = House.objects.create(street=afon, number=3)

    glyn_1 = House.objects.create(street=glyn, number=1)
    glyn_2 = House.objects.create(street=glyn, number=2)
    glyn_3 = House.objects.create(street=glyn, number=3)

    ysgol_1 = House.objects.create(street=ysgol, number=1)
    ysgol_2 = House.objects.create(street=ysgol, number=2)
    ysgol_3 = House.objects.create(street=ysgol, number=3)
    ysgol_4 = House.objects.create(street=ysgol, number=4)

    lowri_jones = Person.objects.create(name='Lowri', family='Jones', residence=afon_1)
    dafydd_jones = lowri_jones.begat('Dafydd')
    dafydd_jones.moved(glyn_1)
    bethan_jones = lowri_jones.begat('Bethan')
    bethan_jones.moved(glyn_3)

    cerys_jones = Person.objects.create(name='Cerys', family='Jones', residence=glyn_1)
    dafydd_jones.married(cerys_jones)
    cerys_jones.begat('Arthur')

    gareth_williams = Person.objects.create(name='Gareth', family='Williams', residence=afon_2)
    gwen_williams = Person.objects.create(name='Gwen', family='Williams', residence=afon_2)
    gareth_williams.married(gwen_williams)
    gwen_williams.begat('Ieuan')

    john_davies = Person.objects.create(name='John', family='Davies', residence=afon_3)
    anna_davies = Person.objects.create(name='Anna', family='Davies', residence=afon_3)
    john_davies.married(anna_davies)
    llewelyn_davies = anna_davies.begat('Llewelyn')
    llewelyn_davies.moved(ysgol_1)
    gwyneth_davies = Person.objects.create(name='Gwyneth', family='Davies', residence=ysgol_2)
    llewelyn_davies.married(gwyneth_davies)
    gwyneth_davies.begat('Huw')
    gwyneth_davies.begat('Gethin')

    lloyd_davies = anna_davies.begat('Lloyd')
    lloyd_davies.moved(ysgol_2)

    Person.objects.create(name='Tristan', family='Roberts', residence=glyn_2)
    Person.objects.create(name='Nia', family='Evans', residence=ysgol_3)
    Person.objects.create(name='Owain', family='Thomas', residence=ysgol_4)


def destroy_village():
    Person.objects.all().delete()
    House.objects.all().delete()
    Street.objects.all().delete()
