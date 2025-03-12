bits 32
global start
extern exit
import exit msvcrt.dll
segment data use32 class = data
s db 'a', 'A', 'b', 'B', '2', '%', 'x'
l equ $-s ; lungimea sirului
d resb l 
segment code use32 class = code
;Se da un sir de caractere S. Sa se construiasca sirul D care sa contina toate literele mici din ;sirul S.
;Exemplu:
;S: 'a', 'A', 'b', 'B', '2', '%', 'x'
;D: 'a', 'b', 'x'

start:
    
    mov ecx, l 
    mov esi, 0
    mov edx, 0
    
    jecxz final
    
    inceput_loop:
        
        mov al, [s+esi]
        
        cmp al, 'a' 
        
        jge compara_z ; daca caracterul e >= 'a' verificam daca e si <= 'z' (daca e litera mica)
        jmp continua  ; altfel trecem la urmatorul element
        
        compara_z:
            
            cmp al, 'z' 
            jle adauga   ; daca caracterul e <= 'z' il adaugam in d
            jmp continua ; altfel trecem la urmatorul element
            
            adauga:
            mov [d+edx], al
            inc edx
        
        continua:
            inc esi
            
    loop inceput_loop
    
final:

push dword 0
call [exit]