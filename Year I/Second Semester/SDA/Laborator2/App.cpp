#include <iostream>
#include "TestScurt.h"
#include "TestExtins.h"
//#include <cstdlib>
#include <crtdbg.h>

int main(){
    //int* x = new int;
    testAll();
    testAllExtins();
    _CrtDumpMemoryLeaks();
    std::cout<<"Finished LP Tests!"<<std::endl;
}
