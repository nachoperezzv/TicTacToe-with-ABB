import os

def getFullPatch():
    try:
        dir = os.path.dirname(os.path.realpath(__file__))
    except Exception as e:
        print("fallo en el path")
    return dir
 
