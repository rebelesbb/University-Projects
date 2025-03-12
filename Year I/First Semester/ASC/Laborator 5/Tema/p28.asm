bits 32
global start
extern exit
import exit msvcrt.dll
segment data use32 class = data
s1 db '+', '4', '2', 'a', '8', '4', 'X', '5'
l1 equ $-s1
s2 db 'a', '4', '5'
l2 equ $-s2
lungime equ $-s1 ;=l1+l2 ,deoarece s2 e pus in continuarea lui s1
d resb lungime
segment code use32 class = code
;Se dau doua siruri de caractere S1 si S2. Sa se construiasca sirul D prin concatenarea elementelor 
;de pe pozitiile multiplu de 3 din sirul S1 cu elementele sirului S2 in ordine inversa.
;Exemplu:
;S1: '+', '4', '2', 'a', '8', '4', 'X', '5'
;S2: 'a', '4', '5'
;D: '+', 'a', 'X', '5', '4', 'a'
start:
    ;punem elementele de pe pozitie multiplu de 3 din s1 in d 
        
        ;am calculat cate elemente sunt pe pozitie multiplu de 3
        mov eax, l1
        mov edx, 0
        mov ebx, 3 
        div ebx 
        
        cmp edx, 0
        je continua
        add eax, 1 
        
        continua:
        
        ;adaugarea elementelor in d
        mov ecx, eax ;ecx = contor = cate elemente sunt pe pozitii multiplu de 3
        
        jecxz final ;daca s2 e gol nu se intra in loop
        
        mov esi, 0 ;index pentru s1
        mov edx, 0 ; index penru d 
        
        adaugare_s1:
            mov al, [s1+3*esi]
            mov [d+edx], al
            inc edx
            inc esi
            
        loop adaugare_s1
    
    ;punem in d elementele din s2 in ordine inversa
        
        mov ecx, l2
        
        jecxz final ;daca s2 e gol nu se intra in loop
        
        mov esi, l2 ;indexul pentru s2
        dec esi ; esi ia valori de la l2-1 la 0
        
        ;nu modificam indexul pentru d, adica edx, 
        ;pentru ca elementele sa fie puse in continuare
        
        adaugare_s2:
            mov al, [s2+esi]
            mov [d+edx], al
            inc edx
            dec esi
        
        loop adaugare_s2

final:

push dword 0
call [exit]