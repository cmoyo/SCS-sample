# Test_sim_1.py
"""
This module contains the test Trading Agent simulator.

"""

import Fodiac_api

class Model:
    """Simple model that sends values *SD* of format *datatype* to each
    device with *device_addr* every step.
    
    You can optionally set the initial value *init_val*. It defaults to
    "0".
    
    """

    def __init__(self, device_addr, datatype):
        self.device_addr= device_addr
        self.datatype=datatype
        self.val=[0,0,0,0]
        

    def step(self, SD):
        """Perform a simulation step by sending data to device.

        *self.val* contains data response from device """

        self.SD=SD

        for i in range(4):
            self.val[i]=send_to_FDIAC(self.device_addr[i], self.datatype[i], self.SD[i])


class Simulator(object):
    """Simulates a number of "Model" models and collects some data."""

    def __init__(self):
        self.models=[]
        self.data=[]

    def add_model(self, device_addr, datatype):
        """Create instances of "Model" with *init_val*."""
        model=Model(device_addr, datatype)
        self.models.append(model)
        self.data.append([]) #Add list for simulation data

    def step(self, tx_data=None):
        """Set new model inputs from *tx_data* to the models and perform
        a simulation step.

        *tx_data* is a dictionary that maps model indices to new transmit
        values for the model.

        """

        if tx_data:
            #Set new data for transmission to model instances
            for idx, SD in tx_data.items():
                self.models[idx].SD=SD

        #Step models and collect data
        for i, model in enumerate(self.models):
            model.step()
            self.data[i].append(model.val)



if __name__=='__main__':
    #This is how the simulator could be used:
    sim=Simulator()

    dev1_tcp=[61501, 61502, 61503, 61504]
    dev2_tcp=[61505, 61506, 61507, 61508]
    tcp_list=[dev1_tcp, dev2_tcp]

    d_type1=['real','real','real', 'real']
    d_type2=['real','real','real', 'real']
    data_list=[d_type1, d_type2]
    
    
    for i in range(2):
        sim.add_model(device_addr=tcp_list[1],datatype=data_list[1])
    sim.step()
    sim.step({0: [2000,-1800,300,55], 1: [3000,-2500,700,-70]})
    print('Simulation finished with data:')
    for i, inst in enumerate(sim.data):
        print('%d: %s' % (i, inst))
'''
