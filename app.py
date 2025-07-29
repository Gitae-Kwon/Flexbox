import streamlit as st
import requests

st.title("🤖 KoGPT 생성형 AI 도우미")

prompt = st.text_area("✍ 어떤 내용을 생성할까요?", height=200)
temperature = st.slider("창의성 (temperature)", 0.0, 1.0, 0.7)

if st.button("생성하기"):
    headers = {
        "Authorization": f"KakaoAK {st.secrets['kogpt_api_key']}",
        "Content-Type": "application/json"
    }

    data = {
        "prompt": prompt,
        "max_tokens": 300,
        "temperature": temperature,
        "top_p": 0.8,
        "n": 1,
        "stop": ["\n"]
    }

    res = requests.post("https://api.kakaobrain.com/v1/inference/kogpt/generation", headers=headers, json=data)
    
    if res.status_code == 200:
        result = res.json()["generations"][0]["text"]
        st.success("✅ 생성 결과:")
        st.write(result)
    else:
        st.error(f"❌ 오류 발생: {res.status_code}")
