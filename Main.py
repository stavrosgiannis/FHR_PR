from Flugzeug import Flugzeug
from Transportflugzeug import Transportflugzeug
from Zuladung import Zuladung

Z = Zuladung(1, 5, 600)
F = Flugzeug(None, 25)
Tf = Transportflugzeug(F, 5, 5000)
Tf.addZuladung(Z)
print(Tf.getMaximalesZuladungsgewicht())
print(F.getFlugzeugnummer())
print(F.istFlugzeugGueltig())

