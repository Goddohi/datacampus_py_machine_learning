import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.svm import SVC
import warnings
# 경고 끄기 끈이유는 가끔 테스트하다보면 데이터셋문제로 껐는데 필요는없다 
warnings.filterwarnings("ignore")

# 변수들의 값 ->DB로 받을것
'''
SEX = 1
AGE = 25
HT = 170
WT = 70
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
STRESS = 4
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
'''
SEX = 2
AGE = 23
HT = 168
WT = 47
SELF = 3
DI1 = 0
DI2 = 0
DE1 = 0
DE2 = 0
DC = 0
DF = 0
HE = 1
D_Y = 1
D_M = 2
D_G = 4
SLP = 3
STRESS = 3
SMOKE = 0
SIT = 2
W_DAY = 0
LW_P = 0
LW_G = 0
LW_I = 0
LW_S = 0
L_BR = 5
L_LN = 5
L_DN = 5
WATER = 1
#'''

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

#모델을 한개로 돌린이유 사실 model_1=  으로 해도되는데 test 파일이라 일단 model 복붙으로 처리 
# 데이터 불러오기 및 전처리
data = pd.read_csv('total16_21_masin8.csv', low_memory=False)
#다중 공선성문제 해결하는겸 불필요파일정리
data = data.drop(['ID', 'year', 'BMI'], axis=1)
df = pd.DataFrame(data)
#결측값제거
df = df.replace(' ', pd.NA)
df = df.dropna()

# 특성 변수 설정 (예측할 변수를 제외한 변수)
X = df.drop(['P_A_test', 'P_B1_test', 'P_B2_test', 'P_B3_test', 'P_B9_test', 'P_C_test', 'P_D_test', 'P_E_test', 'P_CA_test', 'P_K_test', 'P_MG_test', 'P_FE_test', 'P_ZN_test', 'VITA', 'VITB1', 'VITB2', 'VITB3', 'VITB9', 'VITC', 'VITD', 'VITE', 'CA', 'K', 'MG', 'FE', 'ZN'], axis=1)
#((환경별섭취량/권장량)*100)/70
# 각 목표 변수 설정
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


######################################
#############VITA#####################
######################################
# train, test 데이터셋 분리
# X_scaled와 y1 데이터를 80:20 비율로 훈련(train) 및 테스트(test) 데이터셋으로 분리합니다.
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y1, test_size=0.2)
# RandomForestRegressor 모델 초기화
# 랜덤 포레스트 회귀 모델을 생성하고, random_state를 42로 설정하여 재현성을 확보
#모델들은 각자 해놓은 이유는 각자 다른 튜닝을 할가능성이 있기 때문
model = RandomForestRegressor(random_state=42)
# 모델 학습## 훈련 데이터를 사용하여 모델을 학습
model.fit(X_train, y_train)
# 테스트 데이터에 대한 예측 수행
y1_pred = model.predict(X_test)

# 평가 - 평균 제곱 오차 (MSE) 출력 (평가지표)
# 실제값(y_test)과 예측값(y1_pred) 간의 평균 제곱 오차(MSE)를 계산하여 모델의 예측 성능을 평가합니다.

mse = mean_squared_error(y_test, y1_pred)
print(f"오차 제곱: {mse}")


# 새 데이터에 대한 예측 수행 및 출력
# new_data에 저장된 새로운 데이터를 사용하여 VITA 비타민 섭취량을 예측하고 결과를 p_vita에 저장합니다.
p_vita = model.predict(new_data)
print("Prediction for VITA:", p_vita)


#############VITB1##############
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y2, test_size=0.2)
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)
y2_pred = model.predict(X_test)

# 예측 결과 출력
p_vitb1 = model.predict(new_data)
print("Prediction for VITB1:", p_vitb1)

#############VITB2#############

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y3, test_size=0.2)
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)
y3_pred = model.predict(X_test)

# 예측 결과 출력
p_vitb2 = model.predict(new_data)
print("Prediction for VITB2:", p_vitb2)

#############VITB3##############
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y4, test_size=0.2)
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)
y4_pred = model.predict(X_test)

# 예측 결과 출력
p_vitb3 = model.predict(new_data)
print("Prediction for VITB3:", p_vitb3)

