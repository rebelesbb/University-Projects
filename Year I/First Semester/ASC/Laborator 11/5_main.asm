bits 32
global start
extern exit, scanf, printf
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll

extern calcul

segment data use32 class=data
mesaj_citire_a db "a=", 0
mesaj_citire_b db "b=", 0
mesaj_citire_c db "c=", 0
format_citire_numar db "%d", 0
format_afisare_numere db "%d   %d   %d",0
format_afisare_calcul db 10, "a + b - c = %d", 0


a dd 0
b dd 0
c dd 0

segment code use32 class=code


start:
    
    push mesaj_citire_a
    call [printf]
    add esp, 4
    
    push a
    push format_citire_numar
    call [scanf]
    add esp, 4 * 2
    
    push mesaj_citire_b
    call [printf]
    add esp, 4
    
    push b
    push format_citire_numar
    call [scanf]
    add esp, 4 * 2
    
    push mesaj_citire_c
    call [printf]
    add esp, 4
    
    push c
    push format_citire_numar
    call [scanf]
    add esp, 4 * 2
    
    push dword [c]
    push dword [b]
    push dword [a]
    push dword format_afisare_numere
    call [printf]
    add esp, 4 * 4

    push dword [c]
    push dword [b]
    push dword [a]
    call calcul
    
    push eax
    push format_afisare_calcul
    call [printf]
    add esp, 4 * 2
     
    
push dword 0
call [exit]
    