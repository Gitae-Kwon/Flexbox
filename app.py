import streamlit as st
import requests

st.title("🤖 KoGPT 테스트")

prompt = st.text_input("입력 프롬프트")
if st.button("생성"):
    headers = {
        "Authorization": f"KakaoAK {st.secrets['kogpt_api_key']}",
        "Content-Type": "application/json"
    }

    data = {
        "prompt": prompt,
        "max_tokens": 100,
        "temperature": 0.7,
        "top_p": 0.9
    }

    try:
        res = requests.post(
            "https://api.kakaobrain.com/v1/inference/kogpt/generation",
            headers=headers,
            json=data,
            timeout=15
        )

        st.write("상태코드:", res.status_code)
        st.write("응답:", res.text)

        if res.status_code == 200:
            result = res.json()["generations"][0]["text"]
            st.success("결과:")
            st.write(result)
        else:
            st.error("오류 발생!")

    except Exception as e:
        st.error(f"예외 발생: {e}")
