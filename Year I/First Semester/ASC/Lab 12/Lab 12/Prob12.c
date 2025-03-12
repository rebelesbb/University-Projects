//Se dau doua siruri de caractere de lungimi egale. 
// Se cere sa se calculeze si sa se afiseze rezultatele intercalarii literelor, 
// pentru cele doua intercalari posibile (literele din primul sir pe pozitii pare, 
// respectiv literele din primul sir pe pozitii impare).

#include <stdio.h>
#include <string.h>
char sir_rezultat[200];

// functie pentru citire sir
void citire_sir(char sir[])
{
	printf("Introduceti sirul:");
	scanf_s("%s", sir, 100);
}

// functie pentru afisare sir
void afisare_sir(char sir[])
{
	printf("%s\n", sir);
}

//functia asm
char intercalare(lenght, sir1, sir2);



int main()
{
	char sir1[100], sir2[100];
		int lenght;
	citire_sir(sir1);   // citim sirurile si le afisam pentru a verifica ca  le-am citit corect
	afisare_sir(sir1);
	citire_sir(sir2);
	//afisare_sir(sir2);
	lenght = strlen(sir1);
	printf("%d", lenght);
	//sir_rezultat = intercalare(lenght, sir1, sir2);
	//printf("%s", sir_rezultat);
}