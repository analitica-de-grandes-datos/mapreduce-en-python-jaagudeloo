#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    tabla = [line.replace("\n", "") for line in sys.stdin]
    tabla = [line.split(",") for line in tabla]
    col_2 = [tabla[i][2] for i in range(len(tabla))]

    for line in col_2:
        sys.stdout.write("{}\t1\n".format(line))