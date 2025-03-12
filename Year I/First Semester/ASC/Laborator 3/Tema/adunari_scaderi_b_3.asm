bits 32 
global start
extern exit
import exit msvcrt.dll
segment data use32 class=data
;a - byte, b - word, c - double word, d - qword 
;Interpretare cu semn
a db 7Dh
b dw 392Ch
c dd 21E01A4Bh
d dq 10AA137F9F406A91h
rezultat resq 1
segment code use32 class=code
;(b+b+d)-(c+a)
start:

;b+b+d 
mov ax, [b] 
add ax, [b] ;ax = b+b = 72 58h
cwde
cdq ;edx:eax= b+b = 00 00 00 00 00 00 72 58h 

mov ebx, [d]
mov ecx, [d+4] ;ecx:ebx = d  

clc
add eax, ebx
adc edx, ecx ;edx:eax = b+b+d = 10 AA 13 7F 9F 40 DC E9h

mov [rezultat], eax
mov [rezultat+4], edx

;a+c

mov al, [a]
cbw
cwde ;eax = a 

add eax, [c] ;eax = a+c
cdq ;edx:eax = a+c =00 00 00 00 21 E0 1A C8h

mov ebx, eax
mov ecx, edx 

;(b+b+d)-(c+a)
mov eax, [rezultat]
mov edx, [rezultat+4]

clc
sub eax, ebx
sbb edx, ecx ;edx:eax = (b+b+d)-(c+a)

mov [rezultat], eax
mov [rezultat+4], edx

;rezultat = (b+b+d)-(c+a) = 10 AA 13 7F 7D 60 C2 21h

push dword 0
call [exit]