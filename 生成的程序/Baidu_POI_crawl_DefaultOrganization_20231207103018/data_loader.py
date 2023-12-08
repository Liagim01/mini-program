'''
DataLoader class
'''
import random
class DataLoader:
    def load_data(self):
        # Load input data
        data = {
            'text': [
                'This is a positive sentence.',
                'This is a negative sentence.',
                'Another positive sentence.',
                'Another negative sentence.'
            ],
            'label': [
                1,
                0,
                1,
                0
            ]
        }
        return data