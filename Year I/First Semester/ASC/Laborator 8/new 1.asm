bits 32
global start
extern exit, fopen, scanf, fprintf, printf
import exit msvcrt.dll
import fopen msvcrt.dll
import scanf msvcrt.dll
import fprintf msvcrt.dll
import printf msvcrt.dll

segment data use32 class=data
nume_fisier db 0
numar dd 0
format_citire_fisier db "%s", 0
format_citire_numar db "%d", 0
format_afisare db "%s", 0
format_scriere_numar db "%d", 0
mod_acces db "w", 0
mesaj1 db "Introduceti numele fisierului: ", 0
mesaj2 db "Introduceti numarul: ", 0

segment code use32 class=code
start:

        push dword mesaj2
        push dword format_afisare
        call [printf]
        add esp, 2*4
        
        push dword numar
        push dword format_citire_numar
        call [scanf]
        add esp, 2*4
        
    push dword 0
    call [exit]