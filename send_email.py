import smtplib
import ssl
import streamlit as st


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = st.secrets.mail_username
    password = st.secrets.mail_password

    receiver = st.secrets.mail_receiver
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
