bits 32 
global start
extern exit
import exit msvcrt.dll
segment data use32 class=data
s dd 12345678h, 1A2C3C4Dh, 98FCDD76h, 12783A2Bh

;s dd 142DA763h, 13392710h, 10AACC14h, 9A304015h
;s dd 22222222h, 22222222h, 22222222h, 22222222h, 44444444h
;s dd 17171717h, 19191919h, 202121AAh, 99999999h, 14141414h

len equ ($-s)/4 
d dd 0FFFFFFFFh

segment code use32 class=code
;Se da un sir de dublucuvinte. Sa se obtina, incepand cu partea inferioara a dublucuvantului, ;dublucuvantul format din octetii
;superiori pari ai cuvintelor inferioare din elementele sirului de dublucuvinte. Daca nu sunt ;indeajuns octeti
;se va completa cu octetul FFh.
;   EXEMPLU:
;   Se da sirul de dublucuvinte:
;   s DD 12345678h, 1A2C3C4Dh, 98FCDD76h, 12783A2Bh
;   Sa se obtina dublucuvant
;   d DD FF3A3C56h.
start:
    mov ecx, len
    
    mov esi, s 
    mov edi, d 
    mov edx, 0
    
    jecxz final
    
    parcurgere:
    
        
        lodsd ;ax = dword din s, inc esi+4
        mov bl, ah
        
        test bl, 01h
        
        jnz nu_se_adauga ; jnz = jne <=> zf = 0 adica bl & 01h != 0 deci nu e par
        
        ;tratam cazul in care octetul este par
        ;se adauga in d octetul
        
        mov al, bl 
        stosb      ;adaugam in d
        
        nu_se_adauga:
        
        inc edx
        cmp edx, 4
        je final
        
        
    loop parcurgere;
    
    final:

push dword 0
call [exit]