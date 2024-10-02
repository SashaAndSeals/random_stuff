import random
import math
letters = {"a": [47, 79, 13, 18, 33, 85, 89], "b": [4, 56, 107, 5, 35, 83, 97],
           "c": [20, 55, 24, 27, 29, 48, 112, 6, 17, 58, 96, 98], "d": [105, 110, 66], "e": [63, 68, 99],
           "f": [87, 26, 9, 114, 100], "g": [32, 64], "h": [1, 2, 72, 80, 108, 67], "i": [77, 49, 53], "j": [31],
           "k": [19, 36], "l": [3, 71, 103, 116, 57], "m": [12, 25, 42, 109, 115, 101],
           "n": [11, 28, 41, 7, 10, 113, 60], "o": [76, 8], "p": [46, 78, 82, 84, 59, 61, 91, 94], "q": [118],
           "r": [37, 88, 44, 45, 75, 104, 111, 86], "s": [38, 21, 106, 14, 16, 34, 50, 51, 62],
           "t": [22, 43, 73, 52, 81, 117, 65, 69, 90], "u": [92], "v": [23], "w": [74],
           "x": [54], "y": [39, 70], "z": [30, 40]}
while 1:
    operation = input("Encode or decode? ")
    while operation != "encode" and operation != "decode":
        print("Please type in 'encode' or 'decode' (without the ')")
        operation = input("Encode or decode? ")
    if operation == "encode":
        data_in = input("Message to encode: ").lower()
        data_out = ""
        for letter in data_in:
            if letter in letters.keys():
                a = random.choice(letters[letter])
                b = random.randrange(2, 10)
                if b == 9:
                    b_push = 0
                else:
                    b_push = random.randrange(0, 9-b)
                c = ""
                d = 1
                e = 0
                while True:
                    f = math.floor((a % (d * b)) / d)
                    e += f*d
                    c = str(f)+c
                    d *= b
                    if d > a:
                        break
                data_out += str(b_push) + str(b-1+b_push) + c + " "
            else:
                if letter == " ":
                    data_out += " "
                else:
                    data_out += letter + " "
        print(data_out)
    elif operation == "decode":
        data_in = input("Message to decode (separate numbers by spaces):").split(" ")
        data_out = ""
        for num in data_in:
            if not num == "":
                if num[0] in "0123456789":
                    a = 0
                    b = 1
                    c = int(num[1]) - int(num[0]) + 1
                    for i in range(len(num)-2):
                        a += int(num[-(i+1)])*b
                        b *= c
                    for vals in letters.values():
                        for val in vals:
                            if val == a:
                                data_out += list(letters.keys())[list(letters.values()).index(vals)]
                else:
                    data_out += num
            else:
                data_out += " "
        print(data_out)

