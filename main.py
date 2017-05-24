from machine import Pin, PWM
import socket
import array

def unpackCommand4Bytes(input):
    # Only lower two bytes are used for command
    return input[0] + input[1]*(2**8)

pinR = 5
pinG = 4
pinB = 0

pwmR = PWM(Pin(pinR), freq=120, duty=512)
pwmG = PWM(Pin(pinG), freq=120, duty=512)
pwmB = PWM(Pin(pinB), freq=120, duty=512)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('0.0.0.0', 45225)
sock.bind(server_address)
sock.listen(1)

while True:
    print('ready for another connection')
    connection, client_address = sock.accept()

    print('got connection from client_address', client_address)
    _valR = connection.recv(4)
    _valG = connection.recv(4)
    _valB = connection.recv(4)

    valR = unpackCommand4Bytes(array.array("l", reversed(_valR)))
    valG = unpackCommand4Bytes(array.array("l", reversed(_valG)))
    valB = unpackCommand4Bytes(array.array("l", reversed(_valB)))

    print('decoded RGB', valR, valG, valB)

    pwmR.duty(valR)
    pwmG.duty(valG)
    pwmB.duty(valB)

    # return OK message
    connection.send(b'\x00\x00\x00\x01')

    connection.close()
