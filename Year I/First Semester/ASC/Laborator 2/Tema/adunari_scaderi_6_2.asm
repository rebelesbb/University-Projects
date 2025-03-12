bits 32
global start
extern exit
import exit msvcrt.dll
segment data use32 class=data
a dw 273
b dw 20
c dw 300
d dw 1000
segment code use32 class=code
start:
;c-(d+a)+(b+c)
mov ax, [c] ;ax=c=300
mov bx, [d] ;bx=d=1000
add bx, [a] ;bx=d+a=1273
sub ax, bx ;ax=c-(d+a)=-973
mov bx, [b] ;bx=b=20 
add bx, [c] ;bx=b+c=320
add ax, bx ;ax=c-(d+a)+(b+c)=-973+320=-653
push dword 0
call [exit]