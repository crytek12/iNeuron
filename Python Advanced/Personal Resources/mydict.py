class dict_parsing:
    def __init__(self, a):
        self.a = a
    
    def getkeys(self):
        if self.notdict():
            return list(self.a.keys())
        
    def getvalues(self):
        if self.notdict():
            return list(self.a.values())
        
    def notdict(self):
        if type(self.a) != dict:
            raise Exception(self.a, 'Not a dictionary')
        return 1
    
    def userinput(self):
        self.a = eval(input())
        print(self.a, type(self.a))
        print(self.getkeys())
        print(self.getvalues())
        
    def insertion(self, k, v):
        self.a[k] = v