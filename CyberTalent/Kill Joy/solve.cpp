// solve.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <stdint.h>

std::string convert_hex_value_to_str(uint32_t inp) {
    uint32_t s[4];
    std::string out_str;
    s[0] = (inp >> 0x18) & 0xff;
    s[1] = (inp >> 0x10) & 0xff;
    s[2] = (inp >> 0x8) & 0xff;
    s[3] = (inp >> 0x0) & 0xff;

    for (int i = 0; i < 4; i++)
    {
        out_str += (char)s[i];
    }
    return out_str;
}

void decipher(uint32_t num_rounds, uint32_t v[2], uint32_t key[4]) {
    uint32_t i;
    uint32_t v0 = v[0], v1 = v[1], delta = 0x9E3779B9, sum = delta * num_rounds;
    for (i = 0; i < num_rounds; i++) {
        v1 -= (((v0 << 4) ^ (v0 >> 5)) + v0) ^ (sum + key[(sum >> 11) & 3]);
        sum -= delta;
        v0 -= (((v1 << 4) ^ (v1 >> 5)) + v1) ^ (sum + key[sum & 3]);
    }
    v[0] = v0; v[1] = v1;
}

int main()
{
    uint32_t key[4] = { 0x34561234, 0x111F3423, 0x1333337, 0x34D57910 };
    uint32_t enc_flag[4][2] = { {0xD6F74320, 0x636A7B0A},
                                {0xEEC58E45, 0x5F1E3AF5},
                                {0x14D72088, 0x819BF516},
                                {0x10A4D83A, 0x2C1001E7} };
    uint32_t idx_enc_flag[2];
    std::string flag = "";
    for (uint32_t i = 0; i < 4; i++)
    {
        for (uint32_t j = 0; j < 2; j++)
        {
            idx_enc_flag[j] = enc_flag[i][j];
        }
        decipher(0x20, idx_enc_flag, key);
        flag += convert_hex_value_to_str(idx_enc_flag[0]);
        flag += convert_hex_value_to_str(idx_enc_flag[1]);
    }
    std::cout << "FLAG is: " << flag << std::endl;
    return 0;
}