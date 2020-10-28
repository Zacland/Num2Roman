# Roman Numeral > 4000 : https://www.math-salamanders.com/roman-numerals-list.html

def  intToRoman(nombre):
    val = [
        1000000, 900000, 500000, 400000,
        100000, 90000, 50000, 40000,
        10000, 9000, 5000, 4000,
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "/M", "/C/M", "/D", "/C/D",
        "/C", "/X/C", "/L", "/X/L",
        "/X", "M/X", "/V", "M/V",
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    romanNum = ''
    i = 0
    while nombre > 0:
        for _ in range(nombre // val[i]):
            romanNum += syb[i]
            nombre -= val[i]
        i += 1
    return romanNum

def main():
    print(f"4 = {intToRoman(4)}")               # IV
    print(f"49 = {intToRoman(49)}")             # XLIX
    print(f"789 = {intToRoman(789)}")           # DCCLXXXIX
                                                #  _
    print(f"4896 = {intToRoman(4896)}")         # MVDCCCXCVI
                                                #  _
    print(f"9999 = {intToRoman(9999)}")         # MXCMXCIX
                                                # __
    print(f"16897 = {intToRoman(16897)}")       # XVMDCCCXCVII
                                                # __
    print(f"42000 = {intToRoman(42000)}")       # XLMM
                                                # _
    print(f"52874 = {intToRoman(52874)}")       # LMMDCCCLXXIV
                                                # ____
    print(f"241365 = {intToRoman(241365)}")     # CCXLMCCCLXV
                                                # _______
    print(f"845620 = {intToRoman(845620)}")     # DCCCXLVDCXX

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


