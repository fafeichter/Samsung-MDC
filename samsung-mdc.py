# Samsung Multiple Display Control (MDC) protocol
#
# I made this simple program to disable the key-lock of my Samsung 400DXn-2 screen.
#
# Use Python 2.x!

import serial
  
port = "/dev/tty.usbserial-A600bWIe"
baud = 9600

ser = serial.Serial(port, baud, timeout=1)

if ser.isOpen():
     print(ser.name + ' is open...')

DisableKeyLockAll = bytearray([0xaa, 0x5F, 0xFE, 0x1, 0x0, 0x5e])
DisableChildLockAll = bytearray([0xaa, 0x5D, 0xFE, 0x1, 0x0, 0x5c])
PowerOffAll = bytearray([0xaa, 0x11, 0xFE, 0x1, 0x0, 0x10])
PowerOnAll =  bytearray([0xaa, 0x11, 0xFE, 0x1, 0x1, 0x11])

ser.write(DisableKeyLockAll)
out = ser.read()
print('Receiving...')
for c in out:
    print (ord(c))

ser.close()