import streamlit as st
import time
from openai import OpenAI
import streamlit as st

# 코드스니펫 - 제목
st.title('[스파르타] 제품 홍보 포스터 생성기')

# 코드스니펫 - 입력
keyword = st.text_input("키워드를 입력하세요.")

# 코드스니펫 - 버튼
if st.button('생성 :fire:'):
  with st.spinner('생성 중입니다.'):
    # time.sleep(3)
    # st.write('hello') - 필요없어서 삭제

    # 2_prac_chatgpt.py 코드
    client = OpenAI(api_key=st.secrets["API_KEY"])

    chat_completion = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": keyword + "라는 키워드로 제품 홍보 카피를 150자 이내로 작성해줘",
        }],
        model="gpt-4o",
    )

    # 홍보카피 = messages[0].message.content -> prompt에 홍보카피를 넣어서 키워드에 대해서 생성된 홍보카피를 이미지 생성 프롬프트에 넣을 수 있음

    chat_result = chat_completion.choices[0].message.content
    # print(chat_result) -> 결과를 콘솔에서만 보임
    st.write(chat_result)
    # st.write(변수) -> 브라우저에서 결과 보여줌
    # 드래그된 상태에서 alt + 방향키 : 선택한 글자 옮기기

    # 3_prac_dalle.py 코드
    client = OpenAI(api_key=st.secrets["API_KEY"])

    response = client.images.generate(
        model="dall-e-3",
        prompt=keyword,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    # print(image_url)
    st.image(image_url)
