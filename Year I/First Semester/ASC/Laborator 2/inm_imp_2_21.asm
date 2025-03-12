bits 32
global start
extern exit
import exit msvcrt.dll
segment data use32 class=data
a db 7
b db 14
c db 7
d db 8
e dw 5
f dw 1247
g dw 10
h dw 429
segment code use32 class=code
;(f*g-a*b*e)/(h+c*d)
;!!!
start:
mov al, [a]
mul byte [b]
mul word [e]
push dx
push ax
pop eax
mov ebx,eax
mov ax, f 
mul word [g]
push dx
push ax
pop eax
sub eax, ebx
mov ebx, eax
mov al, [c]
mul byte [d]
add ax, [h]
mov cx, ax
mov eax, ebx
div cx

push dword 0
call [exit]