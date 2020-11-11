class unionFind(object):
    def __init__(self,length):
        self.parent = [i for i in range(length+1)]
    
    def get_parent(self,parent,x):
        self.parent = parent
        if self.parent[x] == x:
            return x
        self.parent[x] = self.get_parent(self.parent,self.parent[x])
        return self.parent[x]
        
    def union_parent(self,parent,a,b):
        self.parent = parent
        a = self.get_parent(self.parent,a)
        b = self.get_parent(self.parent,b)
        
        if a<b:
            self.parent[b] = a
        else:
            self.parent[a] = b
            
    def find_parent(self,parent,a,b):
        self.parent = parent
        a = self.get_parent(self.parent,a)
        b = self.get_parent(self.parent,b)
        
        if a==b:
            return 1
        else:
            return 0
