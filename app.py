import streamlit as st

st.set_page_config(page_title="حاسبة اللياقة الذكية", page_icon="🏋️‍♂️", layout="centered")

st.title("🏋️️‍♂️ حاسبة السعرات واللياقة الذكية")
st.write("أدخل بياناتك اليومية لمعرفة احتياجك من السعرات والبروتين والماء!")

st.divider()

# المدخلات
weight = st.number_input("الوزن (كغم):", min_value=30.0, max_value=200.0, value=70.0, step=0.5)
height = st.number_input("الطول (سم):", min_value=100.0, max_value=220.0, value=170.0, step=1.0)
age = st.number_input("العمر:", min_value=10, max_value=100, value=20)
steps = st.number_input("عدد الخطوات اليومية تقريباً:", min_value=0, max_value=50000, value=8000, step=500)

goal = st.selectbox("ما هو هدفك الحالي؟", ["تنزيل وزن", "بناء عضلات", "المحافظة على الوزن"])

if st.button("🚀 احسب النتائج الآن", type="primary"):
    # حساب الحرق والاحتياج
    bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    step_calories = (steps / 1000) * 40
    total_calories = bmr + step_calories
    
    # حساب احتياج الماء والبروتين
    water_liters = (weight * 0.033)
    protein_grams = weight * 2.0
    
    st.success("تم الحساب بنجاح!")
    
    col1, col2 = st.columns(2)
    col1.metric("حرق الجسم الأساسي", f"{round(bmr)} سعرة")
    col2.metric("إجمالي الحرق اليومي", f"{round(total_calories)} سعرة")
    
    st.subheader("📊 الاحتياج اليومي المغذي:")
    st.write(f"💧 **احتياجك اليومي من الماء:** حوالي `{round(water_liters, 1)} لتر`")
    st.write(f"🥩 **البروتين اليومي الموصى به:** حوالي `{round(protein_grams)} غرام`")
    
    st.subheader("🎯 هدف السعرات اليومي:")
    if goal == "تنزيل وزن":
        target = total_calories - 400
        st.warning(f"استهدف تناول: **{round(target)} سعرة حرارية** يومياً.")
    elif goal == "بناء عضلات":
        target = total_calories + 300
        st.success(f"استهدف تناول: **{round(target)} سعرة حرارية** يومياً.")
    else:
        st.info(f"استهدف تناول: **{round(total_calories)} سعرة حرارية** يومياً.")
