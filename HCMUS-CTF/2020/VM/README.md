# VM_HCMUS-CTF2020

Bài này là 1 dạng VM điển hình, đầu tiên chúng ta sẽ xem qua hàm main:
```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int result; // eax
  int res; // [rsp+Ch] [rbp-74h]
  VM vm; // [rsp+10h] [rbp-70h]
  char input[64]; // [rsp+30h] [rbp-50h]
  unsigned __int64 v7; // [rsp+78h] [rbp-8h]

  v7 = __readfsqword(0x28u);
  puts("[+] Please input the password");
  scanf("%63s", input);
  if ( strlen(input) == 39
    && !memcmp(input, "HCMUS-CTF{", 0xAuLL)
    && input[38] == 125
    && (initVM(&vm, (BYTE *)&input[10], 28, c, 228), res = runVM(&vm), destroyVM(&vm), res) )
  {
    puts("[+] That's the flag");
    result = 0;
  }
  else
  {
    puts("[+] Next time!");
    result = 0;
  }
  return result;
}
```
Như vậy là chương trình này sẽ lấy đủ 39 ký tự sau khi người dùng nhập vào, sau đó chương trình sẽ thoát nếu kiểm tra điều kiện không có **HCMUS-CTF{}**, tiếp theo ta lại quan sát 3 hàm chính trong chương trình này:
```text
intVM(): lưu trữ các bytecode bao gồm 228 bytes
runVM(): xử lý các bytecode - hàm này chúng ta sẽ phân tích sâu hơn
destroyVM(): trỏ đến các bộ nhớ sau khi chạy xong chương trình
```
Quan sát hàm runVM():
```c
int __cdecl runVM(VM *vm)
{
  BYTE val; // [rsp+1Fh] [rbp-31h]
  int idx_0; // [rsp+24h] [rbp-2Ch]

  while ( vm->ip < vm->code_size )
  {
    switch ( vm->code[vm->ip] )
    {
      case 5u:
        vm->r1 = vm->data[vm->code[vm->ip + 2]] + vm->data[vm->code[vm->ip + 1]];
        vm->ip += 3;
        break;
      case 0xAu:
        vm->r1 = vm->data[vm->code[vm->ip + 1]] - vm->data[vm->code[vm->ip + 2]];
        vm->ip += 3;
        break;
      case 0xFu:
        vm->r1 = vm->data[vm->code[vm->ip + 2]] * vm->data[vm->code[vm->ip + 1]];
        vm->ip += 3;
        break;
      case 0x1Eu:
        vm->r1 = vm->data[vm->code[vm->ip + 2]] ^ vm->data[vm->code[vm->ip + 1]];
        vm->ip += 3;
        break;
      case 0x64u:
        vm->r2 = vm->code[vm->ip + 1] == vm->r1;
        vm->ip += 2;
        break;
      case 0x69u:
        vm->r2 = vm->r1 == vm->data[vm->code[vm->ip + 1]];
        vm->ip += 2;
        break;
      case 0x96:
        idx_0 = vm->code[vm->ip + 1];
        val = vm->code[vm->ip + 2];
        switch ( idx_0 )
        {
          case 1:
            vm->r1 = val;
            break;
          case 2:
            vm->r2 = val;
            break;
          case 3:
            vm->r3 = val;
            break;
        }
        vm->ip += 3;
        break;
      case 0xCD:
        if ( vm->r2 )
          vm->ip += 3;
        else
          vm->ip = *(_WORD *)&vm->code[vm->ip + 1];
        break;
      default:
        if ( vm->code[vm->ip] != -1 )
          printf("[+] Wrong opcode: 0x%02X\n", vm->code[vm->ip]);
        return vm->r3;
    }
  }
  return vm->r3;
}
```
Ơn giời là bài này các hàm rất là clear nên trong quá trình rev cũng không gặp nhiều trở ngại gì :)), phân tích sơ bộ thì hàm này có 8 case với các chức năng như **MOV**, **ADD**, **XOR**,.... Bạn đọc có thể tham khảo solution hàm vm_run của mình, dưới đây là kq sau khi chạy :v
```asm
MOV R1, 0x4d
MOV vm->data[0x00], R1
CMP R1, 0
IMUL R1, vm->data[0x1b], vm->data[0x00]
MOV R1, 0x57
CMP R1, 0
MOV R1, 0x34
MOV vm->data[0x01], R1
CMP R1, 0
ADD R1, vm->data[0x1a], vm->data[0x01]
MOV R1, 0xa2
CMP R1, 0
MOV R1, 0x4c
MOV vm->data[0x02], R1
CMP R1, 0
XOR R1, vm->data[0x19], vm->data[0x02]
MOV R1, 0x25
CMP R1, 0
MOV R1, 0x77
MOV vm->data[0x03], R1
CMP R1, 0
XOR R1, vm->data[0x18], vm->data[0x03]
MOV R1, 0x1f
CMP R1, 0
MOV R1, 0x61
MOV vm->data[0x04], R1
CMP R1, 0
SUB R1, vm->data[0x04], vm->data[0x17]
MOV R1, 0xfe
CMP R1, 0
MOV R1, 0x72
MOV vm->data[0x05], R1
CMP R1, 0
XOR R1, vm->data[0x16], vm->data[0x05]
MOV R1, 0x46
CMP R1, 0
MOV R1, 0x33
MOV vm->data[0x06], R1
CMP R1, 0
IMUL R1, vm->data[0x15], vm->data[0x06]
MOV R1, 0xb7
CMP R1, 0
MOV R1, 0x5f
MOV vm->data[0x07], R1
CMP R1, 0
IMUL R1, vm->data[0x14], vm->data[0x07]
MOV R1, 0x41
CMP R1, 0
MOV R1, 0x75
MOV vm->data[0x08], R1
CMP R1, 0
SUB R1, vm->data[0x08], vm->data[0x13]
MOV R1, 0x29
CMP R1, 0
MOV R1, 0x73
MOV vm->data[0x09], R1
CMP R1, 0
ADD R1, vm->data[0x12], vm->data[0x09]
MOV R1, 0xd4
CMP R1, 0
MOV R1, 0x33
MOV vm->data[0x0a], R1
CMP R1, 0
ADD R1, vm->data[0x11], vm->data[0x0a]
MOV R1, 0xa8
CMP R1, 0
MOV R1, 0x73
MOV vm->data[0x0b], R1
CMP R1, 0
IMUL R1, vm->data[0x10], vm->data[0x0b]
MOV R1, 0x1c
CMP R1, 0
MOV R1, 0x5f
MOV vm->data[0x0c], R1
CMP R1, 0
IMUL R1, vm->data[0x0f], vm->data[0x0c]
MOV R1, 0x4e
CMP R1, 0
MOV R1, 0x76
MOV vm->data[0x0d], R1
CMP R1, 0
SUB R1, vm->data[0x0d], vm->data[0x0e]
MOV R1, 0x45
CMP R1, 0
MOV R3, R1, 0xff
```
# solve
Sau 1 hồi phân tích asm code này thì mình có thể trình bày như sau:
```text
 - Đầu tiên nó sẽ kiểm tra 28 ký tự bên trong flag, sau đó kiểm tra lần lượt 14 ký tự đầu của flag, nếu sai thì thoát
 - Các lệnh ADD, XOR,.. sẽ tạo thành 1 hệ phương trình tuyến tính, mình sẽ dùng z3 để giải quyết bài này :))
```
```asm
IMUL R1, vm->data[0x1b], vm->data[0x00]
MOV R1, 0x57
CMP R1, 0
```
Đoạn trên có thể hiểu là: **arr[0x1b] * arr[0x00] == 0x57**, tương tự với các đoạn khác, ta thu được 1 hệ phương trình tuyến tính như sau:
```text
(x[0x1b] * x[0x00]) & 0xff == 0x57
(x[0x1a] + x[0x01]) & 0xff == 0xa2
(x[0x19] ^ x[0x02]) & 0xff == 0x25
(x[0x18] ^ x[0x03]) & 0xff == 0x1f
(x[0x04] - x[0x17]) & 0xff == 0xfe
(x[0x16] ^ x[0x05]) & 0xff == 0x46
(x[0x15] * x[0x06]) & 0xff == 0xb7
(x[0x14] * x[0x07]) & 0xff == 0x41
(x[0x08] - x[0x13]) & 0xff == 0x29
(x[0x12] + x[0x09]) & 0xff == 0xd4
(x[0x11] + x[0x0a]) & 0xff == 0xa8
(x[0x10] * x[0x0b]) & 0xff == 0x1c
(x[0x0f] * x[0x0c]) & 0xff == 0x4e
(x[0x0d] - x[0x0e]) & 0xff == 0x45
```
Kết hợp với 14 ký tự đầu mà ta tìm được, sẽ thu được flag: **HCMUS-CTF{M4Lwar3_us3s_v1rtuaL_m4chin3}**
