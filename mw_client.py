from synth_code_andserver import ClientForServer, SynthHDSerial

clientmw = ClientForServer(SynthHDSerial, 'tcp://localhost:5556')
