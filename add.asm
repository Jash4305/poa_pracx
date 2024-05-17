DATA SEGMENT
    NUM1 DW 9
    NUM2 DW 9
    RESULT DW ?
DATA ENDS

CODE SEGMENT
    START:
    ASSUME CS:CODE, DS:DATA
    MOV AX, DATA
    MOV DS, AX
    MOV AX, NUM1
    MOV BX,NUM2
    
    ; Multiply BX by DX, storing the result in AX
    MUL BX
    
    ; Move the result from AX to RESULT
    MOV RESULT, AX
CODE ENDS
END START
