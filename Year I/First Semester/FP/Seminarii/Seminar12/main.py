# complexitate timp


"""
O(n) -> Limita superioara                               |   WORST CASE = cel mai rau caz, exista cazuri cand functioneaza mai bine
Theta(n) -> Limita superioara + Limita inferioara       |   AVG CASE = intotdeauna v-a merge asa
Omega(n) -> Limita inferioara                           |   BEST CASE
"""


def f_1(n: int):

    count = 0
    for i in range(10):
        for j in range(n):
            count += 1

# BC=WC=AC (tot timpul se evalueaza cele doua foruri)
# T(n) = numar de pasi
# T(n) = 10 * n -> Theta(n) [T(n) apartine clasei de complexitate Theta(n)]
#               -> E corect si sa spunem O(n), dar nu este la fel de precis
#               -> E corect si sa spunem O(n^2) dar, din nou, nu este precis


def f_2(n: int):
    count = 0
    for i in range(n, n + 10): # n+10-n = 10 -> range(n, n+10) = 10 pasi
        for j in range(n):
            count += 1
# BC=WC=AC



