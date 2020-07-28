#   Date    :   Monday, 9th March 2020
#   Nama    :   Kevin Akbar Adhiguna

# Fungsi memetakan string diantara dua karakter
def antara(nilai, a, b):
    # Menemukan string sebelumnya
    pos_a = nilai.find(a)
    if pos_a == -1: return ""
    # Menemukan string setelahnya
    pos_b = nilai.rfind(b)
    if pos_b == -1: return "" 
    # Mengembalikan bagian tengah
    adjusted_pos_a = pos_a + len(a)
    if adjusted_pos_a >= pos_b: return ""
    return nilai[adjusted_pos_a:pos_b]

# Fungsi memetakan string sebelum sebuah karakter
def depan(nilai, a):
    # Menemukan string sebelumnya
    pos_a = nilai.find(a)
    if pos_a == -1: return ""
    # Mengembalikan nilai(slice) dari index ke-0 hingga indeks awal variabel
    return nilai[0:pos_a]

# Fungsi memetakan string setelah sebuah karakter
def belakang(nilai, a):
    # Menemukan string setelahnya
    pos_a = nilai.rfind(a)
    if pos_a == -1: return ""
    # Mengembalikan nilai setelah string ditemukan
    adjusted_pos_a = pos_a + len(a)
    if adjusted_pos_a >= len(nilai): return ""
    return nilai[adjusted_pos_a:]

# Input uri
uri = input("URI: ")

scheme = depan(uri,":") # scheme ada sebelum karakter ":"
authority = antara(uri,"//","/") # authority berada diantara "//" dan "/"
query = antara(uri,"?","#") # query berada diantara "?" dan "#" 
fragment = belakang(uri,"#") # fragment ada setelah karakter "#"
path = antara(uri,authority,query) #path berada diantara authority dan query

print("scheme : "+ scheme)
print("authority : "+ authority)
print("path : "+ path)
print("query : "+ query)
print("fragment : "+ fragment)
