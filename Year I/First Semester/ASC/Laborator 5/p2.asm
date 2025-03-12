bits 32
global start
extern exit
import exit msvcrt.dll
segment data use32 class=data
s db 1,2,3,4,5,6 ; declaram sirul, fiecare litera are dimensiunea unui byte
l equ $-s ;cati bytes alocam in sirul s
d resb l
segment code use32 class=code
start:
;Se da un sir de numere
;Dublam numere pare, triplam impare
     mov ecx, l
     jecxz final
     mov esi, 0
     
     start_loop:
     
         mov al, [s+esi]
         cbw ;ax = elementul
         mov bl, 2
         idiv bl ; ah= [s+esi] % 2
         
         cmp ah, 0
         
         je dublare
         jne triplare
         
         dublare: 
             mov al, [s+esi]
             add al, [s+esi]
             jmp adaugare
             
         triplare:
             mov al, [s+esi]
             add al, [s+esi]
             add al, [s+esi]
             
         adaugare:
             mov [d+esi], al
             
         inc esi
             
     loop start_loop
         
           

final:

push dword 0
call [exit]