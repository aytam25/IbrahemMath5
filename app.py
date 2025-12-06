import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="الوحدة الثالثة - الصف الخامس", layout="wide")

st.title("📘 منصة تفاعلية للوحدة الثالثة (صفحات ٥٤–٦١)")
st.markdown("تمارين ضرب وقسمة الكسور العشرية، مسائل نصية، وضع الفاصلة، وامتحان نهائي.")

with open("unit3.html", "r", encoding="utf-8") as f:
    html_code = f.read()

components.html(html_code, height=1000, scrolling=True)