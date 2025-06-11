import pyautogui
import time

def main():

    # 1. abrir o Google chrome
    print("O robô começará em 1 segundos...")
    time.sleep(1)
    pyautogui.rightClick(x=518, y=1056)
    time.sleep(1)
    pyautogui.click(x=440, y=936)
    time.sleep(5)

    # 2. Abrindo o diario de bordo
    pyautogui.click(x=199, y=100) #abre o diário de bordo
    time.sleep(15)
    pyautogui.click(x=1427, y=379) #clica no seletor de agrupamentos
    time.sleep(1)
    pyautogui.click(x=1447, y=410) #limpa os agrupamentos
    time.sleep(1)


    # 3. Adicionando novo lançamento de horas
    pyautogui.click(x=167, y=309) #clica em adicionar novo item
    time.sleep(1)
    pyautogui.click(x=792, y=397) #clica no campo do titulo
    time.sleep(1)
    pyautogui.write(" Projeto: 86dwr15hr - NIO | Wi-Fi 6 Atendimento Digital", interval=0.1)
    time.sleep(1)
    pyautogui.scroll(-200)
    time.sleep(1)
    pyautogui.click(x=624, y=413) #clica em horas trabalhadas
    time.sleep(1)
    pyautogui.write("7,5", interval=0.1)
    time.sleep(1)
    pyautogui.click(x=568, y=500) #clica em tipo de atividade
    time.sleep(1)
    pyautogui.click(x=566, y=544) #escolhe o tipo de atividade
    time.sleep(1)
    pyautogui.click(x=568, y=585) #clica em projeto da carteira
    time.sleep(1)
    pyautogui.write("NIO | Wi", interval=0.1)
    time.sleep(1)
    pyautogui.click(x=573, y=621) #clica no projeto
    time.sleep(1)
    pyautogui.click(x=569, y=671) #clica em etapa
    time.sleep(1)
    pyautogui.click(x=576, y=860) #escolhe a etapa
    time.sleep(1)
    pyautogui.click(x=573, y=753) #clica em squad
    time.sleep(1)
    pyautogui.click(x=573, y=840) #escolhe squad
    time.sleep(1)
    pyautogui.click(x=570, y=843) #clica em fabrica
    time.sleep(1)
    pyautogui.click(x=565, y=957) #escolhe fabrica
    time.sleep(1)

    # 4. salva
    pyautogui.click(x=1273, y=973) #salva apontamento


if __name__ == "__main__":
    main()
