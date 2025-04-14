# Housing Price Prediction - Deployment Workflow

This repository contains a deployment workflow for predicting housing prices based on features like area, bedrooms, and bathrooms.

## Repository Contents
- `Housing.csv`: The dataset used for training the model.
- `model.pkl`: A pre-trained model used for making predictions.
- `app.py`: A script which provides a web interface for predictins using Gradio.

## Usage Instructions
To run this project, you will need Python installed on your local machine. Follow these steps:

Clone the repository:
    ```bash
    git clone https://github.com/<your-username>/housing-mlops-deployment.git
    cd housing-mlops-deployment
Install the required Python libraries:
    pip install gradio joblib pandas
Run the application
    python app.py
    
This will launch a local Gradio interface in your browser where you can input housing features and get a price prediction.
