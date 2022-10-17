from prepare_data import data_path


def get_split(fold):
    folds = {0: [1, 2, 3],
             1: [4, 5, 6],
             2: [7, 8, 9],
             3: [10, 11, 12]}

    train_path = data_path / 'cropped_train'

    train_file_names = []
    val_file_names = []

    for instrument_id in range(1, 12):
        if instrument_id in folds[fold]:
            val_file_names += list((train_path / ('seq_' + str(instrument_id)) / 'images').glob('*'))
        else:
            train_file_names += list((train_path / ('seq_' + str(instrument_id)) / 'images').glob('*'))

    return train_file_names, val_file_names
