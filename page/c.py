'''import streamlit as st
from PIL import Image
st.title("먹거리 주문")
st.title('라면')

col0,col1,col2,col3,col4,col5 = st.columns(6)

with col1:
    st.checkbox('너구리')
    img=Image.open('ngr.png')
    st.image(img)

with col2:
    st.checkbox('짜파게티')
    img2=Image.open('Jpgt.png')
    st.image(img2)

with col3:

    st.checkbox('불닭볶음면')
    img3=Image.open('buldak.png')
    st.image(img3)

with col4:

    st.checkbox('신라면')
    img4=Image.open('srm.png')
    st.image(img4)

with col5:

    st.checkbox('비빔면')
    img5=Image.open('bbm.png')
    st.image(img5)


with col0:
    st.title('밥')

with col1:

    st.checkbox('야채볶음밥')
    img6=Image.open('bap.png')
    st.image(img6)
with col2:

        st.checkbox('새우볶음밥')
        img7=Image.open('sbap.png')
        st.image(img7)

with col3:

        st.checkbox('참치마요덮밥')
        img8=Image.open('ccbap.png')
        st.image(img8)

with col4:

        st.checkbox('스팸마요덮밥')
        img9=Image.open('spbap.png')
        st.image(img9)

with col5:

        st.checkbox('김치볶음밥')
        img10=Image.open('gcbap.png')
        st.image(img10)



st.text('간식')

with col1:

    st.checkbox('핫도그')
    img11=Image.open('hotdog.png')
    st.image(img11)

with col2:

    st.checkbox('치즈스틱')
    img12=Image.open('cheese stick.png')
    st.image(img12)

with col3:

    st.checkbox('감자튀김')
    img13=Image.open('fried.png')
    st.image(img13)

with col4:

    st.checkbox('고기만두')
    img14=Image.open('ggmd.png')
    st.image(img14)

with col5:
    
    st.checkbox('김치만두')
    img15=Image.open('gcmd.png')
    st.image(img15)


st.title('음료')

with col1:

    st.checkbox('커피')
    img16=Image.open('cofee.png')
    st.image(img16)

with col2:

    st.checkbox('탄산음료')
    img17=Image.open('coke.png')
    st.image(img17)

with col3:

    st.checkbox('이온음료')
    img18=Image.open('pocari.png')
    st.image(img18)

with col4:

    st.checkbox('카페인음료')
    img19=Image.open('monster.png')
    st.image(img19)

with col5:

    st.checkbox('아이스티')
    img20=Image.open('icetea.png')
    st.image(img20)

total_price=0

if st.checkbox('너구리'):
    total_price +=1500

st.write(f"총 가격: {total_price} 원")
'''
import streamlit as st
from PIL import Image

# 제목 설정
st.title("먹거리 주문")


# 가격 설정
prices = {
    '너구리': 1500,
    '짜파게티': 1500,
    '불닭볶음면': 2000,  # 예시 가격
    '신라면': 1500,      # 예시 가격
    '비빔면': 2000,      # 예시 가격
    '야채볶음밥': 2500,  # 예시 가격
    '새우볶음밥': 3000,  # 예시 가격
    '참치마요덮밥': 3500, # 예시 가격
    '스팸마요덮밥': 4000, # 예시 가격
    '김치볶음밥': 2500,   # 예시 가격
    '핫도그': 2000,       # 예시 가격
    '치즈스틱': 1500,     # 예시 가격
    '감자튀김': 1500,     # 예시 가격
    '고기만두': 2500,     # 예시 가격
    '김치만두': 2500,     # 예시 가격
    '커피': 2000,         # 예시 가격
    '탄산음료': 1500,     # 예시 가격
    '이온음료': 2000,     # 예시 가격
    '카페인음료': 2500,   # 예시 가격
    '아이스티': 1500      # 예시 가격
}

# 주문 항목 선택 및 이미지 표시
items = [
    ('너구리', 'ngr.png'),
    ('짜파게티', 'Jpgt.png'),
    ('불닭볶음면', 'buldak.png'),
    ('신라면', 'srm.png'),
    ('비빔면', 'bbm.png'),
    ('야채볶음밥', 'bap.png'),
    ('새우볶음밥', 'sbap.png'),
    ('참치마요덮밥', 'ccbap.png'),
    ('스팸마요덮밥', 'spbap.png'),
    ('김치볶음밥', 'gcbap.png'),
    ('핫도그', 'hotdog.png'),
    ('치즈스틱', 'cheese stick.png'),
    ('감자튀김', 'fried.png'),
    ('고기만두', 'ggmd.png'),
    ('김치만두', 'gcmd.png'),
    ('커피', 'cofee.png'),
    ('탄산음료', 'coke.png'),
    ('이온음료', 'pocari.png'),
    ('카페인음료', 'monster.png'),
    ('아이스티', 'icetea.png')
]

# 총 가격 계산
total_price = 0

# 5개의 열로 나누어 표시
num_columns = 5  # 열 수 설정
for i in range(0, len(items), num_columns):
    cols = st.columns(num_columns)  # 5개의 열 생성
    for j in range(num_columns):
        if i + j < len(items):  # 인덱스 초과 방지
            item, img_file = items[i + j]
            with cols[j]:
                checked = st.checkbox(item, key=item)
                img = Image.open(img_file)
                st.image(img)
                if checked:
                    total_price += prices[item]

# 총 가격 출력
st.header(f"총 가격: {total_price} 원")

st.header("결제 방법 선택")
payment_method = st.radio("결제 방법을 선택하세요:", ("신용카드", "계좌이체", "휴대폰 결제"))

# 선택한 결제 방법 표시
st.write(f"선택한 결제 방법: {payment_method}")