from tkinter import *
from K_welcome_message import *
from K_Convert import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo


class Konwerter(Tk):

    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.winfo_parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        # Pola tekstowe sciezek do plikow
        self.InputEntryVariable = StringVar()
        self.InputEntry = Entry(self, textvariable=self.InputEntryVariable, width=100)
        self.InputEntry.grid(column=1, row=0, sticky='EW')

        self.OutputEntryVariable = StringVar()
        self.OutputEntry = Entry(self, textvariable=self.OutputEntryVariable, width=100)
        self.OutputEntry.grid(column=1, row=1, sticky=E)

        # Przyciski wyboru plikow
        buttonOpenInputFile = Button(self, text=u"Wskaz plik raportu",
                                     command=self.open_file_in, height=1, width=22)
        buttonOpenInputFile.grid(column=2, row=0, columnspan=2, sticky=EW)

        buttonOpenOutputFile = Button(self, text=u"Wskaz plik wynikowy",
                                      command=self.open_file_out, height=1, width=22)
        buttonOpenOutputFile.grid(column=2, row=1, columnspan=2, sticky=EW)

        # Przycisk instrukcji
        buttonInstrukcje = Button(self, text=u"Instrukcje",
                                  command=self.instructions_clicked)
        buttonInstrukcje.grid(column=0, row=3, sticky=W)

        # Przyciski uruchomienia konwertera i wyjscia z programu

        buttonRun = Button(self, text=u"Konwertuj",
                           command=self.run, height=1, width=10)
        buttonRun.grid(column=2, row=3, sticky=EW)
        buttonRun.configure(foreground='green')

        buttonExit = Button(self, text="Wyjdz",
                            command=self.quit, height=1, width=10)
        buttonExit.grid(column=3, row=3, sticky=E)
        buttonExit.configure(foreground='red')

        # Teksty oznaczenia pol sciezek do plikow
        labelInput = Label(self, text="Sciezka do pliku raportu    ", anchor="w")
        labelInput.grid(column=0, row=0, sticky=W)

        labelOutput = Label(self, text="Sciezka do pliku wyjsciowego  ", anchor="w")
        labelOutput.grid(column=0, row=1, sticky=W)

        # Teksty w stopce
        labelStopka1 = Label(self, text="Konwerter Raportow v 1.1", anchor="w")
        labelStopka1.grid(column=0, row=5, sticky=W)

        labelStopka2 = Label(self, text="Grzegorz Pawlowski: g.pawlowski.65@gmail.com", anchor="e")
        labelStopka2.grid(column=3, row=5, sticky=E)

        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, True)

    # FUNKCJE
    def instructions_clicked(self):
        instrukcje = main_c.message
        showinfo("Instrukcje", instrukcje)

    def open_file_in(self):
        filename_x = askopenfilename()
        self.InputEntryVariable.set(filename_x)
        filename_y = filename_x.replace(".", "_conv.")
        self.OutputEntryVariable.set(filename_y)

    def open_file_out(self):
        filename_z = askopenfilename()
        self.OutputEntryVariable.set(filename_z)

    def is_empty(self, string, in_out):
        if string == "":
            showinfo("Blad", "Sciezka " + in_out + " jest pusta")

    def run(self):
        in_filepath = self.InputEntryVariable.get()
        out_filepath = self.OutputEntryVariable.get()

        self.is_empty(in_filepath, "pliku raportu")
        self.is_empty(out_filepath, "pliku wyjsciowego")

        in_file = open(in_filepath, 'r')
        out_file = open(out_filepath, 'w')

        convert(in_file, out_file)


if __name__ == "__main__":
    app = Konwerter(None)
    app.title("Konwerter Raportow v 1.1")
    app.mainloop()
