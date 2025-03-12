#include "ListaAdiacenta.h"
#include <iostream>
#include <fstream>
#include <map>
#include <vector>
using namespace std;

void listaAdiacenta()
{
    ifstream file(R"(C:\Users\Bogdan Rebeles\Desktop\Grafuri\Conversii\graf.txt)");
    int n, i, j;
    file>>n;

    map<int, vector<int>> lista;

    while(file >> i >> j) {
        lista[i].push_back(j);
        lista[j].push_back(i);
    }

    file.close();

    for(i = 1; i <= n; i++, cout << '\n') {
        cout << i << ':';
        for (int vecin: lista[i])
            cout <<' '<< vecin;
    }

    cout << '\n';

}