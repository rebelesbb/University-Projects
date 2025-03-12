bits 32
global start
extern exit
import exit msvcrt.dll
segment code use32 class=code
start:
;256*1
mov ax, 256 ;ax=256
mov bx, 1   ;bx=1
mul bx      ;dx:ax=256*1
push dx
push ax
pop eax     ;eax=256
push dword 0
call [exit]