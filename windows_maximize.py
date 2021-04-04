import win32gui, win32con
import time

while 1:

    try:
        hwnd = win32gui.FindWindow(None, "ProfitPro - 5.0.0.95 - Registrado")
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsIconic(hwnd):
            print ("Tela Minimizada")
            # win32gui.SetForegroundWindow(hwnd)
            win32gui.ShowWindow(hwnd, win32con.SW_SHOWMAXIMIZED)
        else:
            print ("Tela Maximizada")
    except:
        print("An exception occurred")

    time.sleep(5)
