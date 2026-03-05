import pyperclip, time

print('Obteniendo texto copiado... (Ctrl-C para detener)')
previous_content = ''
try:
    while True:
        content = pyperclip.paste() 
        if content != previous_content:
            print(content)
            previous_content = content
        time.sleep(0.1) 
except KeyboardInterrupt:
    pass