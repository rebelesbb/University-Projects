#include<bits/stdc++.h>
using namespace std;
char ar[1001][1001];
char br[1001][1001];
bool vis[1001][1001];
int n , m;
pair<int, int> start, end;
/*
bool isValid(int n, int m, char a[][1002], int x , int y) {

    if(x < 0 || y < 0 || x > n || y > m) return false;
    if (a[x][y] == '1' || visited[x][y]) return false;

    return true;
}

bool BFSOnGrid(int n, int m, char a[][1002]) {
    int x, y;
    queue<pair<int, int>> Q;

    Q.push(start);
    visited[start.first][start.second] = true;

    while (!Q.empty()) {
        x = Q.front().first;
        y = Q.front().second;
        Q.pop();

        if (a[x][y] == 'F') {
            while (true) {
                path.push_back(p[x][y]);

                if (path.back() == 'L') y++;
                if (path.back() == 'R') y--;
                if (path.back() == 'U') x++;
                if (path.back() == 'D') x--;

                if (x == start.first && y == start.second)
                    break;
                return true;
            }
        }
        //left
        if (isValid(n, m, a, x, y - 1))
            p[x][y - 1] = 'L', Q.push(std::pair(x, y - 1)), visited[x][y - 1] = true;

        //right
        if (isValid(n, m, a, x, y + 1))
            p[x][y + 1] = 'R', Q.push(std::pair(x, y + 1)), visited[x][y + 1] = true;

        //up
        if (isValid(n, m, a, x - 1, y))
            p[x - 1][y] = 'U', Q.push(std::pair(x - 1, y)), visited[x - 1][y] = true;

        //down
        if (isValid(n, m, a, x + 1, y))
            p[x + 1][y] = 'D', Q.push(std::pair(x + 1, y)), visited[x + 1][y] = true;

    }

    return false;

}



void getStart(int n, int m, char a[][1002])
{
    for(int i = 0; i < n; i++)
        for( int j = 0; j < m; j++)
            if(a[i][j] == 'S') {
                start.first = i, start.second = j;
                break;
            }
}

void get_labyrinth(int &n, int &m, char a[][1002])
{
    char str[1000];

    int index, i, j;

    f.getline(str, 1000);
    //g << str << '\n';
    m = strlen(str);
    n = 0;
    strcpy_s(a[n], str);
    n++;
    while(f.getline(str, 1000))
    {
        strcpy_s(a[n], str);
        n++;
    }

    for(i = 0; i < n; i++, g << endl)
        for(j = 0; j < m; j++)
            g << a[i][j];

}

int run()
{
    char a[1002][1002];
    int m = 0, n = 0;


    get_labyrinth(n,m,a);
    getStart(n, m, a);
    cout << start.first << ' ' << start.second;

    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
            visited[i][j] = false;

    if(BFSOnGrid(n,m,a)){
        cout<<"YES"<<endl<<path.size()<<endl;
        while(!path.empty()) cout<<path.back() , path.pop_back();
    }
    else{
        cout<<"NO";
    }
    f.close();
    g.close();
	return 0;
}*/

bool inside(int row, int col, int N, int M) {
    return (0 <= row && row < N && 0 <= col && col < M);
}

void labyrinth(vector<vector<char>> graph, int st_x, int st_y, int end_x, int end_y) {
    int rows = (int)graph.size();
    int cols = (int)graph[0].size();
    int current_x, current_y;

    vector<vector<int>> dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    vector<vector<pair<int, int>>> paths(rows, vector<pair<int, int>>(cols));
    graph[st_x][st_y] = '-';

   queue<pair<int, int>> queue;
    queue.push(pair{st_x, st_y});


    while (!queue.empty()) {
        auto [currRow, currCol] = queue.front();
        queue.pop();

        for (vector<int> &dir: dirs) {
            int nextRow = currRow + dir[0];
            int nextCol = currCol + dir[1];

            if (inside(nextRow, nextCol, rows, cols)
                && (graph[nextRow][nextCol] == '0' || graph[nextRow][nextCol] == 'F')) {
                paths[nextRow][nextCol] = pair(currRow, currCol);
                graph[nextRow][nextCol] = '-';

                if (nextRow == end_x && nextCol == end_y) {
                    break;
                }

                queue.push(pair(nextRow, nextCol));
            }
        }
    }

    current_x = end_x, current_y = end_y;

    while (current_x != st_x && current_y != st_y) {
        graph[current_x][current_y] = 'X';
        current_x = paths[current_x][current_y].first;
        current_y = paths[current_x][current_y].second;
    }

    graph[st_x][st_y] = 'X';

    if(rows && cols){
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                cout << graph[row][col];
            }

            cout << '\n';
        }
    }
    else cout << "Nu exista solutie\n";
}

void run() {
    ifstream file;
    file.open(R"(C:\Users\Bogdan Rebeles\Desktop\Grafuri\Labirint\labirint_1.txt)");
    
    if (file.is_open()) {
        string line;
        vector<vector<char>> graph;
        
        int startX, startY;
        
        int endX, endY;
        
        while(getline(file, line)) {
            if (line.back() == '\n') {
                line.pop_back();
            }

            vector<char> currentLayer(line.size());

            for(int index = 0; index < line.size(); index++) {
                if (line[index] == 'S') {
                    startX = (int)graph.size();
                    startY = index;
                    currentLayer[index] = 'S';
                } else if (line[index] == 'F') {
                    endX = (int)graph.size();
                    endY = index;
                    currentLayer[index] = 'F';
                } else if (line[index] == ' ') {
                    currentLayer[index] = '0';
                } else if (line[index] == '1') {
                    currentLayer[index] = '-';
                }
            }

            graph.push_back(currentLayer);
        }

        labyrinth(graph, startX, startY, endX, endY);
        file.close();
    } else {
        cout << "Unable to open file...\n";
        return ;
    }
}

