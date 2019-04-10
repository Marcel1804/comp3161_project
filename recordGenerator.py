from itertools import permutations
from random import randint
import datetime
import sqlGen
import random
import string
import sys


#CustomerAccount(acc_id, email, password,  fname, lname, gender, date_of_birth, street, city, parish, telephone, created_on)
def generateBirthday():
    date = datetime.date(randint(1920,2003), randint(1,12),randint(1,28))
    return date

def generateDate():
    date = datetime.date(randint(2000,2018), randint(1,12),randint(1,28))
    return date

def phoneNumber():
    p=list('0000000000')
    p[0] = str(random.randint(1,9))
    for i in [1,2,6,7,8]:
        p[i] = str(random.randint(0,9))
    for i in [3,4]:
        p[i] = str(random.randint(0,8))
    if p[3]==p[4]==0:
        p[5]=str(random.randint(1,8))
    else:
        p[5]=str(random.randint(0,8))
    n = range(10)
    if p[6]==p[7]==p[8]:
        n = (i for i in n if i!=p[6])
    p[9] = str(random.choice(n))
    p = ''.join(p)
    return p[:3] + '-' + p[3:6] + '-' + p[6:]

def generateCustomers():
    #f = open("customers.txt", "r")
    #n = sqlGen.databaseGenerator("CompuStore", sqlGen.columns)
    #name = permutations([1, 2, 3])
    #n.addRecord([], "CustomerAccount")
    p = phoneNumber()
    print(generateName(), generateName(), getGender() , p, generateDate())

def getGender():
    lst = ["Male", "Female"]
    return random.choice(lst)

def generateName():
    vowels = "aeiou"
    consonants = "".join(set(string.ascii_lowercase) - set(vowels))
    word = ""
    l    = [5,6,7,8]
    for i in range(random.choice(l)):
        if i % 2 == 0:
            word += random.choice(consonants)
        else:
            word += random.choice(vowels)
        word    = list(word)
        word[0] = word[0].upper()
        word    = "".join(word)
    return word

if __name__ == "__main__":
    print(generateCustomers())