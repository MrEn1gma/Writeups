**FSM (37 solves)**

Solution:
- First, This challenge required to read a serial key which has formatted is 3 numbers in hexamical concatted together. Then it used string "Thomas A. Anderson" to calculate each of 3 outputs. After that, using `CreateThread(0i64, 0i64, StartAddress, 0i64, 0, 0i64)` to made a check flag function.

`StartAddress` function.
```c
__int64 __fastcall StartAddress(LPVOID lpThreadParameter)
{
  DWORD v1; // eax
  DWORD v2; // eax
  DWORD v3; // eax

  while ( 1 )
  {
    while ( 1 )
    {
      while ( 1 )
      {
        v1 = WaitForMultipleObjects(4u, &Handles, 0, 0xFFFFFFFF);
        if ( v1 )
          break;
        if ( 1620 * second_input + 5447 * third_input + 17170 * first_input == ((unsigned int)first_output ^ 0x2ED0F8B0) )
          SetEvent(qword_7FF6DEDF5660);
        else
LABEL_7:
          SetEvent(hEvent);
      }
      v2 = v1 - 1;
      if ( v2 )
        break;
      if ( 9543 * third_input + 19218 * first_input + 27870 * second_input != (HIDWORD(first_output) ^ 0x63987AEB) )
        goto LABEL_7;
      SetEvent(qword_7FF6DEDF5668);
    }
    v3 = v2 - 1;
    if ( !v3 )
      break;
    if ( v3 == 1 )
      return 0i64;
  }
  if ( 7287 * third_input + 11210 * first_input + 24874 * second_input != (third_output ^ 0xB6DDCFF6) )
    goto LABEL_7;
  SetEvent(hHandle);
  return 0i64;
}
```

This equations can be solved by z3-solver to get the flag, my script here !(./solve.py)
