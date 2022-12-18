import os

def getFullPatch():
    try:
        dir = os.path.dirname(os.path.realpath(__file__))
    except Exception as e:
        print("fallo en el path")
    return dir

def createLogger():
    try:
        if os.path.exists('./log') == False:
            os.mkdir('log')
        return True
        
    except Exception as e:
        print('Fallo al crear logger')
        return False    
