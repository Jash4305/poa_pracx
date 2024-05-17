data segment
    str1 db 12, 20, 25, 10, 35
    min db ?
    max db ?
data ends

code segment
    assume cs:code, ds:data
    start:
    mov ax, data
    mov ds, ax
    mov ch, 04h
    loop1:
        lea si, str1
        mov cl, 04h
    loop2:
        
        mov al, [si]
        mov bl, [si+1]
        cmp al, bl  
        jc x
        mov dl, [si+1]
        xchg [si],dl
        mov [si+1],dl 
        
        x:
            inc si
            dec cl
            jnz loop2
            dec ch
            jnz loop1
        mov ax, [si]
        mov max, al
        lea si, str1
        mov al, [si]
        mov min, al
code ends
end start
    
    