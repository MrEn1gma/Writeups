# WeirdProtocol (12 solves)

Attachments:
* [WeirdProtocol.exe](./WeirdProtocol.exe)

## Solution
File được viết bằng c++, trên Visual Studio, PE 32-bit.

Main function : 
```c
  v3 = j____acrt_iob_func(1u);
  j__setbuf(v3, 0);
  v4 = j____acrt_iob_func(0);
  j__setbuf(v4, 0);
  v5 = j____acrt_iob_func(2u);
  j__setbuf(v5, 0);
  v6 = sub_408310(0);
  j__srand(v6);
  dword_4D0358 = j__rand() % 5 + 5;
  sub_4019B5("[+] Please enter the password: ");
  v7 = j____acrt_iob_func(0);
  j__fgets(Str, 64, v7);
  v10 = j__strlen(Str) - 1;
  if ( v10 >= 0x40 )
    j____report_rangecheckfailure();
  Str[v10] = 0;
  sub_404183();                                 // Create file dump to execute in Temp folder
  if ( (unsigned __int8)sub_403F62() )          // Check connection
  {
    j__puts("[+] Connecting to the online service ...");
    Sleep(0x1388u);
    if ( (unsigned __int8)sub_401F32() )
    {
      v13 = sub_408310(0);
      while ( 1 )
      {
        v12 = sub_408310(0);
        if ( v12 - v13 >= (unsigned int)dword_4D0358 )
          break;
        sub_402F04(L"[+] Fail, reconnecting ...\n");
        Sleep(0x3E8u);
      }
      v11[0] = j__strlen(Str);
      sub_40204A(s, (int)v11, 4);
      sub_40204A(s, (int)Str, v11[0]);
      sub_4013DE(s, (int)v11, 4);
      if ( v11[0] <= 1023 && v11[0] > 0 )
      {
        sub_4013DE(s, (int)v14, v11[0]);
        v9 = v11[0];
        if ( v11[0] >= 0x400u )
          j____report_rangecheckfailure();
        v14[v9] = 0;
        sub_4019B5("-----> %s\n");
      }
      sub_403850();
      result = 0;
    }
    else
    {
      sub_402F04(L"[+] CONNECT ERROR\n");
      result = 0;
    }
  }
  else
  {
    sub_402F04(L"[+] RUN ERROR\n");
    result = 0;
  }
  return result;
}
```
Nhìn tổng quan chương trình có thể cho chúng ta kết luận sơ bộ:
- Chương trình nhận input (chưa rõ độ dài ký tự)
- Qua hàm `sub_4076E0` để thực thi thêm 1 file nũa
- Thực hiện connect tới server để check flag

Phân tích hàm sub_4076E0:
```c
  __CheckForDebuggerJustMyCode(&unk_4D3018);
  v9 = 1;
  hResData = 0;
  v6 = 0;
  v4 = 0;
  v3 = 0;
  hFile = (HANDLE)-1;
  hResInfo = FindResourceW(0, (LPCWSTR)0x6E, L"Binary");
  if ( hResInfo )
  {
    hResData = LoadResource(0, hResInfo);
    if ( hResData )
    {
      v6 = (char *)LockResource(hResData);
      v4 = SizeofResource(0, hResInfo);
      if ( v6 && v4 )
      {
        GetTempPathW(0x208u, CommandLine);
        sub_4014A6(String2, 6);
        lstrcatW(CommandLine, String2);
        lstrcatW(CommandLine, L".tmp2");
        hFile = CreateFileW(CommandLine, 0x40000000u, 1u, 0, 2u, 0x80u, 0);
        if ( hFile == (HANDLE)-1 )
        {
          v9 = 0;
        }
        else
        {
          while ( v3 < v4 )
          {
            _mm_lfence();
            NumberOfBytesWritten = 0;
            if ( !WriteFile(hFile, &v6[v3], v4 - v3, &NumberOfBytesWritten, 0) )
              break;
            v3 += NumberOfBytesWritten;
          }
          if ( v3 != v4 )
            v9 = 0;
        }
      }
      else
      {
        v9 = 0;
      }
    }
    else
    {
      v9 = 0;
    }
  }
  else
  {
    v9 = 0;
  }
  if ( hFile != (HANDLE)-1 )
    CloseHandle(hFile);
  return v9;
}
```

Đầu tiên hàm này sẽ gọi `LoadResource()` với size là 0xd1a00 byte, sau đó gọi hàm `GetTempPathW()` lấy đường dẫn của thư mục Temp, 
tiếp đến `sub_4014A6()` được gọi để khởi tạo tên file ngẫu nhiên với độ dài 6 chữ số có dạng: `%random%.tmp2` và sẽ được lưu 
tại `C:\Users\%your user%\AppData\Local|Temp`.

