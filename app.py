import streamlit as st
import base64
import codecs
from formatting import format_html
from datetime import date
from fpdf import FPDF

st.title("G.O.O.D. Innovation Playbook Generator")
st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis feugiat, orci vel iaculis malesuada, diam tortor scelerisque ligula, a accumsan mauris justo nec dui. Pellentesque tincidunt lectus quis facilisis aliquet. Suspendisse ac consequat lectus. Proin lacinia lobortis maximus. Pellentesque eros libero, fringilla vitae sodales a, placerat ut mi. Curabitur sed tincidunt mi, quis pellentesque justo. Vivamus commodo, sem sit amet tempor sagittis, tellus quam maximus quam, et tincidunt mi ligula eget arcu. Praesent ac orci commodo, lacinia lacus vel, semper magna. Nunc pulvinar imperdiet nibh at aliquet.")

st.divider()
st.subheader("Let's build your Playbook")

####BASIC INFORMATION
user_name = st.text_input(label="What is your first and last name?", value="", max_chars=256, placeholder="e.g. Paola Bennings", help="We'll use this to attribute you as the author of your G.O.O.D. Innovation Playbook.")

organization_name= st.text_input(label="What organization are you building this Playbook for?", value="", max_chars=256, placeholder="e.g. Youtube", help="We'll use this to help establish the scope of impact for your Playbook.")

if organization_name != "":
    team_name= st.text_input(label="Is this Playbook designed for a specific team within {}? If not, leave blank.".format(organization_name), value="", max_chars=256, placeholder="e.g. Automoations Team", help="We'll use this to help establish the scope of impact for your Playbook.")
else:
    team_name= st.text_input(label="Is this Playbook designed for a specific team within your organization? If not, leave blank.", value="", max_chars=256, placeholder="e.g. Automoations Team", help="We'll use this to help establish the scope of impact for your Playbook.")

st.divider()
st.subheader("Problem Framing")

problem_statement = st.text_area(label="What is your Problem Statement?", placeholder = "e.g. How might we make the Youtube Shorts algorithm more inclusive and free from bias?", help="Your Problem Statement is a clearly defined one or two sentences that describes that challenge you are facing. This Playbook will orient your strategies around solving for this Problem Statement. If you are a memeber of the G.O.O.D. Innovation Program, you will have worked with our team to define this statement.")

generate_playbook = st.button(label="Generate Playbook")

if generate_playbook:
    today = str(date.today())
    formatted_html = format_html(user_name, organization_name, team_name, problem_statement, today)
    st.download_button("Download", data=formatted_html, file_name="test.html", mime='text/html')
