import socket
import json


def get_constants(prefix):
    """Create a dictionary mapping socket module constants to their names."""
    return dict((getattr(socket, n), n)
                for n in dir(socket)
                if n.startswith(prefix)
                )


families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

# Create a TCP/IP socket
sock = socket.create_connection(('localhost', 10000))

print('Family  :', families[sock.family])
print('Type    :', types[sock.type])
print('Protocol:', protocols[sock.proto])
print()

try:

    # Send data
    config_path = 'test.json'
    with open(config_path, 'r') as file:
        message = json.load(file)
    # message = 'This is the message.  It will be repeated.'
    print('sending json message:', message)
    sock.sendall(json.dumps(message).encode('utf-8'))

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        # amount_received += len(data)
        # parsed_data = json.loads(data)
        print('received', data)
        # print('received "%s"' % data)

finally:
    print('closing socket')
    sock.close()
