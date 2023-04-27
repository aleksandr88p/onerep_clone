# import async_parsers.a411locate as a411locate
# import async_parsers.advanced_people_search as advanced_people_search
# import async_parsers.anywho as anywho
# import async_parsers.cyberbackgroundcheck as cyberbackgroundcheck
# import async_parsers.fast_people_search as fast_people_search
# import async_parsers.fast_people_searchIO as fast_people_searchIO
# import async_parsers.findpeoplesearch as findpeoplesearch
# import async_parsers.freepeople_directory as freepeople_directory
# import async_parsers.freepeoplesearch as freepeoplesearch
# import async_parsers.golookup as golookup
# import async_parsers.information_com as information_com
# import async_parsers.instant_checkmate as instant_checkmate
# import async_parsers.intelius as intelius
# import async_parsers.kidslivesafe as kidslivesafe
# import async_parsers.peekyou as peekyou
# import async_parsers.peeplookup as peeplookup
# import async_parsers.people_finders as people_finders
# import async_parsers.people_search as people_search
# import async_parsers.people_search_now as people_search_now
# import async_parsers.privateeye as privateeye
# import async_parsers.propeoplesearch as propeoplesearch
# import async_parsers.publicinfoservices as publicinfoservices
# import async_parsers.publicrecordsnow as publicrecordsnow
# import async_parsers.quickpeopletrace as quickpeopletrace
# import async_parsers.Radaris as Radaris
# import async_parsers.search_people_free as search_people_free
# import async_parsers.spokeo as spokeo
# import async_parsers.spyfly as spyfly
# import async_parsers.spytox as spytox
# import async_parsers.truth_finder as truth_finder
# import async_parsers.unmask as unmask
# import async_parsers.usatrace as usatrace
# import async_parsers.usphonebook as usphonebook
# import async_parsers.white_pages as white_pages
# import async_parsers.zaba_search as zaba_search



import a411locate
import advanced_people_search
import anywho
import cyberbackgroundcheck
import fast_people_search
import fast_people_searchIO
import findpeoplesearch
import freepeople_directory
import freepeoplesearch
import golookup
import information_com
import instant_checkmate
import intelius
import kidslivesafe
import peekyou
import peeplookup
import people_finders
import people_search
import people_search_now
import privateeye
import propeoplesearch
import publicinfoservices
import publicrecordsnow
import quickpeopletrace
import Radaris
import search_people_free
import spokeo
import spyfly
import spytox
import truth_finder
import unmask
import usatrace
import usphonebook
import white_pages
import zaba_search

import aiohttp
import asyncio


all_func = [
    a411locate.a411locate, advanced_people_search.advanced_people_search, anywho.anywho,
    cyberbackgroundcheck.cyberbackgroundcheck, fast_people_search.fast_people_search,
    fast_people_searchIO.fast_people_IO,
    findpeoplesearch.findpeoplesearch, freepeoplesearch.free_people_search, freepeople_directory.freepeople_directory,
    golookup.golookup, information_com.information_com, instant_checkmate.instant_checkmate, intelius.intelius,
    kidslivesafe.kidslivesafe, peekyou.peekyou, peeplookup.peeplookup, people_search.people_search,
    people_finders.people_finders,
    people_search_now.people_search_now, privateeye.privateeye, propeoplesearch.propeoplesearch,
    publicinfoservices.publicinfoservices,
    publicrecordsnow.publicrecordsnow, quickpeopletrace.quikpeopletrace, Radaris.radaris,
    search_people_free.search_people_free,
    spokeo.spokeo, spyfly.spyfly, spytox.spytox, truth_finder.truth_finder, unmask.unmask, usatrace.usatrace,
    usphonebook.usphonebook,
    white_pages.white_pages, zaba_search.zaba_search
]



async def general_func(*args, **kwargs):
    all_functions = kwargs['functions']
    first_name = kwargs["first_name"]
    middle_name = kwargs["middle_name"]
    last_name = kwargs["last_name"]
    city = kwargs["city"]
    state = kwargs["state"]
    proxy = {
            "server": "http://196.17.66.143:8000",
            "username": "2xxh1Q",
            "password": "NCm6xp"
        }
    big_dict = {}
    tasks = []
    bad_funcs = []
    async with aiohttp.ClientSession() as session:
        for num, function in enumerate(all_functions):
            try:
                task = asyncio.ensure_future(
                    function(first_name=first_name, last_name=last_name, middle_name=middle_name, state=state,
                             city=city, session=session, proxy=proxy))
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

# start_time = time.time()
#
# d = asyncio.run(
#     general_func(functions=all_func, first_name='John', last_name='Doe', middle_name='', state='CA', city=''))
#
# import json
#
# print(json.dumps(d, indent=4))
# print(len(d))
# end_time = time.time()
# elapsed_time = end_time - start_time
#
# print(f"Elapsed time: {elapsed_time} seconds")
