'''
Hash
    - similar to python dictionary
    - fixed size of elems
    - has some methods
'''

class HashTable():

    def __init__(self, size=17):
        self. size = size
        self.stored_keys = [None] * self.size
        self.stored_values = [None] * self.size
    

    def insert(self, key, value):
        # Insert key-val pair or overwrites and existing one"
        hash_val = self._hash(key)

        # insert new key if it does not exist
        if self.stored_keys[hash_val] is None:
            self.stored_keys[hash_val] = key
            self.stored_values[hash_val] = value
        
        # overwrite key if it already exists
        else:
            if self.stored_keys[hash_val] == key:
                self.stored_values[hash_val] = value

            # collision
            elif len(self.keys()) == self.size:
                raise ValueError("Hash table is full")
            
            else:
                next_hash = self._rehash(hash_val)

                while(self.stored_keys[next_hash] is not None 
                and self.stored_keys[next_hash] != key):
                    next_hash = self._rehash(next_hash)

                # insert new key if it does not exist
                if self.stored_keys[next_hash] is None:
                    self.stored_keys[next_hash] = key
                    self.stored_values[next_hash] = value
                
                # overwrite key if already exist
                else:
                    self.stored_values[next_hash] = value
                    

    def __setitem__(self, key, value):
        return self.insert(key, value)
    

    def get(self, key):
        # Retrieve the value corresponding to the key
        hash_val = self._hash(key)
        if self.stored_keys[hash_val] == key:
            return self.stored_values[hash_val]

        elif self.stored_keys[hash_val] is None:
            return KeyError(key)
        else:
            next_hash = self._rehash(hash_val)
            while self.stored_keys[next_hash] != key:
                next_hash = self._rehash(next_hash)

                if next_hash == hash_val:
                    return KeyError(key)
                elif self.stored_keys[next_hash] is None:
                    return KeyError(key)
            
            return self.stored_values[next_hash]

    def __getitem__(self, key):
        return self.get(key)
    

    def keys(self):
        # Get all keys from hash table
        return [k for k in self.stored_keys if k is not None]
    
    def _hash(self, key):
        # Computer hash position
        if isinstance(key, str):
            key = sum(ord(c) for c in key)
        
        position = key % hash_table_size
        return position

    def _rehash(self, previous_hash):
        # Find the next hash for linear probing, whats probing!?
        return (previous_hash + 1) % self.size        


'''
For collision use linear probing
    - if new key hashes to same position, increase old hash by a skip
    constant and check if slot empyt, if not repeat step until next
    empty slot is found and insert new key in that slot.
    This is "rehashing".


For look ups, we do this
    - Check the key in the hash table that maps to the hash value of a 
    key we want to look up
        * If keys are identical, return the value
        * Else, go through the hash table using "rehashing" look up key
        is found or return None if an empyty solot was found

Implement reshashing will skip constant 1.
'''

hash_table_size = 17

hashtable = HashTable()
# add key values
#hashtable["abc"] = 1
# print all keys
#print(hashtable.keys())
# print hash position
#print(hashtable._hash('abc'))
#print(hashtable._hash('abcdefgh')) # same position as "abc" (collision)

hashtable = HashTable()
hashtable['abc'] = 1
hashtable['xyz'] = 2
hashtable['abcdefgh'] = 3

print(hashtable['abc'])



