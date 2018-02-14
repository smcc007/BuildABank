class Bank:
    '''This is an empty class'''
    def __init__(self, strName):
        self.name = strName

    def __str__(self):
        return 'The name of the bank is %s' %self.name
        
