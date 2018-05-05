section .text
do_this:
  push ebp
  mov ebp, esp	;frame now set
  push edi	;edi is local var

  mov al, 33h	;load 33 into al
  mov cl, 4	;load 4 into cl
  lea edi, [x]	;loads address 0 into edi

  rep stosb	;store string from al (33) at address edi (0)

  xor BYTE [x], 0	;xor value @address 0 with 0
  xor BYTE [x+1], 0bh	;xor value @address 1 with 0b
  xor BYTE [x+2], 0ah	;xor value @address 2 with 0a
  xor BYTE [x+3], 61h	;xor value @address 3 with 61

  mov eax, [x]		;load value @address 0 into eax

  pop edi	;reset stack frame before func returns
  mov esp, ebp
  pop ebp
  ret

section .data
x dd 0
