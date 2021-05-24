# Self Modify

# Idea & Solution

```txt
- Vượt qua đoạn anti-debug đơn giản (nếu các bạn muốn debug để hiểu rõ chương trình)
- Thông qua các shellcode, ta thu được hàm check flag sau đó cộng 2 số với giá trị 0x1F2582BD69 (133773311337)
- Dùng binascii để tính toán các giá trị với nhau sẽ thu được kết quả cuối cùng
```

Quan sát hàm main:

```c
__int64 __fastcall main(__int64 a1, char **a2, char **a3)
{
  unsigned int v3; // eax
  int i; // [rsp+0h] [rbp-B0h]
  int j; // [rsp+4h] [rbp-ACh]
  char *v7; // [rsp+8h] [rbp-A8h]
  char s[136]; // [rsp+10h] [rbp-A0h]
  unsigned __int64 v9; // [rsp+98h] [rbp-18h]

  v9 = __readfsqword(0x28u);
  if ( ptrace(PTRACE_TRACEME, 0LL, 1LL, 0LL) != -1 )
  {
    puts("Wait! No debugging here!!!");
    exit(1);
  }
  printf("%s", "Give me your key: ");
  fgets(s, 128, stdin);
  s[strlen(s) - 1] = 0;
  for ( i = 0; i <= 6; ++i )
  {
    byte_201010[i] ^= 0x10u;
    byte_201010[i] += 2;
  }
  for ( j = 0; j <= 4; ++j )
    dword_201020[j] ^= 0xDEADBEEF;
  v7 = s;
  v3 = strlen(s);
  if ( (*(unsigned __int8 (__fastcall **)(_QWORD))byte_201010)(v3)
    && (*(unsigned __int8 (__fastcall **)(_QWORD, __int64))dword_201020)(*(_QWORD *)v7, -3773791187856632570LL)
    && (*(unsigned __int8 (__fastcall **)(_QWORD, __int64))dword_201020)(*((_QWORD *)v7 + 1), -2387310594418845445LL) )
  {
    printf("Congratulation, the flag is: efiensctf{%s}\n", s);
  }
  return 0LL;
}
```
**Main assembly**
```asm
lea     rax, dword_201020
mov     rdx, [rbp+var_A8]
mov     rdx, [rdx]
mov     rsi, 0CBA0CCE8B74E5506h
mov     rdi, rdx
call    rax ; dword_201020
test    al, al
jz      short loc_A5D
-------------------------
lea     rax, dword_201020
mov     rdx, [rbp+var_A8]
add     rdx, 8
mov     rdx, [rdx]
mov     rsi, 0DEDE91A9B32358FBh
mov     rdi, rdx
call    rax ; dword_201020
test    al, al
jz      short loc_A5D
```
Ta dễ dàng tính được lần lượt các giá trị của byte_201010 và dword_201020, ez
```c
for ( i = 0; i <= 6; ++i )
{
   byte_201010[i] ^= 0x10u;
   byte_201010[i] += 2;
}
for ( j = 0; j <= 4; ++j ){
   dword_201020[j] ^= 0xDEADBEEF;
}
```
Để giải thích tại sao ở mục solution mình khẳng định đây là shellcode, vì mình quan sát hàm if có đoạn **call    rbx ; byte_201010** và **call    rax ; dword_201020**, 
có nghĩa là chương trình đã lấy 7 bytes của byte_201010 và 20 bytes của dword_201020 sau khi tính toán xong để decode thành 2 hàm. Dưới đây là kết quả sau khi decode 2 shellcode
```c
#shellcode của byte_201010
bool __usercall checkLen@<al>(int a1@<edi>)
{
  return a1 == 16;
}
```

```c
#shellcode của dword_201020
bool __usercall checkFlag@<al>(__int64 a1@<rdi>, __int64 a2@<rsi>)
{
  return a2 + a1 == 0x1F2582BD69i64;
}
```

OK, vậy là mình đã làm sáng tỏ các hàm ẩn của các shellcode trên, dễ dàng nhận ra flag có độ dài là 16 và load 2 giá trị 0xCBA0CCE8B74E5506 và 0xDEDE91A9B32358FB để cộng với
16 bytes của flag xem có bằng 0x1F2582BD69 hay không, ta có thể dùng z3 để giải quyết, nhưng mình sẽ dùng binascii để giải quyết trong nháy mắt :))

```python
binascii.unhexlify(hex((0x1F2582BD69 - 0xCBA0CCE8B74E5506) & 0xffffffffffffffff)[2:])[::-1].decode('utf-8')
binascii.unhexlify(hex((0x1F2582BD69 - 0xDEDE91A9B32358FB) & 0xffffffffffffffff)[2:])[::-1].decode('utf-8')
```

Sau khi đã hoàn thành các bước trên, làm nốt thủ tục cuối thôi :v

```txt
efiensctf{ch4n63_4nd_run!!}
```
