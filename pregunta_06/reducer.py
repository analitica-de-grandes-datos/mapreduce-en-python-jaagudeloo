#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    maximo = 0
    minimo = 0

    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)

        if key == curkey:
            if maximo > val:
                maximo = maximo
            else:
                maximo = val
            
            if minimo < val:
                minimo = minimo
            else:
                minimo = val
        else:

            if curkey is not None:

                sys.stdout.write("{}\t{}\t{}\n".format(curkey, maximo, minimo))
                contador = 0

            curkey = key
            maximo = val
            minimo = val

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, maximo, minimo))