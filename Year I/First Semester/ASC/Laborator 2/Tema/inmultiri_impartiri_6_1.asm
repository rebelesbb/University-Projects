bits 32
global start
extern exit
import exit msvcrt.dll
segment data use32 class=data
a db 23
b db 10
c db 7
d dw 5

segment code use32 class=code
;[2*(a+b)-5*c]*(d-3)
start:
mov al, [a] ;al=a=23
add al, [b] ;al=a+b=33 
mov bl, 2 ;bl=2
mul bl ;ax=al*bl=2*(a+b)=66 
mov cx, ax ;cx=2*(a+b)=66
mov al, [c] ;al=c=7
mov bl, 5 ;bl=5
mul bl ;ax=al*bl=c*5=35
sub cx, ax ;cx=2*(a+b)-5*c=66-35=31
mov ax, [d] ;ax=5
sub ax, 3 ;ax=d-3=2
mul cx ;dx:ax=ax*cx=(d-3)*[2*(a+b)-5*c]=62
push dx
push ax
pop eax ;eax=dx:ax=[2*(a+b)-5*c]*(d-3)=62
push dword 0
call [exit]