bits 32 glogal 
start extern 
exit 
import exit msvcrt.dll

segment data use32 class = data
s dd 1,2,3,4 ;...
l equ ($-s)/4 ;pt ca e sir de dword
d resd l 

segment code use32 class = code
start:
    lodsb ; al = [esi] <=>  mov esi, 0
          ;                 mov al, [s+esi]
          ;                 inc esi  cand df = 0
          ;w => ax = [esi], d => eax = [esi]
    stosb ;[esi] = al <=> mov esi, 0
          ;               mov [s+esi], al
          ;               inc esi   cand df = 0
    movsb ;[edi] = [esi] <=> mov esi, 0
          ;                  mov edi, 0
          ;                  mov al, [s+esi]
          ;                  mov [s+edi], al
          ;                  inc esi
          ;                  inc edi 
    scasb ;cmp al, [esi]
          ;inc esi 
    cmpsb ;cmp [edi], [esi]
          ;inc esi
          ;inc edi
         