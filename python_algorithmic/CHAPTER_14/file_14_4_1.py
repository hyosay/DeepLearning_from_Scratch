Full_name = input("영문이름을 입력하시요.")

space_pos = Full_name.find(" ")

name1 = Full_name[:space_pos]
name2 = Full_name[space_pos + 1:]

rev_name = name2 + " " + name1
print(rev_name)

#file_14_4_2
import random

last_name = input("당신의 이름을 입력하시요")
random_int = random.randrange(100,1000)

print("ID : " + last_name[:4].upper() + str(random_int))

#file_14_4_3a

import string
alphabet = string.ascii_uppercase

random_word = alphabet[random.randrange(26)]+   \
              alphabet[random.randrange(26)]+   \
              alphabet[random.randrange(26)]+   \
              alphabet[random.randrange(26)]

rnadom_word1 =  alphabet[random.randrange(len(alphabet))]+   \
                alphabet[random.randrange(len(alphabet))]+   \
                alphabet[random.randrange(len(alphabet))]+   \
                alphabet[random.randrange(len(alphabet))]+   \
print(random_word)