# main.py
from model import AttentionModel
from train import train_model
from data_loader import load_data

def main():
    # Load dataset
    train_data, test_data = load_data()

    # Initialize model
    model = AttentionModel()

    # Train model
    train_model(model, train_data, test_data)

if __name__ == "__main__":
    main()
