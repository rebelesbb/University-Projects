bits 32
global start
extern exit
import exit msvcrt.dll
segment data use32 class=data
a db 27 
b db 13
c db 13
d dw 3000
 
segment code use32 class=code
;[(10+d)-(a*a-2*b)]/c
;a=27,b=13,c=9,d=3000
start:
mov al, 2
mul byte [b]
mov bx, ax
mov al, [a]
mul byte [a]
sub ax, bx
mov bx, ax
mov ax, 10
;add ax, [d] sau
add word [d], 10
mov ax, [d]
sub ax, bx
div byte [c]

push dword 0
call [exit]