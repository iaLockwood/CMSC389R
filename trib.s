global _start
section .text

_start:
  mov ebp, 5
  push ebp		;push parameter (5)
  mov ebp, esp
  push ebx
  call _trib		;call func, result stored in eax
  pop ebx      
  add eax, 0x30
  mov eax, 4
  mov ebx, 1		
  mov ecx, eax
  mov edx, 1		;length to print
  int 80h

  mov eax, 1
  mov ebx, 0		
  int 80h

_trib:
  push ebp		;save frame ptr
  mov esp, ebp		;set new frame

  mov edx, [ebp+8] 	;retrieve parameter
  mov ecx, 0
  cmp edx, ecx		;check if 0
  je case0
  mov ecx, 1
  cmp edx, ecx		;check if 1
  je case1
  mov ecx, 2
  cmp edx, ecx		;check if 2
  je case2

recurs:
  sub edx, 1
  push edx 		;push n-1 param
  call _trib
  pop edx 		;get rid of passed param

  sub edx, 1 		;subtract again for n-2
  call _trib
  pop edx

  sub edx, 1 		;subtract again for n-3
  call _trib
  pop edx		;get rid of passed param
  jmp tribEnd

case0: 
  add eax, 0	 	;add 0 to eax
  jmp tribEnd

case1: 
  add eax, 1	 	;add 1 to eax
  jmp tribEnd

case2: 
  add eax, 1	 	;add 1 to eax

tribEnd:
  mov ebp, esp		;on_exit reset stack ptr
  pop ebp		;on_exit restore old frame
  ret		

