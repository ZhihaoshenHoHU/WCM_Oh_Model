import numpy as np
import pandas as pd

from config import DATA_PATH, REF_ANGLE, OUTPUT_DIR
from models.oh_model import Oh2004_inverse
from models.wcm_model import fitFunc
from calibration.optimizer import optimize_params
from utils.metrics import rmse, correlation
from utils.plotting import plot_sm

# === 1. 读取数据 ===
data = pd.read_excel(DATA_PATH)
x = data.values

sigma0 = 10**(x[:, 7] / 10)
thr = x[:, 10] * np.pi / 180
VI = x[:, 5]
SM = x[:, 11]

# === 入射角归一化 ===
sigma0 = sigma0 * (np.cos(np.deg2rad(REF_ANGLE))**2) / (np.cos(thr)**2)
thr = np.deg2rad(REF_ANGLE)

# === 2. 搜索 ks ===
ks_list = np.arange(0.1, 10, 0.1)

best_rmse = 999
best_params = None

for ks in ks_list:
    params = optimize_params(SM, thr, ks, sigma0, VI)

    sigma_soil = fitFunc((sigma0, VI), *params)
    ypred = Oh2004_inverse(sigma_soil, thr, ks)

    error = rmse(SM, ypred)

    print(f"ks={ks:.2f}, RMSE={error:.4f}")

    if error < best_rmse:
        best_rmse = error
        best_params = params
        best_ks = ks
        best_pred = ypred

# === 3. 输出结果 ===
print("\nBest result:")
print("ks =", best_ks)
print("params =", best_params)
print("RMSE =", best_rmse)
print("R =", correlation(SM, best_pred))

# 保存结果
df = pd.DataFrame({
    "SM_obs": SM,
    "SM_pred": best_pred
})
df.to_excel(f"{OUTPUT_DIR}/result.xlsx", index=False)

# === 4. 绘图 ===
plot_sm(SM, best_pred, f"{OUTPUT_DIR}/scatter.png")