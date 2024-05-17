DATA SEGMENT
    NUM DW 5
    FAC DW ?
DATA ENDS

CODE SEGMENT
    ASSUME CS: CODE, DS: DATA
    START:
        MOV AX, DATA
        MOV DS, AX
        MOV AX, 0001H
        MOV CL, 5
        CALL FACT
        MOV AX, 4CH
        INT 21
        
        FACT PROC
        X: 
            MOV BX, NUM
            MUL BX
            DEC NUM
            DEC CL
            JNZ X
            MOV FAC, AX
         ENDP
        
CODE ENDS
END START