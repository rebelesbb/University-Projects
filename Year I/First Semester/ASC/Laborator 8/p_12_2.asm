bits 32
global start
extern exit, fopen, scanf, fprintf, printf, fclose
import exit msvcrt.dll
import fopen msvcrt.dll
import scanf msvcrt.dll
import fprintf msvcrt.dll
import printf msvcrt.dll
import fclose msvcrt.dll

segment data use32 class=data
descriptor_fisier db 0
nume_fisier_debug db "text.txt", 0
numar dd 0
format_citire_numar db "%d", 0
format_afisare db "%s", 0
format_scriere_numar db "%d ", 0
mod_acces db "w", 0
mesaj2 db "Introduceti numarul: ", 0

segment code use32 class=code
;Se da un nume de fisier (definit in segmentul de date). Sa se creeze un fisier cu numele dat, apoi sa se citeasca de la tastatura numere si sa se scrie valorile citite in fisier pana cand se citeste de la tastatura valoarea 0.

start:
    ;citire nume fisier
    ;push dword mesaj1
    ;push dword format_afisare
    ;call [printf]
    ;add esp, 2*4
    
    ;push dword nume_fisier
    ;push dword format_citire_fisier
    ;call [scanf]
    ;add esp, 2*4
    
    ;creare fisier
    push dword mod_acces
    push dword nume_fisier_debug
    call [fopen]
    add esp, 2*4
    
    cmp eax, 0
    je final
    
    mov [descriptor_fisier], eax
    
    ;adaugare  numere in fisier
    
    adaugare_numar:
        
        push dword mesaj2
        push dword format_afisare
        call [printf]
        add esp, 2*4
        
        push dword numar
        push dword format_citire_numar
        call [scanf]
        add esp, 2*4  
  
        
        cmp dword [numar], 0 ;daca e 0, nu se adauga
        je final
        
        push dword [numar]
        push dword format_scriere_numar
        push dword [descriptor_fisier]
        call [fprintf]
        add esp, 3*4
        
        jmp adaugare_numar ;se adauga urmatorul numar
        
        push dword [descriptor_fisier]
        call [fclose]
        add esp, 1*4
        
        
    
final:

push dword 0
call [exit]
