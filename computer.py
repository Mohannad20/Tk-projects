from customtkinter import *

window = CTk()


class computer:
    motherboardPrices = {
        "ASSUS": 700,
        "VIA": 600,
        "SIS": 500
    }
    categories = {
        "Other" : 0.2,
        "Students": 0.7,
        "Seniors": 0.6,
        "Teachers/Educators": 0.5
    }

    def __init__(self,window) :
        self.window = window
        self.window.geometry("840x560")
        self.window.title("Build your Personal Computer")

        CTkLabel(self.window,
                text="Build your Personal Computer",
                font=("Poppins Bold", 24),
                width=840,
                height=60,
                bg_color='#6b9080',
                text_color='black',
                ).grid(row=1, columnspan=5)

        CTkLabel(self.window,
                 text="Motherboard",
                 font=("Poppins Bold", 20),
                 text_color='black',
                 bg_color='#cce3de').grid(column=2, row=2)
        self.cartEntry = CTkComboBox(self.window,
                                     values=list(self.motherboardPrices.keys()),
                                     font=("Poppins", 16),
                                     text_color='black',
                                     bg_color='#cce3de',
                                     fg_color='#6b9080',)
        self.cartEntry.grid(column=3, row=2, pady=10)

        CTkLabel(self.window,
                 text="Monitor",
                 font=("Poppins Bold", 20),
                 text_color='black',
                 bg_color='#cce3de').grid(column = 2, row=3)

        self.choiceType = StringVar()
        CTkLabel(self.window,
                 text="Type",
                 font=("Poppins Bold", 16),
                 text_color='black',
                 bg_color='#cce3de').grid(column = 2, row=4)
        self.typeEntry = CTkRadioButton(self.window,
                                        value='CRT',
                                        variable=self.choiceType,
                                        text='CRT (cathode ray tube)',
                                        font=("Poppins", 16),
                                        text_color='black',
                                        bg_color='#cce3de')
        self.typeEntry.grid(column=2, row=5)
        self.typeEntry = CTkRadioButton(self.window,
                                        value='LCD',
                                        variable=self.choiceType,
                                        text='LCD (liquid crystal display)',
                                        font=("Poppins", 16),
                                        text_color='black',
                                        bg_color='#cce3de',)
        self.typeEntry.grid(column=3, row=5)
        self.typeEntry = CTkRadioButton(self.window,
                                        value='LED',
                                        variable=self.choiceType,
                                        text='LED (light-emitting diodes)',
                                        font=("Poppins", 16),
                                        text_color='black',
                                        bg_color='#cce3de',)
        self.typeEntry.grid(column=4, row=5, pady=10)

        self.choiceSize = StringVar()
        CTkLabel(self.window,
                 text="Size",
                 font=("Poppins Bold", 18),
                 text_color='black',
                 bg_color='#cce3de').grid(column=2, row=7)
        self.typeEntry = CTkRadioButton(self.window,
                                        value='15',
                                        variable=self.choiceSize,
                                        text='15',
                                        font=("Poppins", 16),
                                        text_color='black',
                                        bg_color='#cce3de',)
        self.typeEntry.grid(column=2, row=8)
        self.typeEntry = CTkRadioButton(self.window,
                                        value='22',
                                        variable=self.choiceSize,
                                        text='22',
                                        font=("Poppins", 16),
                                        text_color='black',
                                        bg_color='#cce3de')
        self.typeEntry.grid(column=3, row=8)
        self.typeEntry = CTkRadioButton(self.window,
                                        value='34',
                                        variable=self.choiceSize,
                                        text='34',
                                        font=("Poppins", 16),
                                        text_color='black',
                                        bg_color='#cce3de',)
        self.typeEntry.grid(column=4, row=8, pady=10)

        CTkLabel(self.window,
                 text="Options",
                 font=("Poppins Bold", 20),
                 text_color='black',
                 bg_color='#cce3de',).grid(column=2, row=9)
        self.card = IntVar()
        self.satCard = CTkCheckBox(self.window,
                                   text='Tv Tuner Card',
                                   variable=self.card,
                                   onvalue=900,
                                   offvalue=0,
                                   font=("Poppins", 12),
                                   text_color='black',
                                   bg_color='#cce3de',)
        self.satCard.grid(column=3, row=9, pady=3)
        self.printer = IntVar()
        self.satPrinter = CTkCheckBox(self.window,
                                      text='Printer',
                                      variable=self.printer,
                                      onvalue=600,
                                      offvalue=0,
                                      font=("Poppins", 12),
                                      text_color='black',
                                      bg_color='#cce3de',)
        self.satPrinter.grid(column=3, row=10, pady=3)
        self.scanner = IntVar()
        self.satScanner = CTkCheckBox(self.window,
                                      text='Scanner',
                                      variable=self.scanner,
                                      onvalue=500,
                                      offvalue=0,
                                      font=("Poppins", 12),
                                      text_color='black',
                                      bg_color='#cce3de',)
        self.satScanner.grid(column=3, row=11, pady=3)

        CTkLabel(self.window,
                 text="Category",
                 font=("Poppins Bold", 20),
                 text_color='black',
                 bg_color='#cce3de').grid(column=2, row=13, pady=10)
        self.catEntry = CTkComboBox(self.window,
                                    font=("Poppins", 14),
                                    text_color='black',
                                    bg_color='#cce3de',
                                    fg_color='#6b9080',
                                    values=list(self.categories.keys()))
        self.catEntry.grid(column= 3, row= 13)

        CTkButton(self.window,
                  text='calculate the price',
                  font=("Poppins Bold", 16),
                  text_color='black',
                  fg_color='#6b9080',
                  bg_color='#cce3de',
                  command=self.calculate).grid(column= 2, row= 17, pady=10)

        self.total = IntVar()
        CTkLabel(self.window,
                 text="This PC Will Cost You",
                 font=("Poppins Bold", 14),
                 text_color='black',
                 bg_color='#cce3de').grid(column=2, row=18, pady=10)
        self.costEntry = CTkEntry(self.window,
                                  state='readonly',
                                  bg_color='#cce3de',
                                  fg_color='#6b9080',
                                  textvariable=self.total)
        self.costEntry.grid(column=3, row=18)

    def calculate(self):
        choice_type = self.choiceType.get()
        choice_size = self.choiceSize.get()
        cart_entry = self.cartEntry.get()
        cat_entry = self.catEntry.get()

        monitor_prices = {
            ('CRT', '15'): 700,
            ('CRT', '22'): 800,
            ('CRT', '34'): 1000,
            ('LCD', '15'): 700,
            ('LCD', '22'): 800,
            ('LCD', '34'): 1000,
            ('LED', '15'): 700,
            ('LED', '22'): 800,
            ('LED', '34'): 1000
        }

        monitor_price = monitor_prices.get((choice_type, choice_size), 0)
        option_price = self.card.get() + self.printer.get() + self.scanner.get()
        motherboard_price = self.motherboardPrices.get(cart_entry, 0)
        catReduction = self.categories.get(cat_entry, 0)

        self.totalPrice = monitor_price + option_price + motherboard_price

        x = round(self.totalPrice*(1-catReduction), 2)
        self.total.set(x)
        


computer(window)
window.config(bg='#cce3de')
window.mainloop()