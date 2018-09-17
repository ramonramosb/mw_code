import serial
from time import sleep

com_port = 'COM3'

# I'll start with just the bare code for the sythhd and then add the server

class SynthHDSerial():
    def __init__(self):
        self.serv = serial.Serial(com_port, 38400, timeout=0, parity = serial.PARITY_EVEN)

    def set_freq(self, mesg):
        freq, ch = mesg['freq'], mesg['ch']
        if (not (ch in ['0','1'])):
            return {'success': 0}
        if (not (type(freq) == float and (freq<=13000.0) and (freq>=100.0))):
            return {'success': 0}

        # str_send = 'C'+ ch + 'f' + str(freq)
        self.serv.write('C'+ ch + 'f' + str(freq))
        # self.socket.send('C'+ ch + 'f' + str(freq))
        return {'success': 1}


    def set_amp(self, mesg):
        amp, ch = mesg['amp'], mesg['ch']
        if (not (ch in ['0','1'])):
            return {'success': 0}
        if (not (type(amp) == int and (amp<=45000) and (amp>=0))):
            return {'success': 0}

        # str_send = 'C'+ ch + 'a' + str(amp)
        self.serv.write('C'+ ch + 'a' + str(amp))
        # self.socket.send('C'+ ch + 'a' + str(amp))
        return {'success': 1}


    def set_phase(self, mesg):
        phase, ch = mesg['phase'], mesg['ch']
        if (not (ch in ['0','1'])):
            return {'success': 0}
        if (not (type(phase) == int and (phase<=359) and (phase>=0))):
            return {'success': 0}

        # str_send = 'C'+ ch + '~' + str(phase)
        self.serv.write('C'+ ch + '~' + str(amp))
        # self.socket.send('C'+ ch + '~' + str(phase))
        return {'success': 1}


    def help(self):
        str_send = '?'
        self.serv.write(str_send)
        sleep(1)
        reply = self.serv.read(2000)
        print(reply)