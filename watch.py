#!/usr/bin/python3

import requests
import config
import json
import pymongo

def save_database(data, path, username, password):
    dbpath = path+username+"@"+password
    client = pymongo.MongoClient(dbpath)
    
    db = client["watch"]
    collection = db["bug_crowd"]
    collection.insert_many(data)
    
    client.close()
    print("insert to db")
    


def get_bug_crowd(url):
    session = requests.session()
    
    session.headers['User-Agent'] = "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36"
    
    res = session.get(url)
    datas = json.loads(res.content)
    save_database(datas, config.DB_PATH, config.DB_USER, config.DB_PASS)
    
get_bug_crowd(config.BUG_CROWD)