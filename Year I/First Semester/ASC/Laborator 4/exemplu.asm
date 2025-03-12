bits 32 
global start
extern exit 
import exit msvcrt.dll
segment data use32 class = data
a dw 1100001110100110b
b dw 1111100000001011b
c resw 1
segment code use32 class = code
start:
mov ax,0

;izolam bitii 10-12 a lui b 

mov bx, [b]

;definim masca
and bx, 0001110000000000b ;bx=0001100000000000b=1800h(binar si hexa)

shr bx, 10
or ax, bx ;ax = 0000000000000110b = 0006h

or ax, 0000000001111000b ; ax = 0000000001111110b = 007Eh

;

mov bx, 0000000000011110b
mov dx, [a]
and dx, bx
shl dx, 6
or ax, dx ;ax=rezultat partial

;bitii 11-12 a lui C au valoarea 0

and ax, 1110011111111111b

;bitii 13-15 a lui C coincid cu inversul bitilor 9-11 a lui B

mov dx, [b]
not dx ;s-au inversat bitii lui b 
and dx, 0000111000000000b
shl dx, 4
or ax, dx

mov [c], ax

push dword 0
call [exit]


