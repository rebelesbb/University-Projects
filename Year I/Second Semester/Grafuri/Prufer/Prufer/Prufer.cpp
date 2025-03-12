#include <iostream>
#include <fstream>
#include <vector>
using std::cout;
using std::vector;
using std::pair;

int minLeaf(int n, vector<int>& T)
{
	int i = -1, j = -1;
	for (i = 0; i < n; ++i)
	{
		if(T.at(i) != -1)
		{
			for (j = 0; j < n; ++j)
				if (i == T.at(j))
					break;         // daca i apare in vectorul de parinti inseamna ca nu e frunza
		}
		if (j == n)  // daca e frunza si am adaugat sau nu in K
			return i;
	}
	return 0;
}

const pair<int, vector<int>> prufer(int n, vector<int>& T)
{
	vector<int> K;
	int count = n, prfN = 0;
	while (count >= 2) // cat timp avem cel putin doua varfuri
	{
		int v = minLeaf(n, T); // extragem frunza minima
		K.push_back(T.at(v)); // punem in K predecesorul lui v (parintele)
		T.at(v) = -1; // adica am introdus frunza i in K <=> T = T - {v}
		count--;
		prfN++;
	}
	pair<int, vector<int>> res = { prfN, K };
	return res;
}

int main(int argc, char* argv[])
{
	std::ifstream fin;
	std::ofstream fout;

	//fin.open("input.txt");
	//fout.open("output.txt");
	
	fin.open(argv[1]);
	fout.open(argv[2]);

	int n;

	fin >> n;

	vector<int> T;
	int cnt = 0, p;

	while (fin >> p)
		T.push_back(p);

	//cout << n << '\n';

	/*
	for (int i = 0; i < n; ++i)
		cout << T.at(i) << ' ';
	cout << "\n\n";
	*/

	fin.close();

	auto res = prufer(n, T);

	fout << res.first << '\n';

	for (const auto& elem : res.second)
		fout << elem << ' ';
	fout << '\n';

	fout.close();

	return 0;
}