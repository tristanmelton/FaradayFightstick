import serial
from serial import SerialException
from tkinter import * 
from time import sleep

import serial.tools.list_ports



ports = serial.tools.list_ports.comports()
serial_port = None

root = Tk()
frame_connect = Frame(root)
frame_buttonconfig = Frame(root)

frame_connect.grid()
frame_buttonconfig.grid(row=0, column=0)
#rame_buttonconfig.pack()

listbox_comports = Listbox(frame_connect,height = 10, width = 50)

label_connect = Label(frame_connect, text="Select a Serial Port")
label_buttonsettings = Label(frame_buttonconfig, text="Button Sensitivity Configuration")

label_lp = Label(frame_buttonconfig, text="LP").grid(row=1, column=0)
entry_lp = Entry(frame_buttonconfig)
entry_lp.grid(row=1,column=1)
label_mp = Label(frame_buttonconfig, text="MP").grid(row=1, column=2)
entry_mp = Entry(frame_buttonconfig)
entry_mp.grid(row=1,column=3)
label_hp = Label(frame_buttonconfig, text="HP").grid(row=1, column=4)
entry_hp = Entry(frame_buttonconfig)
entry_hp.grid(row=1,column=5)
label_shp = Label(frame_buttonconfig, text="SHP").grid(row=1, column=6)
entry_shp = Entry(frame_buttonconfig)
entry_shp.grid(row=1,column=7)

label_lk = Label(frame_buttonconfig, text="LK").grid(row=2, column=0)
entry_lk = Entry(frame_buttonconfig)
entry_lk.grid(row=2,column=1)
label_mk = Label(frame_buttonconfig, text='MK').grid(row=2, column=2)
entry_mk = Entry(frame_buttonconfig)
entry_mk.grid(row=2,column=3)
label_hk = Label(frame_buttonconfig, text="HK").grid(row=2, column=4)
entry_hk = Entry(frame_buttonconfig)
entry_hk.grid(row=2,column=5)
label_shk = Label(frame_buttonconfig, text="SHK").grid(row=2, column=6)
entry_shk = Entry(frame_buttonconfig)
entry_shk.grid(row=2,column=7)

label_up = Label(frame_buttonconfig, text="UP").grid(row=3, column=0)
entry_up = Entry(frame_buttonconfig)
entry_up.grid(row=3,column=1)
label_down = Label(frame_buttonconfig, text="DOWN").grid(row=3, column=2)
entry_down = Entry(frame_buttonconfig)
entry_down.grid(row=3,column=3)
label_left = Label(frame_buttonconfig, text="LEFT").grid(row=3, column=4)
entry_left = Entry(frame_buttonconfig)
entry_left.grid(row=3,column=5)
label_right = Label(frame_buttonconfig, text = "RIGHT").grid(row=3, column=6)
entry_right = Entry(frame_buttonconfig)
entry_right.grid(row=3,column=7)

label_start = Label(frame_buttonconfig, text="START").grid(row=4, column=0)
entry_start = Entry(frame_buttonconfig)
entry_start.grid(row=4,column=1)
label_select = Label(frame_buttonconfig, text = "SELECT").grid(row=4, column=2)
entry_select = Entry(frame_buttonconfig)
entry_select.grid(row=4,column=3)
label_turbo = Label(frame_buttonconfig, text="TURBO").grid(row=4, column=4)
entry_turbo = Entry(frame_buttonconfig)
entry_turbo.grid(row=4,column=5)
label_home = Label(frame_buttonconfig, text="HOME").grid(row=4, column=6)
entry_home = Entry(frame_buttonconfig)
entry_home.grid(row=4,column=7)


def get_button_threshold(serial_port, addr):
    writestr = 'GET;' + str(addr) + '\n'
    serial_port.write(writestr.encode())
    sleep(0.05)
    val = serial_port.readline()
    print(val)
    return float(val)
