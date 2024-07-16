# datacampus_py_machine_learning
This project is a  website developed as a result of DataCampus Healthcare AI Project, which guides users on nutritional deficiencies through body data. We possess the dataset, and we regret to inform you that we cannot distribute it due to copyright restrictions.


이 파일은 연습 및 학습 목적으로 사용되었으며, 데이터셋은 의료데이터관련 제한으로 인해 업로드할 수 없습니다.
또한 연습과 학습을 통해 완성된 머신러닝완성본은 제공할 수 없기에 머신러닝 테스트 파일만 올렸습니다

아래 데이터셋의 문제점은 연속성변수와 명목형변수의 차이를 모르고 만든 문제점이 있습니다 
해당 문제점을 인지하고 제파일을 교육에 도움이 되길바랍니다 

다음은 데이터 관련 처리 내용입니다:

SEX: 성별 (1: 남자 / 2: 여자)
AGE: 만 나이
HT: 신장 (소수점 없음)
WT: 체중 (소수점 없음)
SELF: 주관적 건강상태 (1: 매우 좋음 / 2: 좋음 / 3: 보통 / 4: 나쁨 / 5: 매우 나쁨)
DI1: 고혈압 현재 유병 여부 (0: 없음 / 1: 유병)
DI2: 이상지질혈증 현재 유병 여부 (0: 없음 / 1: 유병)
DE1: 당뇨병 현재 유병 여부 (0: 없음 / 1: 유병)
DE2: 갑상선 질환 현재 유병 여부 (0: 없음 / 1: 유병)
DC: 암 현재 유병 여부 (0: 없음 / 1: 유병)
DF: 우울증 현재 유병 여부 (0: 없음 / 1: 유병)
HE: 빈혈 현재 유병 여부 (0: 없음 / 1: 유병)
D_Y: 평생 음주 여부 (0: 없음 / 1: 음주)
D_M: 1년간 음주 빈도 (0: 0회 / 1: 월 1회 이하 / 2: 월 2-4회 / 3: 주 2-3회 / 4: 주 4회 이상)
D_G: 한 번에 마시는 음주량 (0: 0 / 1: 1-2잔 / 2: 3-4잔 / 3: 5-6잔 / 4: 7-9잔 / 5: 10잔 이상)
SLP: 하루 평균 수면 시간 (시간) (1: 1-2시간 / 2: 3-4시간 / 3: 5-6시간 / 4: 7시간 이상)
STRESS: 평소 스트레스 인지 정도 (1: 매우 많음 / 2: 많음 / 3: 조금 받음 / 4: 거의 안 받음)
SMOKE: 현재 흡연 여부 (0: 아니오 / 1: 예)
SIT: 일상적으로 앉아 있는 시간 (1: 0-2시간 / 2: 2-6시간 / 3: 7-11시간 / 4: 12시간 이상)
W_DAY: 주간 60분 이상 운동한 일 수 (0: 없음 / 1: 1-2일 / 2: 3-4일 / 3: 5-6일 / 4: 매일)
LW_P: 폐경 여부 (0: 없음 / 1: 있음)
LW_G: 경구 피임약 복용 여부 (0: 아니오 / 1: 예)
LW_I: 임신 여부 (0: 없음 / 1: 있음)
LW_S: 수유 여부 (0: 아니오 / 1: 예)
L_BR: 주간 아침식사 빈도 (0: 0회 / 1: 1-2회 / 2: 3-4회 / 3: 5-7회)
L_LN: 주간 점심식사 빈도 (0: 0회 / 1: 1-2회 / 2: 3-4회 / 3: 5-7회)
L_DN: 주간 저녁식사 빈도 (0: 0회 / 1: 1-2회 / 2: 3-4회 / 3: 5-7회)
WATER: 물 섭취량 (컵, 200ml) (1: 0-2컵 / 2: 3-4컵 / 3: 5-6컵 / 4: 7-8컵 / 5: 9컵 이상)


This file is used for practice and learning purposes, and the dataset cannot be uploaded due to copyright restrictions. Furthermore, the completed machine learning model resulting from practice and learning cannot be provided; therefore, only the test file has been uploaded.

The dataset has a notable issue regarding the lack of differentiation between continuous variables and categorical variables. Recognizing this issue is crucial, and I hope that addressing it will contribute to your educational efforts.

Here are the details of the data processing:

SEX: Gender (1: Male / 2: Female)
AGE: Age in years
HT: Height (integer, no decimal)
WT: Weight (integer, no decimal)
SELF: Subjective health status (1: Excellent / 2: Good / 3: Fair / 4: Poor / 5: Very Poor)
DI1: Current presence of hypertension (0: None / 1: Yes)
DI2: Current presence of hyperlipidemia (0: None / 1: Yes)
DE1: Current presence of diabetes (0: None / 1: Yes)
DE2: Current presence of thyroid disease (0: None / 1: Yes)
DC: Current presence of cancer (0: None / 1: Yes)
DF: Current presence of depression (0: None / 1: Yes)
HE: Current presence of anemia (0: None / 1: Yes)
D_Y: Lifetime alcohol consumption (0: None / 1: Yes)
D_M: Frequency of alcohol consumption in the past year (0: None / 1: Less than once a month / 2: 2-4 times a month / 3: 2-3 times a week / 4: 4 or more times a week)
D_G: Amount of alcohol consumed in one sitting (0: None / 1: 1-2 drinks / 2: 3-4 drinks / 3: 5-6 drinks / 4: 7-9 drinks / 5: 10 or more drinks)
SLP: Average hours of sleep per day (1: 1-2 hours / 2: 3-4 hours / 3: 5-6 hours / 4: 7 or more hours)
STRESS: Perceived level of stress (1: Very High / 2: High / 3: Moderate / 4: Low)
SMOKE: Current smoking status (0: No / 1: Yes)
SIT: Daily sitting time (1: 0-2 hours / 2: 2-6 hours / 3: 7-11 hours / 4: 12 or more hours)
W_DAY: Number of days with at least 60 minutes of exercise per week (0: None / 1: 1-2 days / 2: 3-4 days / 3: 5-6 days / 4: Every day)
LW_P: Menopause status (0: None / 1: Yes)
LW_G: Use of oral contraceptives (0: None / 1: Yes)
LW_I: Pregnancy status (0: None / 1: Yes)
LW_S: Breastfeeding status (0: None / 1: Yes)
L_BR: Frequency of breakfast consumption per week (0: 0 times / 1: 1-2 times / 2: 3-4 times / 3: 5-7 times)
L_LN: Frequency of lunch consumption per week (0: 0 times / 1: 1-2 times / 2: 3-4 times / 3: 5-7 times)
L_DN: Frequency of dinner consumption per week (0: 0 times / 1: 1-2 times / 2: 3-4 times / 3: 5-7 times)
WATER: Amount of water consumption (cups of 200ml) (1: 0-2 cups / 2: 3-4 cups / 3: 5-6 cups / 4: 7-8 cups / 5: 9 cups or more)
