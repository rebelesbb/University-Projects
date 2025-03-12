bits 32
global start
extern exit
import exit msvcrt.dll
segment data use32 class=data
; a,b,d-byte; c-doubleword; x-qword
a db 48h
b db 02h
c dd 426Bh 
d db 07h
x dq 3A240C6B28FE71C4h
aux resd 1
rezultat resq 1
segment code use32 calss=code
start:
;(8-a*b*100+c)/d+x
;interpretare fara semn

;a*b*100
mov al, [a]
mul byte [b] ;ax=a*b= 90

mov bx, 100 
mul bx ;dx:ax=a*b*100 = 00 00 38 40 

push dx
push ax 
pop ebx ;ebx = 00 00 38 40

;8-a*b*100+c 
mov eax, [c]
sub eax, ebx ;eax = -a*b*100+c = 00 00 0A 2B

mov ecx, 8
add eax, ecx 
mov edx, 0 ;edx:eax = 8-a*b*100+c = 00 00 00 00 00 00 0A 33
mov ebx, eax
mov ecx, edx ;ecx:ebx = (8-a*b*100+c) = 00 00 00 00 00 00 0A 33

;(8-a*b*100+c)/d 
mov eax, 0
mov al, [d] ; eax = d
mov [aux], eax
mov eax, ebx
mov edx, ecx ;edx:eax = (8-a*b*100+c)
div dword [aux] ; eax = (8-a*b*100+c)/d = 00 00 01 75h

;(8-a*b*100+c)/d+x
mov edx, 0 ; edx:eax = (8-a*b*100+c)/d = 00 00 00 00 00 00 01 75h
clc
add eax, [x]
adc edx, [x+4] ; edx:eax = (8-a*b*100+c)/d + x = 3A 24 0C 6B 28 FE 73 39h

mov [rezultat], eax
mov [rezultat+4], edx

push dword 0
call [exit] 