#include <stdio.h>
int main() {
    int number , sum = 0, value;
    printf("%s", "Introduceti n:");
    scanf("%d", &number);
    ///printf("%d", number);
    printf("%s", "Introduceti valorile: \n");
    for(int i = 1; i <= number; i++) {
        scanf("%d", &value);
        sum += value;
    }
    printf("%s%d", "Suma valorilor introduse este: ", sum);
}
///problema 8