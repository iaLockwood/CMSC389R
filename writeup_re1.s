section .text
do_this:	
  push ebp	;these two lines set the frame for the function
  mov ebp, esp	

  mov ecx, 4	;load ecx with the int 4
  mov dl, 0ffh	;load dl with 8 bits of 1s

f:
  shl eax, 8	;shift eax 8 bits left, making al 0s
  or al, dl	;(0 || 1) == 1, fill al with 1s
  loop f	;while ecx != 0 and decrement, so 4 times
		;eax now all 1s

  mov ecx, 8	;load 8 into ecx
  mov dx, 6761h	;load 6761 into dx
  shl edx, cl	;shift edx cl (8 bits, since we loaded ecx) left
  shl edx, cl	;shift 8 left again
  mov dx, 6c66h	;load 6c66 into dx
		;edx now 67616c66

  xor eax, edx	;eax had compliment of edx
  not eax	;eax now 67616c66

  mov esp, ebp	;reset the frame before function returns
  pop ebp
  ret
