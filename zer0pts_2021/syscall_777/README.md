# syscall_777 (61 solved)
``` 
Description: Did you know system call number 777 in Linux works as a flag checker?
TD;LR: Analyze syscall() in main function use seccomp-tools to dump the asm, then you have to use z3 solver to get the flag
```

# Main function:
```c
__int64 __fastcall main(int a1, char **a2, char **a3)
{
  __int64 v3; // rcx
  unsigned int v4; // er12
  int *v5; // rdi
  __int64 i; // rbx
  int v8[14]; // [rsp+0h] [rbp-68h] BYREF
  unsigned __int64 v9; // [rsp+38h] [rbp-30h]

  v3 = 14LL;
  v4 = 1;
  v9 = __readfsqword(0x28u);
  v5 = v8;
  while ( v3 )
  {
    *v5++ = 0;
    --v3;
  }
  __printf_chk(1LL, "FLAG: ", a3);
  if ( (unsigned int)__isoc99_scanf("%55s", v8) != 1 )
    return v4;
  for ( i = 1LL; i != 15; ++i )
  {
    syscall(
      777LL,
      (unsigned int)v8[i - 1],
      (unsigned int)v8[(int)i % 14],
      (unsigned int)v8[((int)i + 1) % 14],
      (unsigned int)v8[((int)i + 2) % 14]);
    v4 = *__errno_location();
    if ( v4 == 1 )
    {
      puts("Wrong...");
      return v4;
    }
  }
  v4 = 0;
  puts("Correct!");
  return v4;
}
```
