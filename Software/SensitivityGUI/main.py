import serial
from serial import SerialException
from tkinter import * 
from tkinter import ttk
from time import sleep

import serial.tools.list_ports

import threading


ports = serial.tools.list_ports.comports()
serial_port = None

maxvals = []

root = Tk()
root.title("Faraday Fightstick Configurator")
frame_connect = Frame(root)
frame_buttonconfig = Frame(root)

frame_connect.grid()
#rame_buttonconfig.pack()

listbox_comports = Listbox(frame_connect,height = 10, width = 50)

progressbar_reading = ttk.Progressbar(frame_connect, orient=HORIZONTAL,length=160)
progressbar_writing = ttk.Progressbar(frame_buttonconfig, orient=HORIZONTAL,length=160)

label_connect = Label(frame_connect, text="Select a Serial Port")
label_buttonsettings = Label(frame_buttonconfig, text="Button Sensitivity Configuration")



label_lp = Label(frame_buttonconfig, text="LP").grid(row=1, column=0)
slider_lp = Scale(frame_buttonconfig, from_=100, to=0)
slider_lp.grid(row=1,column=1)
label_mp = Label(frame_buttonconfig, text="MP").grid(row=1, column=2)
slider_mp = Scale(frame_buttonconfig, from_=100, to=0)
slider_mp.grid(row=1,column=3)
label_hp = Label(frame_buttonconfig, text="HP").grid(row=1, column=4)
slider_hp = Scale(frame_buttonconfig, from_=100, to=0)
slider_hp.grid(row=1,column=5)
label_shp = Label(frame_buttonconfig, text="SHP").grid(row=1, column=6)
slider_shp = Scale(frame_buttonconfig, from_=100, to=0)
slider_shp.grid(row=1,column=7)

label_lk = Label(frame_buttonconfig, text="LK").grid(row=2, column=0)
slider_lk = Scale(frame_buttonconfig, from_=100, to=0)
slider_lk.grid(row=2,column=1)
label_mk = Label(frame_buttonconfig, text='MK').grid(row=2, column=2)
slider_mk = Scale(frame_buttonconfig, from_=100, to=0)
slider_mk.grid(row=2,column=3)
label_hk = Label(frame_buttonconfig, text="HK").grid(row=2, column=4)
slider_hk = Scale(frame_buttonconfig, from_=100, to=0)
slider_hk.grid(row=2,column=5)
label_shk = Label(frame_buttonconfig, text="SHK").grid(row=2, column=6)
slider_shk = Scale(frame_buttonconfig, from_=100, to=0)
slider_shk.grid(row=2,column=7)

label_up = Label(frame_buttonconfig, text="UP").grid(row=3, column=0)
slider_up = Scale(frame_buttonconfig, from_=100, to=0)
slider_up.grid(row=3,column=1)
label_down = Label(frame_buttonconfig, text="DOWN").grid(row=3, column=2)
slider_down = Scale(frame_buttonconfig, from_=100, to=0)
slider_down.grid(row=3,column=3)
label_left = Label(frame_buttonconfig, text="LEFT").grid(row=3, column=4)
slider_left = Scale(frame_buttonconfig, from_=100, to=0)
slider_left.grid(row=3,column=5)
label_right = Label(frame_buttonconfig, text = "RIGHT").grid(row=3, column=6)
slider_right = Scale(frame_buttonconfig, from_=100, to=0)
slider_right.grid(row=3,column=7)

label_start = Label(frame_buttonconfig, text="START").grid(row=4, column=0)
slider_start = Scale(frame_buttonconfig, from_=100, to=0)
slider_start.grid(row=4,column=1)
label_select = Label(frame_buttonconfig, text = "SELECT").grid(row=4, column=2)
slider_select = Scale(frame_buttonconfig, from_=100, to=0)
slider_select.grid(row=4,column=3)
label_turbo = Label(frame_buttonconfig, text="TURBO").grid(row=4, column=4)
slider_turbo = Scale(frame_buttonconfig, from_=100, to=0)
slider_turbo.grid(row=4,column=5)
label_home = Label(frame_buttonconfig, text="HOME").grid(row=4, column=6)
slider_home = Scale(frame_buttonconfig, from_=100, to=0)
slider_home.grid(row=4,column=7)



