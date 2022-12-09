import serial
import lewansoul_lx16a
from lewansoul_lx16a_controller import ServoController
import time
from math import sin, cos

def main():
    detection = True #will be linked to computer vision

    while detection == True:
    # Oscillate servos out of phase
    #Parametric locomotion method
        servo1.move(sin(t) * 120 - 180) #right intake system
        servo2.move(sin(t) * 120 + 180) #left intake system
        time.sleep(0.05)
        t += 0.05

def homing_routine():
    SERIAL_PORT = '/dev/cu.usbserial-14340'

    #set initial motor positions
    initial_servo1_pos = 0
    initial_servo2_pos = 90

    controller = lewansoul_lx16a.ServoController(
        serial.Serial(SERIAL_PORT, 115200, timeout=1),
    )

    try:
        servo1 = controller.servo(1)
        servo2 = controller.servo(2)

    except ServoTimeoutError as e:
        print(f"Servo {e.id_} is not responding. Exiting...")
        exit()

    while LX16A.getPhysicalPos(servo1) != initial_servo1_pos:
        servo1.move(initial_servo1_pos)
    while LX16A.getPhysicalPos(servo2) != initial_servo2_pos:
        servo2.move(initial_servo2_pos)
   
def shutdown_routine():
    SERIAL_PORT = '/dev/cu.usbserial-14340'

    #set initial motor positions
    end_servo1_pos = 0
    end_servo2_pos = 0
    

    controller = lewansoul_lx16a.ServoController(
        serial.Serial(SERIAL_PORT, 115200, timeout=1),
    )

    try:
        servo1 = controller.servo(1)
        servo2 = controller.servo(2)
       

    except ServoTimeoutError as e:
        print(f"Servo {e.id_} is not responding. Exiting...")
        exit()

    while LX16A.getPhysicalPos(servo1) != end_servo1_pos:
        servo1.move(end_servo1_pos)
    while LX16A.getPhysicalPos(servo2) != end_servo2_pos:
        servo2.move(end_servo2_pos)
    

def boot_test():
    SERIAL_PORT = '/dev/cu.usbserial-14340'
    controller = lewansoul_lx16a.ServoController(
        serial.Serial(SERIAL_PORT, 115200, timeout=1),
    )
    try:
        servo1 = controller.servo(1)
        servo2 = controller.servo(2)
  

    except ServoTimeoutError as e:
        print(f"Servo {e.id_} is not responding. Exiting...")
        exit()

    #Checks voltage
    voltage_response = self._query(servo1, SERVO_VIN_LIMIT_READ, timeout=timeout)
    voltage_response2 = self._query(servo2, SERVO_VIN_LIMIT_READ, timeout=timeout)





if __name__ == "__main__":
    main()
    #getPositions()
