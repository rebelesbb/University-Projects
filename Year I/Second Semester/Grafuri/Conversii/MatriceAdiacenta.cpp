#include "MatriceAdiacenta.h"
#include <fstream>
#include <iostream>
using namespace std;

void matriceAdicaenta()
{
    ifstream file(R"(C:\Users\Bogdan Rebeles\Desktop\Grafuri\Conversii\graf.txt)");
    int n, i, j;
    file>>n;

    bool a[n + 1][n + 1];

    for(i = 1; i <= n; i++)
        for(j = i; j <= n; j++)
            a[i][j] = a[j][i] = false;

    while(file >> i >> j)
        a[i][j] = a[j][i] = true; //neorientat, neponderat

    file.close();

    for(i = 1; i <= n; i++, cout << '\n')
        for(j = 1; j <= n; j++)
            cout << a[i][j] << ' ';
    cout << '\n';
}