'''Hash function(Remainder method) - 
remainder of key when divide by size of hash table''' 

# for integers
hash_table_size = 17
key = 123456
position = key % hash_table_size
print("Position in hash table is {}".format(position))

# for strings

hash_table_size = 17
string_key = 'abcdef'
key = sum(ord(c) for c in string_key)
position = key % hash_table_size
print('Position in the hash table:', position)
