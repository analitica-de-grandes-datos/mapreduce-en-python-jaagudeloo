#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
from collections import defaultdict
import operator

if __name__ == '__main__':

    diccio = defaultdict(list)

    for line in sys.stdin:

        numero, val = line.replace("\n","").strip().split("	")
        val = val.split(",")
        numero = int(numero)
        for elemento in val:
            diccio[elemento].append(numero)

    diccio_ord = sorted(diccio.items(), key = operator.itemgetter(0))

    for clave, valor in diccio_ord:
        datos_num = sorted(valor, key = int)
        valor = ",".join(map(str, datos_num))
        sys.stdout.write("{}	{}\n".format(clave, valor))