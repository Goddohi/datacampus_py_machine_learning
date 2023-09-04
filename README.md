# datacampus_py_machine_learning
This project is a  website developed as a result of DataCampus Healthcare AI Project, which guides users on nutritional deficiencies through body data. We possess the dataset, and we regret to inform you that we cannot distribute it due to copyright restrictions.
이파일은 데이터 셋 연습용으로 학습을 위한 공부 방식중 하나로 사용되었습니다 
데이터셋은 저작권관련으로 올리지 못하는 점 아쉽습니다..

데이터 관련 처리 내용입니다
SEX 성별( 1 남자 / 2 여자)
AGE 만나이
HT 신장(소수점X 상관은없음)
WT체중(소수점X 상관은없음)
SELF 주관적 건강상태 (1: 매우좋다/ 2:좋다 / 3:보통 / 4:나쁨 / 5: 매우나쁨)
DI1 고혈압 현재 유병 여부( 0 없음 / 1맞음)
DI2 이상지질혈증 현재 유병 여부( 0 없음 / 1맞음)
DE1 당뇨병 현재 유병 여부( 0 없음 / 1맞음)
DE2 갑상선 질환 현재 유병 여부( 0 없음 / 1맞음)
DC 암 현재 유병 여부( 0 없음 / 1맞음)
DF 우울증 현재 유병 여부( 0 없음 / 1맞음)
HE 빈혈 현재 유병여부( 0 없음 / 1맞음)
D_Y 평생 음주여부( 0 없음 / 1맞음)
D_M 1년간 음주빈도(0:0/1: 월1회이하 /2:월2-4회/3:주 2-3 /4:주4회이상)
D_G 한번에 마시는 음주량(0: 0/1: 1-2잔/2: 3-4/3: 5-6/4: 7-9/ 5:10)
SLP 하루 평균 수면시간(h)(1:1~2/ 2:3~4 / 3:5~6/ 4:7이상)
STRESS 평소 스트레스 인지 정도(1 매우많이 / 2 많이/3 조금빋받음/4거의안받음)
SMOKE 현재흡연(0/1)
SIT 평소 하루 앉아서 보내는 시간(1:0~2/2 :2~6/3:7~11/4:12이상)
W_DAY 1주간 60분 이상 운동 일수(0:0 / 1:1~2/2:3~4/3:5~6/4:매일) 
LW_P 폐경여부( 0 없음 /  1맞음)
LW_G 경구피임약 복용여부( 0 없음 / 1맞음)
LW_I 임신여부( 0 없음 /  1맞음)
LW_S 수유여부( 0 없음 / 1맞음)
L_BR 1주 아침식사 빈도(0: 0회/1: 1~2회 /2: 3~4회 /3: 5~7회)
L_LN 1주 점심식사 빈도(0: 0회/1: 1~2회 /2: 3~4회 /3: 5~7회)
L_DN 1주 저녁식사 빈도(0: 0회/1: 1~2회 /2: 3~4회 /3: 5~7회)
WATER 물 섭취량(컵)(200ml)(1 : 0~2 /2: 3~4 /3: 5~6 / 4: 7~8 / 5 9컵이상)

This file was used for practice and learning purposes as part of our study. Unfortunately, we cannot upload the dataset due to copyright restrictions.

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
