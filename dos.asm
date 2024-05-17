data segment
    str db "Enter char:$"
data ends
code segment
    assume cs:code, ds:data
    start:
    mov ax, data
    mov ds, ax
    lea si, str
    
    mov ah, 09H ;display the str
    int 21H
    
    mov ah, 01H ; take input
    int 21H
   
    mov dl, al
    
    mov ah, 02H
    int 21H
    
    hlt 
    
code ends
end start