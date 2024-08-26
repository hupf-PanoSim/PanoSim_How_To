from DataInterfacePython import *
import matplotlib.pyplot as plt

def ModelStart(userData):
    userData['sensor'] = BusAccessor(userData["busId"], 'UltrasonicSensor.0', 'time@i,1@[,distance@d')
    userData['last_time'] = 0
    userData['ts'] = []
    userData['distance'] = []
    plt.ion()
    plt.figure(dpi=100).canvas.set_window_title('PanoSim HowTo Sensor: Free Space Perception')

def ModelOutput(userData):
    timestamp, count = userData['sensor'].readHeader()
    if timestamp > userData['last_time']:
        userData['last_time'] = timestamp
        plt.clf()
        plt.title('Sensor: Free Space Perception')
        plt.xlabel('time(s)')
        plt.xlim((0, 20))
        plt.ylabel('distance(m)')
        plt.ylim((-1, 11))
        if count > 0:
            distance = userData['sensor'].readBody(0)[0]
            userData['ts'].append(timestamp / 1000)
            userData['distance'].append(distance)
        plt.plot(userData['ts'], userData['distance'])
        print(userData['ts'])
        plt.pause(interval=0.0001)

def ModelTerminate(userData):
    plt.ioff()
    plt.close()