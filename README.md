**House Price Prediction Web App**
 **Overview**
This project is a machine learning-powered web application for predicting real estate prices based on key property features. The model is trained on the King County House Sales dataset and deployed using Streamlit for an interactive user experience.
**dataset link: https://drive.google.com/file/d/1yo0tcwIDSeSVsrDY55qLUw83dKgoTdqp/view?usp=sharing**
**pickel model link(https://drive.google.com/file/d/1CpebN94qLXx3vpgKWHXCz1bzG1JheGgD/view?usp=sharing)**
🚀 **Features**
- Predicts house prices based on user input
-Location-based predictions (Latitude & Longitude)
- Confidence interval for price estimation
-Feature importance visualization

**model performance**
The Random Forest Regressor model was trained with the following results:

Train R² Score: 0.9780

Test R² Score: 0.8272

**Tech Stack**
Machine Learning: Scikit-learn, XGBoost

**Web Framework:** Streamlit

**Data Processing:** Pandas, NumPy

**Installation & Usage**
1.Clone the repository:
git clone https://github.com/keltaimpex/house_price_prediction.git
cd house_price_prediction
2.Install dependencies:
pip install -r requirements.txt
3.Run the app:
streamlit run stapp.py
