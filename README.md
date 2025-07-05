# 🧠 Mental Health Treatment Predictor

A Streamlit-based machine learning app that predicts the likelihood of an individual seeking mental health treatment based on personal and workplace factors.

🔗 Live app: [Launch App](https://mental-health-predictor-3awvy97txhyhei2sdj2frg.streamlit.app/)

![App Banner](https://images.unsplash.com/photo-1620147461831-a97b99ade1d3?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8bWVudGFsJTIwaGVhbHRofGVufDB8fDB8fHww)  
> _Built with ❤️ using Logistic Regression and public survey data_

---

## 🚀 Features

- Clean UI built with **Streamlit**
- **Logistic Regression** model trained on real mental health survey data
- Interactive form for users to input workplace and personal attributes
- Visual explanation of model performance (confusion matrix, reports)
- Deployed as a web app

---

## 🧰 Tech Stack

- Python
- pandas, scikit-learn, joblib
- Streamlit
- XGBoost, Matplotlib, Seaborn (for EDA)
- Deployed on Netlify / Streamlit Cloud

---

## 📁 Project Structure

```bash
Mental-Health-Predictor/
├── app.py                   # Streamlit app
├── models/
│   └── model.joblib         # Trained ML model
├── requirements.txt         # For environment setup
└── README.md                # You're here
```

---

## 📦 Installation (Local)

```bash
git clone https://github.com/ShravanKulkarni1004/Mental-Health-Predictor.git
cd Mental-Health-Predictor
pip install -r requirements.txt
streamlit run app.py
```

---

## 📊 Model Performance

| Model             | Accuracy | Recall (Class 1) | F1 (Class 1) |
|------------------|----------|------------------|--------------|
| Logistic Reg.     | 75.6%    | 0.73             | 0.76         |
| Random Forest     | 72.4%    | 0.67             | 0.72         |
| XGBoost           | 67.2%    | 0.62             | 0.67         |
| Decision Tree     | 64.0%    | 0.56             | 0.62         |

---

## 📌 Dataset

- Data Source: [Kaggle Mental Health in Tech Survey](https://www.kaggle.com/datasets/osmi/mental-health-in-tech-survey)
- Cleaned and processed for binary classification

---

## 📬 Contact

For feedback or collaboration, reach out on [LinkedIn](https://www.linkedin.com/in/shravan-kulkarni-966586288/)

---

## 📜 License

This project is open-source and available under the MIT License.

## ✍️ Author
Shravan Kulkarni
