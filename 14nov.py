USERNAME = 'OOIAPI-TFWIQ9W27S5XJI'
TOKEN = 'TSB1PZMOBD1H4T'

import requests, json
from pprint import pprint #pprint used to format json objects.  pprint(data[0]) is formatted to be legible.

#response = requests.get('https://ooinet.oceanobservatories.org/api/m2m/12576/sensor/inv/RS03CCAL/MJ03F/05-BOTPTA301/streamed/botpt_nano_sample?beginDT=2017-07-04T17:54:58.050Z&endDT=2017-07-04T17:55:58.050Z&limit=1000&parameters=7,848', auth=(USERNAME, TOKEN)) #the bt sensor
#response = requests.get('https://ooinet.oceanobservatories.org/api/m2m/12576/sensor/inv/RS03INT1/MJ03C/10-TRHPHA301/streamed/trhph_sample?beginDT=2017-11-07T00:00:00.000Z&limit=1000', auth=(USERNAME, TOKEN))     #the trhph

try:
    while True:
        response = requests.get('https://ooinet.oceanobservatories.org/api/m2m/12576/sensor/inv/RS03INT1/MJ03C/10-TRHPHA301/streamed/trhph_sample?beginDT=2017-11-07T00:00:00.000Z&limit=1000', auth=(USERNAME, TOKEN))
    
        data = response.json()
    #for the TRHPH
        time = data[0]['time']                          #sec since 1-1-1900
        temperature = data[0]['vent_fluid_temperaure']  #deg C
        chloride = data[0]['vent_fluid_chloride_conc']  #mmol/kg
        print(time, temperature, chloride)
except KeyboardInterrupt:
    print('Halting data acquisition')