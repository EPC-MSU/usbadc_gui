import urpcadcgui.urpcadc as urpcadc
import serial.tools.list_ports
import time

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

device = urpcadc.UrpcadcDeviceHandle("com:///dev/ttyACM0")
# device = urpcadc.UrpcadcDeviceHandle("com:\\\\.\\COM5")
# data = device.get_identity_information()
# time.sleep(10)
timer = time.time()
for i in range(100000):
    data = device.get_conversion()
    print(data.data[0])
timer = time.time() - timer
device.close_device()

print(timer)
