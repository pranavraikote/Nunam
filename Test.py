# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 02:01:00 2020

@author: Pranav
"""

#Import the class from Nunam.py, libraries
from Nunam import Nunam
import unittest
import pandas as pd

class TestNunam(unittest.TestCase):
    
    #Function to test the concat_dataframes function
    def test_concat(self):
        
        dfz = pd.DataFrame.from_dict({
                'Record ID': [1, 1],
                'Gap of Voltage': [0.0, 0.0]
                })
        
        dfz1 = pd.DataFrame.from_dict({
                'Record ID': [2, 2],
                'Gap of Voltage': [0.0, 0.0]
                })

        output = pd.DataFrame.from_dict({
            'Record ID': [1, 1, 2, 2],
            'Gap of Voltage': [0.0, 0.0, 0.0, 0.0]
            })
        a = n.concat_dataframes(dfz, dfz1)
        pd.testing.assert_frame_equal(a, output, check_names=False, check_index_type = False)
    
    #Function to test the read_and_extract function
    def test_read_and_extract(self):
        
        b = n.read_and_extract('Book1.xls', 'Sheet1')
        
        output = pd.DataFrame.from_dict({
            'Record ID': [1],
            'Step Name': ['Rest'],            
            'Realtime': ['11-15-2019 19:38:18'],
            'Auxiliary channel TU1 U(V)': [-0.0046],
            'Gap of Voltage': [0]
            })
        
        pd.testing.assert_frame_equal(b, output)
        
    def test_sampling(self):
        
        a = n.read_and_extract('Book2.xls', 'Sheet1')
        b = n.resample_data(a, 'Realtime', ['Record ID'])
        
        output = pd.DataFrame.from_dict({
            'Realtime': ['2019-11-15 19:38:00'],
            'Auxiliary channel TU1 U(V)': [-0.004436],
            'Gap of Voltage': [0]
            })
        
        output.set_index(pd.DatetimeIndex(output['Realtime']), inplace = True)
        
        pd.testing.assert_frame_equal(b, output, check_names=False, check_index_type = False)
    
if __name__ == '__main__':
    #Instantiating the Nunam class for accessing the functions
    n = Nunam()
    unittest.main()