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

Đầu tiên hàm này sẽ gọi `LoadResource()` khởi tạo 0xd1a00 byte, sau đó gọi hàm `GetTempPathW()` lấy đường dẫn của thư mục Temp, 
sau đó gọi tiếp hàm `sub_4014A6()` để khởi tạo tên file ngẫu nhiên dạng số với độ dài 6 ký tự, 
