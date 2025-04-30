import streamlit as st
import re
st.set_page_config(page_title="Password Strength Meter",page_icon="🔐")
st.title("Password Strength Meter")
st.markdown("""
   ## Welcome to Password Srength Meter 🕐
  use this tool to check how strong is your password and also get suggestion on how to strengthen
  your password that helps you create **💪Strong Password**""")

password = st.text_input("Enter your Password", type="password")
suggestion = []
points = 0

if password:

  if len(password) >= 0:
    points +=1

  else:
    suggestion.append("❌ Password should be contain min 8 character")  

  if re.search(r'[A-Z]', password) and re.search(r'[a-z]',password):
    points += 1

  else:
    suggestion.append("❌ Password should contain both upper and lower case letter")

  if re.search(r'\d', password):
    points+=1
  
  else:
    suggestion.append("❌ password should contain atleast one digit")
  
  if re.search(r'[!@#$%*]', password):
    points+=1

  else:
    suggestion.append("❌ password should contain aleast one special character(!@#$%&*)")

  if points == 4:
    suggestion.append("✅ Your password is strong 🎉")
  
  elif points==3:
    suggestion.append("🟡 your Password is medium . It could be stronger.")

  else:
    suggestion.append("🔴 High alert ! your password is weak needed to strengthen it...")

  if suggestion:
    st.markdown("## Improvement Suggestions :")
    for tip in suggestion:
     st.write(tip)
else:
  st.info("Please enter your Password to get started.")

