#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    tabla = [line.replace("\n", "") for line in sys.stdin]
    tabla = [line.split("   ") for line in tabla]
    col_1 = [tabla[i][1] for i in range(len(tabla))]
    col_1 = [line.split("-") for line in col_1]
    col_1_1 = [col_1[i][1] for i in range(len(col_1))]

    for line in col_1_1:
        sys.stdout.write("{}\t1\n".format(line))