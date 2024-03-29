
def coconut_fixed_func(data, startAddr, endAddr):
    org_file = [i for i in open("okchua.exe", "rb").read()] # COPIED FROM COCONUT.EXE
    for i in range(endAddr - startAddr):
        org_file[startAddr + i] = data[i]
        
    open("okchua.exe", "wb").write(bytearray(org_file))
    print("Patching bytes from 0x%x to 0x%x DONE !!!" % (startAddr , endAddr))

def ASCIS_coconut_decrypt(meat, water):
    for i in range(len(meat)):
        water[meat[i][0]] = meat[i][1] & 0xff
        water[meat[i][0] + 1] = (meat[i][1] >> 8) & 0xff
        water[meat[i][0] + 2] = (meat[i][1] >> 16) & 0xff
        water[meat[i][0] + 3] = (meat[i][1] >> 24) & 0xff

    return water

# PRINT: ENTER KEY
coconut28_meat28 = [(1, 1879048193), (6, 167772164), (11, 167772165)]
coconut28_water28 = [114, 0, 0, 0, 0, 40, 0, 0, 0, 0, 40, 0, 0, 0, 0, 42]
coconut82_addr = 0x7bc + 21

# convert key to hex string
coconut15_meat15 = [(1, 167772220), (7, 167772211), (12, 167772221), (17, 1879048389), (22, 1879048217), (27, 167772222)]
coconut15_water15 = [40, 0, 0, 0, 0, 2, 111, 0, 0, 0, 0, 40, 0, 0, 0, 0, 114, 0, 0, 0, 0, 114, 0, 0, 0, 0, 111, 0, 0, 0, 0, 42]
coconut51_addr = 0xe34 + 13

# Decrypt check flag 2
coconut89_meat89 = [(1, 1879048217), (38, 167772238), (43, 167772215), (64, 167772238), (69, 167772215), (91, 167772223)]
coconut89_water89 = [114, 0, 0, 0, 0, 10, 2, 11, 22, 12, 56, 63, 0, 0, 0, 7, 8, 145, 13, 9, 31, 10, 60, 26, 0, 0, 0, 6, 9, 31, 48, 88, 209, 19, 4, 18, 4, 40, 0, 0, 0, 0, 40, 0, 0, 0, 0, 10, 56, 21, 0, 0, 0, 6, 9, 31, 87, 88, 209, 19, 4, 18, 4, 40, 0, 0, 0, 0, 40, 0, 0, 0, 0, 10, 8, 23, 88, 12, 8, 7, 142, 105, 50, 187, 6, 32, 3, 2, 0, 0, 40, 0, 0, 0, 0, 42]
coconut98_addr = 0x1128 + 24

coconut25_meat25 = [(7, 167772223), (12, 67108874), (17, 100663318), (22, 167772224), (27, 67108875), (32, 100663318), (37, 167772225), (42, 67108876), (47, 100663318), (52, 167772226)]
coconut25_water25 = [2, 32, 3, 2, 0, 0, 40, 0, 0, 0, 0, 126, 0, 0, 0, 0, 40, 0, 0, 0, 0, 40, 0, 0, 0, 0, 126, 0, 0, 0, 0, 40, 0, 0, 0, 0, 40, 0, 0, 0, 0, 126, 0, 0, 0, 0, 40, 0, 0, 0, 0, 40, 0, 0, 0, 0, 57, 2, 0, 0, 0, 23, 42, 22, 42]
coconut52_addr = 0xea0 + 32

coconut46_meat46 = [(1, 100663326), (7, 100663314)]
coconut46_water46 = [40, 0, 0, 0, 0, 2, 40, 0, 0, 0, 0, 42]
coconut64_addr = 0x10bc + 33

