bits 32
global start
extern exit
import exit msvcrt.dll
segment data use32 class=data
a db 100
b db 20
c db 120
d db 15
segment code use32 class=code
start:
;(a+b)-(a+d)+(c-a)
mov al, [a] ;al=a=100
add al, [b] ;al=a+b=120
mov bl, [a] ;bl=a=100
add bl, [d] ;bl=a+d=115
sub al, bl ; bl=(a+b)-(a+d)=5
mov bl, [c] ;bl=c=120
sub bl, [a] ;bl=c-a=20
add al, bl ;al=(a+b)-(a+d)+(c-a)=5+20=25

push dword 0
call [exit]