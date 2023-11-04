/*
I stolen the base64 algorthim here: https://stackoverflow.com/questions/180947/base64-decode-snippet-in-c
*/
#include <iostream>

// change base64 table
static const std::string base64_chars = "6789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz012345+/";//"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

static inline bool is_base64(unsigned char c) {
    return (isalnum(c) || (c == '+') || (c == '/'));
}

std::string base64_decode(std::string const& encoded_string) {
    int in_len = encoded_string.size();
    int i = 0;
    int j = 0;
    int in_ = 0;
    unsigned char char_array_4[4], char_array_3[3];
    std::string ret;

    while (in_len-- && (encoded_string[in_] != '=') && is_base64(encoded_string[in_])) {
        char_array_4[i++] = encoded_string[in_]; in_++;
        if (i == 4) {
            for (i = 0; i < 4; i++)
                char_array_4[i] = base64_chars.find(char_array_4[i]);

            char_array_3[0] = (char_array_4[0] << 2) + ((char_array_4[1] & 0x30) >> 4);
            char_array_3[1] = ((char_array_4[1] & 0xf) << 4) + ((char_array_4[2] & 0x3c) >> 2);
            char_array_3[2] = ((char_array_4[2] & 0x3) << 6) + char_array_4[3];

            for (i = 0; (i < 3); i++)
                ret += char_array_3[i];
            i = 0;
        }
    }

    if (i) {
        for (j = i; j < 4; j++)
            char_array_4[j] = 0;

        for (j = 0; j < 4; j++)
            char_array_4[j] = base64_chars.find(char_array_4[j]);

        char_array_3[0] = (char_array_4[0] << 2) + ((char_array_4[1] & 0x30) >> 4);
        char_array_3[1] = ((char_array_4[1] & 0xf) << 4) + ((char_array_4[2] & 0x3c) >> 2);
        char_array_3[2] = ((char_array_4[2] & 0x3) << 6) + char_array_4[3];

        for (j = 0; (j < i - 1); j++) ret += char_array_3[j];
    }

    return ret;
}

std::string ISITDTU_dec_flag(std::string enc_flag) {
    std::string b64dec = base64_decode(enc_flag), x, tmp;

    for (int j = 0; j < b64dec.length(); j++)
    {
        x += (char)(b64dec[j] ^ 0x2a);
    }

    for (unsigned int i = 0; i < x.length(); i++) {
        if (((((x[i] - 97)) & 0xffffffff) <= 0x19)) {
            unsigned int t = x[i] - 26 * ((int)((unsigned __int64)(0x9D89D89ELL * (int)(x[i] - 84)) >> 32) >> 4);
            tmp += (char)(t + 13);
        }
        else if (((((x[i] - 65)) & 0xffffffff) > 0x19)) {
            tmp += (char)(x[i]);
        }
        else {
            unsigned int t = x[i] - 26 * ((int)((unsigned __int64)(0x9D89D89ELL * (int)(x[i] - 52)) >> 32) >> 4);
            tmp += (char)(t + 13);
        }
    }
    return tmp;
}

int main()
{
    //std::cout << ISITDTU_enc_flag(test_flag) << std::endl;
    std::cout << "ISITDTU{" << ISITDTU_dec_flag("XR4XPDQXPDRICx7FQthxCQpWPwVFPTR6CwxbZT0WCdkWCdkH") << "}" << std::endl;
    return 0;
}
