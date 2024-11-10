import streamlit as st
from PIL import Image
st.title("먹거리 주문")
st.title('라면')

col0,col1,col2,col3,col4,col5 = st.columns(6)

with col1:
    st.checkbox('너구리  1500')
    img=Image.open('ngr.png')
    st.image(img)

with col2:
    st.checkbox('짜파게티 1500')
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

if st.checkbox('너구리  1500'):

    total_price += 1500
    
st.write(f"총: {total_price}원")

menu = st.selectbox("결제수단", ['카드', '현금','계좌이체','시간차감'])
