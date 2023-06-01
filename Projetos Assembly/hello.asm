section .data

section .text

global_start

_start:
    ; destino, origem
    mov eax, 0x1
    mov ebx, 0x0
    int 0x80