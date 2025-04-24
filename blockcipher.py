
n = 8

print(f"text length (mod 8) | number of padding bytes added | value of each padding byte")
for x in range(n):
  print(f" {x}  {n-x}   0x{n-x} ")
  # print(f"\n")




msg1 = input("Enter message: ")

padding_byte = len( list(msg1) )
padd = 8 - padding_byte
print(f"message length: {  padding_byte  } | 0x{padd}")

# print( list(msg1)[0] , list(msg1)[1] , list(msg1)[2], list(msg1)[3] )

full_padd = [] 

for n in range(padding_byte):
  p1 = list(msg1)[n]
  # print( p1 )
  full_padd.append(p1)

for x in range(padd,8):
  # print(f" 0x{padd}", end=' ')
  p2 = f"0x{padd}"
  full_padd.append(p2)

print(full_padd)
print(f"text length: {len( full_padd) }")
print('\n')