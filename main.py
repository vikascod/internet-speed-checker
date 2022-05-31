from tkinter import *
import speedtest


def Speed_check():
    st = speedtest.Speedtest()
    st.get_servers()
    down = str(round(st.download()/(10**6), 3))+"Mbps"
    up = str(round(st.upload()/(10**6), 3))+"Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

st = Tk()
st.title('Internet Speed Checker')
st.geometry('500x600')
st.config(bg='blue')

lab_net = Label(st, text="Internet Speed Tester", font=('Time New Roman', 30, 'bold'), bg='black', foreground='white')
lab_net.place(x=30, y=40, height=50, width=450)

lab_down = Label(st, text="Downloading Speed", font=('Time New Roman', 30, 'bold'), bg='black', foreground='white')
lab_down.place(x=40, y=130, height=50, width=430)

lab_down = Label(st, text="00", font=('Time New Roman', 30, 'bold'), bg='black', foreground='white')
lab_down.place(x=40, y=210, height=50, width=430)

lab_up = Label(st, text="Uploading Speed", font=('Time New Roman', 30, 'bold'), bg='black', foreground='white')
lab_up.place(x=40, y=290, height=50, width=430)

lab_up = Label(st, text="00", font=('Time New Roman', 30, 'bold'), bg='black', foreground='white')
lab_up.place(x=40, y=370, height=50, width=430)

button = Button(st, text="Check Speed", font=('Time New Roman', 30, 'bold'), bg='red', foreground='white', relief=RAISED, command=Speed_check)
button.place(x=60, y=460, height=60, width=400)



st.mainloop()