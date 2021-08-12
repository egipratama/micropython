from machine import UART
import time

# for esp 32 using serial 2
uart = UART(2, 9600)                        
uart.init(9600, bits=8, parity=None, stop=1)

while(1):
    data = []
    for i in range(4):
        data.append(uart.read(1))
    if data[0]:
        _header = int.from_bytes(data[0], "big")
        _data_h = int.from_bytes(data[1], "big")
        _data_l = int.from_bytes(data[2], "big")
        _check_sum = int.from_bytes(data[3], "big")
        
        checksum = (_header + _data_h + _data_l)&0x00ff
        
        if checksum == _check_sum:
            distance = _data_h * 255 + _data_l
            if distance > 280:
                print(str(distance/10) + " cm")
            else:
                print("blank spot distance")
        else:
            print("error read sensor")

    time.sleep(0.100)
