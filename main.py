class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.how_many_words_from_me = 1
        
    def __str__(self):
        return str(self.value)
    
    def add(self, name):
        dad = self
        dad.how_many_words_from_me += 1
        for char in name:
            if char not in dad.children:
                new = TrieNode()
                dad.children[char] = new
                dad = new
            else:
                dad = dad.children[char]
                dad.how_many_words_from_me += 1
        dad.end = True
    
    def search(self, name):
        dad = self
        for char in name:
            dad = dad.children.get(char)
            if dad is None:
                return 0
        return dad.how_many_words_from_me

def contacts(queries):
    contacts = TrieNode()
    output = []
    for operation_query in queries:
        operation, name = operation_query
        if operation == "add":
            contacts.add(name)
        else:
            occurrences = contacts.search(name)
            output.append(occurrences)
    return output
