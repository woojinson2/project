'''import streamlit as st
import sqlite3



conn = sqlite3.connect('db.db')
cursor = conn.cursor()
st.title("회원가입")
id = st.text_input("아이디")
pw = st.text_input("비밀번호", type='password')
pw_check = st.text_input("비밀번호 확인", type='password')
email = st.text_input("이메일")
gender = st.radio("성별을 선택하세요", ['male','female'])
btn = st.button("회원가입")
if btn:
        #비밀번호가 잘 입력되었는지를 확인
        if pw == pw_check:            
            #입력한 정보를 DB에 저장
            sql = f"""
insert into user(username, password, email, gender)
values('{id}','{pw}','{email}'{gender}')"""
            cursor.execute(sql)
            conn.commit()
            st.success("회원가입 성공!")
        else:
            #회원가입 실패
            st.error("비밀번호가 일치하지 않습니다.")
conn.close()
'''
import streamlit as st
import sqlite3

conn = sqlite3.connect('db.db')
cursor = conn.cursor()
st.title("회원가입")
id = st.text_input("아이디")
pw = st.text_input("비밀번호", type='password')
pw_check = st.text_input("비밀번호 확인", type='password')

gender = st.radio("성별을 선택하세요", ['male', 'female'])
btn = st.button("회원가입")

if btn:
    # 비밀번호가 잘 입력되었는지를 확인
    if pw == pw_check:
        # 입력한 정보를 DB에 저장
        sql = """
        INSERT INTO user (username, password, gender)
        VALUES (?, ?, ?)
        """
        cursor.execute(sql, (id, pw,  gender))
        conn.commit()
        st.success("회원가입 성공!")
    else:
        # 회원가입 실패
        st.error("비밀번호가 일치하지 않습니다.")

conn.close()
