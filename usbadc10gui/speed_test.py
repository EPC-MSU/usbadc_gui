import usbadc10gui.usbadc10 as usbadc10
import serial.tools.list_ports
import time
import numpy as np

ports = serial.tools.list_ports.comports(include_links=True)
valid_ports = []


for port in sorted(ports):
    print(port.device)
    try:
        s = serial.Serial(port.device)
        s.close()
        valid_ports.append(port)
    except (OSError, serial.SerialException):
        pass

device = usbadc10.Usbadc10DeviceHandle("com:///dev/ttyACM0")
# device = usbadc10.usbadc10DeviceHandle("com:\\\\.\\COM5")
# data = device.get_identity_information()
# time.sleep(10)
timer = time.time()
for i in range(100000):
    # a = np.roll(a, -1)
    # a = np.append(a[1:], a[-1])
    data = device.get_conversion()
    print(np.array(data.data)/10000)
timer = time.time() - timer
device.close_device()

print(timer)
