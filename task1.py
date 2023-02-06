import sys
import hashlib
import time
from collections import defaultdict
#from bitstring import BitArray

def getSHA256(s):
    return hashlib.sha256(s.encode()).digest()

def bytesToBin(bytes):
    return bin(int.from_bytes(bytes, byteorder=sys.byteorder))[2:]

def getHammingDistanceOfOne(s):
    lastChar = chr((ord(s[len(s)-1:].upper())+1 - 65) % 26 + 65).lower() # get the next alphabet
    res = s[:len(s)-1]
    return res + lastChar

def getCollision():
    s = "agfas678adw23"
    results = []

    for i in range(8, 52, 2):
        d = defaultdict(lambda: False)
        count = 0
        hash = bytesToBin(getSHA256(s))[:i]
        # print("HASH #1: ", hash)

        startTime = time.time()
        while True:
            if d[hash]:
                break
            d[hash] = True
            count += 1
            hash = bytesToBin(getSHA256(s + str(count)))[:i]
            # print("HASH #2: ", hash)
        endTime = time.time()

        result = {"hash_size": i, "inputs": count, "time":endTime - startTime}
        results.append(result)
        print("Hash size: ", i, "bits | Total inputs: ", count , " | Time it takes for collision: ", endTime - startTime, "seconds")

def main():
    # task 1-a
    # userInput = input("Enter any string for part 1-a: ")
    # print("Hash: ", getSHA256(userInput))
    # print()

    # task 1-b
    # for i in range(3):
    #     userInput = input("Enter string #" + str(i+1) + " for part 1-b: ")
    #     shd = getHammingDistanceOfOne(userInput)
    #     print("One Hamming Distance string: ", shd)
    #     print("Original String Hash: ", getSHA256(userInput))
    #     print("String with one Hamming Distance Hash: ", getSHA256(shd))
    #     print()

    # task 1-c
    getCollision()


if __name__ == "__main__":
    main()