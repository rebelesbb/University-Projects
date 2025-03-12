#include <iostream>
#include <fstream>
#include <climits>
#include <queue>
#include <crtdbg.h>

bool residualPathExists(int n, int** residualGraph, int* parent) // folosim bfs (Edmonds-Karp)
{
	bool* visited = new bool[n];
	for (int i = 0; i < n; ++i)
		visited[i] = false;

	int source = 0, dest = n - 1;

	std::queue<int> q;
	q.push(source);
	visited[source] = true;
	parent[source] = -1;

	while (!q.empty())
	{
		int u = q.front();
		q.pop();

		for (int v = 0; v < n; ++v)
			if (!visited[v] && residualGraph[u][v])
			{
				if (v == dest)
				{
					// daca ajungem la nodul destinatie ne oprim 
					// deoarece inseamna ca avem o cale reziduala
					parent[v] = u;

					delete[] visited;

					return true;
				}

				// daca nu continuam normal bfs
				q.push(v);
				parent[v] = u;
				visited[v] = true;
			}
	}

	delete[] visited;

	// daca ajungem pana aici inseamna ca nu mai exista o cale reziduala de la nodul
	// sursa la nodul destinatie
	return false;
}

int fordFulkerson(int n, int** a)
{
	int u, v;
	int** residualGraph = new int*[n];
	for (int i = 0; i < n; ++i)
		residualGraph[i] = new int[n];

	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j)
			residualGraph[i][j] = a[i][j];

	int* parent = new int[n];

	int maxFlow = 0;

	int source = 0;
	int dest = n - 1;

	// cat timp exista o cale reziduala de la nodul sursa la nodul
	// destinatie
	while (residualPathExists(n,residualGraph,parent))
	{
		int pathFl = INT_MAX;
		for (v = dest; v != source; v = parent[v])
		{
			// parcurgem calea reziduala gasita pentru determinarea fluxului maxim
			u = parent[v];
			pathFl = std::min(pathFl, residualGraph[u][v]);
		}

		// modificam valorile din graful rezidual
		for (v = dest; v != source; v = parent[v])
		{
			u = parent[v];
			residualGraph[u][v] -= pathFl;
			residualGraph[v][u] += pathFl;
		}

		// actualizam valoarea fluxului maxim
		maxFlow += pathFl;

	}

	delete[] parent;
	for (int i = 0; i < n; ++i)
		delete[] residualGraph[i];
	delete[] residualGraph;

	return maxFlow;;
}

int main(int argc, char* argv[])
{
	
	if (argc != 3)
	{
		std::cout << "Numar insuficient de argumente\n";
		exit(EXIT_FAILURE);
	}
	
	std::ifstream fin;
	std::ofstream fout;

	//fin.open("input.txt");
	//fout.open("output.txt");

	fin.open(argv[1]);
	fout.open(argv[2]);

	if (!fin.is_open())
	{
		perror("ifstream::open()");
		exit(EXIT_FAILURE);
	}

	int n, m;

	fin >> n >> m;

	int** a = new int*[n];
	for (int i = 0; i < n; ++i)
	{
		a[i] = new int[n];
		for (int j = 0; j < n; ++j)
			a[i][j] = 0;
	}
	int u, v, c;
	for (int i = 0; i < m; ++i)
	{
		fin >> u >> v >> c;
		a[u][v] = c;
	}

	/*
	for (int i = 0; i < n; ++i, std::cout << '\n')
		for (int j = 0; j < n; ++j)
			std::cout << a[i][j] << ' ';
			*/
	int maxF = fordFulkerson(n, a);
	fout << maxF<< '\n';

	for (int i = 0; i < n; ++i)
		delete[] a[i];
	delete[] a;

	fin.close();
	fout.close();

	_CrtDumpMemoryLeaks();

	return 0;
}
