import pandas as pd
import requests

def get_and_format_accident_data(file_name):
    '''
    input: file name
    output: pandas data frame
    '''
    parse_dates = ['addr']
    accident = pd.read_csv(file_name)
    accident=accident[accident.long.notnull()]
    accident=accident[accident.lat.notnull()]
    accident=accident[accident.addr.notnull()]
    accident.to_pickle('/media/danguir/Transcend/MASciR/ni/myapp/resources/accident.pkl')
    return accident
