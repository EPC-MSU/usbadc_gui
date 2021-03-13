import usbadc10gui.usbadc10 as usbadc10
import serial.tools.list_ports
import time
import numpy as np
sample_number = 10000
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
systimer = time.time()
x = np.empty(1000)
x[...] = None
y = np.empty((1000, 10))
y[...] = None
data_to_scv = np.empty((0, 11))
start_stop_recording_status = True
for i in range(sample_number):
    try:
        time_now = time.time() - systimer
        data = device.get_conversion()
        x = np.append(x[1:], time_now)
        y = np.vstack((y[1:, :], np.array(data.data)/10000))
        if start_stop_recording_status:
            data_to_scv = np.vstack((data_to_scv,
                                     np.append(time_now, y[-1, :])))
    except usbadc10.UrpcDeviceUndefinedError:
        break
    # print(np.array(data.data)/10000)
systimer = time.time() - systimer
device.close_device()

print(systimer/sample_number)
