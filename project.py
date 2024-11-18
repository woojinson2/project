import streamlit as st
import time
from datetime import datetime, timedelta


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

# 사이드바에 타이머 설정
st.sidebar.title("남은시간")
timer_duration_hours = st.sidebar.number_input("남은시간 설정 (시간)", min_value=0.1, value=2.0, step=0.1)

# 버튼 클릭 시 타이머 시작
if st.sidebar.button("타이머 시작"):
    # 현재 시간과 종료 시간 계산
    end_time = datetime.now() + timedelta(hours=timer_duration_hours)
    timer_placeholder = st.sidebar.empty()  # 사이드바에 타이머 업데이트를 위한 빈 컨테이너

    while datetime.now() < end_time:
        remaining_time = end_time - datetime.now()
        remaining_hours = remaining_time.total_seconds() / 3600
        timer_placeholder.write(f"남은 시간: {remaining_hours:.2f}시간")
        time.sleep(1)  # 1초 대기

    timer_placeholder.write("타이머가 종료되었습니다!")