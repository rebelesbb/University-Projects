cmake_minimum_required(VERSION 3.27)
project(untitled C)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra")

add_executable(untitled main.c
        List.c
        List.h
        Testing.c
        Testing.h
        Medicament.c
        Medicament.h
        Console.c
        Console.h
        Undo.c
        Undo.h
)
