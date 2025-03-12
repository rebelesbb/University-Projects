cmake_minimum_required(VERSION 3.27)
project(lab2_4 C)

set(CMAKE_C_STANDARD 23)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra")

add_executable(lab2_4 main.c
        participants_functions.c
        participants_functions.h
        participants_tests.c
        participants_tests.h
        sort_function.c
        sort_function.h
        participant.c
        participant.h
        list.c
        list.h)
