#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    contador = 0

    for line in sys.stdin:

        key, val = line.split("\t")
        val = int(val)

        if key == curkey:
            if contador >= val:
                contador = contador
            else:
                contador = val
        else:

            if curkey is not None:

                sys.stdout.write("{}\t{}\n".format(curkey, contador))
                contador = 0

            curkey = key
            contador = val

    sys.stdout.write("{}\t{}\n".format(curkey, contador))