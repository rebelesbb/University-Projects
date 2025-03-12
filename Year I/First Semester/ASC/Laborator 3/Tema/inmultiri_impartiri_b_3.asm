bits 32  
global start
extern exit
import exit msvcrt.dll
segment data use32 class=data
; a,b,d-byte; c-doubleword; x-qword
a db 20 ;14h
b db -50 ; CEh    (256-50=206)
c dd 9992 ;00 00 27 08h
d db 100 ;64h
x dq 3A240C6B28FE71C4h
aux resd 1
rezultat resq 1
segment code use32 calss=code
start:
;(8-a*b*100+c)/d+x
;interpretare cu semn

;a*b*100
mov al, [a]
imul byte [b] ;ax=a*b= -1000 = FC 18h

mov bx, 100 
imul bx ;dx:ax=a*b*100 = -100000 = FF FE 79 60h

push dx
push ax 
pop ebx ;ebx = FF FE 79 60h

;8-a*b*100+c 
mov eax, 8
sub eax, ebx ; eax = 8-a*b*100 = 8+100000 = 100008 = 00 01 86 A8h
add eax, [c] ; eax = 8-a*b*100+c = 110000 = 00 01 AD B0h
cdq ; edx:eax = 8-a*b*100+c = 110000 = 00 00 00 00 00 01 AD B0h
mov ebx, eax
mov ecx, edx ;ecx:ebx = (8-a*b*100+c) 

;(8-a*b*100+c)/d 
mov al, [d]
cbw
cwde ;eax = d = 100 = 00 00 00 64h
mov [aux], eax
mov eax, ebx
mov edx, ecx ;edx:eax = (8-a*b*100+c) = 110000
idiv dword [aux] ; eax = (8-a*b*100+c)/d = 1100 = 00 00 04 4Ch 

;(8-a*b*100+c)/d+x
cdq ;edx:eax = 00 00 00 00 00 00 04 4Ch
clc 
add eax, [x]
adc edx, [x+4] ; edx:eax = (8-a*b*100+c)/d + x = 3A 24 0C 6B 28 FE 76 10h

mov [rezultat], eax
mov [rezultat+4], edx

push dword 0
call [exit] 