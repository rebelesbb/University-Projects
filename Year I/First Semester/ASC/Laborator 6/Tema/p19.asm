bits 32 glogal 
global start 
extern exit, printf
import exit msvcrt.dll
import printf msvcrt.dll
segment data use32 class = data
;s db 'a','b','c','d','b','c','d'
s db 'b','c','d','c','d','b','c','d','r','b','c','d'
len_s equ $-s
d db 'b','c','d'
len_d equ $-d
aux dd 0

pozitii times len_s db 0  ;folosim precum un vector de aparitii
indici_pozitii times len_s db 0 
segment code use32 class = code
;19.Dandu-se doua siruri de octeti sa se calculeze toate pozitiile unde al doilea sir apare ca subsir in primul sir.
start:
    ;mov byte [pozitii], 73h
    ;mov byte [pozitii], 00h
    
    mov esi, s
    mov ecx, len_s
    mov ebx, 0    ;folosim ebx pe post de contor pentru sirul pozitii
    jecxz final
    
    parcurgere:
        mov [aux], ecx ; aux = len_s
        mov edx, esi ; edx = esi = initial, offset s, ulterior o pozitie din s
                     ; in felul asta pastram in edx pozitia din s de la care am inceput 
                     ; sa verificam daca d e subsir, pentru a reveni la ea cand terminam verificarea
                     ; si a trece la urmatoarea 
                     
        mov ecx, len_d ;ecx = len_d
        mov edi, d ; edi = offset d

        jecxz final
        
        verif_subsir:
        
            cmpsb           ; comparam cate un caracter din s cu cate unul din d 
            jne nu_e_subsir ; daca nu sunt egale inseamna ca nu e subsir, mergem mai departe
            
        loop verif_subsir
        
        mov byte [pozitii + ebx], 01h  ; daca ajungem aici inseamna ca d e subsir in s 
                                       ; punem 1 in pozitii la pozitia de inceput a lui d in s
        
        nu_e_subsir:
        
        inc ebx     
        
        mov esi, edx ; punem inapoi in esi offsetul lui s
        inc esi      ; incrementam pentru a verifica urmatoarele 3 elemente din s
        
        mov ecx, [aux] ; ecx = cat a mai ramas din len_s
    
    loop parcurgere    
    
    mov ecx, len_s
    jecxz final
    mov edi, indici_pozitii
    mov ebx, 0
    
    ;determinam pozitiile efective
    indici:
        mov al, 01h
        cmp al, [pozitii + ebx]
        
        jne sari
        
        mov al, bl
        
        stosb 
        
    sari:  
        inc ebx
        loop indici
            
    final:
            
         
push dword 0
call [exit]