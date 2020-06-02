secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
x = len(secret)
max_key = 26
cipher = 7
result = ""

while len(secret) != len(result):
    for char in secret:
        if char.isupper() == True:
            count = ord(char) + cipher
            if count > 90:
                count = count - 26
                encr_ltr = chr(count)
                result += encr_ltr
            else:
                encr_ltr = chr(count)
                result += encr_ltr
        if char.islower() == True:
            count = ord(char) + cipher
            if count > 122:
                count = count - 26
                encr_ltr = chr(count)
                result += encr_ltr
            else:
                encr_ltr = chr(count)
                result += encr_ltr
        elif char.isupper() is False or char.lower() is False:
            result += char
print("Encrypted message is: \n" + result)