#############VITB9###############################

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y5, test_size=0.2)
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)
y5_pred = model.predict(X_test)

# 예측 결과 출력
p_vitb9 = model.predict(new_data)
print("Prediction for VITB9:", p_vitb9)

#############VITC###############################
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y6, test_size=0.2)
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)
y6_pred = model.predict(X_test)

# 예측 결과 출력
p_vitc = model.predict(new_data)
print("Prediction for VITC:", p_vitc)

#############VITD###############################

# train, test 셋 분리
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y7, test_size=0.2)
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)
y7_pred = model.predict(X_test)

# 예측 결과 출력
p_vitd = model.predict(new_data)
print("Prediction for VITD:", p_vitd)

#############VITE###############################
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y8, test_size=0.2)
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)
y8_pred = model.predict(X_test)

# 예측 결과 출력
p_vite = model.predict(new_data)
print("Prediction for VITE:", p_vite)

#############CA###############################
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y9, test_size=0.2)
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)
y9_pred = model.predict(X_test)

# 예측 결과 출력
p_ca = model.predict(new_data)
print("Prediction for CA:", p_ca)

#############KKKKKK###############################
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y10, test_size=0.2)
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)
y10_pred = model.predict(X_test)

# 예측 결과 출력
p_k = model.predict(new_data)
print("Prediction for K:", p_k)


#############MG###############################
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y11, test_size=0.2)
model = RandomForestRegressor(random_state=42)
#model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)
y11_pred = model.predict(X_test)

# 예측 결과 출력
p_mg = model.predict(new_data)
print("Prediction for MG:", p_mg)

#############FE###############################
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y12, test_size=0.2)
model = RandomForestRegressor(random_state=42)
#model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)
y12_pred = model.predict(X_test)


#평균 제곱 오차(MSE)를 출력 (평가지표)
mse = mean_squared_error(y_test, y12_pred)
print(f"오차 제곱: {mse}")
# 예측 결과 출력
p_fe = model.predict(new_data)
print("Prediction for FE:", p_fe)

#############ZN###############################
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y13, test_size=0.2)
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)
y13_pred = model.predict(X_test)

# 예측 결과 출력
p_zn = model.predict(new_data)
print("P_ZN:", p_zn)

######################################
# 예측 결과를 딕셔너리에 저장
# 영양소에 대한 예측 결과를 딕셔너리에 저장합니다.
predictions = {
    'p_vita': p_vita, 'p_vitb1': p_vitb1, 'p_vitb2': p_vitb2, 'p_vitb3': p_vitb3,
    'p_vitb9': p_vitb9, 'p_vitc': p_vitc, 'p_vitd': p_vitd, 'p_vite': p_vite,
    'p_ca': p_ca, 'p_k': p_k, 'p_mg': p_mg, 'p_fe': p_fe, 'p_zn': p_zn
}
# 최소값을 가진 변수 찾기
# predictions 딕셔너리에서 예측값 중 최소값을 가진 변수명을 찾습니다.
min_mineral = min(predictions, key=lambda x: predictions[x][0])
# 최소값을 가진 영양소의 예측값 출력
print("최소 예측 영양소:", min_mineral)

min_mineral_value = globals()[min_mineral]
print("최소영양소수치:", min_mineral_value)

# 영양에 대한 코드 매핑
code_mapping = {
    'p_vita': '10000', 'p_vitb1': '10001', 'p_vitb2': '10010', 'p_vitb3': '10011',
    'p_vitb9': '10100', 'p_vitc': '10101', 'p_vitd': '10110', 'p_vite': '10111',
    'p_ca': '11000', 'p_k': '11001', 'p_mg': '11010', 'p_fe': '11011', 'p_zn': '11100'
}
# 최소값을 가진 영양에 해당하는 코드 가져오기
min_mineral_code = code_mapping.get(min_mineral)
# 결핍 여부 확인 및 출력 (70%이상 ->  권장/필수량이상)
if min_mineral_value < 70 :
    print("결핍:", min_mineral,min_mineral_code)#code DB로 보낼것
else :
    print("건강") #code 11111로 설정해서 보낼것 DB에 보낼것