def get_button_threshold(serial_port, addr):
    writestr = 'GETTRIG;' + str(addr) + '\n'
    serial_port.write(writestr.encode())
    sleep(0.05)
    val = serial_port.readline()
    print(val)
    return float(val)
def get_all_thresholds(serial_port):
    writestr = 'GETALLTRIG;\n'
    serial_port.write(writestr.encode())
    sleep(0.05)
    val = serial_port.readline()
    val = str(val)[2::].split(';')
    val[15] = val[15][:-6]
    return val
def get_maxvals(serial_port):
    writestr = 'GETALLVAL;' + '\n'
    serial_port.write(writestr.encode())
    sleep(0.05)
    val = serial_port.readline()
    val = str(val)[2::].split(';')
    val[15] = val[15][:-6]
    return val


def initialize_entries():
    global maxvals, serial_port, progressbar_reading, slider_lp, slider_mp, slider_hp, slider_shp, slider_lk, slider_mk, slider_hk, slider_shk, slider_up, slider_down, slider_left, slider_right, slider_start, slider_select, slider_home, slider_turbo
    
    maxvals = get_maxvals(serial_port)
    vals = get_all_thresholds(serial_port)

    slider_lp.set(int(float(vals[0])/float(maxvals[0])*100))
    progressbar_reading.step(float(1)/16*100)
    slider_mp.set(int(float(vals[1])/float(maxvals[1])*100))
    progressbar_reading.step(float(1)/16*100)
    slider_hp.set(int(float(vals[2])/float(maxvals[2])*100))
    progressbar_reading.step(float(1)/16*100)
    slider_shp.set(int(float(vals[3])/float(maxvals[3])*100))
    
    progressbar_reading.step(float(1)/16*100)
    slider_lk.set(int(float(vals[4])/float(maxvals[4])*100))
    progressbar_reading.step(float(1)/16*100)
    slider_mk.set(int(float(vals[5])/float(maxvals[5])*100))
    progressbar_reading.step(float(1)/16*100)
    slider_hk.set(int(float(vals[6])/float(maxvals[6])*100))
    progressbar_reading.step(float(1)/16*100)
    slider_shk.set(int(float(vals[7])/float(maxvals[7])*100))

    progressbar_reading.step(float(1)/16*100)
    slider_left.set(int(float(vals[8])/float(maxvals[8])*100))
    progressbar_reading.step(float(1)/16*100)
    slider_right.set(int(float(vals[10])/float(maxvals[10])*100))
    progressbar_reading.step(float(1)/16*100)
    slider_up.set(int(float(vals[11])/float(maxvals[11])*100))
    progressbar_reading.step(float(1)/16*100)
    slider_down.set(int(float(vals[9])/float(maxvals[9])*100))

    progressbar_reading.step(float(1)/16*100)
    slider_start.set(int(float(vals[13])/float(maxvals[13])*100))
    progressbar_reading.step(float(1)/16*100)
    slider_select.set(int(float(vals[12])/float(maxvals[12])*100))
    progressbar_reading.step(float(1)/16*100)
    slider_home.set(int(float(vals[14])/float(maxvals[14])*100))
    progressbar_reading.step(float(1)/16*100)
    slider_turbo.set(int(float(vals[15])/float(maxvals[15])*100))
    progressbar_reading.step(float(1)/16*100)

    frame_buttonconfig.grid(row=0, column=0)
    frame_buttonconfig.tkraise()
    frame_connect.destroy()


def submit_new_thresholds():
    threading.Thread(target=submit_new_thresholds_threaded).start()
