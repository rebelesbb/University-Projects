bits 32
global start
extern exit
import exit msvcrt.dll
segment data use32 class=data
;a - byte, b - word, c - double word, d - qword
;Interpretare fara semn
a db 21h
b dw 75D3h
c dd 9034FD9Ch
d dq 439AF301F6B3919Eh 
rezultat resq 1
segment code use32 class=code
;(c+d)-(a+d)+b
start:

mov eax, [c]
mov edx, 0
;edx:eax=c
mov ebx, [d+0]
mov ecx, [d+4] 
;ecx:ebx=d
clc
add eax, ebx
adc edx, ecx
;edx:eax=c+d
mov [rezultat+0], eax
mov [rezultat+4], edx
;rezultat=edx:eax=c+d=43 9A F3 02 86 E8 8F 3A


mov eax, 0
mov al, [a]
;eax=a
mov edx, 0
;edx:eax=a
add eax, ebx
adc edx, ecx
;edx:eax=a+d=43 9A F3 01 F6 B3 91 BF



mov ebx, [rezultat+0]
mov ecx, [rezultat+4]
;ecx:ebx=c+d
clc
sub ebx, eax
sbb ecx, edx
;ecx:ebx=(c+d)-(a+d)=00 00 00 00 90 34 FD 7B
mov [rezultat+0], ebx
mov [rezultat+4], ecx
;rezultat=edx:eax=(c+d)-(a+d)=00 00 00 00 90 34 FD 7B


mov ecx, 0
mov ebx, 0
mov bx, [b]
;ecx:ebx=b
mov eax, [rezultat+0]
mov edx, [rezultat+4]
;edx:eax=(c+d)-(a+d)


clc
add eax, ebx
adc edx, ecx
;edx:eax=(c+d)-(a+d)+b = 00 00 00 00 90 35 73 4E


mov [rezultat+0], eax
mov [rezultat+4], edx
;rezultat=(c+d)-(a+d)+b=00 00 00 00 90 35 73 4E
push dword 0
call [exit]