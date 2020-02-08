import pandas as pd
import os

def hello():
    return 'hello world'

def create_table(start_date,slots: int = 6, size: str = '10min' ):
    index = pd.date_range(start_date, periods=slots, freq=size ,tz='Europe/Berlin')
    empty_data = ['']*slots
    data = zip(empty_data,empty_data)
    df = pd.DataFrame(data=data, index=index, columns=['Name' , 'Notiz'])
    df.index.name = " Datum /Uhrzeit"
    return df

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

def get_data_from_path(path):
    data_names = []
    possible_anf = []
    for file in files(path):
        possible_anf.append(file.split(".csv")[0])
        data_names.append(file)
    return dict(zip(possible_anf,data_names))