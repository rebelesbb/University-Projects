bits 32 glogal 
start extern 
exit 
import exit msvcrt.dll

segment data use32 class = data
s dd 127F5678h, 0ABCDABCDh  ;78 56 7F 12
                        ;poz  0  1  2  3
s_par dw 0              ;poz  4  3  2  1
s_impar dw 0
l equ ($-s)/4 ;pt ca e sir de dword
b resd l 
aux dd 0

segment code use32 class = code
start:
    
    mov ecx, l
    
    mov esi, s ;ca sa putem folosi operatiile pe siruri
    mov edi, b
    
    parcurgere:
    
    mov [aux], ecx
    
    mov ecx, 4
    mov [s_par], ax
    mov [s_impar], ax
    
    formare:
        mov al, cl 
        cbw ;ax = cl
        mov bl, 2
        idiv bl ; al = cl/2 , ah = cl%2
        
        cmp ah, 0
        je aduna_par
        jne aduna_impar
        
        aduna_par:
            lodsb ;al = byte din esi
            cbw 
            add [s_par], ax
            jmp gata
        
        aduna_impar:
            lodsb ;al = byte din esi
            cbw
            add [s_impar], ax
        
        gata:
        
    loop formare  ;ecx = ecx - 1 , pana cand ecx = 0
    
    mov edi, b 
    mov ax, [s_par]
    stosw 
    
    mov ax, [s_impar]
    stosw
    
    mov ecx, [aux]
    
    
push dword 0
call [exit]
         