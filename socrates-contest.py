import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(('', 9000))

class Funcs():
    
    def ADD(self, params):
        return int(reduce(lambda x,y: float(x)+float(y), params))

    def SUBTRACT(self, params):
        return int(reduce(lambda x,y: float(x)-float(y), params))
    
    def MULTIPLY(self, params):
        return int(reduce(lambda x,y: float(x)*float(y), params))

funcs_object = Funcs()
while True:
    data, addr = sock.recvfrom(1024)
    print 'Got:', data
    if '__SHUTDOWN__' in data:
        break
    d = data.split(':')
    func, uuid, params = d[0], d[1], d[2:]
    #Python3k Only: func, uuid, *params = d
    result =  getattr(funcs_object, func)(params)
    sock.sendto('%s:%s' %(uuid, result), ('localhost', 9001))
    
    
