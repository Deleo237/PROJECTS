from smtplib import SMTP
import datetime as dt
from random import choice
me="EMAIL ADDRESS"
mp="PASSWORD TO EMAIL ACCOUNT"
n=dt.datetime.now()
d=n.weekday()
if d==3:
    with open("quotes.txt") as q:
        qq=q.readlines()
    mes=choice(qq)
    con=SMTP("smtp.gmail.com")
    con.starttls()
    con.login(user=me,password=mp)
    con.sendmail(from_addr=me,to_addrs="tendongmohdeleoanang@gmail.com",msg=f"Subject:Motivation\n\n{mes}")
    con.close()
