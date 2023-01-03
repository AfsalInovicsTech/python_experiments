

from collections import UserDict



class StringKeyDict(UserDict):

    def __setitem__(self, key, value):
        if type(key) != str or not key.isalpha():
            raise Exception('Key must be alphabet')
        super().__setitem__(key, value)




a = StringKeyDict()
a["a"] = "test"
a["b"] = 2
print(a)
a["ab2"] = "test"