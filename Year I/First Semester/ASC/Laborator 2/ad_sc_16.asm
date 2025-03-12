bits 32
global start
extern exit 
import exit msvcrt.dll

segment data use32 class=data
a db 19
b db 23
c db 45
d db 17

segment code use32 class=code
;a+13-c+d-7+b

start:  
mov al, [a] 
add al, 13
sub al, [c] 
add al, [d]
sub al, 7
add al, [b] 

push dword 0
call [exit]

