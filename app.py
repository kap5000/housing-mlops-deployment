import gradio as gr
import joblib
import pandas as pd

model = joblib.load('model.pkl')

def predict_price(square_feet, num_rooms):
	data = pd.DataFrame({'square_feet': [square_feet], 'num_rooms': [num_rooms]})
	prediction = model.predict(data)
	return prediction[0]

demo = gr.Interface(fn=predict_price, inputs=["number", "number"], outputs="number", title="House Price Predictor")
if __name__ == "__main__":
	demo.launch()
