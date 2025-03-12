bits 32
global start
extern exit
import exit msvcrt.dll

segment data use32 class=data
a dw 1000
b dw 5000
c dw 740

segment code use32 class=code
;b-(b+c)+a

start:
mov ax, [b]
mov bx, [b]
add bx, [c] 
sub ax, bx
add ax, [a]

push dword 0
call [exit]