def initialize_entries(serial_port):
    global entry_lp, entry_mp, entry_hp, entry_shp, entry_lk, entry_mk, entry_hk, entry_shk, entry_up, entry_down, entry_left, entry_right, entry_start, entry_select, entry_home, entry_turbo
    #entry_lp.delete(0, END)
    entry_lp.insert(0, str(get_button_threshold(serial_port, 0)))
    #entry_mp.delete(0, END)
    entry_mp.insert(0, str(get_button_threshold(serial_port, 4)))
    #entry_hp.delete(0, END)
    entry_hp.insert(0, str(get_button_threshold(serial_port, 8)))
    #entry_shp.delete(0, END)
    entry_shp.insert(0, str(get_button_threshold(serial_port, 12)))
    
    #entry_lk.delete(0,END)
    entry_lk.insert(0, str(get_button_threshold(serial_port, 16)))
    #entry_mk.delete(0, END)
    entry_mk.insert(0, str(get_button_threshold(serial_port, 20)))
    #entry_hk.delete(0, END)
    entry_hk.insert(0, str(get_button_threshold(serial_port, 24)))
    #entry_shk.delete(0, END)
    entry_shk.insert(0, str(get_button_threshold(serial_port, 28)))

    #entry_left.delete(0, END)
    entry_left.insert(0, str(get_button_threshold(serial_port, 32)))
    #entry_right.delete(0, END)
    entry_right.insert(0, str(get_button_threshold(serial_port, 36)))
    #entry_up.delete(0, END)
    entry_up.insert(0, str(get_button_threshold(serial_port, 40)))
    #entry_down.delete(0, END)
    entry_down.insert(0, str(get_button_threshold(serial_port, 44)))       

    #entry_start.delete(0, END)
    entry_start.insert(0, str(get_button_threshold(serial_port, 48)))
    #entry_select.delete(0, END)
    entry_select.insert(0, str(get_button_threshold(serial_port, 52)))
    #entry_home.delete(0, END)
    entry_home.insert(0, str(get_button_threshold(serial_port, 56)))
    #entry_turbo.delete(0, END)
    entry_turbo.insert(0, str(get_button_threshold(serial_port, 60)))       
5
def submit_new_thresholds():
    global serial_port
    lp_val = entry_lp.get()
    st = 'LP;' + str(lp_val) + '\r\n'
    serial_port.write(st.encode())
    sleep(2)
    mp_val = entry_mp.get()
    st = 'MP;' + str(mp_val) + '\r\n'
    serial_port.write(st.encode())
    sleep(2)
    hp_val = entry_hp.get()
    st = 'HP;' + str(hp_val) + '\r\n'
    serial_port.write(st.encode())
    sleep(2)
    shp_val = entry_shp.get()
    st = 'SHP;' + str(shp_val) + '\r\n'
    serial_port.write(st.encode())
    sleep(2)

    lk_val = entry_lk.get()
    st = 'LK;' + str(lk_val) + '\r\n'
    serial_port.write(st.encode())
    sleep(2)
    mk_val = entry_mk.get()
    st = 'MK;' + str(mk_val) + '\r\n'
    serial_port.write(st.encode())
    sleep(2)
    hk_val = entry_hk.get()
    st = 'HK;' + str(hk_val) + '\r\n'
    serial_port.write(st.encode())
    sleep(2)
    shk_val = entry_shk.get()
    st = 'SHK;' + str(shk_val) + '\r\n'
    serial_port.write(st.encode())
    sleep(2)

    left_val = entry_left.get()
    st = 'LEFT;' + str(left_val) + '\r\n'
    serial_port.write(st.encode())
    sleep(2)
    right_val = entry_right.get()
    st = 'RIGHT;' + str(right_val) + '\r\n'
    serial_port.write(st.encode())
    sleep(2)
    up_val = entry_up.get()
    st = 'UP;' + str(up_val) + '\r\n'
    serial_port.write(st.encode())
    sleep(2)
    down_val = entry_down.get()
    st = 'DOWN;' + str(down_val) + '\r\n'
    serial_port.write(st.encode())
    sleep(2)

    start_val = entry_start.get()
    st = 'START;' + str(start_val) + '\r\n'
    serial_port.write(st.encode())
    sleep(2)
    select_val = entry_select.get()
    st = 'SELECT;' + str(select_val) + '\r\n'
    serial_port.write(st.encode())
    sleep(2)
    home_val = entry_home.get()
    st = 'HOME;' + str(home_val) + '\r\n'
    serial_port.write(st.encode())
    sleep(2)
    turbo_val = entry_turbo.get()
    st = 'TURBO;' + str(turbo_val) + '\r\n'
    serial_port.write(st.encode())
    sleep(2)

def connect_to_serial():
    global serial_port
    global frame_buttonconfig

    comport = listbox_comports.get(ACTIVE)
    comport = comport.split(':')[0]
    
    frame_buttonconfig.tkraise()
    frame_connect.destroy()

    serial_port = serial.Serial(comport, 57600)
    if serial_port.is_open:
        initialize_entries(serial_port)
        frame_buttonconfig.tkraise()
        frame_connect.destroy()
    print(comport)


button_openport = Button(frame_connect, text = "Open Config", command=connect_to_serial)
button_submitchanges = Button(frame_buttonconfig, text="Submit New Thresholds", command=submit_new_thresholds).grid(row=5, column=0,columnspan=8)


i = 0
for port, desc, hwid in sorted(ports):
    listbox_comports.insert(i,"{}: {}".format(port, desc))
    i += 1


label_connect.pack()
label_buttonsettings.grid(row=0,column=0, columnspan=8)
listbox_comports.pack()
button_openport.pack()

frame_connect.tkraise()
root.mainloop()
