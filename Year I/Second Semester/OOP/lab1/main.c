#include <stdio.h>
#include <stdbool.h>

//8.  Tipareste exponentul la care numarul prim p apare in descompunerea
//in factori primi a numarului N = 1*2*...*n (n natural nenul dat).

// 1*2*3*4*5*6

/*
 * Checks if a given number is prime.
 * param number: the given number
 * type number: int
 * return: true if the number is prime, false otherwise
 * rtype: bool
 */
bool prim(int number)
{
    if(number <= 1) return 0;
    if(number == 2) return 1;
    if(number%2 == 0) return 0;
    for(int d = 3; d*d <= number; d++)
        if(number%d == 0)
            return 0;
    return 1;
}

/*
 *Computes the exponent of a prime value in the prime factorization of a given natural number
 * param number: the given number
 * type number: int
 * param factor: the prime value
 * type factor: int
 * return: the exponent of the value in the prime factorization of the number
 *         or -1 if the given value is not prime
 * rtype: int
 */
int exponent(int number, int factor)
{
    if(!prim(factor)) return -1;
    int d, fact, exp = 0;
    for(d = factor; d <= number; d++) {
        if (d % factor == 0) {
            fact = d;
            while (fact % factor == 0) { exp++; fact /= factor; }
        }
    }

    return exp;

}

/*
 *Computes the factorial of a natural number
 *param number: a natural number
 *type number: int
 *return: the factorial of the given number
 *rtype: int
*/
int factorial(int number)
{
    int fact = 1;
    while(number > 1)
        fact *= number, number--;
    return fact;
}

void run()
{
    int N, n, p, exp, option;
    while(true) {
        printf("1.Calcul exponent\n2.Iesire\nIntroduceti optiunea:");
        scanf("%d", &option);
        if(option == 1) {
            printf("%s", "n=");
            scanf("%d", &n);
            printf("%s", "p=");
            scanf("%d", &p);

            if (n <= 0)
                printf("Numarul %d nu este natural nenul.\n\n", n);

            else {

                N = factorial(n);

                //printf("%d\n", N);

                exp = exponent(n, p);

                if (exp)
                    if (exp == -1)
                        printf("Numarul %d nu este prim.", p);
                    else
                        printf("Exponentul la care apare %d in descompunerea in factori primi a numarului %d este %d",
                               p, N,
                               exp);
                else
                    printf("Numarul %d nu apare in descompunerea in factori primi ai lui %d", p, N);
                printf("\n\n");
            }
        }
        else if(option == 2) break;
             else printf("Optiunea introdusa nu este valida.\n\n");

    }
}

int main()
{
    run();
    return 0;
}

//prob 1 lab 3
