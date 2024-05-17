DATA SEGMENT
    STR DB 1, 2, 3, 4, 5
    SUM DB ?
    AVG DB ?
DATA ENDS

CODE SEGMENT
    ASSUME CS: CODE, DS: DATA
    START:
    MOV AX, DATA
    MOV DS, AX
    MOV CL, 05
    LEA SI, STR
    MOV AX, 0000H
    MOV BX, 0000H 
    X:
        MOV AL, [SI]
        ADD BL, AL
        INC SI
        DEC CL
        JNZ X
    MOV SUM, BL
    MOV AL, SUM
    MOV BL, 5
    DIV BL
    MOV AVG, AL
    
CODE ENDS
END START