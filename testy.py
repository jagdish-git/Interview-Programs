class TextProcessor:
    def __init__(self, array):
        self.array = array

    def get_slice(self, start: int, end: int):
        try:
            listx = self.array
            new_list = []
            for strng in listx:
                slice_str = strng[start:end]
                new_list.append(slice_str)
            return new_list
        except IndexError:
            pass

    def reverse_strings(self):
        reverse_string = []
        for strn in self.array:
            reverse_string += [strn[::-1]]
        
        return reverse_string


    def add_string(self, new_string: str):
        add_str = self.array.append(new_string)
        return self.array

    def get_list(self):
        return self.array



list1 = ['mirafra','tchnology', 'private', 'limited']
tp = TextProcessor(list1)
# print(tp.get_list())
# print(tp.add_string("anything"))
# print(tp.reverse_strings())
# print(tp.get_slice(1,14))