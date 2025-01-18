users = [
    {
        "first_name": "Angeline",
        "last_name":"Timothy",
        "email":"atimothy0@geocities.com",
        "gender":"Female",
        "ip_address":"48.93.26.14",
        "age": 12
    },
    {
        "first_name":"Shandy",
        "last_name":"Kierans",
        "email":"skierans1@surveymonkey.com",
        "gender":"Female",
        "ip_address":"164.225.85.37",
        "age": 15
    },
    {
        "first_name":"Scott",
        "last_name":"Ketton",
        "email":"sketton2@sogou.com",
        "gender":"Male",
        "ip_address":"71.70.178.85",
        "age": 10
    },
]
female=0
male=0
for e in users:
    if e["gender"]=="Male":
        male+=1
    if e["gender"]=="Female":
        female+=1
#print(male)
#print(female)
sum=male+female
if sum>0:
    m=(male/sum)*100
    f=(female/sum)*100
    print(f"erkaklar: {male} ta, {m:.0f}%")
    print(f"ayollar: {female} ta, {f:.0f}%")
else:
    print("foydalanuvchilar yoq")