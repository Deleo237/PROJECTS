from turtle import Screen,Turtle
FONT = ("Courier", 10, "normal")
import turtle 
import pandas
sc=Screen()
sc.title("U.S States Game")
img="./blank_states_img.gif"
sc.addshape(img)
turtle.shape(img)
state=pandas.read_csv("./50_states.csv")
stat=state["state"]
sta=stat.to_list()
a=1
ll=[]
score=0
while score<50:
    ans=str(sc.textinput(f"{score}/50 Guess the state","What's another state's name? ")).title()
    print(ans)
    if ans=="Exit":
        break
    if ans in sta:
        if ans not in ll:
            ll.append(ans)
            score+=1
            xy=state[state.state==ans]
            x=int(xy.x)  # type: ignore
            y=int(xy.y)  # type: ignore
            t=Turtle()
            t.hideturtle()
            t.pu()
            t.goto(x,y)
            t.write(arg=ans,move=False,align="center",font=FONT) 
stl={"Countries":[]}
stl["Countries"]=[i for i in sta if i not in ll]
#OR
# for i in sta:
#     if i not in ll:
#         stl["Countries"].append(i)
d=pandas.DataFrame(stl)
print(d)
d.to_csv("./learnstate.csv")
turtle.mainloop()
