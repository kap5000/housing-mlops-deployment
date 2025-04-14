import gradio as gr
import joblib
import pandas as pd

model = joblib.load('model.pkl')

def predict_price(area, bedrooms, bathrooms):
	data = pd.DataFrame({'area': [area], 'bedrooms': [bedrooms], 'bathrooms': [bathrooms]})
	prediction = model.predict(data)
	return prediction[0]

demo = gr.Interface(fn=predict_price, inputs=["number", "number", "number"], outputs="number", title="House Price Predictor")
if __name__ == "__main__":
	demo.launch()
