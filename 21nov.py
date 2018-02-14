USERNAME = 'OOIAPI-TFWIQ9W27S5XJI'
TOKEN = 'TSB1PZMOBD1H4T'

import time

#response = requests.get('https://ooinet.oceanobservatories.org/api/m2m/12576/sensor/inv/
#RS03INT1/MJ03C/10-TRHPHA301/streamed/trhph_sample?
#beginDT=2017-11-07T00:00:00.000Z&limit=1000', auth=(USERNAME, TOKEN))#the trhph

startURL = "https://ooinet.oceanobservatories.org/api/m2m/12576/sensor/inv/"
endURL = "Z&limit=1000, auth=(" + USERNAME + ", " + TOKEN + "))"

data = [0,1,2,3,4,5,6,7,8,9]

try:
##    while True:
##        sensor_name = raw_input("sensor name?  ")
##        start_date = raw_input("starting date (y-m-d)?  ")
##        end_date = raw_input("ending date (y-m-d)?  ")
##        pointNo = int(raw_input("# data points (up to 10)?  "))
##        timeframe = start_date + " : " + end_date
##        #url = startURL + sensor_name + endURL
##
##        for currentGo in range(pointNo):
##            url = startURL + sensor_name + str(data[currentGo]) + endURL
##            print(url)
##            print(timeframe)

    sensor_name = sensor_name = raw_input("sensor path from /inv/?  ")
    start_date = raw_input("starting date (y-m-d)?  ")
    start_time = raw_input("starting time (00:00:00.000)?  ")
    end_date = raw_input("ending date (y-m-d)?  ")
    pointNo = int(raw_input("# data points (up to 10)?  "))
    timeframe = start_date + " : " + end_date
    url = ""
    for x in range(pointNo):
        url = startURL + sensor_name + "beginDT=" + start_date + "T" + start_time + endURL
        start_date = str(int(start_date) + 00:00:01.000)
        print(url)
        print(data[x])
except KeyboardInterrupt:
    print('Halting data acquisition')
