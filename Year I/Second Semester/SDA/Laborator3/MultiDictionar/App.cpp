#include <iostream>
#include <crtdbg.h>
#include "TestExtins.h"
#include "TestScurt.h"
using namespace std;

int main() {
	testAll();
	testAllExtins();
	//_CrtDumpMemoryLeaks();
	cout<<"End";

}
