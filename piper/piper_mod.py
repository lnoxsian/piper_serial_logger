import serial.tools.list_ports
import serial
import orjson

def find_ports(disp=False):
    all_ports=[]
    for port in serial.tools.list_ports.comports():
        all_ports.append([port.device,port.name])
    if disp:
        print(all_ports)
    return all_ports

def read_json(filename):
    with open(filename,'r+') as jfile:
        alldata=orjson.loads(jfile.read())
    return alldata

def read_data(comport,baudrate):
    with serial.Serial(comport,baudrate,timeout=1) as ser:
        return ser.readline() # reads one line






