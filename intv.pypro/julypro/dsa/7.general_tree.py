# general tree

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|--" if self.parent else ""
        print(prefix+self.data)
        for child in self.children:
            child.print_tree()

def build_product_tree():
    root = TreeNode('Electronics')

    laptops = TreeNode('Laptops')
    laptops.add_child(TreeNode('MacBook'))
    laptops.add_child(TreeNode('Microsoft Surface'))
    laptops.add_child(TreeNode('Thinkpad'))

    cell_phones = TreeNode('Cell Phones')
    cell_phones.add_child(TreeNode('iPhone'))
    cell_phones.add_child(TreeNode('Black Berry'))
    cell_phones.add_child(TreeNode('Vivo'))

    televisions = TreeNode("Televisions")
    televisions.add_child(TreeNode('Samsung'))
    televisions.add_child(TreeNode('Sony'))

    root.add_child(laptops)
    root.add_child(cell_phones)
    root.add_child(televisions)

    root.print_tree()

if __name__ == '__main__':
    # root = build_product_tree()
    pass


# exercise : management hierarchy of a company
class HierarchyTreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            p = p.parent
            level += 1

        return level
    
    def print_tree(self, req):
        if req == 'name':
            value = self.name
        elif req == 'designation':
            value = self.designation
        else:
            value = self.name +' ('+self.designation+')'

        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|--' if self.parent else ''
        print(prefix+value)
        for i in self.children:
            i.print_tree(req)


def management_hierarchy_company():
    ceo = HierarchyTreeNode('Nipul', 'CEO')

    cto = HierarchyTreeNode("Chinmay", "CTO")
    infra = HierarchyTreeNode("Vishwa", "Infrastructure Head")
    infra.add_child(HierarchyTreeNode("Dhaval", "Cloud Manger"))
    infra.add_child(HierarchyTreeNode("Abhijit", "App Manger"))

    app = HierarchyTreeNode("Aamir", "Application Head")

    cto.add_child(infra)
    cto.add_child(app)

    hr = HierarchyTreeNode("Gels", "HR Head")
    hr.add_child(HierarchyTreeNode("Peter", "Recruitment Manager"))
    hr.add_child(HierarchyTreeNode("Waqs", "Policy Manager"))

    ceo.add_child(cto)
    ceo.add_child(hr)
    
    return ceo

if __name__ == '__main__':
    root_node = management_hierarchy_company()
    # root_node.print_tree("name")
    # root_node.print_tree("designation")
    # root_node.print_tree("both")

# exercise 

class GlobalTreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def print_tree(self, level):
        if self.get_level() > level:
            return
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|--" if self.parent else ""
        print(prefix + self.data)
        for child in self.children:
            child.print_tree(level)


def build_location_tree():
    root = GlobalTreeNode("Global")

    india = GlobalTreeNode("India")

    gujarat = GlobalTreeNode("Gujarat")
    gujarat.add_child(GlobalTreeNode("Ahmedabad"))
    gujarat.add_child(GlobalTreeNode("Baroda"))

    karnataka = GlobalTreeNode("Karnataka")
    karnataka.add_child(GlobalTreeNode("Bangluru"))
    karnataka.add_child(GlobalTreeNode("Mysore"))

    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = GlobalTreeNode("USA")

    nj = GlobalTreeNode("New Jersey")
    nj.add_child(GlobalTreeNode("Princeton"))
    nj.add_child(GlobalTreeNode("Trenton"))

    california = GlobalTreeNode("California")
    california.add_child(GlobalTreeNode("San Francisco"))
    california.add_child(GlobalTreeNode("Mountain View"))
    california.add_child(GlobalTreeNode("Palo Alto"))

    usa.add_child(nj)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)

    return root


if __name__ == '__main__':
    root_node = build_location_tree()
    root_node.print_tree(3)