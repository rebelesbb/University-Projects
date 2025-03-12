bits 32
global start
extern exit, printf, scanf
import exit msvcrt.dll
import printf msvcrt.dll
import scanf msvcrt.dll

segment data use32 class=data
format_scan db '%d', 0
format_print db "a = %d (baza 10), a = %x (baza 16)", 0
a dd 0

segment code use32 class=code

;Se da un numar natural negativ a (a: dword). Sa se afiseze valoarea lui in baza 10 si in baza 16, in urmatorul format: "a = <base_10> (baza 10), a = <base_16> (baza 16)"

start:
    ;mov eax, -7

    push dword a
    push format_scan
    call [scanf]
    add esp, 4 * 2
 
    push dword [a]
    push dword [a]
    push format_print
    call [printf]
    add esp, 4 * 3
    

push dword 0
call [exit]