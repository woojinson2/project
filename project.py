import streamlit as st
st.set_page_config(
    page_title= "매천 PC",
    page_icon="🎮"
)
import sqlite3

pages = {
    "환영합니다!" : [
        st.Page("page/a.py", title="회원가입"),
        st.Page("page/b.py", title="로그인")
    ],
    "카테고리2" : [
        st.Page("page/c.py", title="먹거리주문"),
        st.Page("page/d.py", title="게임")
    ]
}

pg = st.navigation(pages)
pg.run()

