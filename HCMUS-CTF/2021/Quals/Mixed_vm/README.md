# Mixed_vm (19 solves)

Attachment:
* [VM](./m_vm)

Description:
> I just create a new VM. Can you find the secret inside it?

## Solution

> 1 dạng VM điển hình - VM based obfuscation.

Theo lẽ thường thì mình sẽ viết script `vm_disassemble.py` để tái tạo lại các instruction gốc từ các opcodes. Tuy nhiên thì ở challenge này thì nó không dễ viết như vậy, có
quá nhiều switch/case để viết, nên mình quyết định đặt breakpoint ở đầu hàm main và hàm `sub_839()`
> Vì các opcode khi debug sẽ lấy 4 bytes 1 lần nên việc debug không mất quá nhiều thời gian.

## Analysis:

Bằng việc debug như trên, không quá khó để đoán và liệt kê 1 số các chức năng chính của VM:
- Opcodes `0xEFEFEFEF`, `0xCCCCCCCC` và `0xFFFFFFFF`: lần lượt thực hiện việc `read()`, `write()` và set flag sau khi so sánh.
- Opcode `0xCCAA0012`: So sánh 2 giá trị.
- Opcode `0x98762222`: Cộng 2 giá trị. 
- Opcode `0xABCDEF00`: Khỏi tạo giá trị cần tính toán.
- Opcode `0x83660101`: XOR 2 giá trị.
- Opcode `0x34535888`: Khởi tạo giá trị. 

Sau khi nắm rõ các opcode, mình có thể kết luận sơ bộ hàm `check` của VM: đầu tiên chương trình sẽ nhận input là 48 ký tự, sau đó lấy 4 byte đầu xor với 0xdeadbeef rồi cộng 
với 0x13371337, sau đó lấy kết quả đó xor với 4 byte tiếp theo thay cho giá trị 0xdeadbeef rồi lại cộng với 0x13371337,... Mình sẽ demo lại bằng python.

```python
start = 0xdeadbeef
x = input[i] ^ start
output[i] = x + 0x13371337
```
Từ đó ta có thể reverse lại được, output có sẵn trong opcode. Dưới đây là solution của mình: 
[solve](./solve.py)
