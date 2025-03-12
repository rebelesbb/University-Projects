#include "MatriceIncidenta_MatriceAdiacenta.h"
#include <iostream>
#include <fstream>
using namespace std;

void matriceIncidenta_matriceAdiacenta()
{
    ifstream file(R"(C:\Users\Bogdan Rebeles\Desktop\Grafuri\Conversii\graf.txt)");
    int n, i, j, m = 0;
    file>>n;

    bool inc[n + 1][10000], a[n + 1][n + 1];

    for(i = 1; i <= n; i++)
        for(j = 1; j < 10000; j++)
            inc[i][j]  = false;

    for(i = 1; i <= n; i++)
        for(j = i; j <= n; j++)
            a[i][j] = a[j][i] = false;

    while(file >> i >> j)
    {
        m++;
        inc[i][m] = inc[j][m] = true;
    }

    file.close();

    int x, y;
    for(j = 1; j <= m; j++)
    {
        x = 1;
        while(!inc[x][j])
            x++;

        y = x + 1;
        while(!inc[y][j])
            y++;

        a[x][y] = a[y][x] = true;
    }

    for(i = 1; i <= n; i++, cout << '\n')
        for(j = 1; j <= n; j++)
            cout << a[i][j] << ' ';
    cout << '\n';

}