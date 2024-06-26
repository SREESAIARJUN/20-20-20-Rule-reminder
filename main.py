import streamlit as st

# Set the title of the web app
st.title("20-20-20 Rule Reminder App")

# Add a description
st.write("""
### What is the 20-20-20 Rule?
The 20-20-20 rule is a simple and effective way to reduce eye strain caused by prolonged screen time. 
The rule suggests that every 20 minutes, you should take a 20-second break to look at something 20 feet away.
This helps to relax the eye muscles and reduce fatigue.
""")

# Add an image
st.image("https://upload.wikimedia.org/wikipedia/commons/3/3b/Eye_Symbol.png", width=150)

# Add a section for the app features
st.write("""
### Features of the 20-20-20 Rule Reminder App:
- **Automatic Reminders**: Get a reminder every 20 minutes to take a break.
- **Modern and User-Friendly Interface**: Sleek and easy-to-use design.
- **System Tray Integration**: Easily accessible from your system tray with options to start, stop, or quit the app.
- **Topmost Notification**: The reminder popup always appears above all other windows, ensuring you never miss a break.
""")

# Add a download link
st.write("""
### Download the App:
[Download 20-20-20 Rule Reminder App](https://your-download-link-here.com)
""")

# Add a feedback section
st.write("""
### Feedback:
Your feedback is highly valued! Please let us know your thoughts and any suggestions for improvement.
""")

# Add a footer
st.write("""
*Let's take care of our eyes, one break at a time!*
""")
