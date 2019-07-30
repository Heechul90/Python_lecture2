

import pandas as pd
import numpy as np


## 연습 문제 1
## 1. 임의로 두 개의 시리즈 객체를 만든다.
##    모두 문자열 인덱스를 가져야 하며 두 시리즈에 공통적으로 포함되지 않는 라벨이 있어야 한다.
s1 = pd.Series([123, 321, 456, 987],
               index = ['동구', '서구', '중구', '유성구'])

s2 = pd.Series([789, 654, 412, 133],
               index = ['유성구', '대덕구', '중구', '서구'])

## 2. 위에서 만든 두 시리즈 객체를 이용하여 사칙 연산을 한다.

s1 - s2
s1 + s2
s1 * s2
s1 / s2




## 연습 문제 2
## 다음 조건을 만족하는 임의의 데이터프레임을 하나 만든다.

## 1. 열의 갯수와 행의 갯수가 각각 5개 이상이어야 한다.
## 2. 열에는 정수, 문자열, 실수 자료형 데이터가 각각 1개 이상씩 포함되어 있어야 한다.

df = pd.DataFrame({'중구': [1, '대', 7.120, 48855, 'A'],
                   '서구': [2, '전', 9.233, 47412, 'N'],
                   '동구': [3, '광', 2.384, 23662, 'D'],
                   '대덕구': [4, '역', 3.254, 12402, 'A'],
                   '유성구': [5, '시', 4.201, 48752, 'S']},
                  index = ['정수', '문자열', '실수', '숫자', 'P'])
df





## 연습 문제 3
## 다음 데이터프레임에서 지정하는 데이터를 뽑아내거나 처리하라.

data = {
    "국어": [80, 90, 70, 30],
    "영어": [90, 70, 60, 40],
    "수학": [90, 60, 80, 70],
}
columns = ["국어", "영어", "수학"]
index = ["춘향", "몽룡", "향단", "방자"]
df = pd.DataFrame(data, index=index, columns=columns)


# 1. 모든 학생의 수학 점수를 시리즈로 나타낸다.
one = df['수학']
type(one)

# 2. 모든 학생의 국어와 영어 점수를 데이터 프레임으로 나타낸다.
two = df[['국어', '영어']]
type(two)

# 3. 모든 학생의 각 과목 평균 점수를 새로운 열로 추가한다.
df['평균'] = ((df['국어'] + df['영어'] + df['수학']) / 3).round(2)
df

# 4. 방자의 영어 점수를 80점으로 수정하고 평균 점수도 다시 계산한다.
df['영어']['방자'] = 80
df['평균'] = ((df['국어'] + df['영어'] + df['수학']) / 3).round(2)
df


# 5. 춘향의 점수를 데이터프레임으로 나타낸다.
five = df[:1]
type(five)


# 6. 향단의 점수를 시리즈로 나타낸다.
six = df[2:3]
type(six)

