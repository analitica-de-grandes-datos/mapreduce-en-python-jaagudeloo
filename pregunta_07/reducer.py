#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import operator

if __name__ == '__main__':

    tripletas = []

    for line in sys.stdin:

        key, val1, val2 = line.split(",")
        val2 = int(val2)
        tripletas_line = (key, val1, val2)
        tripletas.append(tripletas_line)

    tripletas_ord = sorted(tripletas, key = operator.itemgetter(0, 2))

    for campo in tripletas_ord:
        sys.stdout.write("{}\t{}\t{}\n".format(campo[0], campo[1], campo[2]))