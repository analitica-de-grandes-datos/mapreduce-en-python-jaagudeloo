#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    suma = 0
    recuento = 0

    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)

        if key == curkey:
            recuento = recuento + 1
            suma = suma + val
        else:

            if curkey is not None:

                sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, suma/recuento))
                contador = 0

            curkey = key
            suma = val
            recuento = 1

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, suma/recuento))