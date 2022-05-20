# Nuts And Bolts

## Solution
- This challenge gave me 2 file (1 ELF file written by Rust and source code of chall).
- It using AES Encryption in mode ECB (line 15-18) to generate random key with 32 bytes. Then It will XOR with key and enc_output (after encrypt input by AES)
