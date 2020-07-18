from cmd import *
import datetime
from pprint import pprint

d = datetime.datetime.now()

filename = "Math_Practice_" + d.strftime("%d%b") + ".txt"

def generate_questions(mult = 4, sq = 4, cube = 4, rev_mult = 4):
    multiply(mult)
    cubes(cube)
    squares(sq)
    prime_mult(rev_mult)
    np.random.shuffle(questions)

    with open(filename, 'w') as f:
        for i in questions:
            f.write("%s" % str(questions.index(i) + 1) + ") ")
            f.write("%s\n" % i)
    f.close()

