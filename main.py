import pyautogui
import time
import sys
import datetime


def main():
    pyautogui.MINIMUM_DURATION = 1.2  # opóźnienie ruchu przy funkcji moveTo(), która jest wykorzystywana w funkcji
    # click()

    time.sleep(5)

    while True:

        x = datetime.datetime.now()

        if x.hour >= 16 and x.minute >= 0 and (x.isoweekday() == 2 or x.isoweekday() == 4):

            while True:
                wsp = pyautogui.locateCenterOnScreen(
                    r'C:\Users\Mariusz\PycharmProjects\Bot_wegiel\venv\zdjecia\screen_odswiezanie_szare.png', grayscale=
                    True, region=(0, 0, 300, 400))
                time.sleep(1)
                wsp2 = pyautogui.locateCenterOnScreen(
                    r'C:\Users\Mariusz\PycharmProjects\Bot_wegiel\venv\zdjecia\screen_przycisk_v2.png',
                    region=(1000, 500, 600, 400))

                if (wsp is not None) and (wsp2 is not None):
                    # time.sleep(1)  # opoźnienie dla niepoznaki
                    pyautogui.click(x=wsp2.x, y=wsp2.y)
                    print('Nastąpiło kliknięcie')
                    return 0
                if (wsp is not None) and (wsp2 is None):
                    pyautogui.press('f5')


if __name__ == "__main__":
    main()
# wsp_x, wsp_y = pyautogui.position()

# print(f'x: {wsp.x}, y: {wsp.y}')
# print(f'x: {wsp_x}, y: {wsp_y}')


