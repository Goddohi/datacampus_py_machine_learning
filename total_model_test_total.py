import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.linear_model import LassoLarsCV 
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from lightgbm import LGBMRegressor
from sklearn.svm import NuSVR
import xgboost as xgb
from sklearn.neural_network import MLPRegressor
from sklearn.svm import SVR


import warnings

# 경고 끄기
warnings.filterwarnings("ignore")
# 테스트데이터의 값
SEX = 1
AGE = 50
HT = 780
WT = 80
SELF = 5
DI1 = 0
DI2 = 0
DE1 = 0
DE2 = 0
DC = 0
DF = 0
HE = 0
D_Y = 1
D_M = 2
D_G = 2
SLP = 2
STRESS = 5
SMOKE = 0
SIT = 2
W_DAY = 3
LW_P = 0
LW_G = 0
LW_I = 0
LW_S = 0
L_BR = 0
L_LN = 0
L_DN = 3
WATER = 1

# 새로운 데이터 생성
new_data = pd.DataFrame({
    'SEX': [SEX],
    'AGE': [AGE],
    'HT': [HT],
    'WT': [WT],
    'SELF': [SELF],
    'DI1': [DI1],
    'DI2': [DI2],
    'DE1': [DE1],
    'DE2': [DE2],
    'DC': [DC],
    'DF': [DF],
    'HE': [HE],
    'D_Y': [D_Y],
    'D_M': [D_M],
    'D_G': [D_G],
    'SLP': [SLP],
    'STRESS': [STRESS],
    'SMOKE': [SMOKE],
    'SIT': [SIT],
    'W_DAY': [W_DAY],
    'LW_P': [LW_P],
    'LW_G': [LW_G],
    'LW_I': [LW_I],
    'LW_S': [LW_S],
    'L_BR': [L_BR],
    'L_LN': [L_LN],
    'L_DN': [L_DN],
    'WATER': [WATER]
})

# 데이터 불러오기 및 전처리
data = pd.read_csv('total16_21_masin8.csv', low_memory=False)
data = data.drop(['ID', 'year', 'BMI'], axis=1)
df = pd.DataFrame(data)
df = df.replace(' ', pd.NA)
df = df.dropna()


X = df.drop(['P_A_test', 'P_B1_test', 'P_B2_test', 'P_B3_test', 'P_B9_test', 'P_C_test', 'P_D_test', 'P_E_test', 'P_CA_test', 'P_K_test', 'P_MG_test', 'P_FE_test', 'P_ZN_test', 'VITA', 'VITB1', 'VITB2', 'VITB3', 'VITB9', 'VITC', 'VITD', 'VITE', 'CA', 'K', 'MG', 'FE', 'ZN'], axis=1)
#((환경별섭취량/권장량)*100)/70
y1 = df['P_A_test']
y2 = df['P_B1_test']
y3 = df['P_B2_test']
y4 = df['P_B3_test']
y5 = df['P_B9_test']
y6 = df['P_C_test']
y7 = df['P_D_test']
y8 = df['P_E_test']
y9 = df['P_CA_test']
y10 = df['P_K_test']
y11 = df['P_MG_test']
y12 = df['P_FE_test']
y13 = df['P_ZN_test']

# 정규화 진행
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
#############튜닝작업공간#####################

# train, test 셋 분리
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y13, test_size=0.2)
#model = RandomForestRegressor(random_state=42)
#model = LinearRegression()
model =  RandomForestRegressor(n_estimators=100, random_state=42)
#model  = DecisionTreeRegressor(random_state=0)
#model =   GradientBoostingRegressor(n_estimators=300, random_state=42)
#model = SVR(kernel='linear')#절대아님 과적합 예시 
#model = MLPRegressor(hidden_layer_sizes=(100, 50), max_iter=1000, random_state=0)
#model  = NuSVR()#XX
#model = LassoLarsCV(cv=5)  # 5-fold Cross-Validation #절대아님
#model= LGBMRegressor()
#model = xgb.XGBRegressor(n_estimators=150, random_state=0) #8000 5000 1000 2000 150 
model.fit(X_train, y_train)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

#평균 제곱 오차(MSE)를 출력 (평가지표)
mse = mean_squared_error(y_test, y_pred)
print(f"오차 제곱: {mse}")
# 예측 결과 저장
pre = model.predict(new_data)
print("Prediction for :", pre)
y_test = y_test.astype(float)
y_pred = y_pred.astype(float)

# 실제 값과 예측 값 비교 그래프
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue', alpha=0.5)
plt.xlabel('Real Values')
plt.ylabel('Predicted Values')
plt.title('Real vs. Predicted Values')
plt.show()

# 잔차 계산
residuals = y_test - y_pred

# 예측값과 실제값의 산점도 그리기 (차이에 따라 색상 구분)
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, c=residuals, cmap='RdBu', alpha=0.5)
plt.colorbar(label='Residuals')
plt.xlabel('Real Values')
plt.ylabel('Predicted Values')
plt.title('Real vs. Predicted Values with Color-coded Residuals')
plt.show()

# 잔차 그래프
plt.figure(figsize=(10, 6))
plt.scatter(y_test, residuals, color='blue', alpha=0.5)
plt.xlabel('Real Values')
plt.ylabel('Residuals')
plt.title('Residuals Plot')
plt.axhline(y=0, color='red', linestyle='--', linewidth=2)
plt.show()

# 잔차 그래프2

plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, c='blue', alpha=0.5)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], linestyle='--', color='red', linewidth=2)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs. Predicted Values')
plt.show()

