from sys import argv
import network

class Classify:
    IP_parameter = str(argv[1])
    #IP_parameter = '192.29.1.999/16'
    myNetwork = network.Network(IP_parameter)
    print(myNetwork.class_type())
    print(myNetwork.ip_type())


    #print("This is the name of the program:", IP_parameter)
