import streamlit as st
from PIL import Image

st.title("게임")
col0,col1,col2 = st.columns(3)


image_width = 230


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

with col0:

    img4=Image.open('bg.png')
    st.image(img4)
    lol_link=st.link_button('배틀그라운드',url="https://www.pubg.com/ko/main")

with col1:

    img5=Image.open('fifa.jpg')
    st.image(img5)
    lol_link=st.link_button('피파온라인',url="https://fconline.nexon.com/main/index")

with col2:

    img6=Image.open('star.png')
    st.image(img6)
    star_link=st.link_button('스타크래프트',url="https://us.shop.battle.net/ko-kr/family/starcraft-remastered")

with col0:

    img7=Image.open('jD.png')
    st.image(img7)
    minecraft_link=st.link_button('마인크래프트',url="https://www.minecraft.net/ko-kr")



