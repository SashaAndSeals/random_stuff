import math
import random
# v KEEP THIS LINE IN ITS POSITION
PASSWORD = None
# ^ KEEP THIS LINE IN ITS POSITION
letters = {"a": [47, 79, 13, 18, 33, 85, 89], "b": [4, 56, 107, 5, 35, 83, 97],
           "c": [20, 55, 24, 27, 29, 48, 112, 6, 17, 58, 96, 98], "d": [105, 110, 66], "e": [63, 68, 99],
           "f": [87, 26, 9, 114, 100], "g": [32, 64], "h": [1, 2, 72, 80, 108, 67], "i": [77, 49, 53], "j": [31],
           "k": [19, 36], "l": [3, 71, 103, 116, 57], "m": [12, 25, 42, 109, 115, 101],
           "n": [11, 28, 41, 7, 10, 113, 60], "o": [76, 8], "p": [46, 78, 82, 84, 59, 61, 91, 94], "q": [118],
           "r": [37, 88, 44, 45, 75, 104, 111, 86], "s": [38, 21, 106, 14, 16, 34, 50, 51, 62],
           "t": [22, 43, 73, 52, 81, 117, 65, 69, 90], "u": [92], "v": [23], "w": [74],
           "x": [54], "y": [39, 70], "z": [30, 40]}


def encode(data_in):
    data_in = data_in.lower()
    data_out = ""
    for letter in data_in:
        if letter in letters.keys():
            a = random.choice(letters[letter])
            b = random.randrange(2, 10)
            if b == 9:
                b_push = 0
            else:
                b_push = random.randrange(0, 9 - b)
            c = ""
            d = 1
            e = 0
            while True:
                f = math.floor((a % (d * b)) / d)
                e += f * d
                c = str(f) + c
                d *= b
                if d > a:
                    break
            data_out += str(b_push) + str(b - 1 + b_push) + c + " "
        else:
            if letter == " ":
                data_out += " "
            elif letter in "0123456789":
                data_out += "#" + letter + " "
            else:
                data_out += letter + " "
    return data_out[0:-1]


def decode(data_in):
    data_in = data_in.split(" ")
    data_out = ""
    for num in data_in:
        if not num == "":
            if num[0] in "0123456789":
                a = 0
                b = 1
                c = int(num[1]) - int(num[0]) + 1
                for i in range(len(num) - 2):
                    a += int(num[-(i + 1)]) * b
                    b *= c
                for vals in letters.values():
                    for val in vals:
                        if val == a:
                            data_out += list(letters.keys())[list(letters.values()).index(vals)]
            else:
                if num[0] == "#":
                    data_out += num[1:len(num)]
                else:
                    data_out += num
        else:
            data_out += " "
    return data_out


file_ = open("./"+__file__+".py", "r")
file_data = file_.read().splitlines()
file_.close()
del file_

if PASSWORD is None:
    file_data[3] = 'PASSWORD = "' + encode(input("SET PASSWORD: ")) + '"'
    file_write = ""
    for i in range(len(file_data)):
        file_write += file_data[i] + "\n"
    file_ = open("./"+__file__+".py", "w")
    file_.write(file_write)
    file_.close()
    del file_
else:
    if decode(PASSWORD) != input("ENTER PASSWORD:").lower():
        print("WRONG PASSWORD!")
        quit()

while 1:
    operation = input("ENCODE, DECODE OR RESET PASSWORD? ").lower()
    while operation != "encode" and operation != "decode" and operation != "reset password":
        print("PLEASE TYPE IN 'ENCODE', 'DECODE' OR 'RESET PASSWORD' (WITHOUT THE ')")
        operation = input("ENCODE, DECODE OR RESET PASSWORD? ").lower()
    if operation == "encode":
        print(encode(input("MESSAGE TO ENCODE: ")))
    elif operation == "decode":
        print(decode(input("MESSAGE TO DECODE (SEPARATE NUMBERS BY SPACES):")))
    elif operation == "reset password":
        file_data[3] = 'PASSWORD = "' + encode(input("SET PASSWORD: ")) + '"'
        file_write = ""
        for i in range(len(file_data)):
            file_write += file_data[i] + "\n"
        file_ = open("./"+__file__+".py", "w")
        file_.write(file_write)
        file_.close()
        del file_

