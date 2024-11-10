import streamlit as st
from PIL import Image
st.title("게임")
img=Image.open('dd.jpg')
st.image(img)
diablo_link=st.link_button('디아블로4',url="https://diablo4.blizzard.com/ko-kr/")

img2=Image.open('lol.jpg')
st.image(img2)
lol_link=st.link_button('리그오브레전드',url="https://www.leagueoflegends.com/ko-kr/")

img3=Image.open('ov.png')
st.image(img3)
ov_link=st.link_button('오버워치2',url="https://overwatch.blizzard.com/ko-kr/")

img4=Image.open('bg.png')
st.image(img4)
lol_link=st.link_button('배틀그라운드',url="https://www.pubg.com/ko/main")

img5=Image.open('fifa.jpg')
st.image(img5)
lol_link=st.link_button('피파온라인',url="https://fconline.nexon.com/main/index")
