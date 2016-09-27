#! /usr/local/bin/python3

from wsgiref.simple_server import make_server
from cgi import parse_qs, escape #parse_qs(environ['HTTP_HOST'])
import os,sys,importlib,urllib
import Controller,Model,View #import default abstract classes
#import Loader

DEFAULT_APP_PATH = "/home/francesco/webapp"
WORKING_APP_PATH = ""
CONTROLLERS_DIRECTORY = "controllers/"
MODELS_DIRECTORY = "models/"
VIEWS_DIRECTORY = "views/"

def webapp(environ,start_response):
    #params = processEnviron(environ)

    body = setInsertPaths()
    body = byteEncode(body)
    
    status = '200 OK'
    headers = [('Content-Type','text/html;')]
    start_response(status,headers)

    return body

def splitRequest(request):
    return request

def setInsertPaths():
    global DEFAULT_APP_PATH, WORKING_APP_PATH,CONTROLLERS_DIRECTORY,MODELS_DIRECTORY,VIEWS_DIRECTORY
    os.chdir(DEFAULT_APP_PATH)
    sys.path.insert(0,DEFAULT_APP_PATH+"/"+CONTROLLERS_DIRECTORY)
    sys.path.insert(0,DEFAULT_APP_PATH+"/"+MODELS_DIRECTORY)
    sys.path.insert(0,DEFAULT_APP_PATH+"/"+VIEWS_DIRECTORY)
        
    Controller = importlib.import_module("IndexController")
    Controller = Controller.Index()
    Controller = Controller.Init()
    #print(Controller)
    
    return [Controller]

def byteEncode(array):
    newList = []
    for value in array:
        newList.append(value.encode("utf-8"))
    return newList

def processEnviron(environ):
    return environ


if __name__ == "__main__":
    httpd = make_server('localhost',8080,webapp)
    print('Serving on 8080..')
    httpd.serve_forever()

    #os.path.join(appDirecotry,"controllers")
    #fileRead = os.popen("index.py",'r',1)
    #write (fileRead)
    #self.returnResponse(fileRead)
    #def returnResponse(self,fileread):
