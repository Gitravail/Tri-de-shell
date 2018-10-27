import random
import time
from math import floor

N = 20

"""code qui marche"""


def tri_shell(t):
    incr = N // 2
    while True:

        for k in range(0, incr):
            # tri la k-ieme série

            for i in range(incr + k, N, incr):
                # insertion de t[i] dans sa série
                x = t[i]
                j = i

                while j > 0 and t[j - incr] > x:
                    t[j] = t[j - incr]
                    j = j - incr

                t[j] = x

        if incr == 1:
            break
        incr = incr // 2


def tri_shell_2(t):
    incr = 1
    while True:

        for k in range(0, incr):
            # tri la k-ieme série

            for i in range(incr + k, N, incr):
                # insertion de t[i] dans sa série
                x = t[i]
                j = i

                while j > 0 and t[j - incr] > x:
                    t[j] = t[j - incr]
                    j = j - incr

                t[j] = x

        if incr == 1:
            break
        incr = 3 * incr + 1


def tri_shell_3(t):
    suite = [1, 4, 10, 23, 57, 132, 301, 701]
    ref = 0
    incr = suite[ref]
    while True:
        for k in range(0, incr):
            # tri la k-ieme série

            for i in range(incr + k, N, incr):
                # insertion de t[i] dans sa série
                x = t[i]
                j = i

                while j > 0 and t[j - incr] > x:
                    t[j] = t[j - incr]
                    j = j - incr

                t[j] = x

        if ref < len(suite):
            ref = ref+1
            incr = suite[ref]
        else:
            incr = round(incr * 2.3)

        if incr > N // 2:
            break


def tab_rand(taille):
    tab = []
    for i in range(0, taille):
        tab.append(random.randint(1, taille * 5))
    return tab


def tri_dobosiewicz(t):
    fini = False
    intv = len(t) - 1
    while (intv > 1) or not fini:
        intv = floor(intv / 1.3)
        if intv < 1:
            intv = 1
        i = 0
        fini = True
        while (i + intv) <= len(t)-1:
            if t[i] > t[i + intv]:
                attente = t[i]
                t[i] = t[i + intv]
                t[i + intv] = attente
                fini = False
            i = i + 1




t1 = [5, 41, 53, 11, 20, 5, 1, 9, 12, 102, 15, 23, 43, 2, 36, 209, 167, 125, 97, 49, 43]
t2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#t = [2, 13, 9, 20, 12, 11, 18, 5, 3, 17, 8, 10, 16, 7, 6, 1, 14, 19, 4, 15]
t = tab_rand(N)
print("Avant : ", t)

debut = time.time()
tri_dobosiewicz(t)
#tri_shell_3(t)
fin = time.time()

print("Apres : ", t)
print("duree : ", fin - debut)
