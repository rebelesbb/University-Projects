bits 32 
global start
extern exit, printf
import exit masvcrt.dll
import printf masvcrt.dll
segment data use32 class=data
sir1 db "12345", 0
sir2 db "abcde", 0
len equ 5
format_afisare db  "%s\n", 0
sir_rez times 2 * len db 0

segment code use32 class=code
_intercalare:
    mov esi, [esp + 8]
    mov ecx, [esp + 4]
    mov edi, sir_rez
    
    jecxz final
    
    cld
    incarcare_octeti_pari:
        movsb 
        inc edi
       
    loop incarcare_octeti_pari
    
    mov esi, [esp + 12]
    mov ecx, [esp + 4]
    mov edi, sir_rez
    
    jecxz final
    cld
    inc edi
    
    incarcare_octeti_impari:
        movsb
        inc edi
        
    loop incarcare_octeti_impari
    
    mov eax, sir_rez
    
    ret 3 * 4
    
start:
    push dword sir2
    push dword sir1
    push dword len
    call _intercalare
    
    push eax
    push dword format_afisare
    call [printf]

    final:
push dword 0
call [exit]