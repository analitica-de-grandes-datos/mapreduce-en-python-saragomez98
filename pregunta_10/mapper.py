#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
from operator import itemgetter
import sys 
if __name__ == "__main__":
    for line in sys.stdin:
        column_separated = line.split()

        sys.stdout.write("{}\t{}\n".format(
            column_separated[0], column_separated[1]))
