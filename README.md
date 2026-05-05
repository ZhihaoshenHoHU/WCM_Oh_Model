# WCM + Oh2004 Soil Moisture Retrieval

## 📌 Overview

This repository implements a **soil moisture retrieval framework** based on the combination of:

* **Water Cloud Model (WCM)**
* **Oh (2004) surface scattering model**

The model separates vegetation and soil contributions from SAR backscatter and retrieves **surface soil moisture (SSM)** using an inversion scheme.

---

## ⚙️ Model Description

### 1. Oh (2004) Model

Used to simulate soil backscatter:
[
\sigma_{VV} = f(SM, \theta, ks)
]

### 2. Water Cloud Model (WCM)

Separates total backscatter into:

* Vegetation scattering
* Soil scattering (attenuated by vegetation)

### 3. Inversion Workflow

1. Normalize SAR backscatter to a reference incidence angle
2. Fit WCM parameters using optimization (DE + curve_fit)
3. Estimate soil backscatter
4. Invert soil moisture using Oh2004 model
5. Evaluate using RMSE and correlation

---

## 📁 Project Structure

```
WCM_Oh_Model/
│
├── main.py                  # Main workflow
├── config.py                # Path and parameter settings
│
├── models/                  # Physical & semi-empirical models
│   ├── oh_model.py
│   ├── wcm_model.py
│
├── calibration/             # Parameter optimization
│   ├── optimizer.py
│
├── utils/                   # Utility functions
│   ├── metrics.py
│   ├── plotting.py
│
├── data.xlsx                # Input data (user provided)
├── outputs/                 # Results (auto-generated)
└── README.md
```

---

## 📊 Input Data Format

The input Excel file (`data.xlsx`) should contain at least the following columns:

| Column Index | Description                   |
| ------------ | ----------------------------- |
| 5            | Vegetation Index (e.g., NDVI) |
| 7            | VV backscatter (dB)           |
| 10           | Incidence angle (degrees)     |
| 11           | Soil moisture (ground truth)  |

---

## 🚀 Usage

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Prepare data

Place your dataset as:

```
data.xlsx
```

### 3. Run the model

```
python main.py
```

---

## 📈 Outputs

The following outputs will be generated in `/outputs`:

* `result.xlsx` → Predicted vs observed soil moisture
* `scatter.png` → Scatter plot (SM_obs vs SM_pred)

---

## 📏 Evaluation Metrics

* RMSE (Root Mean Square Error)
* Pearson Correlation Coefficient (R)

---

## 🔬 Features

✔ Joint WCM + Oh2004 inversion
✔ Automatic parameter optimization (Differential Evolution + Least Squares)
✔ Incidence angle normalization
✔ Modular and reusable code structure
✔ Ready for scientific research and publication

---

## ⚠️ Notes

* Ensure input data is clean (no NaN or invalid values)
* Backscatter must be in **dB** format
* NDVI or other vegetation indices should be normalized

---
