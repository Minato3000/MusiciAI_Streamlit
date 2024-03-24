import streamlit as st
from generator import generate_audio

    # background: -webkit-linear-gradient(left, red, orange);
    # background: linear-gradient(to right, red, orange);
gradient_text_html = """
<style>
.gradient-text {
    font-weight: bold;
    background: linear-gradient(90deg, hsla(165, 88%, 16%, 1) 0%, hsla(165, 90%, 38%, 1) 100%);
    background: -webkit-linear-gradient(90deg, hsla(165, 88%, 16%, 1) 0%, hsla(165, 90%, 38%, 1) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;    
    display: inline;
    font-size: 3em;
}
</style>
<div class="gradient-text">MusiciAI</div>
"""

st.markdown(gradient_text_html, unsafe_allow_html=True)

if "conversation" not in st.session_state:
    st.session_state.conversation = []

def AddConversation(prompt, the_list):
    st.session_state.conversation.append({"user": prompt, "assistant": the_list})

prompt = st.chat_input("Enter your prompt here...")

with st.sidebar:
    duration = st.slider("Duration", min_value=5, max_value=60, value=5, step=5)

    if st.button("Clear"):
        st.session_state.conversation = []

for conv in st.session_state.conversation:
    st.write("You:", conv["user"])
    st.audio(conv["assistant"][0], format="audio/ogg", start_time=0, sample_rate=conv["assistant"][1])

if prompt:
    with st.spinner(text="Generating Music..."):
        audio_array, sampling_rate = generate_audio(prompt, duration)
        AddConversation(prompt, [audio_array, sampling_rate])

for conv in st.session_state.conversation:
    st.write("You:", conv["user"])
    st.audio(conv["assistant"][0], format="audio/ogg", start_time=0, sample_rate=conv["assistant"][1])