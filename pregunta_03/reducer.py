#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import operator

if __name__ == '__main__':

    diccio = {}

    for line in sys.stdin:

        key, val = line.split("\t")
        val = int(val)
        diccio[key] = val

    diccio_ord = sorted(diccio.items(), key = operator.itemgetter(1))

    for campo in diccio_ord:
        sys.stdout.write("{},{}\n".format(campo[0], campo[1]))