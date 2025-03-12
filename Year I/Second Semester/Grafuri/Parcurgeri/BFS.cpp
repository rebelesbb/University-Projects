#include "BFS.h"
#include <queue>
#include <iostream>
using namespace std;


void bfs(int n, bool** adj, int start)
{
    queue<int> Q;
    bool visited[n + 1];
    int i, result[n + 1], cnt = 0;

    for(i = 1; i <= n; i++)
        visited[i] = false;

    Q.push(start);

    while (!Q.empty())
    {
        int current = Q.front();
        Q.pop();
        visited[current] = true;
        result[++cnt] = current;

        for(i = 1; i <= n; i++)
            if(adj[current][i] && !visited[i])
            {
                visited[i] = true;
                Q.push(i);
            }
    }

    cout << "BFS:\n";
    for(i = 1; i <= cnt; i++)
        cout << result[i] << ' ';
    cout << '\n';

}
