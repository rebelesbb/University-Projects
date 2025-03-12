#include <iostream>
#include "all_tests.h"
#include "ui.h"
#include "repo_lab.h"
#include <crtdbg.h>
using std::unique_ptr;

int main()
{
	const Tests testApp{};
	_CrtDumpMemoryLeaks();

	try {
		//MovieRepoFromFile repo{ "data.txt" };
		//MovieRepository repo{};
		RepoLab repo{ 0 };
		Validator val{};
		Cart cart{};
		MovieService srv{ repo, val };
		Console console{ srv };
		console.run();
	}
	catch (Exception& err)
	{
		std::cout << err.Message;
		exit(1);
	}

	_CrtDumpMemoryLeaks();
	
	return 0;
}