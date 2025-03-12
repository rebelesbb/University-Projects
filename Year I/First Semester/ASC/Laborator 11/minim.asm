bits 32
segment code use32 public code
global minim

minim:

    mov esi, [esp + 4] ; in stiva punem in main offsetul sirului
                       ; apoi il punem in esi pt a folosi op pe siruri
    mov ecx, [esp + 8]
    
    cld
    
    lodsd 
    mov ebx, eax ;initializam minimul cu prima valoare din sir
    
    dec ecx        ; ca sa nu comparam primul element cu el insusi
    jecxz return
    
    cld
    
    .cautare_minim:
        lodsd     ; punem in eax urmatorul dword din sir
        
        cmp eax, ebx
        jnl .nu_e_mai_mic
        
        mov ebx, eax
        
        .nu_e_mai_mic:
        
        loop .cautare_minim
    
    return:
    ret 8

    
    
    
    
    
