from tkinter import *
import pymsgbox

# ================== THEME ==================
BG_MAIN = "#1e293b"
BTN_BG = "#2563eb"
BTN_EXIT = "#475569"
BTN_FG = "white"
LBL_FG = "#f8fafc"
ENTRY_BG = "white"

FONT_TITLE = ("Segoe UI", 22, "bold")
FONT_LABEL = ("Segoe UI", 12)
FONT_BTN = ("Segoe UI", 12, "bold")
FONT_ENTRY = ("Segoe UI", 11)

APP_PASSWORD = "123"

# ================== WINDOW ==================
win = Tk()
win.title("Library Management System")
win.configure(background=BG_MAIN)
win.state("zoomed")

# ================== MAIN SCREEN ==================
def main():
    mainwin = Canvas(win, bg=BG_MAIN, highlightthickness=0)
    mainwin.pack(fill="both", expand=True)

    def opencmd():
        pwd = pymsgbox.password(title="Password", text="Enter the password")
        if pwd != APP_PASSWORD:
            pymsgbox.alert("Enter the correct password")
            return

        mainwin.destroy()
        openwin = Canvas(win, bg=BG_MAIN, highlightthickness=0)
        openwin.pack(fill="both", expand=True)

        # ---------- MENU BUTTON ----------
        def menu_button(text, cmd, y):
            Button(
                openwin, text=text, command=cmd,
                fg=BTN_FG, bg=BTN_BG, font=FONT_BTN,
                width=25, height=2, bd=0,
                cursor="hand2"
            ).place(relx=0.5, y=y, anchor="center")

        # ================== REGISTER BOOK ==================
        def register():
            openwin.destroy()
            registerwin = Canvas(win, bg=BG_MAIN, highlightthickness=0)
            registerwin.pack(fill="both", expand=True)

            categories = ['Programming', 'Economics', 'Science']
            selected_option = StringVar(value=categories[0])

            Label(registerwin, text="Register Book", font=FONT_TITLE,
                  fg=LBL_FG, bg=BG_MAIN).place(relx=0.5, y=120, anchor="center")

            Label(registerwin, text="Category", fg=LBL_FG,
                  bg=BG_MAIN, font=FONT_LABEL).place(x=540, y=220)

            OptionMenu(registerwin, selected_option, *categories)\
                .place(x=540, y=250)

            Label(registerwin, text="Book Name", fg=LBL_FG,
                  bg=BG_MAIN, font=FONT_LABEL).place(x=540, y=300)

            booktxt = Text(registerwin, width=30, height=1,
                           font=FONT_ENTRY, bg=ENTRY_BG)
            booktxt.place(x=540, y=330)

            Label(registerwin, text="Book ID", fg=LBL_FG,
                  bg=BG_MAIN, font=FONT_LABEL).place(x=540, y=370)

            bookidtxt = Text(registerwin, width=30, height=1,
                             font=FONT_ENTRY, bg=ENTRY_BG)
            bookidtxt.place(x=540, y=400)

            def registerbook():
                book = booktxt.get("1.0", "end-1c")
                bid = bookidtxt.get("1.0", "end-1c")
                if not book or not bid:
                    pymsgbox.alert("All fields are required")
                    return

                files = {
                    "Science": "science.txt",
                    "Programming": "programming.txt",
                    "Economics": "economics.txt"
                }

                with open(files[selected_option.get()], 'a') as f:
                    f.write(book + "," + bid + "\n")

                pymsgbox.alert("Book Registered Successfully")
                booktxt.delete("1.0", END)
                bookidtxt.delete("1.0", END)

            Button(registerwin, text="✔ Register", command=registerbook,
                   fg=BTN_FG, bg=BTN_BG, font=FONT_BTN,
                   width=18, height=2, bd=0).place(x=560, y=460)

            Button(registerwin, text="⬅ Back",
                   command=lambda: (registerwin.destroy(), main()),
                   fg=BTN_FG, bg=BTN_EXIT, font=FONT_BTN,
                   width=18, height=2, bd=0).place(x=560, y=520)

        # ================== LEND BOOK ==================
        def lendbook():
            openwin.destroy()
            lendwin = Canvas(win, bg=BG_MAIN, highlightthickness=0)
            lendwin.pack(fill="both", expand=True)

            Label(lendwin, text="Lend Book", font=FONT_TITLE,
                  fg=LBL_FG, bg=BG_MAIN).place(relx=0.5, y=120, anchor="center")

            labels = ["Student Name", "Student USN", "Book ID"]
            entries = []
            y = 260

            for text in labels:
                Label(lendwin, text=text, fg=LBL_FG,
                      bg=BG_MAIN, font=FONT_LABEL).place(x=540, y=y)
                t = Text(lendwin, width=30, height=1,
                         font=FONT_ENTRY, bg=ENTRY_BG)
                t.place(x=540, y=y+30)
                entries.append(t)
                y += 80

            def lend():
                vals = [e.get("1.0", "end-1c") for e in entries]
                if "" in vals:
                    pymsgbox.alert("All fields are required")
                    return

                with open("lend.txt", "a") as f:
                    f.write(",".join(vals) + "\n")

                pymsgbox.alert("Book Lent Successfully")
                for e in entries:
                    e.delete("1.0", END)

            Button(lendwin, text="📤 Lend", command=lend,
                   fg=BTN_FG, bg=BTN_BG, font=FONT_BTN,
                   width=18, height=2, bd=0).place(x=560, y=520)

            Button(lendwin, text="⬅ Back",
                   command=lambda: (lendwin.destroy(), main()),
                   fg=BTN_FG, bg=BTN_EXIT, font=FONT_BTN,
                   width=18, height=2, bd=0).place(x=560, y=580)

        # ================== RETURN BOOK (FIXED) ==================
        def returnbookwin():
            openwin.destroy()
            retwin = Canvas(win, bg=BG_MAIN, highlightthickness=0)
            retwin.pack(fill="both", expand=True)

            Label(retwin, text="Return Book", font=FONT_TITLE,
                  fg=LBL_FG, bg=BG_MAIN).place(relx=0.5, y=120, anchor="center")

            Label(retwin, text="Student Name", fg=LBL_FG,
                  bg=BG_MAIN, font=FONT_LABEL).place(x=540, y=280)
            nametxt = Text(retwin, width=30, height=1,
                           font=FONT_ENTRY, bg=ENTRY_BG)
            nametxt.place(x=540, y=310)

            Label(retwin, text="Book ID", fg=LBL_FG,
                  bg=BG_MAIN, font=FONT_LABEL).place(x=540, y=360)
            bookidtxt = Text(retwin, width=30, height=1,
                             font=FONT_ENTRY, bg=ENTRY_BG)
            bookidtxt.place(x=540, y=390)

            def returnbook():
                name = nametxt.get("1.0", "end-1c")
                bid = bookidtxt.get("1.0", "end-1c")
                if not name or not bid:
                    pymsgbox.alert("All fields are required")
                    return

                found = False
                with open("lend.txt", "r") as f:
                    lines = f.readlines()

                with open("lend.txt", "w") as f:
                    for line in lines:
                        data = line.strip().split(",")
                        if bid == data[2]:
                            found = True
                        else:
                            f.write(line)

                if found:
                    pymsgbox.alert("Book Returned Successfully")
                else:
                    pymsgbox.alert("Book ID not found in lending records")

                nametxt.delete("1.0", END)
                bookidtxt.delete("1.0", END)

            Button(retwin, text="📥 Return", command=returnbook,
                   fg=BTN_FG, bg=BTN_BG, font=FONT_BTN,
                   width=18, height=2, bd=0).place(x=560, y=460)

            Button(retwin, text="⬅ Back",
                   command=lambda: (retwin.destroy(), main()),
                   fg=BTN_FG, bg=BTN_EXIT, font=FONT_BTN,
                   width=18, height=2, bd=0).place(x=560, y=520)

        # ---------- DASHBOARD ----------
        Label(openwin, text="Library Dashboard", font=FONT_TITLE,
              fg=LBL_FG, bg=BG_MAIN).place(relx=0.5, y=140, anchor="center")

        menu_button("📘 Register Book", register, 280)
        menu_button("📤 Lend Book", lendbook, 340)
        menu_button("📥 Register Return", returnbookwin, 400)
        menu_button("❌ Exit", lambda: (openwin.destroy(), main()), 460)

    Button(mainwin, text="OPEN LIBRARY", command=opencmd,
           fg=BTN_FG, bg=BTN_BG, font=FONT_TITLE,
           width=20, height=2, bd=0).place(relx=0.5, rely=0.5, anchor="center")

# ================== START ==================
main()
win.mainloop()
