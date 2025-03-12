bits 32
global start
extern exit
import exit msvcrt.dll
segment data use32 class = data
a dw 1011010111101101b


segment code use32 class = code
;Se da cuvantul A. Sa se formeze doublewordul B in felul urmator:
;bitii 0-3 ai lui B sunt bitii 1-4 ai rezultatului A XOR 0Ah
;bitii 4-11 ai lui B sunt bitii 7-14 ai lui A
;bitii 12-19 ai lui B au valoarea 0
;bitii 20-25 ai lui B au valoarea 1
;bitii 26-31 ai lui C sunt bitii 3-8 ai lui A complementati
start:
;bitii 0-3 ai lui B sunt bitii 1-4 ai rezultatului A XOR 0Ah
    mov eax, 0 ;in eax il construim pe b
    
    mov ebx, 0
    mov bx, [a]
    xor bx, 0Ah ;a xor 0Ah
    
    and bx, 0000000000011110b ;izolam bitii 1-4 a lui a xor 0Ah
    shr bx, 1 ; mutam bitii 1-4 a lui a pe 0-3

    or eax, ebx ;  copiem bitii 1-4 a lui a xor 0Ah pe pozitiile  0-3 in b 
    ;b = 00 00 00 03h

;bitii 4-11 ai lui B sunt bitii 7-14 ai lui A
    mov ebx, 0
    mov bx, [a]
    
    and bx, 0111111110000000b
    shr bx, 3
    
    or eax, ebx
    ;b = 00 00 06 B3h
 
;bitii 12-19 ai lui B au valoarea 0
    ; nu e necesar sa facem vreo schimbare, au deja valoarea 0
  
;bitii 20-25 ai lui B au valoarea 1
    or eax, 03F00000h ; punem 1 pe pozitiile 20-25 in b 
    ;b = 03 F0 06 B3h
    
;bitii 26-31 ai lui C sunt bitii 3-8 ai lui A complementati
    mov ebx, 0
    mov bx, [a]
    not bx ; complementam bitii lui a 
    
    and bx, 0000000111111000b
    shl ebx, 23 ; mutam bitii complementati 3-8 ai lui a pe 26-31
    
    or eax, ebx ; mutam bitii 3-8 complementati ai lui a pe pozitiile 26-31 in b
    ;b = 0B F0 06 B3h

push dword 0
call [exit]