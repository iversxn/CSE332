def convertBinToHex(bin):
    hex =" "
    if bin == "0000":
        hex = "0"
    elif bin == "0001":
        hex = "1"
    elif bin == "0010":
        hex = "2"
    elif bin == "0011":
        hex = "3"
    elif bin == "0100":
        hex = "4"
    elif bin == "0101":
        hex = "5"
    elif bin == "0110":
        hex = "6"
    elif bin == "0111":
        hex = "7"
    elif bin == "1000":
        hex = "8"
    elif bin == "1001":
        hex = "9"
    elif bin == "1010":
        hex = "A"
    elif bin == "1011":
        hex = "B"
    elif bin == "1100":
        hex = "C"
    elif bin == "1101":
        hex = "D"
    elif bin == "1110":
        hex = "E"
    elif bin == "1111":
        hex = "F"
    return hex

def binaryToHex(binary):
    # Make sure the binary string length is a multiple of 4
    while len(binary) % 4 != 0:
        binary = '0' + binary
    
    hex_result = ""
    for i in range(0, len(binary), 4):
        hex_digit = convertBinToHex(binary[i:i+4])
        hex_result += hex_digit
    
    return hex_result.strip()

def checkInstruction(inst):
    convertInstruction = " "
    if inst == "add":
        convertInstruction = "0000"
    elif  inst == "nand":
        convertInstruction = "0000"
    elif  inst == "nor":
        convertInstruction = "0000"
    elif  inst == "slt":
        convertInstruction = "0000"
    elif  inst == "subi":
        convertInstruction = "0001"
    elif inst == "ori":
        convertInstruction = "0010"
    elif inst == "beq":
        convertInstruction = "0011"
    elif inst == "lw":
        convertInstruction = "0100"
    elif inst == "sw":
        convertInstruction = "0101"
    elif inst == "j":
        convertInstruction = "1000"
    else:
        convertInstruction = "Invalid instructions"
    return convertInstruction


def checkRegister(reg):
    
    convertReg = ""
    if  reg == "r0": 
        convertReg ="0000" 
    elif reg == "r1":
        convertReg ="0001"
    elif reg == "r2":
        convertReg ="0010"
    elif reg == "r3":
        convertReg ="0011"
    elif reg == "r4":
        convertReg ="0100"
    elif reg == "r5":
        convertReg ="0101"
    elif reg == "r6":
        convertReg ="0110"
    elif reg == "r7":
        convertReg ="0111"
    elif reg == "r8":
        convertReg ="1000"
    elif reg == "r9":
        convertReg ="1001"
    elif reg == "r10":
        convertReg ="1010"
    elif reg == "r11":
        convertReg ="1011"
    elif reg == "r12":
        convertReg ="1100"
    elif reg == "r13":
        convertReg ="1101"
    elif reg == "r14":
        convertReg ="1110"
    elif reg == "r15":
        convertReg ="1111"
    else:
        convertReg ="Invalid Register"
        
    return convertReg

def decimalToBinary(num, bits=6):
    """Convert a decimal number to binary with specified bits"""
    if(num < 0):
        # Handle negative numbers using 2's complement
        num = (1 << bits) + num
    
    # Convert to binary and remove '0b' prefix
    binary = bin(num)[2:]
    
    # Zero-pad to reach the required bit length
    binary = binary.zfill(bits)
    
    # Ensure we only return the least significant 'bits'
    return binary[-bits:]

readf = open("inputs","r")
writef = open("outputs","w")
writef.write("v2.0 raw\n")

for i in readf:
    splitted = i.split()
    
    if(splitted[0] == "add"):
        conv_inst = checkInstruction(splitted[0])
        conv_rd = checkRegister(splitted[1])
        conv_rs = checkRegister(splitted[2])
        conv_rt = checkRegister(splitted[3])

        binary = conv_inst + conv_rs + conv_rt + conv_rd + "00"
        hex_output = binaryToHex(binary)
        print(f"Binary: {binary}, Hex: {hex_output}")
        writef.write(hex_output+"\n")

    elif(splitted[0] == "nand"):
        conv_inst = checkInstruction(splitted[0])
        conv_rd = checkRegister(splitted[1])
        conv_rs = checkRegister(splitted[2])
        conv_rt = checkRegister(splitted[3])

        binary = conv_inst + conv_rs + conv_rt + conv_rd + "01"
        hex_output = binaryToHex(binary)
        print(f"Binary: {binary}, Hex: {hex_output}")
        writef.write(hex_output+"\n")

    elif(splitted[0] == "nor"):
        conv_inst = checkInstruction(splitted[0])
        conv_rd = checkRegister(splitted[1])
        conv_rs = checkRegister(splitted[2])
        conv_rt = checkRegister(splitted[3])

        binary = conv_inst + conv_rs + conv_rt + conv_rd + "10"
        hex_output = binaryToHex(binary)
        print(f"Binary: {binary}, Hex: {hex_output}")
        writef.write(hex_output+"\n")

    elif(splitted[0] == "slt"):
        conv_inst = checkInstruction(splitted[0])
        conv_rd = checkRegister(splitted[1])
        conv_rs = checkRegister(splitted[2])
        conv_rt = checkRegister(splitted[3])

        binary = conv_inst + conv_rs + conv_rt + conv_rd + "11"
        hex_output = binaryToHex(binary)
        print(f"Binary: {binary}, Hex: {hex_output}")
        writef.write(hex_output+"\n")

    elif(splitted[0] == "lw" or splitted[0] == "sw" or splitted[0] == "beq" or splitted[0] == "subi" or splitted[0] == "ori"):
        conv_inst = checkInstruction(splitted[0])
        conv_rs = checkRegister(splitted[1])
        conv_rt = checkRegister(splitted[2])
        conv_im = decimalToBinary(int(splitted[3]))

        binary = conv_inst + conv_rs + conv_rt + conv_im
        hex_output = binaryToHex(binary)
        print(f"Binary: {binary}, Hex: {hex_output}")
        writef.write(hex_output+"\n")  
     
    elif(splitted[0] == "j"):
        conv_inst = checkInstruction(splitted[0])
        
        # Get target address as a number
        target_value = int(splitted[1])
        
        # Convert target address to 14-bit binary
        target_binary = decimalToBinary(target_value, bits=14)
        
        # Combine instruction and target
        binary = conv_inst + target_binary
        
        # Convert to hex
        hex_output = binaryToHex(binary)
        
        print(f"Binary: {binary}, Hex: {hex_output}")
        writef.write(hex_output+"\n")
