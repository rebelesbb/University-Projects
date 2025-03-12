#include "MatriceIncidenta.h"
#include <fstream>
#include <iostream>
using namespace std;

void matriceIncidenta()
{
    ifstream file(R"(C:\Users\Bogdan Rebeles\Desktop\Grafuri\Conversii\graf.txt)");
    int n, i, j, m = 0;
    file>>n;

    bool inc[n + 1][10000];

    for(i = 1; i <= n; i++)
        for(j = 1; j < 10000; j++)
            inc[i][j]  = false;

    while(file >> i >> j)
    {
        m++;
        inc[i][m] = inc[j][m] = true;
    }

    file.close();

    for(i = 1; i <= n; i++, cout << '\n')
        for(j = 1; j <=m; j++)
            cout << inc[i][j] << ' ';
    cout << '\n';
}