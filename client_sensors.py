from requests import get, post
import time

base_url = 'http://34.154.14.199:80'
sensor = 's1'
#leggo il file
with open('CleanData_PM10.csv') as f:
    #leggo tutte le righe del file e salto la prima riga (intestazione)
    for l in f.readlines()[1:]:
        data,val = l.strip().split(',')
        print(data,val)
        r = post(f'{base_url}/sensors/{sensor}',
                 data={'data':data,'val':val})
        time.sleep(5) # ogni 5 secondi effettua chiamata


print('done')
