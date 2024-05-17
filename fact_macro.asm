data segment
    num1 db 5
    fac dw ?
data ends
    
fact macro f
    mov ax, 0001H
    up:
    mul f
    dec f
    jnz up
    mov fac, ax
    endm

code segment
    assume cs:code, ds:data
    start:
    mov ax, data
    mov ds, ax
    mov cl, num1
    fact num1

    hlt
code ends
end start