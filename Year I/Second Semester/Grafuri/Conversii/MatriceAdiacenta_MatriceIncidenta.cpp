#include "MatriceAdiacenta_MatriceIncidenta.h"
#include <iostream>
#include <fstream>
using namespace std;

void matriceAdiacenta_matriceIncidenta()
{
    ifstream file(R"(C:\Users\Bogdan Rebeles\Desktop\Grafuri\Conversii\graf.txt)");
    int n, i, j, m = 0, cnt=0;
    file>>n;

    bool a[n + 1][n + 1];

    for(i = 1; i <= n; i++)
        for(j = i; j <= n; j++)
            a[i][j] = a[j][i] = false;

    while(file >> i >> j) {
        m++;
        a[i][j] = a[j][i] = true; //neorientat, neponderat
    }

    file.close();

    bool inc[n + 1][m + 1];

    for(i = 1; i <= n; i++)
        for(j = 1; j <= m; j++)
            inc[i][j]  = false;

    for(i = 1; i <= n; i++)
        for(j = i + 1; j <=n; j++)
            if(a[i][j])
            {
                cnt++;
                inc[i][cnt] = inc [j][cnt] = true;
            }

    for(i = 1; i <= n; i++, cout << '\n')
        for(j = 1; j <= m; j++)
            cout << inc[i][j] << ' ';
    cout << '\n';

}
