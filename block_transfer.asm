data segment
    str1 db 10, 20, 30
data ends

extra segment
    str2 db ?
extra ends

code segment
    assume: cs:code, ds: data, es: extra
    start:
    mov ax, data
    mov ds, ax
    mov ax, extra
    mov es, ax
    
    mov cl, 03h
    lea si, str1
    lea di, str2
    
x:  mov AH, ds:[si]
    mov es:[di], AH
    inc si
    inc di
    dec cl
    jnz x
code ends
end start
    
    