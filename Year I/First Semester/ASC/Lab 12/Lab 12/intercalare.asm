bits 32

global _intercalare

segment data use32 global data
sir_rez times 100 db 0

segment code use32 global code
;intercalare(len, sir1, sir2)
_intercalare:
    push ebp
    mov ebp, esp
    mov esi, [esp + 12]
    mov ecx, [esp + 8]
    mov edi, sir_rez
    
    jecxz final
    
    cld
    incarcare_octeti_pari:
        movsb 
        inc edi
       
    loop incarcare_octeti_pari
    
    mov esi, [esp + 16]
    mov ecx, [esp + 8]
    mov edi, sir_rez
    
    jecxz
    cld
    inc edi
    
    incarcare_octeti_impari:
        movsb
        inc edi
        
    loop incarcare_octeti_impari
    
    mov eax, sir_rez
    
    mov esp,ebp
    pop ebp
    
    ret
        
        
       
    

