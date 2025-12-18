import streamlit as st
import time
from datetime import datetime
import winsound

st.header("⏱️ Alarm Clock")

time_input = st.text_input("Enter alarm time (HH:MM)", "10:30")

try:
    target = datetime.strptime(time_input, "%H:%M").time()
except ValueError:
    st.error("Please enter time in HH:MM format.")
    st.stop()


time_placeholder = st.empty()


stop_alarm = st.button("Stop Alarm")


st.info("Alarm is running...")


alarm_triggered = False

while True:
    now = datetime.now().time()
    time_placeholder.text(f"Current time: {now.strftime('%H:%M:%S')}")

    if stop_alarm:
        st.warning("⏹ Alarm stopped by user")
        break


    if now.hour == target.hour and now.minute == target.minute and not alarm_triggered:
        st.success("⏰ Time's up!")
        winsound.PlaySound('audio.wav', winsound.SND_ASYNC)
        alarm_triggered = True  

    time.sleep(1)
