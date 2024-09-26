from IDS.Math import maths
class Nodo:
    def __init__(self, name, id, value=None,  father = None):
        self.name = name
        self.value = value
        self.id = id
        self.father = father
        self.children=[]
        if father is None:
            self.level = 0  
        else:
            self.level = self.father.level + 1
        
    def add_child(self, child):
        self.children.append(child)
        
    def get_children(self):
        return self.children
    
    def get_level(self):
        return self.level
    
    def get_father(self):
        return self.father
    
    def get_name(self):
        return self.name
    
    def get_value(self):
        return self.value
    
    def get_idNodo(self):
        return self.id

    def __str__(self):
        return self.name + " --> " + self.value
    
    def result(self):
        values = []
        math_module = maths()
        try:
            for nodo in self.children:
                values.append(nodo.get_value())
            result = math_module.average(values)
            self.value = result
            return result
        except:
            pass
        return None