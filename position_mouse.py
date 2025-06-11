import pyautogui
import time

print("Você tem 5 segundos para posicionar o mouse onde deseja.")
time.sleep(1)
posicao = pyautogui.position()
print(f"A posição do mouse é: {posicao}")
