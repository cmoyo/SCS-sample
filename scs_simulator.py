# scs_simulator.py
"""
This module contains a simple example simulator.

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
        

    def step(self, SD):
        """Perform a simulation step by sending data to device.

        *self.val* contains data response from device """
        
        self.SD=SD
        self.val=send_to_FDIAC(self.device_addr, self.datatype, self.SD)


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
        """Set new transmit data inputs from *tx_data* to the models and perform
        a simulation step.

        *tx_data* is a dictionary that maps model indices to new transmit
        values for the model.

        """

        if tx_data:
            #Set new data for transmission to model instances
            for idx, in_val in tx_data.items():
                self.models[idx].in_val=in_val

        #Step models and collect data
        for i, model in enumerate(self.models):
            model.step()
            self.data[i].append(model.val)


'''
if __name__=='__main__':
    #This is how the simulator could be used:
    sim=Simulator()
    for i in range(2):
        sim.add_model(init_val=0)
    sim.step()
    sim.step({0: 23, 1: 42})
    print('Simulation finished with data:')
    for i, inst in enumerate(sim.data):
        print('%d: %s' % (i, inst))
'''
