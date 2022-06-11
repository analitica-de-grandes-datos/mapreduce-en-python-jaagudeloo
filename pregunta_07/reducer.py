#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import operator

if __name__ == '__main__':

    diccio = {}

    for line in sys.stdin:

        key, val1, val2 = line.split("\t")
        val2 = int(val2)
        diccio[key] = (val1, val2)

    lista_ord = sorted(diccio.items(), key = operator.itemgetter(0,2))

    for campo in lista_ord:
        sys.stdout.write("{},{},{}\n".format(campo[0], campo[1], campo[2]))