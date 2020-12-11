#read text from a url
def read_url_txt(url):
    import urllib.request
    file = urllib.request.urlopen(url)

    s = ""
    for line in file:
    	s = s + line.decode()
    return s

s = read_url_txt("https://projecteuler.net/project/resources/p059_cipher.txt")
List = s.split(",")

start = 97
end = 122

def xor_decrypt_check(List, key):
    for x in range(len(List)):
        v = int(List[x]) ^ key[x % 3]
        if v < 32 or v > 122:
            return False
    return True

def xor_decrypt_check(List, key):
    for x in range(len(List)):
        v = int(List[x]) ^ key[x % 3]
        if v < 32 or v > 122:
            return False
    return True

def xor_decrypt(List,key):
    new_List =[]
    for x in range(len(List)):
        v = int(List[x]) ^ key[x % 3]
        new_List.append(v)
    return new_List

def decrypt_to_text(List):
    s = ""
    for x in List:
        s = s + chr(x)
    return s

def sum_decrypt(List, key):
    sum = 0
    for x in range(len(List)):
        v = int(List[x]) ^ key[x % 3]
        sum += v
    return sum

#Find all the key which can decrypt (8 possible keys)
# right_key = []
# for i in range(start, end + 1):
#     for j in range(start, end + 1):
#         for k in range(start, end + 1):
#             key = [i,j,k]
#             if xor_decrypt_check(List, key) == True:
#                 right_key.append(key)


key1 = [101, 120, 112]
print(sum_decrypt(List, key1))

#D_list = xor_decrypt(List, right_key)
