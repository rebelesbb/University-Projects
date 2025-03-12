;25.(a*a+b+x)/(b+b)+c*c; a-word; b-byte; c-doubleword; x-qword
bits 32 
global start
extern exit
import exit msvcrt.dll
segment data use32 class=data
a dw 400 ;
b db 120 ; 02h
c dd 7235756 ; 
x dq 0000000000011111h
rez resq 1
segment code use32 class=code
start:

;a*a+b+x
;a*a
mov ax, [a]
imul word [a] ;dx:ax = a*a = 160000
push dx
push ax 
pop eax ; eax = a*a

;a*a+b 
mov ebx, eax
mov al, [b]
cbw
cwde
add eax, ebx ; eax = a*a+b 
cdq ;edx:eax =a*a+b

;a*a+b+x
mov ebx, [x]
mov ecx, [x+4]
clc
add eax, ebx
adc edx, ecx ; edx:eax = a*a+b+x
mov ebx, eax
mov ecx, edx ; ecx:ebxx = a*a+b+x

;(a*a+b+x)/(b+b)
mov al, [b]
cbw ;ax=b 

mov dx, ax

mov al, [b]
cbw
add ax, dx

cwde ;eax = b+b 

push eax 

mov eax, ebx
mov edx, ecx

pop ebx

idiv ebx; eax = (a*a+b+x)/(b+b)
cdq

;(a*a+b+x)/(b+b)+c*c
mov ebx, eax
mov ecx, edx
mov eax, [c]
imul dword [c] ; edx:eax = c*c

clc
add eax, ebx
adc edx, ecx

mov [rez], eax
mov [rez+4], edx

push dword 0
call [exit]
