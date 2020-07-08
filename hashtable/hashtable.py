class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, key, value):
        new_entry = HashTableEntry(key, value)
        new_entry.next = self.head
        self.head = new_entry

    def get_value_with_key(self, key):
        current_entry = self.head
        while current_entry != None:
            if current_entry.key == key:
                return current_entry.value
            current_entry = current_entry.next
        return None

    def delete(self, key):
        current_entry = self.head
        if current_entry.key == key:
            self.head = self.head.next
            current_entry.next = None
        prev_entry = current_entry
        current_entry = current_entry.next
        while current_entry != None:
            if current_entry.key == key:
                prev_entry.next = current_entry.next
                current_entry.next = None
            else:
                prev_entry = prev_entry.next
                current_entry = current_entry.next
        return None

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.hashtable = [None] * capacity
        self.capacity = capacity
        self.entries_count = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.hashtable)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.entries_count / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        sb = key.encode()

        offset = 14695981039346656037
        prime = 1099511628211

        for byte in sb:
            hash = offset ^ byte
            hash = hash * prime
        
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # self.hashtable[self.hash_index(key)] = value

        if self.hashtable[self.hash_index(key)] == None:
            # the value at this slot is None and doesn't have a Linked List yet
            new_list = LinkedList()
            new_list.add_to_head(key, value)
            self.hashtable[self.hash_index(key)] = new_list 
        else:
            # check for existing entry with same key in the linked list
            if self.hashtable[self.hash_index(key)].get_value_with_key(key) != None:
                # an existing entry with this key 
                current_entry = self.hashtable[self.hash_index(key)].head
                while current_entry != None:
                    if current_entry.key == key:
                        current_entry.value = value
                    current_entry = current_entry.next
            else:
                self.hashtable[self.hash_index(key)].add_to_head(key, value)

        self.entries_count += 1
        # resize hashtable if load factor is too large
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # self.hashtable[self.hash_index(key)] = None

        if self.hashtable[self.hash_index(key)] != None:
            deleted_node = self.hashtable[self.hash_index(key)].delete(key)
        else:
            print("key was not found")

        if self.get_load_factor() < 0.2:
            self.resize(self.capacity / 2)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # return self.hashtable[self.hash_index(key)]

        if self.hashtable[self.hash_index(key)] != None:
            return self.hashtable[self.hash_index(key)].get_value_with_key(key)
        else:
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        prev_hashtable = self.hashtable
        self.hashtable = [None] * new_capacity
        self.capacity = new_capacity
        self.entries_count = 0

        for slot in prev_hashtable:
            if slot != None:
                current_entry = slot.head
                while current_entry != None:
                    self.put(current_entry.key, current_entry.value)
                    current_entry = current_entry.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
