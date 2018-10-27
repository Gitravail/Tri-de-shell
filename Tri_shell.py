import time
N = 20


"""code dans le cours (ne marche pas)"""
# def Tri_shell(t):
#     incr = N//2
#     while True:
#
#         for k in range(1, incr):
#             # tri la k-ieme série
#
#             for i in range(incr + k, N, incr):
#                 # insertion de t[i] dans sa série
#                 x = t[i]
#                 j = i - incr
#
#                 while j >= 1 and t[j]:
#                     t[j + incr] = t[j]
#                     j = j - incr
#
#                 t[j + incr] = x
#
#
#         if incr == 1:
#             break
#         incr = incr // 2



"""code qui marche"""
def Tri_shell(t):
    incr = N // 2
    while True:

        for k in range(0, incr):
            # tri la k-ieme série

            for i in range(incr + k, N, incr):
                # insertion de t[i] dans sa série
                x = t[i]
                j = i

                while j > 0 and t[j-incr] > x:
                    t[j] = t[j - incr]
                    j = j - incr

                t[j] = x

        if incr == 1:
            break
        incr = incr // 2


def Tri_shell_2(t):
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


def Tri_shell_3(t):
    suite = [1, 4, 10, 23, 57, 132]
    incr = 1
    while True:

        for k in range (1, incr):
            # tri la k-ieme série

            for i in range (incr + k, N, incr):
                # insertion de t[i] dans sa série
                x = t[i]
                j = i - incr

                while j >= 1 and t[j]:
                    t[j + incr] = t[j]
                    j = j - incr


                t[j + incr] = x
        incr = 3*incr + 1
        if incr > N//2:
            break


t1 = [5, 41, 53, 11, 20, 5, 1, 9, 12, 102, 15, 23, 43, 2, 36, 209, 167, 125, 97, 49, 43]
t2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
t = [2, 13, 9, 20, 12, 11, 18, 5, 3, 17, 8, 10, 16, 7, 6, 1, 14, 19, 4, 15]
print("Avant : ", t)

debut = time.time()
Tri_shell_2(t)
fin = time.time()


print("Apres : ", t)
print("duree : ", fin - debut)
