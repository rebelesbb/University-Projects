bits 32 
global start
extern exit
import exit msvcrt.dll
segment data use32 class=data
a dw 1101001011001110b ;
b dw 0100011011110101b ;
c resd 1 
segment code use32 class=code
;Se dau cuvintele A si B. Sa se obtina dublucuvantul C:
;bitii 0-2 ai lui C coincid cu bitii 12-14 ai lui A
;bitii 3-8 ai lui C coincid cu bitii 0-5 ai lui B
;bitii 9-15 ai lui C coincid cu bitii 3-9 ai lui A
;bitii 16-31 ai lui C coincid cu bitii lui A

start:
;bitii 0-2 ai lui C coincid cu bitii 12-14 ai lui A
     mov eax, 0 ;aici il construim pe c 
     
     mov ebx, 0 
     mov bx, [a] 
     
     and bx, 0111000000000000b ;izolam bitii 12-14 ai lui a, cu masca
     rol bx, 4 ; rotim spre stanga cu 4 pozitii bitii lui a 
     
     or eax, ebx ; copiem bitii 12-14 ai lui a in c
     ;c = 00 00 00 05h
    
;bitii 3-8 ai lui C coincid cu bitii 0-5 ai lui B
     mov ebx, 0
     mov bx, [b]
     
     and bx, 0000000000111111b ;izolam bitii 0-5 ai lui b
     shl bx, 3 ; mutam spre stanga cu 3 pozitii bitii lui b 
     
     or eax, ebx; copiem bitii 0-5 ai lui b in c 
     ;c=00 00 01 ADh

;bitii 9-15 ai lui C coincid cu bitii 3-9 ai lui A
     mov ebx, 0
     mov bx, [a]
     
     and bx, 0000001111111000b
     shl bx, 6
     
     or eax, ebx
     ;c = 00 00 B3 ADh
     
;bitii 16-31 ai lui C coincid cu bitii lui A
     mov ebx, 0
     mov bx, [a]
     shl ebx, 16 ;mutam bitii lui pe pozitiile 16-31 in ebx
     
     or eax, ebx
     ;c = D2 CE B3 ADh

push dword 0
call [exit]