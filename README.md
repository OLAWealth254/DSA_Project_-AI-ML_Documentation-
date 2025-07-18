# DSA_Project_-AI-ML_Documentation-


## Diabetes Risk Predictor

The notebook analyzes a dataset of individual from community A to uncover key factors contributing to diabetes. Exploratory Data Analysis and Machine Learning was used to indentify patterns and derive insights.

A machine learning web application was built to analyze and predict diabetes risk using real-world epidemiological data from community A health profile.



### Project Objectives

- Analyze patterns in blood sugar levels.
- Identify key diabetes risk factors.
- Build a supervised machine learning model.
- Deploy a Flask web app for real-time prediction.



### Dataset

*Filename: `Diabetics Profile.xlsx`  
*Source: Community A Epidemiological Review(kaggle) 

*Features: Includes patient profiles, blood sugar readings, and potential risk indicators(Age,Pregnancies,Glucose,BloodPressure (mg/dL) SkinThickness,Insulin,BMI	DiabetesPedigreeFunction)



### Technologies Used

- Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)
- Flask (Web Framework)
- HTML/CSS (Frontend)
- Jupyter Notebook (EDA and Modeling)
- Excel (Data format)


### ML Model

A supervised classification model (e.g., Logistic Regression, Random Forest) trained to predict the likelihood of diabetes based on input features.



### Project Structure

- Data: Raw dataset
- Notebook: Jupyter notebook with full analysis and model building
- App: Flask web app code and model
- Templates: HTML templates for Flask
- Static: CSS for UI
- Requirements.txt: Python dependencies



### Instructions

1. Clone the repository
git clone https://github.com/OLAWealth/diabetes-risk-predictor.git
cd diabetes-risk-predictor

2. Create a virtual environment
python -m venv venv
source venv/bin/activate  
On Windows: venv\Scripts\activate

3 Install dependencies
* pip install -r requirements.txt

4.Run the app
  cd app
python app.py

5.Visit: http://127.0.0.1:5000
Input patient data to get real-time diabetes risk prediction.
Input patient data to get real-time diabetes risk prediction.


### Requirements.txt

* flask
* pandas
* numpy
* scikit-learn
* matplotlib
* seaborn
* openpyxl


### Insights and Recommendations 
* High glucose,BMI,and Age are leading indicators of diabetes risk in this community.
* Individuals over 45 with high BMI should be priotized for intervention.
* Skin thickness and insulin levels shows weaker predictive power here.
* Recommend routine screening and lifestyle counseling for high-risk groups.

  
### Author
 Olarewaju.O.Gift 
