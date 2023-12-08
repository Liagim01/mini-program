'''
Main program file
'''
from classifier import Classifier
from tokenizer import Tokenizer
from preprocessor import Preprocessor
from data_loader import DataLoader
def main():
    # Initialize modules and classes
    classifier = Classifier()
    tokenizer = Tokenizer()
    preprocessor = Preprocessor()
    data_loader = DataLoader()
    # Load input data
    input_data = data_loader.load_data()
    # Preprocess and split data
    preprocessed_data = preprocessor.preprocess(input_data)
    train_data, test_data = preprocessor.split_data(preprocessed_data)
    # Tokenize text
    tokenized_text = tokenizer.tokenize(train_data)
    # Perform classification
    predictions = classifier.classify(tokenized_text)
    # Output results
    print(predictions)
if __name__ == "__main__":
    main()