coconut45_meat45 = [(1, 167772210 ), (7, 167772211 ), (13, 167772210),  (18, 1879048393), (23, 167772211),  (74, 16777218 ), (80, 167772227),  (88, 167772228),  (95, 167772229),  (102, 167772230), (108, 167772231), (113, 167772232), (121, 167772233), (133, 167772234), (142, 167772235), (151, 167772236), (161, 167772237), (181, 167772187), (196, 167772187), (211, 167772187), (224, 167772187), (230, 1879048427), (236, 167772212), (241, 100663308)]
coconut45_water45 = [40, 0, 0, 0, 0, 3, 111, 0, 0, 0, 0, 10, 40, 0, 0, 0, 0, 114, 0, 0, 0, 0, 111, 0, 0, 0, 0, 11, 2, 57, 7, 0, 0, 0, 2, 142, 58, 1, 0, 0, 0, 42, 6, 57, 7, 0, 0, 0, 6, 142, 58, 1, 0, 0, 0, 42, 7, 57, 7, 0, 0, 0, 7, 142, 58, 1, 0, 0, 0, 42, 2, 142, 105, 141, 0, 0, 0, 0, 12, 115, 0, 0, 0, 0, 13, 9, 6, 111, 0, 0, 0, 0, 9, 7, 111, 0, 0, 0, 0, 9, 9, 111, 0, 0, 0, 0, 9, 111, 0, 0, 0, 0, 111, 0, 0, 0, 0, 19, 4, 2, 115, 0, 0, 0, 0, 19, 5, 17, 5, 17, 4, 22, 115, 0, 0, 0, 0, 19, 6, 17, 6, 115, 0, 0, 0, 0, 19, 7, 17, 7, 111, 0, 0, 0, 0, 8, 22, 2, 142, 105, 111, 0, 0, 0, 0, 38, 221, 58, 0, 0, 0, 17, 7, 57, 7, 0, 0, 0, 17, 7, 111, 0, 0, 0, 0, 220, 17, 6, 57, 7, 0, 0, 0, 17, 6, 111, 0, 0, 0, 0, 220, 17, 5, 57, 7, 0, 0, 0, 17, 5, 111, 0, 0, 0, 0, 220, 9, 57, 6, 0, 0, 0, 9, 111, 0, 0, 0, 0, 220, 114, 0, 0, 0, 0, 8, 40, 0, 0, 0, 0, 40, 0, 0, 0, 0, 42]
coconut54_addr = 0xf54 + 16

coconut06_meat06 = [(1, 167772216), (9, 167772217), (24, 1879048331), (29, 167772218), (39, 100663304), (50, 167772219)]
coconut06_water06 = [40, 0, 0, 0, 0, 10, 18, 0, 40, 0, 0, 0, 0, 32, 206, 11, 0, 0, 60, 15, 0, 0, 0, 114, 0, 0, 0, 0, 40, 0, 0, 0, 0, 56, 6, 0, 0, 0, 40, 0, 0, 0, 0, 42, 32, 0, 92, 38, 5, 40, 0, 0, 0, 0, 43, 200]
coconut60_addr = 0xda4 + 28

coconut36_meat36 = [(1, 100663325), (7, 100663306), (13, 167772210), (19, 167772211), (25, 100663302), (31, 1879048293), (37, 167772212)]
coconut36_water36 = [40, 0, 0, 0, 0, 10, 40, 0, 0, 0, 0, 11, 40, 0, 0, 0, 0, 7, 111, 0, 0, 0, 0, 6, 40, 0, 0, 0, 0, 12, 114, 0, 0, 0, 0, 8, 40, 0, 0, 0, 0, 42]
coconut63_addr = 0xca8 + 12

coconut16_meat16 = [(1, 167772213), (9, 167772167), (14, 167772168), (19, 167772214), (26, 167772167), (31, 167772168), (36, 167772214), (41, 167772215)]
coconut16_water16 = [115, 0, 0, 0, 0, 10, 6, 24, 111, 0, 0, 0, 0, 111, 0, 0, 0, 0, 111, 0, 0, 0, 0, 6, 23, 111, 0, 0, 0, 0, 111, 0, 0, 0, 0, 111, 0, 0, 0, 0, 40, 0, 0, 0, 0, 42]
coconut61_addr = 0xd14 + 32

