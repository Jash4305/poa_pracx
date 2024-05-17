data segment
    num1 db 5
    fac dw ?
data ends

code segment
    assume cs:code, ds:data
    start:
    mov ax, data
    mov ds, ax
    ;call factP
    hlt
    
    factP proc
        mov cl, num1
        mov ax, 0001h
        x:
        mul num1
        dec num1
        jnz x
        mov fac, ax
    endp
    
code ends
end start
        
        
        