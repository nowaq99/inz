import pandas as pd
import configparser
import numpy as np
import librosa


def get_data_path(language, config=None):
    if not config:
        config = configparser.ConfigParser()
        config.read('config.ini')
    root_path = config['PATHS']['RootPath']
    val_path = config['PATHS']['ValPath']
    pl_names = config['LANGUAGE NAMES']['PlNames']
    eng_names = config['LANGUAGE NAMES']['EnNames']
    path = root_path
    if language in [i.strip() for i in pl_names.split(',')]:
        pl_path = config['PATHS']['PlPath']
        path = path + pl_path
    elif language in [i.strip() for i in eng_names.split(',')]:
        en_path = config['PATHS']['EnPath']
        path = path + en_path
    path = path + val_path[:-1]
    return path, config


def get_sample_path(sample_path, data_path, config=None):
    if not config:
        config = configparser.ConfigParser()
        config.read('config.ini')
    val_path = config['PATHS']['ValPath']
    audio_path = config['PATHS']['AudioPath']
    val_path_len = len(val_path)
    path = data_path[:-val_path_len] + '/' + audio_path + sample_path
    return path


def get_voice_paths(path):
    data = pd.read_csv(path, sep='\t')
    data['client_id'] = pd.factorize(data['client_id'])[0]
    data = data[['client_id', 'path', 'age', 'gender']]
    data = data.dropna(subset=['age'])
    return data