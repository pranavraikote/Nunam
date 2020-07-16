# -*- coding: utf-8 -*-
"""
Created on Wed Jul  15 23:06:24 2020

@author: Pranav
"""

import re
import pandas as pd
from profilehooks import profile

class Nunam:
    
    def __init__(self):
        pass
    
    #Function for calling
    #@profile(filename = 'read_stats', stdout = False)
    @profile(immediate = True)
    def read_and_extract(self, name, sheet):
        '''
        
        Parameters
        ----------
        name : String
            Name of the Excel Workbook with extension. Ex: abcd.xls
        sheet : String
            Name of the particular Sheet required in the workbook in ReGex format. Ex: '^Detail_'
                
        Returns
        -------
        detail_1 : pandas.DataFrame
            Dataframe which consists data loaded from the given Sheetname and Workbook name
    
        '''
        
        r = re.compile(sheet)
        workbook_1 = pd.read_excel(name, sheet_name = None)
        sheet_n = list(filter(r.match, workbook_1.keys()))
        detail_1 = pd.DataFrame(workbook_1[sheet_n[0]])
    
        return detail_1
    
    #@profile(filename = 'concat_stats', stdout = False)
    @profile(immediate = True)
    def concat_dataframes(self, df1, df2):
        '''
        
        Parameters
        ----------
        df1 : pandas.DataFrame
            First Dataframe 
        df2 : pandas.DataFrame
            Second Dataframe
    
        Returns
        -------
        pandas.Dataframe
            Concatenated DataFrame of given 2 DataFrames 
    
        '''
        
        return pd.concat([df1, df2], ignore_index = True)
    
    #@profile(filename = 'sampling_stats', stdout = False)
    @profile(immediate = True)
    def resample_data(self, df1, index, drop_column = None):
        '''
        
        Parameters
        ----------
        df1 : pandas.DataFrame
            Input DataFrame for which sampling needs to be done
        index : string
            Setting the DatetimeIndex for setting that index for sampling
        drop_column : List, optional
            List of name of columns to be dropped while sampling. The default is None.
    
        Returns
        -------
        pandas.DataFrame
            Sampled DataFrame
    
        '''
    
        df1.set_index(index, inplace = True)
        if drop_column == None:
            return df1.resample('1Min').mean()
        else:
            df1.drop(drop_column, axis = 1, inplace = True)
            return df1.resample('1Min').mean()
    
    
    def run(self):
        '''
        Function for loading the data (Function call to read_and_extract) and sampling (Function call to resample_data)
        
        Returns
        -------
        None.
    
        '''
        
        #Reading and extracting the Detail_ sheet from both workbooks
        global w1_detail
        global w2_detail
        w1_detail = self.read_and_extract('5308.xls', '^Detail')
        w2_detail = self.read_and_extract('5329.xls', '^Detail')
        
        #Reading and extracting the DetailVol_ sheet from both workbooks
        w1_detail_vol = self.read_and_extract('5308.xls', '^DetailVol_')
        w2_detail_vol = self.read_and_extract('5329.xls', '^DetailVol_')
        
        #Reading and extracting the DetailTemp_ sheet from both workbooks
        w1_detail_temp = self.read_and_extract('5308.xls', '^DetailTemp_')
        w2_detail_temp = self.read_and_extract('5329.xls', '^DetailTemp_')
        
        #Combining sheets data into one dataframe taken from both workbooks
        detail_dataframe = self.concat_dataframes(w1_detail, w2_detail)
        detail_vol_dataframe = self.concat_dataframes(w1_detail_vol, w2_detail_vol)
        detail_temp_dataframe = self.concat_dataframes(w1_detail_temp, w2_detail_temp)
        
        #Setting DatetimeIndex, and deleting the Record ID for resampling of detail_dataframe
        resampled_data_detail = self.resample_data(detail_dataframe, 'Absolute Time', ['Record Index'])
        resampled_data_vol = self.resample_data(detail_vol_dataframe, 'Realtime', ['Record ID'])
        resampled_data_temp = self.resample_data(detail_temp_dataframe, 'Realtime', ['Record ID'])
        
        #Printing Sampled DataFrames
        print(resampled_data_detail.head(10))
        print(resampled_data_vol.head(10))
        print(resampled_data_temp.head(10))
