#include <iostream>
#include <fstream>
#include <vector>
using std::cout;
using std::vector;
using std::pair;

int minNat(int n, vector<int>K)
{
	int i = 0;
	while(true)
	{
		auto it = std::find(K.begin(), K.end(), i);
		if (it == K.end())
			return i;
		i++;
	}
}

const pair<int, vector<int>> pruferDecode(int n, vector<int> K)
{
	vector<int> T;
	int count = 1;

	for (int i = 0; i < n + 2; ++i)
		T.push_back(-1);		// initializam T cu -1 (astfel la final ramane -1 doar la indexul radacinii)

	for (int i = 0; i < n; i++)
	{
		int x = K.front();
		int y = minNat(n, K);
		K.erase(K.begin());
		K.push_back(y);
		T.at(y) = x;
		count++;
	}

	pair<int, vector<int>> res = { count, T };
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

	int n, elem;
	vector<int> K;

	fin >> n;

	while (fin >> elem)
		K.push_back(elem);

	/*
	cout << n << '\n';
	for (int i = 0; i < n; ++i)
		cout << K.at(i) << ' ';

	cout << "\n\n";
	*/
	

	fin.close();

	auto res = pruferDecode(n, K);

	fout << res.first << '\n';

	for(int i = 0; i < res.first; ++i)
		fout << res.second.at(i) << ' ';

	fout.close();

	return 0;

}