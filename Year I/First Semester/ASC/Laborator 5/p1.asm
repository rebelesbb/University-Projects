bits 32
global start
extern exit
import exit msvcrt.dll
segment data use32 class=data
s db 'a', 'B', 'C', 'd' ; declaram sirul, fiecare litera are dimensiunea unui byte
l equ $-s ;cati bytes alocam in sirul s
d resb l
segment code use32 class=code
start:
;Se da un sir de caractere (litere mari/mici)
;Facem din litere mici, litere mari 
     mov ecx, l
     mov esi, 0 ;index
     
     jecxz final
     
     inceput_loop:
     
         mov al, [s+esi]
         
         cmp al, 'Z'
         
         jbe pune
         ja transforma
         
         transforma:
             sub al, 'a'-'A' ;transformam din l.mica in mare
         
         pune:
             mov [d+esi], al
          
         inc esi ;esi++ 
         ;dec esi  <=> esi--
         
         
    loop inceput_loop
     

final:

push dword 0
call [exit]