bits 32
global start
extern exit
import exit msvcrt.dll
segment data use32 class=data
a dq 1122334455667788h
b dq 49588723F1AABBCCh
rez resq 1
segment code use32 class=code
start:
;a+b
;edx:eax=a
mov eax, [a+0]
mov edx, [a+4]
;ecx:ebx=b
mov ebx, [b+0]
mov ecx, [b+4]
clc ; cf=0
add eax, ebx
adc edx, ecx 
mov [rez+0],eax 
mov [rez+4],edx
push dword 0
call [exit]