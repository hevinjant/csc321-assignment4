import hashlib
from bcrypt import *
from nltk.corpus import words
import multiprocessing

class user():
    name = ""
    fullhash = b''

    # “Bilbo:$2b$08$L.z8uq99JkFAvX/Q1jGRI.TzrHIIxWMoRi/VzO1sj/UvVFPgW8dW.”
    def parse(self, string):
        split = str(string).split(":")
        self.name = split[0]
        self.fullhash = bytes(split[1].removesuffix("\\r\\n").removesuffix("'"), 'ascii')
        index = split[1].rfind("$") + 23
        self.salt = bytes(split[1][:index], 'ascii')
        self.hsh = bytes(split[1][index:].removesuffix("\\r\\n'").removesuffix("'"), 'ascii')
        return self

    def print(self):
        print(self.name)
        print(self.fullhash)
        print(self.salt)
        print(self.hsh)

    def check(self, word):
        if checkpw(word, self.fullhash):
            file = open("out.txt", "a")
            print("Found pass for '" + self.name + "':\t" + str(word))
            file.write("Found pass for '" + self.name + "':\t" + str(word))
            file.close
            return True
            
def check(trip):
    word = trip[0]
    salts = trip[1]
    hashsets = trip[2]
    for i in range(len(salts)):
        h = hashpw(word, salts[i])
        if h in hashsets[i]:
            file = open("out.txt", "a")
            print("Found pass: '" + str(h) + "':\t" + str(trip[0]))
            file.write("Found pass: '" + str(h) + "':\t" + str(trip[0]) + "\n")
            file.close()

def main():
    print("TASK 2:")
    file = open("shadow.txt", "rb")
    hss = list()
    salts = list()

    # hashes = set()
    bilbo = user().parse(file.readline()) # welcome
    gandalf = user().parse(file.readline()) # wizard
    thorin = user().parse(file.readline()) # diamond
    # salts.append(bilbo.salt)
    # hashes.add(bilbo.fullhash)
    # hashes.add(gandalf.fullhash)
    # hashes.add(thorin.fullhash)
    # hss.append(hashes)

    # hashes = set()
    Fili = user().parse(file.readline()) # desire
    Kili = user().parse(file.readline()) # ossify
    # salts.append(Fili.salt)
    # hashes.add(Fili.fullhash)
    # hashes.add(Kili.fullhash)
    # hss.append(hashes)

    # hashes = set()
    Balin = user().parse(file.readline()) # hangout
    Dwalin = user().parse(file.readline()) # drossy
    Oin = user().parse(file.readline()) # ispaghul
    # salts.append(Balin.salt)
    # hashes.add(Balin.fullhash)
    # hashes.add(Dwalin.fullhash)
    # hashes.add(Oin.fullhash)
    # hss.append(hashes)

    # hashes = set()
    Gloin = user().parse(file.readline()) # oversave
    Dori = user().parse(file.readline()) # indoxylic
    Nori = user().parse(file.readline()) # swagsman
    # salts.append(Gloin.salt)
    # hashes.add(Gloin.fullhash)
    # hashes.add(Dori.fullhash)
    # hashes.add(Nori.fullhash)
    # hss.append(hashes)

    # hashes = set()
    Ori = user().parse(file.readline()) # airway
    Bifur = user().parse(file.readline()) # corrosible
    Bofur = user().parse(file.readline()) # libellate
    # salts.append(Ori.salt)
    # hashes.add(Ori.fullhash)
    # hashes.add(Bifur.fullhash)
    # hashes.add(Bofur.fullhash)
    # hss.append(hashes)

    # hashes = set()
    Durin = user().parse(file.readline()) # purrone
    # salts.append(Durin.salt)
    # hashes.add(Durin.fullhash)
    # hss.append(hashes)
    
    
    #passwords = [(bytes(w, 'ascii'), salts, hss) for w in words.words() if 6 <= len(w) <= 10]
    passwords = [bytes(w, 'ascii') for w in words.words() if 6 <= len(w) <= 10]
    print("Checking " + str(len(passwords)) + " passwords")
    Durin.print()
    p = multiprocessing.Pool(12)

    p.map(Durin.check, passwords)
    

if __name__ == "__main__":
    main()