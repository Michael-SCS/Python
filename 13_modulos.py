### Modules ###

import modules
modules.multiplicacion(2,4)
modules.sumatoria(10,587)
#los import no reciben archivos que su primer caracter sea un número
from modules import multiplicacion, sumatoria
multiplicacion(2,5)
sumatoria(5,10)

import math
print(math.pi)

from math import pi as pi_valor

print(pi_valor*2)