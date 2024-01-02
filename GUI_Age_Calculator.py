from tkinter import *
from tkinter import messagebox
import webbrowser


def clr():
    d.delete(0, END)
    m.delete(0, END)
    y.delete(0, END)
    gd.delete(0, END)
    gm.delete(0, END)
    gy.delete(0, END)
    ry.delete(0, END)
    rm.delete(0, END)
    rd.delete(0, END)


def check_err():
    if (d.get() == "" or m.get() == ""
            or y.get() == "" or gd.get() == ""
            or gm.get() == "" or gy.get() == ""):
        messagebox.showerror("Input Error", "Please fill in all fields")
        clr()
        return -1


def calc_age():
    value = check_err()

    if value == -1:
        return

    else:
        bd = int(d.get())
        bm = int(m.get())
        by = int(y.get())

        gd_ = int(gd.get())
        gm_ = int(gm.get())
        gy_ = int(gy.get())

        mdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if bd > gd_:
            gm_ -= 1
            gd_ += mdays[bm - 1]

        if bm > gm_:
            gy_ -= 1
            gm_ += 12

        cd = gd_ - bd
        cm = gm_ - bm
        cy = gy_ - by

        ry.delete(0, END)
        rm.delete(0, END)
        rd.delete(0, END)

        ry.insert(0, str(cy))
        rm.insert(0, str(cm))
        rd.insert(0, str(cd))


if __name__ == "__main__":

    g = Tk()

    g.configure(background="gray69")

    g.title("Calculate Your Age")

    g.geometry("500x300")

    dob_l = Label(g, text="Date Of Birth", bg="black", fg="white")
    g_l = Label(g, text="Given Date", bg="black", fg="white")

    d_l = Label(g, text="Day", bg="gray69")
    m_l = Label(g, text="Month", bg="gray69")
    y_l = Label(g, text="Year", bg="gray69")

    gd_l = Label(g, text="Given Day", bg="gray69")
    gm_l = Label(g, text="Given Month", bg="gray69")
    gy_l = Label(g, text="Given Year", bg="gray69")

    ry_l = Label(g, text="Years", bg="gray69")
    rm_l = Label(g, text="Months", bg="gray69")
    rd_l = Label(g, text="Days", bg="gray69")

    ra_b = Button(g, text="Resultant Age", fg="Black",
                  bg="Red", command=calc_age)
    ca_b = Button(g, text="Clear All", fg="Black", bg="Red", command=clr)
    
    ra_c = Button(g, text="Project by KyreX",
                  command=webbrowser.open("https://github.com/Saaalil"))

    d = Entry(g)
    m = Entry(g)
    y = Entry(g)

    gd = Entry(g)
    gm = Entry(g)
    gy = Entry(g)

    ry = Entry(g)
    rm = Entry(g)
    rd = Entry(g)

    dob_l.grid(row=0, column=1)
    d_l.grid(row=1, column=0)
    d.grid(row=1, column=1)

    m_l.grid(row=2, column=0)
    m.grid(row=2, column=1)

    y_l.grid(row=3, column=0)
    y.grid(row=3, column=1)

    g_l.grid(row=0, column=4)

    gd_l.grid(row=1, column=3)
    gd.grid(row=1, column=4)

    gm_l.grid(row=2, column=3)
    gm.grid(row=2, column=4)

    gy_l.grid(row=3, column=3)
    gy.grid(row=3, column=4)

    ra_b.grid(row=4, column=2)

    ry_l.grid(row=5, column=2)
    ry.grid(row=6, column=2)

    rm_l.grid(row=7, column=2)
    rm.grid(row=8, column=2)

    rd_l.grid(row=9, column=2)
    rd.grid(row=10, column=2)

    ca_b.grid(row=12, column=2)

    g.mainloop()
    
    
    
    # "A project By Saalil/KyreX"
