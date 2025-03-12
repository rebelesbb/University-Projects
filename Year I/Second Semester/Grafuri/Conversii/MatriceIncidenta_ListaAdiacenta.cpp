#include "MatriceIncidenta_ListaAdiacenta.h"
#include <iostream>
#include <fstream>
#include <map>
#include <vector>
using namespace std;

void matriceIncidenta_listaAdiacenta()
{
    ifstream file(R"(C:\Users\Bogdan Rebeles\Desktop\Grafuri\Conversii\graf.txt)");
    int n, i, j, m = 0;
    file>>n;

    bool inc[n + 1][10000];
    map<int,vector<int>> lista;

    for(i = 1; i <= n; i++)
        for(j = 1; j < 10000; j++)
            inc[i][j]  = false;

    while(file >> i >> j)
    {
        m++;
        inc[i][m] = inc[j][m] = true;
    }

    file.close();

    int x,y;

    for(j = 1; j <= m; j++)
    {
        x = 1;
        while(!inc[x][j])
            x++;

        y = x + 1;
        while(!inc[y][j])
            y++;

        lista[x].push_back(y);
        lista[y].push_back(x);
    }

    for(i = 1; i <= n; i++, cout << '\n') {
        cout << i << ':';
        for (int vecin: lista[i])
            cout <<' '<< vecin;
    }

    cout << '\n';

}