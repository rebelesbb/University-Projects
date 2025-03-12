#include "ListaAdiacenta_MatriceIncidenta.h"
#include <iostream>
#include <fstream>
#include <map>
#include <vector>
using namespace std;

void listaAdiacenta_matriceIncidenta()
{
    ifstream file(R"(C:\Users\Bogdan Rebeles\Desktop\Grafuri\Conversii\graf.txt)");
    int n, i, j, m = 0, cnt = 0;
    file>>n;

    map<int, vector<int>> lista;

    while(file >> i >> j) {
        m++;
        lista[i].push_back(j);
        lista[j].push_back(i);
    }

    file.close();

    bool inc[n + 1][m + 1];

    for(i = 1; i <= n; i++)
        for(j = 1; j <= m; j++)
            inc[i][j]  = false;

    for(i = 1; i <= n; i++)
        for(int vecin: lista[i])
            if(vecin > i)
            {
                cnt++;
                inc[i][cnt] = inc[vecin][cnt] = true;
            }

    for(i = 1; i <= n; i++, cout << '\n')
        for(j = 1; j <=m; j++)
            cout << inc[i][j] << ' ';
    cout << '\n';
}