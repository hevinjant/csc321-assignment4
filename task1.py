import hashlib
#from bitstring import BitArray

def getSHA256(s):
    return hashlib.sha256(s.encode()).digest()

def bytesToBin(bytes):
    return bin(int(bytes, base=16))[2:]

def getHammingDistanceOfOne(s):
    lastChar = chr((ord(s[len(s)-1:].upper())+1 - 65) % 26 + 65).lower() # get the next alphabet
    res = s[:len(s)-1]
    return res + lastChar

def main():
    print("TASK 1:")

    # task 1-a
    userInput = input("Enter any string for part 1-a: ")
    print("Hash: ", getSHA256(userInput))
    print()

    # task 1-b
    for i in range(3):
        userInput = input("Enter string #" + str(i+1) + " for part 1-b: ")
        shd = getHammingDistanceOfOne(userInput)
        print("One Hamming Distance string: ", shd)
        print("Original String Hash: ", getSHA256(userInput))
        print("String with one Hamming Distance Hash: ", getSHA256(shd))
        print()

    # task 1-c



if __name__ == "__main__":
    main()