import streamlit as st
st.write("점심 메뉴를 선택하세요")
짜장면 = st.checkbox("짜장면")
짬뽕 = st.checkbox("짬뽕")
탕수육 = st.checkbox("탕수육")
price=0
if 짜장면:
    price+=6000
if 짬뽕:
    price+=7000
if 탕수육:
    price+=12000
st.write("가격은 :",price)




라디오버튼=st.radio('내가 가장 좋아하는 색상은?',
               [":red[빨강]",":blue[파랑]",":green[녹색]"])

if 라디오버튼==":red[빨강]":
    st.write("빨강색을 선택하셨습니다.")
if 라디오버튼==":blue[파랑]":
    st.write("파랑색을 선택하셨습니다.")    
if 라디오버튼==":green[녹색]":
    st.write("녹색을 선택하셨습니다.")



#selectbox
menu=st.selectbox("과목을 선택하세요",["확률과 통계",'미분과 적분','기하와 벡터'])

st.write(menu+"과목을 선택하셨습니다.")

#multiselect

menu2=st.multiselect("과목을 선택하세요",['물리','생명','화학','지구과학'])
문자열=''
for a in menu2:
    문자열 +=a+' '

st.write(문자열+'과목을 선택하셨습니다.')


id=st.text_input("아이디를 입력하세요",placeholder="아이디 입력")
pw=st.text_input("비밀번호를 입력하세요",type='password')
로그인=st.button("로그인")

if id == 'abc'and pw== '123':
    st.write("로그인 성공")
else:
    st.write("로그인 실패")

st.image("flying.jpg")
st.video('https://www.youtube.com/watch?v=cmpRLQZkTb8')