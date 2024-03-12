import pyautogui as pg
from time import sleep

# Considerações:
# * Só funciona em Windows
# * Se der erro no clicke, use uma resolução próxima de 1366 x 768
# * !! Necessário instalar a biblioteca 'pyautogui' antes de usar o programa
#   (Pra fazer isso, digite 'pip install pyautogui' no seu terminal e espere instalar)
# * !!! Caso dê erro o código, jogue seu mouse para o canto superior esquerdo que o programa para instantâneamente.
# * Tempo médio de duração do programa: 2 Minutos e 50 Segundos

pg.PAUSE = 0.1 # Pausa entre os comandos do pyautogui(Aumentar se seu PC for mais lento!!)
def limpapasta(pasta, ignarquiv, replimpeza):
    pg.hotkey('win', 'r')
    pg.press('backspace')
    pg.write(pasta) # Entra na pasta atráves do menu executar
    pg.press('enter')
    sleep(1)
    pg.hotkey('win', 'up') # Maximiza a janela
    sleep(1)
    pg.click(x=779, y=360) 
    pg.press('enter') # Confirma a permissão à pasta pela primeira vez
    sleep(1)
    pg.click(x=528, y=0)
    sleep(1)
    pg.hotkey('alt', 'f4')
    # Repetir processo sem permissão agora (É aberto 2 vezes porque não
    # trabalhar com esse tipo de condições ainda)

    for i in range(replimpeza): # Número de vezes que vai o processo de limpeza.
        pg.hotkey('win', 'r')
        pg.press('backspace')
        pg.write(pasta)
        pg.press('enter')
        sleep(1)
        pg.hotkey('ctrl', 'a')
        pg.hotkey('shift', 'del')
        sleep(1)
        pg.press('enter')
        sleep(1)

        # Deleta todos os arquivos primeiro
        pg.press('up')
        pg.press('enter')
        pg.press('down')
        pg.press('enter')
        sleep(10) # <- Mudar o tempo caso seu computador demorar mais para excluir !!!

        # Ignora os arquivos restantes que não podem ser excluídos
        for i in range(ignarquiv): # <- Número de vezes que ele vai ignorar arquivos restantes
            pg.press('up')
            pg.press('enter')
            pg.press('down')
            pg.press('right')
            pg.press('enter')
            sleep(5)
        pg.click(x=528, y=0)
        pg.hotkey('alt', 'f4')
        sleep(1)
    # Limpeza concluído

# Função limpapasta(Nome da pasta, Vezes que o programa vai apertar o botão de ignorar arquivos, Vezes que o programa vai repetir limpeza).

limpapasta('temp', 1, 2) # Exclui cache da pasta temp
limpapasta('%temp%', 2, 2) # Excluicache da pasta %temp%
limpapasta('prefetch', 1, 1) # Exclui cache da pasta prefetch
limpapasta('C:\Windows\SoftwareDistribution\Download', 1, 1) # Exclui cache da pasta 'C:\Windows\SoftwareDistribution\Download'

# Limpa cache da Windows Store (WSReset.exe)
pg.hotkey('win', 'r')
pg.press('backspace')
pg.write('WSReset.exe') # Executa o programa que limpa o cache automaticamente
pg.press('enter')
sleep(10)
pg.hotkey('alt', 'f4')

# Limpa o cache do DNS (ipconfig /flushdns)
pg.hotkey('win', 'r')
pg.press('backspace')
pg.write('cmd') # Abre o prompt de comando
pg.press('enter')
sleep(1)
pg.write('ipconfig /flushdns')
pg.press('enter')
sleep(2)
pg.hotkey('alt', 'f4')
