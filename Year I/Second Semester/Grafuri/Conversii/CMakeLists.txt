cmake_minimum_required(VERSION 3.27)
project(Conversii)

set(CMAKE_CXX_STANDARD 23)

add_executable(Conversii main.cpp
        MatriceAdiacenta.cpp
        MatriceAdiacenta.h
        MatriceIncidenta.cpp
        MatriceIncidenta.h
        ListaAdiacenta.cpp
        ListaAdiacenta.h
        MatriceAdiacenta_MatriceIncidenta.cpp
        MatriceAdiacenta_MatriceIncidenta.h
        MatriceAdiacenta_ListaAdiacenta.cpp
        MatriceAdiacenta_ListaAdiacenta.h
        MatriceIncidenta_MatriceAdiacenta.cpp
        MatriceIncidenta_MatriceAdiacenta.h
        MatriceIncidenta_ListaAdiacenta.cpp
        MatriceIncidenta_ListaAdiacenta.h
        ListaAdiacenta_MatriceAdiacenta.cpp
        ListaAdiacenta_MatriceAdiacenta.h
        ListaAdiacenta_MatriceIncidenta.cpp
        ListaAdiacenta_MatriceIncidenta.h
        GOrientat_MatriceIncidenta.cpp
        GOrientat_MatriceIncidenta.h)
