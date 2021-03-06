class Person:

    def __init__(self, name, parent, spouse):
        '''
        Initializing a node storing it's key, item and number of children
        '''
        self.parent = parent
        self.name = name
        self.children = []
        self.spouse = spouse

    def addChildren(self, childname, spouse):
        '''
        adding a child to a person by creating a new instance of a Person
        and appending it to the list of children
        '''
        self.children.append(Person(childname, self, spouse))

    def findPerson(self, name):
        # return child that matches that name, with all attributes
        # depth first search will return referecne to the Person
        # Note that no two family members have the same name
        # if the current person has the same name return that person
        if self.name == name:
            return self

        # otherwise go through that persons children recursively
        # to find a person with that name
        # if you find that name, return the person
        for i in range(len(self.children)):
            n = self.children[i].findPerson(name)
            if n is not None:
                return n

    def getChild(self, n):
        # return a child at the specific index
        if n >= len(self.children):
            raise IndexError("Person does not have that many children!")
        return self.children[n]

    def getAllChildren(self, name):
        # get all the children of a specific person
        list = []
        p = self.findPerson(name)
        for i in range(len(p.children)):
            list.append(p.getChild(i).name)
        return list

    def getSiblings(self, name):
        # get all the siblings of a specific person
        list = []
        p = self.findPerson(name)
        if p.parent == "None":
            return None

        for i in range(len(p.parent.children)):
            if p.parent.children[i].name != p.name:
                list.append(p.parent.children[i].name)
        return list

    def getParents(self, name):
        if (self.findPerson(name).parent) == "None":
            return None
        list = []
        list.append(self.findPerson(name).parent.name)
        list.append(self.findPerson(name).parent.spouse)
        return list

    def getSpouse(self, name):
        return self.findPerson(name).spouse

    def getFirstCousins(self, name): 
        list = []
        p = self.findPerson(name)
        if p.parent == "None" or p.parent.parent == "None":
            return None
        grandparent = p.parent.parent
        for i in range(len(grandparent.children)):
            if p.parent.name == grandparent.children[i].name:
                continue
            else:
                for x in range(len(grandparent.children[i].children)):
                    list.append(grandparent.children[i].getChild(x).name)

        return list
