# Convert binary array to string

# '''Function to converting binary array to String'''

def bits2str(b):
    NumOfChar = int(len(b)/7)
    string = ''
    for i in range(NumOfChar):
        # 7 digits represents 1 char
        bitsChar = ''.join(str(j) for j in bitsArray[7*i:7*i+7])
    decimalChar = int(bitsChar, 2)  # convert binary to decimal
    string = string + chr(decimalChar)  # convert decimal to string
    return string
