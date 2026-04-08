#include <windows.h>
#include <wincrypt.h>
#include <iostream>
#include <vector>
#include <iomanip>
#include <sstream>

// ==================== MẢNG BẠN CUNG CẤP (ciphertext) ====================
const std::vector<BYTE> hardcoded_ciphertext = {
    0xF8, 0x50, 0xCC, 0xEF, 0xE6, 0x3C, 0x35, 0x96, 0x1D, 0x61,
    0xAE, 0xC0, 0xC5, 0x31, 0xCE, 0xB0, 0xE7, 0x1D, 0xED, 0xBC,
    0x5D, 0x81, 0x69, 0x8A, 0x35, 0x74, 0x57, 0xB6
};

int main() {
    const char* key_str = "https://www.youtube.com/watch?v=dQw4w9WgXcQ";

    HCRYPTPROV hProv = NULL;
    HCRYPTHASH hHash = NULL;
    HCRYPTKEY hKey = NULL;

    std::cout << "=== RC4 Decrypt (CryptoAPI - chính xác như mã IDA) ===\n";
    std::cout << "Key (SHA1): " << key_str << "\n";
    std::cout << "Ciphertext length: " << hardcoded_ciphertext.size() << " bytes\n\n";

    // Bước 1: Acquire context
    if (!CryptAcquireContextA(&hProv, NULL, NULL, PROV_RSA_FULL, CRYPT_VERIFYCONTEXT)) {
        std::cerr << "CryptAcquireContextA thất bại! Error: " << GetLastError() << std::endl;
        return 1;
    }

    // Bước 2: Tạo hash SHA1
    if (!CryptCreateHash(hProv, CALG_SHA1, 0, 0, &hHash)) {
        std::cerr << "CryptCreateHash thất bại! Error: " << GetLastError() << std::endl;
        CryptReleaseContext(hProv, 0);
        return 1;
    }

    // Bước 3: Hash key
    if (!CryptHashData(hHash, reinterpret_cast<const BYTE*>(key_str), static_cast<DWORD>(strlen(key_str)), 0)) {
        std::cerr << "CryptHashData thất bại! Error: " << GetLastError() << std::endl;
        CryptDestroyHash(hHash);
        CryptReleaseContext(hProv, 0);
        return 1;
    }

    // Bước 4: Derive RC4 key
    if (!CryptDeriveKey(hProv, CALG_RC4, hHash, 0, &hKey)) {
        std::cerr << "CryptDeriveKey thất bại! Error: " << GetLastError() << std::endl;
        CryptDestroyHash(hHash);
        CryptReleaseContext(hProv, 0);
        return 1;
    }
    CryptDestroyHash(hHash);

    // Bước 5: Giải mã (CryptEncrypt trên ciphertext = decrypt vì RC4 đối xứng)
    std::vector<BYTE> plaintext = hardcoded_ciphertext;
    DWORD dwDataLen = static_cast<DWORD>(plaintext.size());

    if (CryptEncrypt(hKey, NULL, TRUE, 0, plaintext.data(), &dwDataLen, static_cast<DWORD>(plaintext.size()))) {
        std::cout << "=== DECRYPT SUCCESFUL ===\n\n";
        std::cout << "Plaintext (hex): ";
        for (BYTE b : plaintext) {
            std::cout << std::hex << std::uppercase << std::setw(2) << std::setfill('0') << static_cast<int>(b) << " ";
        }
        std::cout << "\n\n";

        // In dạng string (nếu có ký tự printable)
        std::string result(plaintext.begin(), plaintext.end());
        std::cout << "Plaintext (string): " << result << std::endl;
        std::cout << "Length: " << dwDataLen << " bytes\n";
    }
    else {
        std::cerr << "CryptEncrypt failed, Error: " << GetLastError() << std::endl;
    }

    // Cleanup
    if (hKey) CryptDestroyKey(hKey);
    if (hProv) CryptReleaseContext(hProv, 0);

    return 0;
}