def submit_new_thresholds_threaded():
    global serial_port, progressbar_writing, maxvals
    lp_val = slider_lp.get() / 100.0 * float(maxvals[0])
    st = 'LP;' + str(lp_val) + '\r\n'
    serial_port.write(st.encode())
    sleep(2)
    progressbar_writing.step(float(1)/16*100)
    mp_val = slider_mp.get() / 100.0 * float(maxvals[1])
    st = 'MP;' + str(mp_val) + '\r\n'
    serial_port.write(st.encode())
    sleep(2)
    progressbar_writing.step(float(1)/16*100)
    hp_val = slider_hp.get() / 100.0 * float(maxvals[2])
    st = 'HP;' + str(hp_val) + '\r\n'
    serial_port.write(st.encode())
    sleep(2)
    progressbar_writing.step(float(1)/16*100)
    shp_val = slider_shp.get() / 100.0 * float(maxvals[3])
    st = 'SHP;' + str(shp_val) + '\r\n'
    serial_port.write(st.encode())
    sleep(2)
    progressbar_writing.step(float(1)/16*100)
    lk_val = slider_lk.get() / 100.0 * float(maxvals[4])
    st = 'LK;' + str(lk_val) + '\r\n'
    serial_port.write(st.encode())
    sleep(2)
    progressbar_writing.step(float(1)/16*100)
    mk_val = slider_mk.get() / 100.0 * float(maxvals[5])
    st = 'MK;' + str(mk_val) + '\r\n'
    serial_port.write(st.encode())
    sleep(2)
    progressbar_writing.step(float(1)/16*100)
    hk_val = slider_hk.get() / 100.0 * float(maxvals[6])
    st = 'HK;' + str(hk_val) + '\r\n'
    serial_port.write(st.encode())
    sleep(2)
    progressbar_writing.step(float(1)/16*100)
    shk_val = slider_shk.get() / 100.0 * float(maxvals[7])
    st = 'SHK;' + str(shk_val) + '\r\n'
    serial_port.write(st.encode())
    sleep(2)
    progressbar_writing.step(float(1)/16*100)

    left_val = slider_left.get() / 100.0 * float(maxvals[8])
    st = 'LEFT;' + str(left_val) + '\r\n'
    serial_port.write(st.encode())
    sleep(2)
    progressbar_writing.step(float(1)/16*100)
    right_val = slider_right.get() / 100.0 * float(maxvals[10])
    st = 'RIGHT;' + str(right_val) + '\r\n'
    serial_port.write(st.encode())
    sleep(2)
    progressbar_writing.step(float(1)/16*100)
    up_val = slider_up.get() / 100.0 * float(maxvals[11])
    st = 'UP;' + str(up_val) + '\r\n'
    serial_port.write(st.encode())
    sleep(2)
    progressbar_writing.step(float(1)/16*100)
    down_val = slider_down.get() / 100.0 * float(maxvals[9])
    st = 'DOWN;' + str(down_val) + '\r\n'
    serial_port.write(st.encode())
    sleep(2)
    progressbar_writing.step(float(1)/16*100)

    start_val = slider_start.get() / 100.0 * float(maxvals[13])
    st = 'START;' + str(start_val) + '\r\n'
    serial_port.write(st.encode())
    sleep(2)
    progressbar_writing.step(float(1)/16*100)
    select_val = slider_select.get() / 100.0 * float(maxvals[12])
    st = 'SELECT;' + str(select_val) + '\r\n'
    serial_port.write(st.encode())
    sleep(2)
    progressbar_writing.step(float(1)/16*100)
    home_val = slider_home.get() / 100.0 * float(maxvals[14])
    st = 'HOME;' + str(home_val) + '\r\n'
    serial_port.write(st.encode())
    sleep(2)
    progressbar_writing.step(float(1)/16*100)
    turbo_val = slider_turbo.get() / 100.0 * float(maxvals[15])
    st = 'TURBO;' + str(turbo_val) + '\r\n'
    serial_port.write(st.encode())
    sleep(2)
    progressbar_writing.step(float(1)/16*100)

def connect_to_serial(comport=None):
    global serial_port
    global frame_buttonconfig

    if comport == None:
        comport = listbox_comports.get(ACTIVE)
        comport = comport.split(':')[0]

    serial_port = serial.Serial(comport, 57600)
    if serial_port.is_open:
        threading.Thread(target=initialize_entries).start()


button_openport = Button(frame_connect, text = "Open Config", command=connect_to_serial)
button_submitchanges = Button(frame_buttonconfig, text="Submit New Thresholds", command=submit_new_thresholds).grid(row=5, column=0,columnspan=8)
progressbar_writing.grid(row=6,column=0,columnspan=8)

i = 0
for port, desc, hwid in sorted(ports):
    listbox_comports.insert(i,"{}: {}".format(port, desc))
    i += 1
    if "Arduino Micro" in desc:
        connect_to_serial(comport=port)


label_connect.pack()
progressbar_reading.pack()
label_buttonsettings.grid(row=0,column=0, columnspan=8)
listbox_comports.pack()
button_openport.pack()

frame_connect.tkraise()
root.mainloop()
