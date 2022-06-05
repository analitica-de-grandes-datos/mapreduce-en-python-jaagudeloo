#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    tabla = [line.replace("\n", "") for line in sys.stdin]
    tabla = [line.split(",") for line in tabla]
    col_3 = [tabla[i][3] for i in range(len(tabla))]
    col_4 = [tabla[i][4] for i in range(len(tabla))]

    for line in range(len(tabla)):
        sys.stdout.write("{}\t{}\n".format(col_3[line],col_4[line]))