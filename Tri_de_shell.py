import random
import time
from math import floor

N = 10000



def tri_shell_1(t):
    cpt_comp = 0
    cpt_trans = 0
    start = time.time()
    incr = N // 2
    while True:

        for k in range(0, incr):
            # tri la k-ieme série

            for i in range(incr + k, N, incr):
                # insertion de t[i] dans sa série
                x = t[i]
                j = i
                cpt_comp += 1
                while j > 0 and t[j - incr] > x:
                    t[j] = t[j - incr]
                    j = j - incr
                    cpt_trans += 1
                t[j] = x

        if incr == 1:
            break
        incr = incr // 2

    temps = time.time()-start
    return (cpt_comp, cpt_trans, temps)


def tri_shell_2(t):
    cpt_comp = 0
    cpt_trans = 0
    start = time.time()
    incr = 1
    while True:

        for k in range(0, incr):
            # tri la k-ieme série

            for i in range(incr + k, N, incr):
                # insertion de t[i] dans sa série
                x = t[i]
                j = i
                cpt_comp += 1
                while j > 0 and t[j - incr] > x:
                    t[j] = t[j - incr]
                    j = j - incr
                    cpt_trans += 1
                t[j] = x

        if incr > N // 2:
            break
        incr = 3 * incr + 1

    temps = time.time() - start
    return (cpt_comp, cpt_trans, temps)


def tri_shell_3(t):
    cpt_comp = 0
    cpt_trans = 0
    start = time.time()
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
                cpt_comp += 1
                while j > 0 and t[j - incr] > x:
                    t[j] = t[j - incr]
                    j = j - incr
                    cpt_trans += 1
                t[j] = x
        if incr > N // 2:
            break
        if ref+1 < len(suite):
            ref = ref+1
            incr = suite[ref]
        else:
            incr = round(incr * 2.3)

    temps = time.time() - start
    return (cpt_comp, cpt_trans, temps)


def tab_rand(taille):
    tab = []
    for i in range(0, taille):
        tab.append(random.randint(1, taille * 5))
    return tab


def tri_dobosiewicz(t):
    cpt_comp = 0
    cpt_trans = 0
    start = time.time()
    fini = False
    intv = len(t) - 1
    while (intv > 1) or not fini:
        intv = floor(intv / 1.3)
        if intv < 1:
            intv = 1
        i = 0
        fini = True
        while (i + intv) <= len(t)-1:
            cpt_comp += 1
            if t[i] > t[i + intv]:
                cpt_trans += 1
                attente = t[i]
                t[i] = t[i + intv]
                t[i + intv] = attente
                fini = False
            i = i + 1

    temps = time.time() - start
    return (cpt_comp, cpt_trans, temps)

def printResult(tupleValues):
    print("\n" + "Comparaisons : " + str(tupleValues[0]) + "\t" + "Transferts : " + str(tupleValues[1]))
    print("Temps : " + str(tupleValues[2]) + "\n")


t = tab_rand(N)
t1 = []
t2 = []
t3 = []
t4 = []
t1 += t
t2 += t
t3 += t
t4 += t


printResult(tri_shell_1(t1))

printResult(tri_shell_2(t2))

printResult(tri_shell_3(t3))

printResult(tri_dobosiewicz(t4))




