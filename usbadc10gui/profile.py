import usbadc10gui.usbadc10 as usbadc10
import numpy as np
import time

device = usbadc10.Usbadc10DeviceHandle("com:///dev/ttyACM0")
x = np.linspace(-0.2*1000, 0, 1000)
y = np.zeros((1000, 10))
data_to_scv = np.empty((0, 11))
systimer = time.time()
for i in range(100000):
    time_now = time.time() - systimer
    data = device.get_conversion()
    x = np.append(x[1:], time_now)
    y = np.vstack((y[1:], data.data))
    # if self.gstates[i]:
    #     self.linias[i].setData(self.x, self.y[:, i])
    # data_to_scv = np.vstack((data_to_scv, np.append(time_now, y[-1, :])))
time_now = time.time() - systimer
print(data_to_scv)
print(time_now)
