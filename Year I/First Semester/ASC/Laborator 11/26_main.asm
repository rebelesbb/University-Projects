bits 32
global start
extern exit, fopen, fprintf, scanf, printf, fclose
import exit msvcrt.dll
import fopen msvcrt.dll
import fprintf msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll
import fclose msvcrt.dll

extern minim

segment data use32 class=data
mesaj_citire_lungime db "Introduceti lungimea sirului: ", 0
mesaj_citire_numar db "Introduceti un numar: ", 0
format_numar db '%d', 0
format_afisare_ecran db '%d  ', 0
format_afisare_minim db "Minimul din sir este: %d", 0

lungime_sir dd -1

nume_fisier db "sir.txt", 0
mod_acces db 'w', 0
descriptor_fisier dd -1

minim_ dd -1
aux dd 0
numar dd 0
sir dd -1


segment code use32 class=code
    citire_sir:
        ;afisam mesaj pentru citirea lungimii sirului
        push dword mesaj_citire_lungime
        call [printf]
        add esp, 4 * 1
        
        ;citim lungimea sirului
        push dword lungime_sir
        push dword format_numar
        call [scanf]
        add esp, 4 * 2
        
        mov ecx, [lungime_sir]
        jecxz final_proc
        
        mov edi, sir  ; folosesc operatii pe siruri ca sa citesc pun 
                      ; in variabila sir numerele
        cld
        .citire_numar:
            mov [aux], ecx                ; salvez ecx in aux ca sa nu pierd valoarea in
                                          ; timpul apelurilor de functii
            
            push dword mesaj_citire_numar ; afiseaza mesaj ca sa citeasca un numar
            call [printf]
            add esp, 4 * 1
            
            push dword numar              ; citeste un numar
            push dword format_numar
            call [scanf]
            add esp, 4 * 2
            
            mov eax, [numar]              ; pune in sir numarul
            stosd
            
            mov ecx, [aux]
            loop .citire_numar
        
        
        mov esi, sir    
        mov ecx, [lungime_sir]
        cld
        .afisare_sir_ecran: ; am facut o afisare pe ecran pentru a verifica 
            mov [aux], ecx  ; ca sirul a fost citit corect
        
            lodsd
            push eax
            push dword format_afisare_ecran
            call [printf]
            add esp, 4 * 2
 
            mov ecx, [aux]
            loop .afisare_sir_ecran
            
    final_proc: 
    ret 
    
    start:
    call citire_sir      ;citim sirul
    
    push dword [lungime_sir]
    push dword sir
    call minim           ;apelam functia minim care calculeaza minimul in eax
    
    mov [minim_], ebx 
    
    push dword mod_acces
    push dword nume_fisier
    call [fopen]
    add esp, 4 * 2
    
    mov [descriptor_fisier], eax
    
    push dword [minim_]
    push dword format_afisare_minim
    push dword [descriptor_fisier]
    call [fprintf]
    add esp, 4 * 3
    
    push dword [descriptor_fisier]
    call [fclose]
    add esp, 4 * 1
    
    
final:

push dword 0
call  [exit]