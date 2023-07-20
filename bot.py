from multiprocessing.connection import wait
from pyautogui import *
import time
import keyboard
import pyautogui

from pynput.mouse import Button, Controller

mouse = Controller()

# Read pointer position
print('The current pointer position is {0}'.format(
    mouse.position))

"""# Set pointer position
mouse.position = (520, 530)
print('Now we have moved it to {0}'.format(
    mouse.position))

# Move pointer relative to current position
mouse.move(5, -5)

# Press  release
mouse.press(Button.left)
mouse.release(Button.left)

# Double click; this is different from pressing  releasing
# twice on Mac OSX
mouse.click(Button.left, 2)

# Scroll two steps down
mouse.scroll(0, 2)"""



time.sleep(2)

def click():
    print("click")
    mouse.press(Button.left) 
    time.sleep(0.5) 
    mouse.release(Button.left)


def click2(x,y):
    pyautogui.SetCursorPos((x,y))
    pyautogui.mouse_event(pyautogui.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    pyautogui.mouse_event(pyautogui.MOUSEEVENTF_LEFTUP, 0, 0)


def fenetre():
    print("recherche fenetre")
    fenetre = pyautogui.locateCenterOnScreen('fenetre.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
    if fenetre is not None:
        print("fenetre trouvé")
        mouse.position = (fenetre)  # Moves the mouse to the coordinates of the image
        click()
        tmp = 15
        time.sleep(2)
    else:
        tmp = 0
        if fenetre is None:
            while tmp < 15:
                if fenetre is None:
                    fenetre = pyautogui.locateCenterOnScreen('fenetre.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
                    print("fenetre pas trouvé")
                    time.sleep(1)
                    tmp = tmp+1
                    print(tmp)
                    if tmp == 15:
                        print(tmp)
                        refresh()
                if fenetre is not None:
                    print("fenetre trouvé")
                    mouse.position = (fenetre)  # Moves the mouse to the coordinates of the image
                    click()
                    tmp = 15
                    time.sleep(2)


def connect():
    print("recherche connect")
    connect = pyautogui.locateCenterOnScreen('connect.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
    if connect is not None:
        print("connect trouvé")
        mouse.position = (connect)  
        click()
        tmp = 15
        time.sleep(2)
    else:
        tmp = 0
        if connect is None:
            while tmp < 15:
                if connect is None:
                    connect = pyautogui.locateCenterOnScreen('connect.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
                    print("connect pas trouvé")
                    time.sleep(1)
                    tmp = tmp+1
                    print(tmp)
                    if tmp == 15:
                        print(tmp)
                        refresh()
                if connect is not None:
                    print("connect trouvé")
                    mouse.position = (connect)  
                    click()
                    tmp = 15
                    time.sleep(2)


def refresh():
    print("debut refresh")   
    fenetre()
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'r')
    pyautogui.hotkey('ctrl', 'F5')
    """pyautogui.press('F5')"""
    """keyboard.press__release('F5')"""
    time.sleep(1)
    connect()
    time.sleep(1)
    meta()
    time.sleep(1)
    signer()
    time.sleep(1)
    treasure_hunt()

def refresh_2():
    print("debut refresh_2")     
    fenetre_2()
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'r')
    """pyautogui.press('F5')"""
    """keyboard.press__release('F5')"""
    time.sleep(1)
    connect_2()
    time.sleep(1)
    meta_2()
    time.sleep(1)
    signer_2()
    time.sleep(1)
    treasure_hunt_2()



def fenetre_2():
    print("recherche fenetre_2")
    fenetre_2 = pyautogui.locateCenterOnScreen('fenetre_2.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
    if fenetre_2 is not None:
        print("fenetre_2 trouvé")
        mouse.position = (fenetre_2)  # Moves the mouse to the coordinates of the image
        click()
        tmp = 15
        time.sleep(2)
    else:
        tmp = 0
        if fenetre_2 is None:
            while tmp < 15:
                if fenetre_2 is None:
                    fenetre_2 = pyautogui.locateCenterOnScreen('fenetre_2.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
                    print("fenetre_2 pas trouvé")
                    time.sleep(1)
                    tmp = tmp+1
                    print(tmp)
                    if tmp == 15:
                        print(tmp)
                        refresh_2()
                if fenetre_2 is not None:
                    print("fenetre_2 trouvé")
                    mouse.position = (fenetre_2)  # Moves the mouse to the coordinates of the image
                    click()
                    tmp = 15
                    time.sleep(2)


def connect_2():
    print("recherche connect_2")
    connect_2 = pyautogui.locateCenterOnScreen('connect_2.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
    if connect_2 is not None:
        print("connect_2 trouvé")
        mouse.position = (connect_2)  # Moves the mouse to the coordinates of the image
        click()
        tmp = 15
        time.sleep(2)
    else:
        tmp = 0
        if connect_2 is None:
            while tmp < 15:
                if connect_2 is None:
                    connect_2 = pyautogui.locateCenterOnScreen('connect_2.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
                    print("connect_2 pas trouvé")
                    time.sleep(1)
                    tmp = tmp+1
                    print(tmp)
                    if tmp == 15:
                        print(tmp)
                        refresh_2()
                if connect_2 is not None:
                    print("connect_2 trouvé")
                    mouse.position = (connect_2)  # Moves the mouse to the coordinates of the image
                    click()
                    tmp = 15
                    time.sleep(2)




def signer():
    print("recherche signer")
    signer = pyautogui.locateCenterOnScreen('signer.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.70)
    if signer is not None:
        print("signer trouvé")
        mouse.position = (signer)  # Moves the mouse to the coordinates of the image
        click()
        tmp = 15
        time.sleep(2)
    else:
        tmp = 0
        if signer is None:
            while tmp < 15:
                if signer is None:
                    signer = pyautogui.locateCenterOnScreen('signer.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.70)
                    print("signer pas trouvé")
                    time.sleep(1)
                    tmp = tmp+1
                    print(tmp)
                    if tmp == 15:
                        print(tmp)
                        refresh()
                if signer is not None:
                    print("signer trouvé")
                    mouse.position = (signer)  # Moves the mouse to the coordinates of the image
                    click()
                    tmp = 15
                    time.sleep(2)
    

        
    
           

def signer_2():
    print("recherche signer_2")
    signer_2 = pyautogui.locateCenterOnScreen('signer_2.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
    if signer_2 is not None:
        print("signer_2 trouvé")
        mouse.position = (signer_2)  # Moves the mouse to the coordinates of the image
        click()
        tmp = 15
        time.sleep(2)
    else:
        tmp = 0
        if signer_2 is None:
            while tmp < 15:
                if signer_2 is None:
                    signer_2 = pyautogui.locateCenterOnScreen('signer_2.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
                    print("signer_2 pas trouvé")
                    time.sleep(1)
                    tmp = tmp+1
                    print(tmp)
                    if tmp == 15:
                        print(tmp)
                        refresh_2()
                if signer_2 is not None:
                    print("signer_2 trouvé")
                    mouse.position = (signer_2)  # Moves the mouse to the coordinates of the image
                    click()
                    tmp = 15
                    time.sleep(2)
    

        


def heroes():
    print("recherche heroes")
    heroes = pyautogui.locateCenterOnScreen('heroes.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.70)
    if heroes is not None:
        print("heroes trouvé")
        mouse.position = (heroes)  # Moves the mouse to the coordinates of the image
        click()
        time.sleep(0.5)
        click()
        tmp = 15
        time.sleep(2)
    else:
        tmp = 0
        if heroes is None:
            while tmp < 15:
                if heroes is None:
                    heroes = pyautogui.locateCenterOnScreen('heroes.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.70)
                    print("heroes pas trouvé")
                    time.sleep(1)
                    tmp = tmp+1
                    print(tmp)
                    if tmp == 15:
                        print(tmp)
                        fleche_retour()
                if heroes is not None:
                    print("heroes trouvé")
                    mouse.position = (heroes)  # Moves the mouse to the coordinates of the image
                    click()
                    time.sleep(0.5)
                    click()
                    tmp = 15
                    time.sleep(2)
            
def meta():
    print("recherche metas")
    meta = pyautogui.locateCenterOnScreen('meta.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.70)
    if meta is not None:
        print("meta trouvé")
        mouse.position = (meta)  # Moves the mouse to the coordinates of the image
        click()
        time.sleep(0.5)
        click()
        tmp = 15
        time.sleep(2)
    else:
        tmp = 0
        if meta is None:
            while tmp < 15:
                if meta is None:
                    meta = pyautogui.locateCenterOnScreen('meta.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.70)
                    print("meta pas trouvé")
                    time.sleep(1)
                    tmp = tmp+1
                    print(tmp)
                    if tmp == 15:
                        print(tmp)
                        fleche_retour()
                if meta is not None:
                    print("meta trouvé")
                    mouse.position = (meta)  # Moves the mouse to the coordinates of the image
                    click()
                    time.sleep(0.5)
                    click()
                    tmp = 15
                    time.sleep(2)            
                    


def heroes_2():
    print("recherche heroes_2")
    heroes_2 = pyautogui.locateCenterOnScreen('heroes_2.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.70)
    if heroes_2 is not None:
        print("heroes_2 trouvé")
        mouse.position = (heroes_2)  # Moves the mouse to the coordinates of the image
        click()
        time.sleep(0.5)
        click()
        tmp = 15
        time.sleep(2)
    else:
        tmp = 0
        if heroes_2 is None:
            while tmp < 15:
                if heroes_2 is None:
                    heroes_2 = pyautogui.locateCenterOnScreen('heroes_2.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.70)
                    print("heroes_2 pas trouvé")
                    time.sleep(1)
                    tmp = tmp+1
                    print(tmp)
                    if tmp == 15:
                        print(tmp)
                        fleche_retour_2()
                if heroes_2 is not None:
                    print("heroes_2 trouvé")
                    mouse.position = (heroes_2)  # Moves the mouse to the coordinates of the image
                    click()
                    time.sleep(0.5)
                    click()
                    tmp = 15
                    time.sleep(2)

def meta_2():
    print("recherche meta_2")
    meta_2 = pyautogui.locateCenterOnScreen('meta_2.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.70)
    if meta_2 is not None:
        print("meta trouvé")
        mouse.position = (meta_2)  # Moves the mouse to the coordinates of the image
        click()
        time.sleep(0.5)
        click()
        tmp = 15
        time.sleep(2)
    else:
        tmp = 0
        if meta_2 is None:
            while tmp < 15:
                if meta_2 is None:
                    meta_2 = pyautogui.locateCenterOnScreen('meta_2.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.70)
                    print("meta_2 pas trouvé")
                    time.sleep(1)
                    tmp = tmp+1
                    print(tmp)
                    if tmp == 15:
                        print(tmp)
                        fleche_retour()
                if meta_2 is not None:
                    print("meta_2 trouvé")
                    mouse.position = (meta_2)  # Moves the mouse to the coordinates of the image
                    click()
                    time.sleep(0.5)
                    click()
                    tmp = 15
                    time.sleep(2) 





def all():
    print("recherche all")
    all = pyautogui.locateCenterOnScreen('all.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
    if all is not None:
        print("all trouvé")
        mouse.position = (all)  # Moves the mouse to the coordinates of the image
        click()
        time.sleep(0.5)
        click()
        tmp = 15
        time.sleep(2)
    else:
        tmp = 0
        if all is None:
            while tmp < 15:
                if all is None:
                    all = pyautogui.locateCenterOnScreen('all.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
                    print("all pas trouvé")
                    time.sleep(1)
                    tmp = tmp+1
                    print(tmp)
                    if tmp == 15:
                        print(tmp)
                        all_rest()
                if all is not None:
                    print("all trouvé")
                    mouse.position = (all)  # Moves the mouse to the coordinates of the image
                    click()
                    tmp = 15
                    time.sleep(2)

def all_2():
    print("recherche all_2")
    all_2 = pyautogui.locateCenterOnScreen('all_2.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
    if all_2 is not None:
        print("all_2 trouvé")
        mouse.position = (all_2)  # Moves the mouse to the coordinates of the image
        click()
        time.sleep(0.5)
        click()
        tmp = 15
        time.sleep(2)
    else:
        tmp = 0
        if all_2 is None:
            while tmp < 15:
                if all_2 is None:
                    all_2 = pyautogui.locateCenterOnScreen('all_2.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
                    print("all_2 pas trouvé")
                    time.sleep(1)
                    tmp = tmp+1
                    print(tmp)
                    if tmp == 15:
                        print(tmp)
                        all_rest_2()
                if all_2 is not None:
                    print("all_2 trouvé")
                    mouse.position = (all_2)  # Moves the mouse to the coordinates of the image
                    click()
                    tmp = 15
                    time.sleep(2)

def all_rest():
    print("recherche all_rest")
    all_rest = pyautogui.locateCenterOnScreen('all_rest.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
    if all_rest is not None:
        print("all_rest trouvé")
        mouse.position = (all_rest)  # Moves the mouse to the coordinates of the image
        click()
        time.sleep(0.5)
        click()
        tmp = 15
        time.sleep(2)
    """else:
        tmp = 0
        if all_rest is None:
            while tmp < 15:
                if all_rest is None:
                    all_rest = pyautogui.locateCenterOnScreen('all_rest.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
                    print("all_rest pas trouvé")
                    time.sleep(1)
                    tmp = tmp+1
                    print(tmp)
                    if tmp == 15:
                        print(tmp)
                        refresh()
                if all_rest is not None:
                    print("all_rest trouvé")
                    mouse.position = (all_rest)  # Moves the mouse to the coordinates of the image
                    click()
                    tmp = 15
                    time.sleep(2)"""


   
def perso1():
    print("recherche perso1")    
    perso1 = pyautogui.locateCenterOnScreen('perso1.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
    if perso1 is not None:
        pyautogui.moveTo(perso1)  # Moves the mouse to the coordinates of the image
        mouse.press(Button.left)  
        time.sleep(0.5)  
        mouse.release(Button.left)
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 250
        pyautogui.moveTo(currentMouseX, currentMouseY)
        mouse.press(Button.left)  
        time.sleep(0.5)  
        mouse.release(Button.left)

def perso2():   
    print("recherche perso2")  
    perso2 = pyautogui.locateCenterOnScreen('perso2.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.80)
    if perso2 is not None:
        pyautogui.moveTo(perso2)  # Moves the mouse to the coordinates of the image
        mouse.press(Button.left)  
        time.sleep(0.5)  
        mouse.release(Button.left)
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 250
        pyautogui.moveTo(currentMouseX, currentMouseY)
        mouse.press(Button.left)  
        time.sleep(0.5)  
        mouse.release(Button.left)

def perso3():  
    print("recherche perso3")   
    perso3 = pyautogui.locateCenterOnScreen('perso3.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.80)
    if perso3 is not None:
        pyautogui.moveTo(perso3)  # Moves the mouse to the coordinates of the image
        mouse.press(Button.left)  
        time.sleep(0.5)  
        mouse.release(Button.left)
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 250
        pyautogui.moveTo(currentMouseX, currentMouseY)
        mouse.press(Button.left)  
        time.sleep(0.5)  
        mouse.release(Button.left)

def perso4():  
    print("recherche perso4")   
    perso4 = pyautogui.locateCenterOnScreen('perso4.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.99)
    if perso4 is not None:
        pyautogui.moveTo(perso4)  # Moves the mouse to the coordinates of the image
        mouse.press(Button.left)  
        time.sleep(0.5)  
        mouse.release(Button.left)
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 250
        pyautogui.moveTo(currentMouseX, currentMouseY)
        mouse.press(Button.left)  
        time.sleep(0.5)  
        mouse.release(Button.left)

def perso5():  
    print("recherche perso5")   
    perso5 = pyautogui.locateCenterOnScreen('perso5.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.80)
    if perso5 is not None:
        pyautogui.moveTo(perso5)  # Moves the mouse to the coordinates of the image
        mouse.press(Button.left)  
        time.sleep(0.5)  
        mouse.release(Button.left)
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 250
        pyautogui.moveTo(currentMouseX, currentMouseY)
        click()

def perso6():   
    print("recherche perso6")  
    perso6 = pyautogui.locateCenterOnScreen('perso6.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
    if perso6 is not None:
        pyautogui.moveTo(perso6)  # Moves the mouse to the coordinates of the image
        click()
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 250
        pyautogui.moveTo(currentMouseX, currentMouseY)
        click()

def perso7():  
    print("recherche perso7")   
    perso7 = pyautogui.locateCenterOnScreen('perso7.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.99)
    if perso7 is not None:
        pyautogui.moveTo(perso7)  # Moves the mouse to the coordinates of the image
        click()
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 250
        pyautogui.moveTo(currentMouseX, currentMouseY)
        click()

def perso8():    
    print("recherche perso8") 
    perso8 = pyautogui.locateCenterOnScreen('perso8.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.99)
    if perso8 is not None:
        pyautogui.moveTo(perso8)  # Moves the mouse to the coordinates of the image
        click()
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 250
        pyautogui.moveTo(currentMouseX, currentMouseY)
        click()

def perso9():   
    print("recherche perso9")  
    perso9 = pyautogui.locateCenterOnScreen('perso9.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.99)
    if perso9 is not None:
        pyautogui.moveTo(perso9)  # Moves the mouse to the coordinates of the image
        click()
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 250
        pyautogui.moveTo(currentMouseX, currentMouseY)
        click()

def perso10():   
    print("recherche perso10")  
    perso10 = pyautogui.locateCenterOnScreen('perso10.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.99)
    if perso10 is not None:
        pyautogui.moveTo(perso10)  # Moves the mouse to the coordinates of the image
        click()
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 250
        pyautogui.moveTo(currentMouseX, currentMouseY)
        click()

def perso11():   
    print("recherche perso11")  
    perso11 = pyautogui.locateCenterOnScreen('perso11.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
    if perso11 is not None:
        pyautogui.moveTo(perso11)  # Moves the mouse to the coordinates of the image
        click()
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 250
        pyautogui.moveTo(currentMouseX, currentMouseY)
        click()

def perso12():  
    print("recherche perso12")   
    perso12 = pyautogui.locateCenterOnScreen('perso12.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
    if perso12 is not None:
        pyautogui.moveTo(perso12)  # Moves the mouse to the coordinates of the image
        click()
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 250
        pyautogui.moveTo(currentMouseX, currentMouseY)
        click()

def perso13():   
    print("recherche perso13")  
    perso13 = pyautogui.locateCenterOnScreen('perso13.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.99)
    if perso13 is not None:
        pyautogui.moveTo(perso13)  # Moves the mouse to the coordinates of the image
        click()
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 250
        pyautogui.moveTo(currentMouseX, currentMouseY)
        click()

def perso14():    
    print("recherche perso14") 
    perso14 = pyautogui.locateCenterOnScreen('perso14.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.99)
    if perso14 is not None:
        pyautogui.moveTo(perso14)  # Moves the mouse to the coordinates of the image
        click()
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 250
        pyautogui.moveTo(currentMouseX, currentMouseY)
        click()

def perso15():  
    print("recherche perso15")   
    perso15 = pyautogui.locateCenterOnScreen('perso15.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
    if perso15 is not None:
        pyautogui.moveTo(perso15)  # Moves the mouse to the coordinates of the image
        click()
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 250
        pyautogui.moveTo(currentMouseX, currentMouseY)
        click()


def vaguesuivante():    
    print("vaguesuivante") 
    g = 0
    while g < 4:
        pyautogui.scroll(-5)
        time.sleep(.5)
        g = g+1


def veille():
    print("debut veille") 
    time.sleep(10)
    ok_error()
    time.sleep(30)
    mouse.position = (520, 530)
    time.sleep(1)
    click()

def attack_all():
    print("attack_all") 
    time.sleep(1)
    fleche_retour()
    time.sleep(1)
    heroes()
    time.sleep(1)
    all()
    time.sleep(1)
    croix_rouge()
    time.sleep(1)
    treasure_hunt()

def attack1speed():
    print("attack1speed") 
    fleche_retour()
    time.sleep(1)
    heroes()
    time.sleep(1)
    all()
    time.sleep(1)
    all_rest()
    time.sleep(1)
    perso1()
    time.sleep(1)
    perso4()
    time.sleep(1)
    vaguesuivante()
    time.sleep(1)
    perso9()
    time.sleep(1)
    perso10()
    time.sleep(1)
    vaguesuivante()
    time.sleep(1)
    perso15()
    time.sleep(1)
    croix_rouge()
    time.sleep(1)
    treasure_hunt()
    
def attack2speed():
    print("attack2speed") 
    fleche_retour()
    time.sleep(1)
    heroes()
    time.sleep(1)
    all()
    time.sleep(1)
    all_rest()
    time.sleep(1)
    perso2()
    time.sleep(1)
    perso3()
    time.sleep(1)
    perso5()
    time.sleep(1)
    vaguesuivante()
    time.sleep(1)
    perso6()
    time.sleep(1)
    vaguesuivante()
    time.sleep(1)
    perso11()
    croix_rouge()
    time.sleep(2)
    treasure_hunt()

def attack3speed():
    print("attack3speed") 
    fleche_retour()
    time.sleep(1)
    heroes()
    time.sleep(1)
    all()
    time.sleep(1)
    all_rest()
    time.sleep(1)
    perso1 = pyautogui.locateCenterOnScreen('perso1.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
    if perso1 is not None:
        pyautogui.moveTo(perso1)  # Moves the mouse to the coordinates of the image
        click()
    vaguesuivante()
    perso7()
    time.sleep(1)
    perso8()
    time.sleep(1)
    vaguesuivante()
    time.sleep(1)
    perso12()
    time.sleep(1)
    perso13()
    time.sleep(1)
    perso14()
    time.sleep(1)
    croix_rouge()
    time.sleep(1)
    treasure_hunt()














    
def all_rest_2():
    print("recherche all_rest_2")
    all_rest_2 = pyautogui.locateCenterOnScreen('all_rest_2.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
    if all_rest_2 is not None:
        print("all_rest_2 trouvé")
        mouse.position = (all_rest_2)  # Moves the mouse to the coordinates of the image
        click()
        time.sleep(0.5)
        click()
        tmp = 15
        time.sleep(2)
    """else:
        tmp = 0
        if all_rest_2 is None:
            while tmp < 15:
                if all_rest_2 is None:
                    all_rest_2 = pyautogui.locateCenterOnScreen('all_rest_2.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
                    print("all_rest_2 pas trouvé")
                    time.sleep(1)
                    tmp = tmp+1
                    print(tmp)
                    if tmp == 15:
                        print(tmp)
                        refresh_2()
                if all_rest_2 is not None:
                    print("all_rest_2 trouvé")
                    mouse.position = (all_rest_2)  # Moves the mouse to the coordinates of the image
                    click()
                    tmp = 15
                    time.sleep(2)"""


def croix_rouge():
    print("recherche croix_rouge")
    croix_rouge = pyautogui.locateCenterOnScreen('croix_rouge.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
    if croix_rouge is not None:
        print("croix_rouge trouvé")
        mouse.position = (croix_rouge)  # Moves the mouse to the coordinates of the image
        click()
        tmp = 15
        time.sleep(2)
    else:
        tmp = 0
        if croix_rouge is None:
            while tmp < 15:
                if croix_rouge is None:
                    croix_rouge = pyautogui.locateCenterOnScreen('croix_rouge.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
                    print("croix_rouge pas trouvé")
                    time.sleep(1)
                    tmp = tmp+1
                    print(tmp)
                    if tmp == 15:
                        print(tmp)
                        refresh()
                if croix_rouge is not None:
                    print("croix_rouge trouvé")
                    mouse.position = (croix_rouge)  # Moves the mouse to the coordinates of the image
                    click()
                    tmp = 15
                    time.sleep(2)


def croix_rouge_2():
    print("recherche croix_rouge_2")
    croix_rouge_2 = pyautogui.locateCenterOnScreen('croix_rouge_2.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.75)
    if croix_rouge_2 is not None:
        print("croix_rouge_2 trouvé")
        mouse.position = (croix_rouge_2)  # Moves the mouse to the coordinates of the image
        click()
        tmp = 15
        time.sleep(2)
    else:
        tmp = 0
        if croix_rouge_2 is None:
            while tmp < 15:
                if croix_rouge_2 is None:
                    croix_rouge_2 = pyautogui.locateCenterOnScreen('croix_rouge_2.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.75)
                    print("croix_rouge_2 pas trouvé")
                    time.sleep(1)
                    tmp = tmp+1
                    print(tmp)
                    if tmp == 15:
                        print(tmp)
                        refresh_2()
                if croix_rouge_2 is not None:
                    print("croix_rouge_2 trouvé")
                    mouse.position = (croix_rouge_2)  # Moves the mouse to the coordinates of the image
                    click()
                    tmp = 15
                    time.sleep(2)

def fleche_retour():
    print("recherche fleche_retour")
    fleche_retour = pyautogui.locateCenterOnScreen('fleche_retour.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
    if fleche_retour is not None:
        print("fleche_retour trouvé")
        mouse.position = (fleche_retour)  # Moves the mouse to the coordinates of the image
        click()
        tmp = 15
        time.sleep(0.5)
        click()
        time.sleep(2)
    else:
        tmp = 0
        if fleche_retour is None:
            while tmp < 15:
                if fleche_retour is None:
                    fleche_retour = pyautogui.locateCenterOnScreen('fleche_retour.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
                    print("fleche_retour pas trouvé")
                    time.sleep(1)
                    tmp = tmp+1
                    print(tmp)
                    if tmp == 15:
                        print(tmp)
                        refresh()
                if fleche_retour is not None:
                    print("fleche_retour trouvé")
                    mouse.position = (fleche_retour)  # Moves the mouse to the coordinates of the image
                    click()
                    time.sleep(0.5)
                    click()
                    tmp = 15
                    time.sleep(2)

def fleche_retour_2():
    print("recherche fleche_retour_2")
    fleche_retour_2 = pyautogui.locateCenterOnScreen('fleche_retour_2.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
    if fleche_retour_2 is not None:
        print("fleche_retour_2 trouvé")
        mouse.position = (fleche_retour_2)  # Moves the mouse to the coordinates of the image
        click()
        time.sleep(0.5)
        click()
        tmp = 15
        time.sleep(2)
    else:
        tmp = 0
        if fleche_retour_2 is None:
            while tmp < 15:
                if fleche_retour_2 is None:
                    fleche_retour_2 = pyautogui.locateCenterOnScreen('fleche_retour_2.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
                    print("fleche_retour_2 pas trouvé")
                    time.sleep(1)
                    tmp = tmp+1
                    print(tmp)
                    if tmp == 15:
                        print(tmp)
                        refresh_2()
                if fleche_retour_2 is not None:
                    print("fleche_retour_2 trouvé")
                    mouse.position = (fleche_retour_2)  # Moves the mouse to the coordinates of the image
                    click()
                    tmp = 15
                    time.sleep(2)


def treasure_hunt_2():
    print("recherche treasure_hunt_2")
    treasure_hunt_2 = pyautogui.locateCenterOnScreen('treasure_hunt_2.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
    if treasure_hunt_2 is not None:
        print("treasure_hunt_2 trouvé")
        mouse.position = (treasure_hunt_2)  # Moves the mouse to the coordinates of the image
        click()
        time.sleep(0.5)
        click()
        tmp = 15
        time.sleep(2)
    else:
        tmp = 0
        if treasure_hunt_2 is None:
            while tmp < 15:
                if treasure_hunt_2 is None:
                    treasure_hunt_2 = pyautogui.locateCenterOnScreen('treasure_hunt_2.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
                    print("treasure_hunt_2 pas trouvé")
                    time.sleep(1)
                    tmp = tmp+1
                    print(tmp)
                    if tmp == 15:
                        print(tmp)
                        refresh_2()
                if treasure_hunt_2 is not None:
                    print("treasure_hunt_2 trouvé")
                    mouse.position = (treasure_hunt_2)  # Moves the mouse to the coordinates of the image
                    click()
                    time.sleep(0.5)
                    click()
                    tmp = 15
                    time.sleep(2)


def treasure_hunt():
    print("recherche treasure_hunt")
    treasure_hunt = pyautogui.locateCenterOnScreen('treasure_hunt.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
    if treasure_hunt is not None:
        print("treasure_hunt trouvé")
        mouse.position = (treasure_hunt)  # Moves the mouse to the coordinates of the image
        click()
        tmp = 15
        time.sleep(2)
    else:
        tmp = 0
        if treasure_hunt is None:
            while tmp < 15:
                if treasure_hunt is None:
                    treasure_hunt = pyautogui.locateCenterOnScreen('treasure_hunt.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
                    print("treasure_hunt pas trouvé")
                    time.sleep(1)
                    tmp = tmp+1
                    print(tmp)
                    if tmp == 15:
                        print(tmp)
                        refresh()
                if treasure_hunt is not None:
                    print("treasure_hunt trouvé")
                    mouse.position = (treasure_hunt)  # Moves the mouse to the coordinates of the image
                    click()
                    tmp = 15
                    time.sleep(2)
   
def perso16():    
    perso16 = pyautogui.locateCenterOnScreen('perso16.png', region=(960, 0 , 2560, 1440), grayscale=False, confidence=0.90)
    if perso16 is not None:
        pyautogui.moveTo(perso16)  # Moves the mouse to the coordinates of the image
        click()
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 240
        pyautogui.moveTo(currentMouseX, currentMouseY)
        click()

def perso17():    
    perso17 = pyautogui.locateCenterOnScreen('perso17.png', region=(960, 0 , 2560, 1440), grayscale=False, confidence=0.80)
    if perso17 is not None:
        pyautogui.moveTo(perso17)  # Moves the mouse to the coordinates of the image
        click()
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 240
        pyautogui.moveTo(currentMouseX, currentMouseY)
        click()

def perso18():    
    perso18 = pyautogui.locateCenterOnScreen('perso18.png', region=(960, 0 , 2560, 1440), grayscale=False, confidence=0.80)
    if perso18 is not None:
        pyautogui.moveTo(perso18)  # Moves the mouse to the coordinates of the image
        click()
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 240
        pyautogui.moveTo(currentMouseX, currentMouseY)
        click()

def perso19():    
    perso19 = pyautogui.locateCenterOnScreen('perso19.png', region=(960, 0 , 2560, 1440), grayscale=False, confidence=0.99)
    if perso19 is not None:
        pyautogui.moveTo(perso19)  # Moves the mouse to the coordinates of the image
        click()
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 240
        pyautogui.moveTo(currentMouseX, currentMouseY)
        click()

def perso20():    
    perso20 = pyautogui.locateCenterOnScreen('perso20.png', region=(960, 0 , 2560, 1440), grayscale=False, confidence=0.80)
    if perso20 is not None:
        pyautogui.moveTo(perso20)  # Moves the mouse to the coordinates of the image
        click()
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 240
        pyautogui.moveTo(currentMouseX, currentMouseY)
        click()

def perso21():    
    perso21 = pyautogui.locateCenterOnScreen('perso21.png', region=(960, 0 , 2560, 1440), grayscale=False, confidence=0.90)
    if perso21 is not None:
        pyautogui.moveTo(perso21)  # Moves the mouse to the coordinates of the image
        click()
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 240
        pyautogui.moveTo(currentMouseX, currentMouseY)
        click()

def perso22():    
    perso22 = pyautogui.locateCenterOnScreen('perso22.png', region=(960, 0 , 2560, 1440), grayscale=False, confidence=0.99)
    if perso22 is not None:
        pyautogui.moveTo(perso22)  # Moves the mouse to the coordinates of the image
        click()
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 240
        pyautogui.moveTo(currentMouseX, currentMouseY)
        click()

def perso23():    
    perso23 = pyautogui.locateCenterOnScreen('perso23.png', region=(960, 0 , 2560, 1440), grayscale=False, confidence=0.99)
    if perso23 is not None:
        pyautogui.moveTo(perso23)  # Moves the mouse to the coordinates of the image
        click()
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 240
        pyautogui.moveTo(currentMouseX, currentMouseY)
        click()


def perso24():    
    perso24 = pyautogui.locateCenterOnScreen('perso24.png', region=(960, 0 , 2560, 1440), grayscale=False, confidence=0.99)
    if perso24 is not None:
        pyautogui.moveTo(perso24)  # Moves the mouse to the coordinates of the image
        click()
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 240
        pyautogui.moveTo(currentMouseX, currentMouseY)
        click()

def perso25():    
    perso25 = pyautogui.locateCenterOnScreen('perso25.png', region=(960, 0 , 2560, 1440), grayscale=False, confidence=0.99)
    if perso25 is not None:
        pyautogui.moveTo(perso25)  # Moves the mouse to the coordinates of the image
        click()
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 240
        pyautogui.moveTo(currentMouseX, currentMouseY)
        click()


def perso26():    
    perso26 = pyautogui.locateCenterOnScreen('perso26.png', region=(960, 0 , 2560, 1440), grayscale=False, confidence=0.99)
    if perso26 is not None:
        pyautogui.moveTo(perso26)  # Moves the mouse to the coordinates of the image
        click()
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 240
        pyautogui.moveTo(currentMouseX, currentMouseY)
        click()

def perso27():    
    perso27 = pyautogui.locateCenterOnScreen('perso27.png', region=(960, 0 , 2560, 1440), grayscale=False, confidence=0.99)
    if perso27 is not None:
        pyautogui.moveTo(perso27)  # Moves the mouse to the coordinates of the image
        click()
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 240
        pyautogui.moveTo(currentMouseX, currentMouseY)
        click()

"""def perso24():    
    perso24 = pyautogui.locateCenterOnScreen('perso24.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.99)
    if perso24 is not None:
        pyautogui.moveTo(perso24)  # Moves the mouse to the coordinates of the image
        click()
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 250
        pyautogui.moveTo(currentMouseX, currentMouseY)
        click()

def perso10():    
    perso10 = pyautogui.locateCenterOnScreen('perso10.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.99)
    if perso10 is not None:
        pyautogui.moveTo(perso10)  # Moves the mouse to the coordinates of the image
        click()
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 250
        pyautogui.moveTo(currentMouseX, currentMouseY)
        click()

def perso11():    
    perso11 = pyautogui.locateCenterOnScreen('perso11.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
    if perso11 is not None:
        pyautogui.moveTo(perso11)  # Moves the mouse to the coordinates of the image
        click()
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 250
        pyautogui.moveTo(currentMouseX, currentMouseY)
        click()

def perso12():    
    perso12 = pyautogui.locateCenterOnScreen('perso12.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
    if perso12 is not None:
        pyautogui.moveTo(perso12)  # Moves the mouse to the coordinates of the image
        click()
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 250
        pyautogui.moveTo(currentMouseX, currentMouseY)
        click()

def perso13_2():    
    perso13_2 = pyautogui.locateCenterOnScreen('perso13_2.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.99)
    if perso13_2 is not None:
        pyautogui.moveTo(perso13)  # Moves the mouse to the coordinates of the image
        click()
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 250
        pyautogui.moveTo(currentMouseX, currentMouseY)
        click()

def perso14_2():    
    perso14_2 = pyautogui.locateCenterOnScreen('perso14_2.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.99)
    if perso14_2 is not None:
        pyautogui.moveTo(perso14_2)  # Moves the mouse to the coordinates of the image
        click()
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 250
        pyautogui.moveTo(currentMouseX, currentMouseY)
        click()

def perso15_2():    
    perso15_2 = pyautogui.locateCenterOnScreen('perso15_2.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
    if perso15_2 is not None:
        pyautogui.moveTo(perso15_2)  # Moves the mouse to the coordinates of the image
        click()
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        time.sleep(2)
        currentMouseX = currentMouseX + 250
        pyautogui.moveTo(currentMouseX, currentMouseY)
        click()
"""

def vaguesuivante_2():    
    print("vaguesuivante_2") 
    g = 0
    while g < 3:
        pyautogui.scroll(-7)
        time.sleep(.5)
        g = g+1


def veille_2():
    print("debut veille_2")
    time.sleep(10)
    ok_error_2()
    time.sleep(20)
    mouse.position = (1520, 530)
    time.sleep(2)
    click()

def attack_legend_2():
    print(" debut attack legend")
    fleche_retour_2()
    time.sleep(2)
    heroes_2()
    time.sleep(2)
    all_2()
    time.sleep(2)
    all_rest_2()
    time.sleep(1)
    perso16 = pyautogui.locateCenterOnScreen('perso16.png', region=(960, 0 , 2560, 1440), grayscale=False, confidence=0.90)
    if perso16 is not None:
        pyautogui.moveTo(perso16)  # Moves the mouse to the coordinates of the image
        click()
    vaguesuivante_2()
    time.sleep(2)
    perso22()
    time.sleep(2)
    croix_rouge_2()
    time.sleep(2)
    treasure_hunt_2()
    time.sleep(2)




def attack_2_1speed():
    print("attack_all_2_1speed")
    fleche_retour_2()
    time.sleep(1)
    heroes_2()
    time.sleep(1)
    all_2()
    time.sleep(1)
    all_rest_2()
    time.sleep(1)
    perso17()
    time.sleep(1.5)
    perso18()
    time.sleep(1.5)
    vaguesuivante_2()
    time.sleep(1.5)
    perso21()
    time.sleep(1.5)
    perso25()
    time.sleep(1.5)
    vaguesuivante_2()
    time.sleep(1.5)
    perso26()
    time.sleep(1.5)
    croix_rouge_2()
    time.sleep(1)
    treasure_hunt_2()

def attack_2_2speed():
    print("attack_all_2_2speed")
    fleche_retour_2()
    time.sleep(1)
    heroes_2()
    time.sleep(1)
    all_2()
    time.sleep(1)
    all_rest_2()
    time.sleep(1)
    perso16()
    time.sleep(1.5)
    perso19()
    time.sleep(1.5)
    perso20()
    time.sleep(1.5)
    vaguesuivante_2()
    time.sleep(1.5)
    perso23()
    time.sleep(1.5)
    perso24()
    time.sleep(1.5)
    vaguesuivante_2()
    time.sleep(1.5)
    perso27()
    time.sleep(1.5)
    croix_rouge_2()
    time.sleep(1)
    treasure_hunt_2()

def ok_error():
    print("recherche error")    
    ok_error = pyautogui.locateCenterOnScreen('ok_error.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.70)
    if ok_error is not None:
        pyautogui.moveTo(ok_error)  # Moves the mouse to the coordinates of the image
        mouse.press(Button.left)  
        time.sleep(0.5)  
        mouse.release(Button.left)
        time.sleep(1)
        refresh()

def ok_error_2():
    print("recherche error_2")    
    ok_error_2 = pyautogui.locateCenterOnScreen('ok_error_2.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.70)
    if ok_error_2 is not None:
        pyautogui.moveTo(ok_error_2)  # Moves the mouse to the coordinates of the image
        mouse.press(Button.left)  
        time.sleep(0.5)  
        mouse.release(Button.left)
        time.sleep(1)
        refresh_2()
"""""
def meta():
    print("recherche meta") 
    meta = pyautogui.locateCenterOnScreen('meta.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
    if meta is not None:
        pyautogui.moveTo(meta)  # Moves the mouse to the coordinates of the image
        mouse.press(Button.left) 
        time.sleep(0.5) 
        mouse.release(Button.left)

def meta_2():
    print("recherche meta_2")
    meta_2 = pyautogui.locateCenterOnScreen('meta_2.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
    if meta_2 is not None:
        pyautogui.moveTo(meta_2)  # Moves the mouse to the coordinates of the image
        click()"""

"""def metamask():
    metamask = pyautogui.locateCenterOnScreen('metamask.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
    if metamask is not None:
        pyautogui.moveTo(metamask)  # Moves the mouse to the coordinates of the image
        click()

def metamask_2():
    metamask_2 = pyautogui.locateCenterOnScreen('metamask_2.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
    if metamask_2 is not None:
        pyautogui.moveTo(metamask_2)  # Moves the mouse to the coordinates of the image
        click()




def menu():
    print("recherche menu")
    menu = pyautogui.locateCenterOnScreen('menu.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
    if menu is not None:
        pyautogui.moveTo(menu)  # Moves the mouse to the coordinates of the image
        mouse.press(Button.left)
        time.sleep(0.5)
        mouse.release(Button.left)
        

def menu_2():
    print("recherche menu_2")
    menu_2 = pyautogui.locateCenterOnScreen('menu_2.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
    if menu_2 is None:
        pyautogui.moveTo(menu_2)  # Moves the mouse to the coordinates of the image
        mouse.press(Button.left)
        time.sleep(0.5)
        mouse.release(Button.left)"""

"""def refresh():
    print("recherche refresh")
    refresh = pyautogui.locateCenterOnScreen('refresh.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
    if refresh is not None:
        print("refresh trouvé")
        mouse.position = (refresh)  # Moves the mouse to the coordinates of the image
        click()
    if refresh is None:
        while refresh is None:
            refresh = pyautogui.locateCenterOnScreen('refresh.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
            print("refresh pas trouvé")
            time.sleep(2)
            if refresh is not None:
                print("refresh trouvé")
                mouse.position = (refresh)  # Moves the mouse to the coordinates of the image
                click()"""

def coffres():
    nb_cof = 0
    nb_cofv = 0
    nb_cofd = 0
    for pos in pyautogui.locateAllOnScreen('coffre.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.85):
        print(pos)
        nb_cof = nb_cof +1
        print(nb_cof)
    time.sleep(1)
    print("beuh")
    for pos in pyautogui.locateAllOnScreen('coffrev.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.85):
        print(pos)
        nb_cofv = nb_cofv +1
        print(nb_cofv)
    for pos in pyautogui.locateAllOnScreen('coffred.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.85):
        print(pos)
        nb_cofd = nb_cofd +2
        print(nb_cofv)
        if nb_cof + nb_cofv + nb_cofd > 20:
            attack_legend_2()
        
def coffres_2():
    nb_cof = 0
    nb_cofv = 0
    nb_cofd = 0
    for cof in pyautogui.locateAllOnScreen('coffre_2.png', region=(960, 0, 2560, 1440), grayscale=False, confidence=0.77):
        print(cof)
        nb_cof = nb_cof +1
        print(nb_cof)
    time.sleep(1)
    print("beuh")
    for cofv in pyautogui.locateAllOnScreen('coffrev_2.png', region=(960, 0, 2560, 1440), grayscale=False, confidence=0.73):
        print(cofv)
        nb_cofv = nb_cofv +1
        print(nb_cofv)
    for cofd in pyautogui.locateAllOnScreen('coffred_2.png', region=(960, 0, 2560, 1440), grayscale=False, confidence=0.85):
        print(cofd)
        nb_cofd = nb_cofd +2
        print(nb_cofd)
        
    nb_total = nb_cof + nb_cofv + nb_cofd
    print(nb_total)
    if nb_total > 15:
        attack_legend_2()
    if nb_total < 5:
        attack_all_rest_2()

def attack_all_rest_2():
    print("debut repos_all_rest_2")
    fleche_retour_2()
    time.sleep(2)
    heroes_2()
    time.sleep(2)
    all_rest_2()
    time.sleep(1)
    croix_rouge_2()
    time.sleep(1)
    treasure_hunt_2()


"""def coffrev():
    nb_cofv = 0
    for pos in pyautogui.locateAllOnScreen('coffrev.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.85):
        print(pos)
        nb_cofv = nb_cofv +1
        print(nb_cofv)"""
        

while not keyboard.is_pressed('esc'):
        
    refresh()
    time.sleep(1)
    refresh_2()
    time.sleep(1)  
    attack1speed()
    time.sleep(2)
    print("coucou")  
    attack_2_1speed()
    print("niceouuuuh")
    time.sleep(4)
    attack_2_2speed()
    print("beuuuuuuuuuuu")
    y = 0
    while y < 17:
        veille()
        veille_2()
        y = y +1
    coffres_2()
    time.sleep(5)
    attack2speed()
    y = 0
    while y < 15:
        veille()
        veille_2()
        y = y +1
        if y == 1:
            attack_all_rest_2()
    coffres_2()
    attack3speed()
    y = 0
    while y < 15:
        veille()
        veille_2()
        y = y +1
        if y == 1:
            attack_all_rest_2()
    
   
    """
    
    
    attack3speed()
    y = 0
    while y < 17:
        veille()
        veille_2()
        y = y +1
    
    """"""y = 0
    x = 0
    t = 0
    while y < 3:
        while x < 5:
            fenetre()
            fenetre_2()
            time.sleep(1)
            fleche_retour()
            time.sleep(1)
            fleche_retour_2()
            time.sleep(1)
            treasure_hunt()
            time.sleep(1)
            treasure_hunt_2()
            while t < 2:
                veille()
                veille_2()
                t = t + 1
            t = 0
            x = x+1
        fleche_retour()
        time.sleep(1)
        fleche_retour_2()
        time.sleep(4)
        treasure_hunt()
        time.sleep(1)
        treasure_hunt_2()
        y = y +1

    attack2speed()
    y = 0
    x = 0
    t = 0
    while y < 3:
        while x < 5:
            fleche_retour()
            time.sleep(1)
            fleche_retour_2()
            time.sleep(1)
            treasure_hunt()
            time.sleep(1)
            treasure_hunt_2()
            while t < 2:
                veille()
                veille_2()
                t = t + 1
            t = 0
            x = x+1
        fleche_retour()
        time.sleep(1)
        fleche_retour_2()
        time.sleep(4)
        treasure_hunt()
        time.sleep(1)
        treasure_hunt_2()
        y = y +1

    attack3speed()
    y = 0
    x = 0
    t = 0
    while y < 3:
        while x < 5:
            fleche_retour()
            time.sleep(1)
            fleche_retour_2()
            time.sleep(1)
            treasure_hunt()
            time.sleep(1)
            treasure_hunt_2()
            while t < 2:
                veille()
                veille_2()
                t = t + 1
            x = x+1
            t = 0
        fleche_retour()
        time.sleep(1)
        fleche_retour_2()
        time.sleep(4)
        treasure_hunt()
        time.sleep(1)
        treasure_hunt_2()
        y = y +1

    attack_all()
    time.sleep(10)
    attack_all_2()
    y = 0
    x = 0
    t = 0
    while y < 3:
        while x < 5:
            fleche_retour()
            time.sleep(1)
            fleche_retour_2()
            time.sleep(1)
            treasure_hunt()
            time.sleep(1)
            treasure_hunt_2()
            while t < 2:
                veille()
                veille_2()
                t = t + 1
            x = x+1
            t = 0
        fleche_retour()
        time.sleep(1)
        fleche_retour_2()
        time.sleep(4)
        treasure_hunt()
        time.sleep(1)
        treasure_hunt_2()
        y = y +1"""   




  