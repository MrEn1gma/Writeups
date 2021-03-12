# syscall_777 (61 solved)
``` 
Description: Did you know system call number 777 in Linux works as a flag checker?.
TD;LR: Analyze syscall() in main function use seccomp-tools to dump the asm, then you have to use z3 solver to get the flag.
```
Some RE challenge use techniques to hide the encrypted function. In this challenge, syscall() will load the init before main then run the shellcode in `UNK_B00`.
```c
// sub_7C0 function
unsigned __int64 sub_7C0()
{
  char *v0; // rdi
  _DWORD *v1; // rsi
  __int64 v2; // rcx
  __int16 v4; // [rsp+0h] [rbp-688h] BYREF
  char *v5; // [rsp+8h] [rbp-680h]
  char v6[1640]; // [rsp+10h] [rbp-678h] BYREF
  unsigned __int64 v7; // [rsp+678h] [rbp-10h]

  v7 = __readfsqword(0x28u);
  if ( prctl(38, 1LL, 0LL, 0LL, 0LL) )
    goto LABEL_2;
  v0 = v6;
  v1 = &unk_B00;
  v2 = 410LL;
  v4 = 205;
  while ( v2 )
  {
    *(_DWORD *)v0 = *v1++;
    v0 += 4;
    --v2;
  }
  v5 = v6;
  if ( prctl(22, 2LL, &v4) )
LABEL_2:
    exit(1);
  return __readfsqword(0x28u) ^ v7;
}
```
