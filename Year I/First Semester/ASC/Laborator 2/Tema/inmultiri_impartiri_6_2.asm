bits 32
global start
extern exit
import exit msvcrt.dll
segment data use32 class=data
a db 19
b db 17
c db 9
segment code use32 class=code
start:
;(a*b)/c
mov al, [a] ;al=a=19
mul byte [b] ;ax=a*b=323 
div byte [c] ;al=(a*b)/c=35 ah=(a*b)%c=8
push dword 0
call [exit]