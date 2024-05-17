DATA SEGMENT
    STR DB 5, 3, 12, 15, 9
    MAX DB ?
    MIN DB ?
    2MAX DB ?
    2MIN DB ?
DATA ENDS

CODE SEGMENT
    ASSUME: CS: CODE, DS: DATA
    START:
    MOV AX, DATA
    MOV DS, AX
    
    MOV CH, 4   ; i loop ke liye
    LOOP1:
        LEA SI, STR
        MOV CL, 4    ; j loop ke liye
        LOOP2:
            MOV AL, [SI]
            MOV BL, [SI+1]
            CMP AL, BL
            JC X
            MOV DL, [SI]
            XCHG DL, [SI+1]
            MOV [SI], DL
            X:
                INC SI
                DEC CL
                JNZ LOOP2
                DEC CH
                JNZ LOOP1
    MOV AL, [SI]
    MOV MAX, AL
    
    MOV AL, [SI-1]
    MOV 2MAX, AL
    
    LEA SI, STR
    MOV AL, [SI]
  
    MOV MIN, AL
    MOV AL, [SI+1]
    MOV 2MIN, AL
CODE ENDS
END START