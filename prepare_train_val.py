import itertools
from prepare_data import data_path


def get_split(fold):
    folds = {0: [1, 2, 3, 17, 18],
             1: [4, 5, 6, 19, 20],
             2: [7, 9, 10, 21, 22],
             3: [11, 12, 13, 23, 24]}

    train_path = data_path / 'cropped_train'

    train_file_names = []
    val_file_names = []

    for instrument_id in itertools.chain(range(1, 13 + 1), range(17, 24 + 1)):
        if instrument_id in folds[fold]:
            val_file_names += list((train_path / ('seq_' + str(instrument_id)) / 'images').glob('*'))
        else:
            train_file_names += list((train_path / ('seq_' + str(instrument_id)) / 'images').glob('*'))

    return train_file_names, val_file_names
