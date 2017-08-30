# give python dictoinary, replace $ from all keys of that dictionary

def replace_dollar(my_dict):

    for key in my_dict.keys():
        if '$' in key:
            val = my_dict[key]
            del (my_dict[key])
            key = key.replace('$', '_')
            my_dict[key] = val

def transform_dict(my_dict):

    if my_dict is None:
        return

    if type(my_dict) == dict:
        replace_dollar(my_dict)

        for key in my_dict.keys():
            if type(my_dict[key]) == dict:
                transform_dict(my_dict[key])
            elif type(my_dict[key]) == list:
                for val in my_dict[key]:
                    transform_dict(val)


if __name__ == '__main__':
    my_dict = {'key$1':'value1', 'key$2':'value2'}
    transform_dict(my_dict)
    print my_dict

    my_dict = {'key1': {'key$2': 'def', 'key3':[1,2]}}
    transform_dict(my_dict)
    print my_dict

    my_dict = {'key$1': 'abc', 'key$2': ['def', 'ghi'], 'key3': [{'key$4': [1,2], 'key$5': 'jkl'}]}
    transform_dict(my_dict)
    print my_dict
