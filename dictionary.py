# # ex: Nested dictionary
# my_dict = {
#     'key1': {'value1': 100},
#     'key2': 'value2',
#     'key3': 'value3',
#     'key4': [1, 2, 3, 4]
# }
# print(my_dict['key1'])
# print(my_dict['key1']['value1'])  # !!!!!
# print(my_dict['key4'][2])  # !!!!!
#
# my_dict['key5'] = 300
# print(my_dict)
# my_dict['key2'] = 'NEW VALUE'
# print(my_dict)
#
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
#
#
#
# Pset5 #######
# words = set()
#
#
# def check(word):
#     if word.lower() in words:
#         return True
#     else:
#         return False
#
#
# def load(dictionary):
#     file = open(dictionary, "r")
#     for line in file:
#         words.add(line.rstrip("\n"))
#     file.close()
#     return True
#
#
# def size():
#     return len(words)
#
#
# def unload():
#     return True