# Phân tích file `%random%.tmp2`

```c
 if ( (unsigned __int8)sub_402F31() )
  {
    sub_4013DE(dword_4CC004, (int)v10, 4);
    if ( v10[0] < 0 || v10[0] > 1023 )
    {
      MessageBoxW(0, L"Error", L"Hacker", 0x10u);
      result = 0;
    }
    else
    {
      sub_4013DE(dword_4CC004, (int)v12, v10[0]);
      v4 = v10[0];
      if ( v10[0] >= 0x400u )
        j____report_rangecheckfailure();
      v12[v4] = 0;
      sub_40173F((int)v9);
      sub_4022E8((int)v9, (int)v12, v10[0]);
      sub_403189(v9, (int)Buf1);
      Buf2[0] = 44;
      Buf2[1] = -14;
      Buf2[2] = 77;
      Buf2[3] = -70;
      Buf2[4] = 95;
      Buf2[5] = -80;
      Buf2[6] = -93;
      Buf2[7] = 14;
      Buf2[8] = 38;
      Buf2[9] = -24;
      Buf2[10] = 59;
      Buf2[11] = 42;
      Buf2[12] = -59;
      Buf2[13] = -71;
      Buf2[14] = -30;
      Buf2[15] = -98;
      Buf2[16] = 27;
      Buf2[17] = 22;
      Buf2[18] = 30;
      Buf2[19] = 92;
      Buf2[20] = 31;
      Buf2[21] = -89;
      Buf2[22] = 66;
      Buf2[23] = 94;
      Buf2[24] = 115;
      Buf2[25] = 4;
      Buf2[26] = 51;
      Buf2[27] = 98;
      Buf2[28] = -109;
      Buf2[29] = -117;
      Buf2[30] = -104;
      Buf2[31] = 36;
      v6[0] = 32;
      v6[1] = 38;
      v6[2] = 33;
      v6[3] = 57;
      v6[4] = 60;
      v6[5] = 69;
      v6[6] = 38;
      v6[7] = 56;
      v6[8] = 42;
      v6[9] = 20;
      v6[10] = 6;
      v6[11] = 10;
      v6[12] = 24;
      v6[13] = 51;
      v6[14] = 28;
      v6[15] = 7;
      v6[16] = 58;
      v6[17] = 27;
      v6[18] = 9;
      v6[19] = 6;
      v6[20] = 26;
      v6[21] = 1;
      v6[22] = 51;
      v6[23] = 4;
      v6[24] = 10;
      v6[25] = 0;
      v6[26] = 0;
      v6[27] = 20;
      v6[28] = 8;
      v6[29] = 18;
      v6[30] = 0;
      if ( !j__memcmp(Buf1, Buf2, 0x20u) )
      {
        for ( i = 0; i < 0x1E; ++i )
          v6[i] ^= v12[(int)i % v10[0]];
        Str = v6;
      }
      else
      {
        Str = "Nice try buddy";
      }
      v10[0] = j__strlen(Str);
      sub_4025B8(dword_4CC004, (int)v10, 4);
      sub_4025B8(dword_4CC004, (int)Str, v10[0]);
      sub_4037D3();
      result = 0;
    }
  }
  else
  {
    MessageBoxW(0, L"Error", L"Error1", 0x10u);
    result = 0;
  }
  return result;
}
```
Ở hàm main trên chính là hàm check flag mà được file chính load, có thể thấy được flow chương trình như sau:
- nhận input 32 ký tự, sau đó đi qua 1 rừng check password  # đoạn này mình thấy quá dài nên mình sẽ skip nó :(
- nếu input trùng với mảng Buf2 thì lập tức print flag

OK bây giờ nhìn vào hàm if dưới đây:
```c
if ( !j__memcmp(Buf1, Buf2, 0x20u) )
{
   for ( i = 0; i < 0x1E; ++i )
       v6[i] ^= v12[(int)i % v10[0]];
       Str = v6;
   }
   else
   {
       Str = "Nice try buddy";
   }
   ..................
}
```
Vì input của Buf1 không ảnh hưởng gì tới giá trị `v6` và `v12` nên ta hoàn toàn có thể skip nó, sau đó chỉ việc đổi instruction làm sao cho nó chạy qua đoạn print 
flag, ở đây mình sẽ viết lại script [solve.py](./solve.py).

=== DONE ===
