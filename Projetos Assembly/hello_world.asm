; hello_world.asm
;
; link do video base: youtube.com/watch?v=HgEGAaYdABA

global _start

section .text:

_start:
    mov eax, 0x4                ; usa the write syscall
    mov ebx, 1                  ; use stout as the fd
    mov ecx, message            ; use the message as the buffer
    mov edx, message_length     ; and supply the length
    int 0x80                    ; invoke the syscall

    ;   NOW EXITING!!

    mov eax, 0x1
    mov ebx, 0

    int 0x80

section .data:
    message: db "Hello World!", 0xA
    message_length eq $-message

