## Task 2 - Exploratory Data Analysis (EDA) 🔍

A credit risk modeling project aimed at developing a robust probability of default model for a digital lending service. The project follows a structured data science pipeline including EDA, feature engineering, and modeling — in partnership with an eCommerce company offering Buy Now, Pay Later services.

---

## 📁 Project Structure

credit-risk-model/

│

├── data/

│ └── raw/ # Contains original raw datasets

│ ├── data.csv

│ └── Xente_Variable_Definitions.csv

│

├── notebooks/

│ └── 1.0-eda.ipynb # Jupyter notebook for exploratory analysis

│

├── src/ # Scripts for data processing and modeling

│ └── (To be developed)

│

├── images/ # Visual outputs/screenshots from EDA

│ └── eda_distribution.png

│

├── requirements.txt # Python dependencies (to be completed)

├── .gitignore # Ignore Python cache, data, and Jupyter checkpoints

├── README.md # Project overview and documentation

└── INTERIM_PROGRESS.md # Interim report with analysis summary and progress


---

## 🎯 Project Objective

To build a machine learning model that predicts the likelihood of loan default, supporting responsible lending decisions for an eCommerce BNPL (Buy Now, Pay Later) service. This aligns with **Basel II** compliance by quantifying **Probability of Default (PD)** and improving credit risk assessment.

---

## 🔍 Task 2 - Exploratory Data Analysis (EDA)

### ✅ Objective  
Explore the dataset to uncover its structure, quality, and key patterns — laying the foundation for informed feature engineering and modeling decisions.

### 📊 Key Activities

- **Data Structure** – Inspected shape, columns, and datatypes.
- **Summary Statistics** – Assessed central tendency and spread.
- **Numerical Feature Distribution** – Visualized with histograms and boxplots.
- **Categorical Feature Distribution** – Checked category frequencies and imbalances.
- **Correlation Analysis** – Used heatmaps to study feature relationships.
- **Missing Values** – Evaluated nulls and concluded no missing data exists.
- **Outlier Detection** – Used boxplots to flag extreme values.

### 📌 Insights

- No missing values ➡️ reduces need for imputation.
- Strong skew and outliers in financial features.
- Some features show multicollinearity.
- Categorical features show imbalance.
- Dataset size is sufficient for modeling.


## ⚙️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Dagi2730/credit-risk-model.git
   cd credit-risk-model
2. Create and activate virtual environment:

python -m venv venv

venv\Scripts\activate   # Windows

3. Install dependencies:

pip install -r requirements.txt

4. Launch Jupyter Notebook:

jupyter notebook

🚧 Next Steps

Implement feature engineering in src/

Build transformation pipelines using sklearn.pipeline.Pipeline

Encode categorical features (One-Hot / Label Encoding)

Handle outliers and normalization

Begin model development and evaluation

🧰 Tools & Libraries

Python 3.12

Pandas, NumPy

Matplotlib, Seaborn

Jupyter Notebook

(Upcoming: Scikit-learn, XGBoost, SHAP)

🗂️ Status

✅ EDA Completed

🕒 Feature Engineering – Pending

🕒 Modeling – Not Yet Started

