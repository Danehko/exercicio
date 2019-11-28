class arvore:
    def __init__(self,val,left=None,right=None):
        self.value = val
        self.leftChild = left
        self.rightChild = right

    def __str__(self):
        return '({}, {}, {})'.format(self.leftChild, self.value, self.rightChild)

    def __repr__(self):
        return str(self)