coconut26_meat26 = [(6, 16777250), (17, 16777250), (26, 16777218)]
coconut26_water26 = [32, 0, 1, 0, 0, 141, 0, 0, 0, 0, 10, 32, 0, 1, 0, 0, 141, 0, 0, 0, 0, 11, 3, 142, 105, 141, 0, 0, 0, 0, 12, 22, 13, 56, 18, 0, 0, 0, 6, 9, 2, 9, 2, 142, 105, 93, 145, 158, 7, 9, 9, 158, 9, 23, 88, 13, 9, 32, 0, 1, 0, 0, 50, 230, 22, 37, 19, 4, 13, 56, 40, 0, 0, 0, 17, 4, 7, 9, 148, 88, 6, 9, 148, 88, 32, 0, 1, 0, 0, 93, 19, 4, 7, 9, 148, 19, 5, 7, 9, 7, 17, 4, 148, 158, 7, 17, 4, 17, 5, 158, 9, 23, 88, 13, 9, 32, 0, 1, 0, 0, 50, 208, 22, 37, 13, 37, 19, 6, 19, 4, 56, 88, 0, 0, 0, 17, 6, 23, 88, 19, 6, 17, 6, 32, 0, 1, 0, 0, 93, 19, 6, 17, 4, 7, 17, 6, 148, 88, 19, 4, 17, 4, 32, 0, 1, 0, 0, 93, 19, 4, 7, 17, 6, 148, 19, 7, 7, 17, 6, 7, 17, 4, 148, 158, 7, 17, 4, 17, 7, 158, 7, 7, 17, 6, 148, 7, 17, 4, 148, 88, 32, 0, 1, 0, 0, 93, 148, 19, 8, 8, 9, 3, 9, 145, 17, 8, 97, 210, 156, 9, 23, 88, 13, 9, 3, 142, 105, 50, 162, 8, 42]
coconut62_addr = 0xb64 + 4

coconut_fixed_func(ASCIS_coconut_decrypt(coconut28_meat28, coconut28_water28), coconut82_addr, coconut82_addr + len(coconut28_water28))
coconut_fixed_func(ASCIS_coconut_decrypt(coconut15_meat15, coconut15_water15), coconut51_addr, coconut51_addr + len(coconut15_water15))
coconut_fixed_func(ASCIS_coconut_decrypt(coconut25_meat25, coconut25_water25), coconut52_addr, coconut52_addr + len(coconut25_water25))
coconut_fixed_func(ASCIS_coconut_decrypt(coconut89_meat89, coconut89_water89), coconut98_addr, coconut98_addr + len(coconut89_water89))
coconut_fixed_func(ASCIS_coconut_decrypt(coconut45_meat45, coconut45_water45), coconut54_addr, coconut54_addr + len(coconut45_water45))
coconut_fixed_func(ASCIS_coconut_decrypt(coconut46_meat46, coconut46_water46), coconut64_addr, coconut64_addr + len(coconut46_water46))
coconut_fixed_func(ASCIS_coconut_decrypt(coconut06_meat06, coconut06_water06), coconut60_addr, coconut60_addr + len(coconut06_water06))
coconut_fixed_func(ASCIS_coconut_decrypt(coconut36_meat36, coconut36_water36), coconut63_addr, coconut63_addr + len(coconut36_water36))
coconut_fixed_func(ASCIS_coconut_decrypt(coconut16_meat16, coconut16_water16), coconut61_addr, coconut61_addr + len(coconut16_water16))
coconut_fixed_func(ASCIS_coconut_decrypt(coconut26_meat26, coconut26_water26), coconut62_addr, coconut62_addr + len(coconut26_water26))


"""_summary_
water06 = 28 00 00 00 00 0a 12 00 28 00 00 00 00 20 ce 0b 00 00 3c 0f 00 00 00 72 00 00 00 00 28 00 00 00 00 38 06 00 00 00 28 00 00 00 
00 2a 20 00 5c 26 05 28 00 00 00 00 2b c8
Before: 28 38 00 00 0a 0a 12 00 28 39 00 00 0a 20 ce 0b 00 00 3c 0f 00 00 00 72 8b 00 00 70 28 3a 00 00 0a 38 06 00 00 00 28 08 00 00 
06 2a 20 00 5c 26 05 28 3b 00 00 0a 2b c8
After: 28 38 00 00 0a 0a 12 00 28 39 00 00 0a 20 e3 07 00 00 3c 0f 00 00 00 72 8b 00 00 70 28 3a 00 00 0a 38 06 00 00 00 28 08 00 00 
06 2a 20 00 5c 26 05 28 3b 00 00 0a 2b c8
"""