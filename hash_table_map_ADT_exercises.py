## 4) Implement the len method (__len__) for
##the hash table Map ADT implementation. DONE
## 5) Implement the in method (__contains__) for the hash
##table Map ADT implementation.
## 6) Implement the del method for the HashTable class.
## -collision resolution cases: chaining/open add., special cases
## 7) Re-implement the put method so that the table will
##automatically resize itself when the loading factor reaches
##a predetermined value (i'll choose 0.7)
## 8) Implement quadratic probing for rehash

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.quadRehashCount = 1

    def put(self,key,data): #7.
        #resizing when load factor > 0.7
        loadF = self.__len__() / len(self.slots)
        if (loadF > 0.7):
            #will resize by 10 more slots
            self.size += 10
            self.slots += ([None] * 10)
            self.data += ([None] * 10)
              
        hashvalue = self.hashfunction(key,len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
              self.data[hashvalue] = data  #replace
            else:
              nextslot = self.rehash(hashvalue,len(self.slots))
              while self.slots[nextslot] != None and \
                              self.slots[nextslot] != key:
                nextslot = self.rehash(nextslot,len(self.slots))

              if self.slots[nextslot] == None:
                self.slots[nextslot]=key
                self.data[nextslot]=data
              else:
                self.data[nextslot] = data #replace

    def hashfunction(self,key,size):
         return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def get(self,key):
      startslot = self.hashfunction(key,len(self.slots))

      data = None
      stop = False
      found = False
      position = startslot
      while self.slots[position] != None and  \
                           not found and not stop:
         if self.slots[position] == key:
           found = True
           data = self.data[position]
         else:
           position=self.rehash(position,len(self.slots))
           if position == startslot:
               stop = True
      return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)

    def __len__(self): #4.
        length = 0
        for i in range(self.size):
            if self.slots[i] != None:
                length += 1
        return length

    def __contains__(self, key): #5. (just key, not payload)
        x = self.get(key)
        if x == None:
            return False
        else:
            return True

    def __del__(self, key):
        #for open addressing case
        #normal case deletion:
        slot = self.hashfunction(key,len(self.slots))
        if self.slots[slot] == key:
            self.slots[slot] = None
            self.data[slot] = None
            print("Sucessful deletion.")
            return
        #hash collision linear probe deletion:
        else:
            for i in range(self.size):
                slot = self.rehash(slot, self.size)
                if self.slots[slot] == None:
                    print("Item surely not in table. No deletion.")
                    return
                elif self.slots[slot] == key:
                    self.slots[slot] = None
                    self.data[slot] = None
                    print("Sucessful deletion.")
                    return
            print("Table full, and nothing deleted.")
            return

        #for chaining resolution case
            #will skip, but psuedo-code:
            #each hash/data slot pair contains lists
            #get hash value to get the the slot that contains list
            #assuming it's there, get to list idx with key
            #delete key at that index, along with value at index in data slot

    def quadRehash(self, oldhash, size):
        #to use, must update put()
        #if a 2nd quadRehash is needed, then quadRehashCount += 1
        #once the quadRehash is successful, set quadReshashCount=1

        # h+1, h+4, h+9, h+16.... etc
        return (oldhash + (self.quadRehashCount**2)) % size
    
h=HashTable()

