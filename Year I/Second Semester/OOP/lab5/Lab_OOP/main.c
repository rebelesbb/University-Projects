#include <stdio.h>
#include "Testing.h"
#include "Console.h"
#define _CRTDBG_MAP_ALLOC
#include <stdlib.h>
#include <crtdbg.h>

int main() {
    test_all();
    _CrtDumpMemoryLeaks();

    run();

    return 0;
}
