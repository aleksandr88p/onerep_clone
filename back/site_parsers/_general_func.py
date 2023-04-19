from a411locate import *
from advanced_people_search import *
from findpeoplesearch import *
from golookup import *
from privateeye import *
from propeoplesearch import *
from publicrecordsnow import *
from quickpeopletrace import *
from spokeo import *
from usatrace import *



# print(usatrace.__name__)

all_funcs = [a411locate, advanced_people_search, findpeoplesearch, golookup, privateeye, propeoplesearch,
             publicrecordsnow, quikpeopletrace, spokeo, usatrace]
def general_func(*args, **kwargs):
    all_functions = kwargs['functions']
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"]
    state = kwargs["state"]
    big_dict = {}
    for num, function in enumerate(all_functions):
        try:
            d = function(first_name=first_name, last_name=last_name, middle_name=middle_name, state=state, city=city)

            big_dict[function.__name__] = d
            print(function.__name__)
            # yield d
        except Exception as ex:
            print(f"error in {function} \n {ex}")

    return big_dict



print('start')
d = general_func(functions=all_funcs, first_name='billie', last_name='bones', middle_name='', state='ID', city='')

import json
print(json.dumps(d, indent=4))

print('finish')