;x-(a*a+b)/(a+c/a); a,c-byte; b-doubleword; x-qword
bits 32 
global start
extern exit 
import exit msvcrt.dll
segment data use32 class=data
a db 17 ;11h
c db 36 ;24h
b dd 109223 ;00 01 AA A7h
x dq 19B6322D9FF3C802h
rez resq 1
segment code use32 class=code
start:
;a*a+b

mov al, [a]
imul byte [a] ;ax=a*a
cwde ;eax = a*a
add eax, [b] ; eax = a*a+b = 289 + 109223 = 109512
mov ebx, eax ; ebx = a*a+b

;a+c/a
mov al, [c]
cbw ; ax = c
idiv byte [a] ;al= ax/c = a/c,   ah = ax%c = a%c 
add al, [a] ; al=a+a/c
cbw ;ax=a+a/c
mov cx, ax

;(a*a+b)/(a+c/a)
mov eax, ebx
push eax
pop ax
pop dx
idiv cx ; ax = (a*a+b)/(a+c/a) = 5763 = 16 83h

;x+(a*a+b)/(a+c/a)
cwde
cdq ; edx:eax = (a*a+b)/(a+c/a)
mov ebx, [x]
mov ecx, [x+4]
clc
add eax, ebx
adc edx, ecx

mov [rez], eax
mov [rez+4], edx
;x+(a*a+b)/(a+c/a) = 19 B6 32 2D 9F F3 DE 85h

push dword 0
call [exit]