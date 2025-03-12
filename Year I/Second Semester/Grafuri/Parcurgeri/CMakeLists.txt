cmake_minimum_required(VERSION 3.27)
project(Parcurgeri)

set(CMAKE_CXX_STANDARD 23)

add_executable(Parcurgeri main.cpp
        BFS.cpp
        BFS.h
        DFS.cpp
        DFS.h
)
