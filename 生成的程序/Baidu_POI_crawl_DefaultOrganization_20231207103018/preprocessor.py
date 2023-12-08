'''
Preprocessor class
'''
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
class Preprocessor:
    def preprocess(self, data):
        # Preprocess data
        preprocessed_data = self.normalize_data(data)
        return preprocessed_data
    def split_data(self, data):
        # Split data into training and testing sets
        train_data, test_data = train_test_split(data, test_size=0.2)
        return train_data, test_data
    def normalize_data(self, data):
        # Normalize data
        scaler = StandardScaler()
        normalized_data = scaler.fit_transform(data)
        return normalized_data