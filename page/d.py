'''import streamlit as st
from PIL import Image

st.title("게임")
col0,col1,col2,col3 = st.columns(4)




with col0:

    img=Image.open('dd.jpg')
    st.image(img)
    diablo_link=st.link_button('디아블로4',url="https://diablo4.blizzard.com/ko-kr/")

with col1:

    img2=Image.open('lol.jpg')
    st.image(img2)
    lol_link=st.link_button('LOL',url="https://www.leagueoflegends.com/ko-kr/")

with col2:

    img3=Image.open('ov.png')
    st.image(img3)
    ov_link=st.link_button('오버워치2',url="https://overwatch.blizzard.com/ko-kr/")

with col3:

    img4=Image.open('bg.png')
    st.image(img4)
    lol_link=st.link_button('배틀그라운드',url="https://www.pubg.com/ko/main")

with col0:

    img5=Image.open('fifa.jpg')
    st.image(img5)
    lol_link=st.link_button('피파온라인',url="https://fconline.nexon.com/main/index")

with col1:

    img6=Image.open('star.png')
    st.image(img6)
    star_link=st.link_button('스타크래프트',url="https://us.shop.battle.net/ko-kr/family/starcraft-remastered")

with col2:

    img7=Image.open('jD.png')
    st.image(img7)
    minecraft_link=st.link_button('마인크래프트',url="https://www.minecraft.net/ko-kr")
'''
import streamlit as st
from PIL import Image

st.title("게임 PC방")

# 이미지 크기 설정
image_width = 250  # 모든 이미지의 너비를 250픽셀로 설정

# 게임 데이터
games = [
    ('디아블로4', 'dd.jpg', 'https://diablo4.blizzard.com/ko-kr/'),
    ('LOL', 'lol.jpg', 'https://www.leagueoflegends.com/ko-kr/'),
    ('오버워치2', 'ov.png', 'https://overwatch.blizzard.com/ko-kr/'),
    ('배틀그라운드', 'bg.png', 'https://www.pubg.com/ko/main'),
    ('피파온라인', 'fifa.jpg', 'https://fconline.nexon.com/main/index'),
    ('스타크래프트', 'star.png', 'https://us.shop.battle.net/ko-kr/family/starcraft-remastered'),
    ('마인크래프트', 'jD.png', 'https://www.minecraft.net/ko-kr')
]

# 카드 형식으로 게임 나열
cols = st.columns(3)  # 4개의 열로 구성

for i, (game_name, img_file, url) in enumerate(games):
    with cols[i % 3]:  # 열에 맞춰 게임 배치
        st.image(Image.open(img_file), width=image_width)
        if st.button(game_name, key=game_name):
            st.markdown(f"[{game_name}]({url})")
