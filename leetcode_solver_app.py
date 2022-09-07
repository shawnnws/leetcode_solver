import streamlit as st

from openai_utils import get_leetcode_answer

st.set_page_config(
    page_title="Shawn's leetcode solver",
    layout="wide"
)

st.header("Please copy and paste your leetcode question here")

leetcode_question: str = st.text_area(
    label="please copy and paste your question here",
    height=400
)

if st.button("Get Answer"):
    st.header("Leetcode Python Answer")
    st.text(get_leetcode_answer(leetcode_question))