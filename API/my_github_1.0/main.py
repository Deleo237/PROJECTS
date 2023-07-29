#Get, Post, Put and Delete requests
from requests import get,post,put,delete
from datetime import datetime
NAME="YOUR ACCOUNT NAME"
PASS="YOUR ACCOUNT PASSWORD"
GID="GRAPH ID"
pe="https://pixe.la/v1/users"
par1={
    "token":PASS,
    "username":NAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
# r=post(url=pe,json=par1)
# print(r.text)
par2={
    "id":GID,
    "name":"Houirs Of Studies",
    "unit":"Hours",
    "type":"int",
    "color":"ajisai"
}
h1={
    "X-USER-TOKEN":PASS
}
ge=f"{pe}/{NAME}/graphs"
# r=post(url=ge,json=par2,headers=h1)
# print(r.text)
m=datetime.now()
n=str(m).split(" ")[0]
dat=m.strftime("%Y%m%d")
#dat=n.replace("-","")
par3={
    "date":dat,
    "quantity":input("How many hours have you been studying: ")
}
ie=f"{ge}/{GID}"
r=post(url=ie,json=par3,headers=h1)
print(r.text)
par4={
    "quantity":"18"
}
re=f"{ie}/{dat}"
# r=put(url=re,json=par4,headers=h1)
# print(r.text)
de=re
# r=delete(url=de,headers=h1)
# print(r.text)
# h2={
#     "X-USER-TOKEN":PASS,
#     "Content-Length":input("How many hours have you been studying: ")
# }
# inc=f"{ie}/increment"
# r=put(url=inc,headers=h2)
# print(r.text)