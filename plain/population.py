from .objects import House, Person, Street


afon = Street('Afon Stryd')
glyn = Street('Glyn Stryd')
ysgol = Street('Ysgol Stryd')

streets = [afon, glyn, ysgol]

afon_1 = House(afon, 1)
afon_2 = House(afon, 2)
afon_3 = House(afon, 3)

glyn_1 = House(glyn, 1)
glyn_2 = House(glyn, 2)
glyn_3 = House(glyn, 3)

ysgol_1 = House(ysgol, 1)
ysgol_2 = House(ysgol, 2)
ysgol_3 = House(ysgol, 3)
ysgol_4 = House(ysgol, 4)

houses = [afon_1, afon_2, afon_3, glyn_1, glyn_2, glyn_3, ysgol_1, ysgol_2, ysgol_3, ysgol_4]

lowri_jones = Person('Lowri', 'Jones', afon_1)
dafydd_jones = lowri_jones.begat('Dafydd')
dafydd_jones.moved(glyn_1)
bethan_jones = lowri_jones.begat('Bethan')
bethan_jones.moved(glyn_3)

cerys_jones = Person('Cerys', 'Jones', glyn_1)
dafydd_jones.married(cerys_jones)
arthur_jones = cerys_jones.begat('Arthur')

gareth_williams = Person('Gareth', 'Williams', afon_2)
gwen_williams = Person('Gwen', 'Williams', afon_2)
gareth_williams.married(gwen_williams)
ieuan_williams = gwen_williams.begat('Ieuan')

john_davies = Person('John', 'Davies', afon_3)
anna_davies = Person('Anna', 'Davies', afon_3)
john_davies.married(anna_davies)
llewelyn_davies = anna_davies.begat('Llewelyn')
llewelyn_davies.moved(ysgol_1)
gwyneth_davies = Person('Gwyneth', 'Davies', ysgol_2)
llewelyn_davies.married(gwyneth_davies)
huw_davies = gwyneth_davies.begat('Huw')
gethin_davies = gwyneth_davies.begat('Gethin')

lloyd_davies = anna_davies.begat('Lloyd')
lloyd_davies.moved(ysgol_2)

tristan_roberts = Person('Tristan', 'Roberts', glyn_2)
nia_evans = Person('Nia', 'Evans', ysgol_3)
owain_thomas = Person('Owain', 'Thomas', ysgol_4)

people = [
    lowri_jones,
    dafydd_jones,
    bethan_jones,
    cerys_jones,
    arthur_jones,
    gareth_williams,
    gwen_williams,
    ieuan_williams,
    john_davies,
    anna_davies,
    llewelyn_davies,
    gwyneth_davies,
    huw_davies,
    gethin_davies,
    lloyd_davies,
    tristan_roberts,
    nia_evans,
    owain_thomas,
]
