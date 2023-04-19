from a411locate import *
from advanced_people_search import *
from fast_people_search import *
from findpeoplesearch import *
from freepeoplesearch import *
from golookup import *
from information_com import *
from instant_checkmate import *
from people_finders import *
from privateeye import *
from propeoplesearch import *
from people_search_now import *
from publicrecordsnow import *
from quickpeopletrace import *
from Radaris import *
from search_people_free import *
from spokeo import *
from truth_finder import *
from unmask import *
from usatrace import *
from white_pages import *
from zaba_search import *

all_func = [a411locate, advanced_people_search, fast_people_search, findpeoplesearch,
            free_people_search, golookup, information_com, instant_checkmate, people_finders,
            privateeye, propeoplesearch, people_search_now, publicrecordsnow, quikpeopletrace,
            radaris, search_people_free, spokeo, truth_finder, unmask, usatrace, white_pages, zaba_search]


# async def general_func(*args, **kwargs):
#     all_functions = kwargs['functions']
#     first_name = kwargs["first_name"]
#     middle_name = kwargs["middle_name"]
#     last_name = kwargs["last_name"]
#     city = kwargs["city"]
#     state = kwargs["state"]
#     big_dict = {}
#     tasks = []
#     async with aiohttp.ClientSession() as session:
#         for num, function in enumerate(all_functions):
#             try:
#                 task = asyncio.ensure_future(
#                     function(first_name=first_name, last_name=last_name, middle_name=middle_name, state=state,
#                              city=city, session=session))
#                 tasks.append(task)
#             except Exception as ex:
#                 print(f"error in {function} \n {ex}")
#
#         results = await asyncio.gather(*tasks)
#
#         for num, function in enumerate(all_functions):
#             big_dict[function.__name__] = results[num]
#
#         return big_dict



async def general_func(*args, **kwargs):
    all_functions = kwargs['functions']
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"]
    state = kwargs["state"]
    big_dict = {}
    tasks = []
    bad_funcs = []
    async with aiohttp.ClientSession() as session:
        for num, function in enumerate(all_functions):
            try:
                task = asyncio.ensure_future(
                    function(first_name=first_name, last_name=last_name, middle_name=middle_name, state=state,
                             city=city, session=session))
                tasks.append(task)
            except Exception as ex:
                print(f"error in {function} \n {ex}")

        for i, completed_task in enumerate(asyncio.as_completed(tasks)):
            try:
                print(f"Running task {all_functions[i].__name__}")
                result = await completed_task
                if result is None:
                    bad_funcs.append(all_functions[i].__name__)
                big_dict[all_functions[i].__name__] = result
                print(f"Task {i}  {all_functions[i].__name__} completed")
                # print(result)
            except Exception as ex:
                print(f"error in {all_functions[i]} \n {ex}")
    print(f"|||||||| BAD FUNCS ||||||||||\n{bad_funcs}")
    return big_dict


import time

start_time = time.time()

d = asyncio.run(
    general_func(functions=all_func, first_name='John', last_name='Doe', middle_name='', state='CA', city=''))

import json

print(json.dumps(d, indent=4))
print(len(d))
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time} seconds")
