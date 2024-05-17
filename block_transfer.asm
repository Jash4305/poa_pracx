DATA SEGMENT
    STR1 DB 1, 2, 3, 4, 5
DATA ENDS

EXTRA SEGMENT
    STR2 DB ?
EXTRA ENDS

CODE SEGMENT
    ASSUME CS: CODE, DS: DATA, ES: EXTRA
    START:
        MOV AX, DATA
        MOV DS, AX
        MOV AX, EXTRA
        MOV ES, AX
        LEA SI, STR1
        LEA DI, STR2
        MOV CL, 05H
        MOV AX, 0000H
        X:
            MOV AL, DS:[SI]
            MOV ES:[DI], AL
            INC DI
            INC SI
            DEC CL
            JNZ X
CODE ENDS
END START