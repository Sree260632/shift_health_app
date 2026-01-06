import streamlit as st
import mysql.connector

st.title("Day vs Night Shift – Health Impact Study")

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@2026",
    database="shift_health_db"
)

cursor = db.cursor()

st.header("Employee Health & Work Survey")

age = st.number_input("Age", 18, 70)
shift = st.selectbox("Shift Type", ["Day", "Night"])
salary = st.number_input("Monthly Salary", 0)

sleep = st.number_input("Average Sleep Hours", 0.0, 12.0)
insomnia = st.checkbox("Insomnia")
day_sleep = st.checkbox("Daytime Sleepiness")

focus = st.checkbox("Poor Focus")
memory = st.checkbox("Memory Issues")

stress = st.selectbox("Stress Level", ["Low","Medium","High"])
anxiety = st.checkbox("Anxiety")
depression = st.checkbox("Depression")
burnout = st.checkbox("Burnout")

back_pain = st.checkbox("Back / Neck Pain")
eye_strain = st.checkbox("Eye Strain")
obesity = st.checkbox("Obesity")
diabetes = st.checkbox("Diabetes")
heart = st.checkbox("Heart Disease Risk")

family = st.checkbox("Family Stress")
social = st.checkbox("Social Life Affected")

routine = st.text_area("Daily Routine")
suggestion = st.text_area("Suggestions")

if st.button("Submit Data"):
    cursor.execute("""
        INSERT INTO worker_health
        (age, shift_type, salary, sleep_hours, insomnia, daytime_sleepiness,
         poor_focus, memory_issues, stress_level, anxiety, depression, burnout,
         back_neck_pain, eye_strain, obesity, diabetes, heart_risk,
         family_stress, social_life_affected, daily_routine, suggestions)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, (
        age, shift, salary, sleep, insomnia, day_sleep,
        focus, memory, stress, anxiety, depression, burnout,
        back_pain, eye_strain, obesity, diabetes, heart,
        family, social, routine, suggestion
    ))

    db.commit()
    st.success("Data saved successfully")
