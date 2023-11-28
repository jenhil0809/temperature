import tkinter as tk
import temperature_calcs


class TemperatureConverter(tk.Tk):
    def __init__(self):
        # Initialised the tk.Tk app
        super().__init__()
        self.bgcolor = "lightblue1"
        self.config(bg=self.bgcolor)
        self.unit_from = tk.StringVar()
        self.unit_from.set("farenheit")
        self.unit_to = tk.StringVar()
        self.unit_to.set("celcius")
        self.value = tk.DoubleVar()
        self.value.set(0.00)

        self.title('Temperature converter')

        self.label = tk.Label(text="Temperature converter", font=("Arial", 14), bg=self.bgcolor)
        self.label.pack(side=tk.TOP)

        self.get_value = GetValue(self)
        self.get_value.pack(ipadx=10, side=tk.LEFT)

        self.get_unit_from = UnitFrom(self)
        self.get_unit_from.pack(side=tk.LEFT)

        self.get_unit_to = UnitTo(self)
        self.get_unit_to.pack(side=tk.LEFT)

        self.convert_frame = DisplayConversion(self)
        self.convert_frame.pack(side=tk.LEFT)


class DisplayConversion(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg=self.master.bgcolor)

        self.response_txt = tk.Label(self, text="", bg=self.master.bgcolor, font=("Arial", 10, "bold"))
        self.convert_txt = tk.Label(self, text="", bg=self.master.bgcolor, font=("Arial", 8, "italic"), foreground="gray12")
        self.btn = tk.Button(self, text="Convert", command=self.get_val, bg="cadetblue1", font=("Arial", 10, "bold"))
        result = tk.StringVar()
        result.set(str(self.get_val()))
        self.place_widgets()

    def get_val(self):
        unit_from = self.master.unit_from.get()
        unit_to = self.master.unit_to.get()
        value = self.master.value.get()
        result = f"{temperature_calcs.convert(unit_from, unit_to, value):.2f} {unit_to}"
        self.response_txt.config(text=result)
        self.convert_rate(unit_from, unit_to)

    def convert_rate(self, unit_from, unit_to):
        if unit_from == "kelvin" and unit_to == "celcius":
            self.convert_txt.config(text="convertion rate:\nkelvin-273=celcius")
        elif unit_from == "celcius" and unit_to == "kelvin":
            self.convert_txt.config(text="convertion rate:\ncelcius+273=kelvin")
        elif unit_from == "farenheit" and unit_to == "celcius":
            self.convert_txt.config(text="convertion rate:\n(farenheit-32)*5/9=celcius")
        elif unit_from == "celcius" and unit_to == "farenheit":
            self.convert_txt.config(text="convertion rate:\ncelcius*9/5+32=farenheit")
        elif unit_from == "farenheit" and unit_to == "kelvin":
            self.convert_txt.config(text="convertion rate:\n(farenheit-32)*5/9+273=kelvin")
        elif unit_from == "kelvin" and unit_to == "farenheit":
            self.convert_txt.config(text="convertion rate:\n(kelvin-273)*9/5+32=farenheit")
        else:
            self.convert_txt.config(text=f"convertion rate:\n{unit_from}={unit_to}")



    def place_widgets(self):
        settings = {'padx': 10, 'pady': 10}

        self.btn.grid(row=1, column=0, **settings)
        self.response_txt.grid(row=2, column=0, **settings)
        self.convert_txt.grid(row=3, column=0, **settings)


class UnitFrom(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.config(bg=self.master.bgcolor)

        # Unit choices
        self.units = ['farenheit', 'celcius', 'kelvin']

        self.selected_unit = tk.StringVar()
        self.selected_unit.set(self.units[0])
        self.label = tk.Label(text="From", bg=self.master.bgcolor)

        self.radio_options = (tk.Radiobutton(self, text=unit,
                                             bg=self.master.bgcolor,
                                             value=unit,
                                             variable=self.selected_unit,
                                             command=self.change_color)
                              for unit in self.units)

        self.place_widgets()

    def place_widgets(self):
        self.label.pack(side=tk.LEFT)
        for ro in self.radio_options:
            ro.pack(side=tk.TOP, anchor='w', padx=(5, 10), pady=5)

    def change_color(self):
        unit = self.selected_unit.get()
        self.master.unit_from.set(unit)


class UnitTo(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.config(bg=self.master.bgcolor)

        # Unit choices
        self.units = ['farenheit', 'celcius', 'kelvin']

        self.selected_unit = tk.StringVar()
        self.selected_unit.set(self.units[1])
        self.label = tk.Label(text="To", bg=self.master.bgcolor)

        self.radio_options = (tk.Radiobutton(self, text=unit,
                                             bg=self.master.bgcolor,
                                             value=unit,
                                             variable=self.selected_unit,
                                             command=self.change_color)
                              for unit in self.units)

        self.place_widgets()

    def place_widgets(self):
        self.label.pack(side=tk.LEFT)
        for ro in self.radio_options:
            ro.pack(side=tk.TOP, anchor='w', padx=(5, 10), pady=5)

    def change_color(self):
        unit = self.selected_unit.get()
        self.master.unit_to.set(unit)


class GetValue(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg=self.master.bgcolor)

        self.value = tk.DoubleVar()
        self.value.set(0.00)

        def return_variables(var, index, mode):
            value = self.value.get()
            self.master.value.set(value)

        self.value.trace_add("write", callback=return_variables)
        self.response_name = tk.Entry(self, textvariable=self.value, justify="right", width=8)
        self.place_widgets()

    def place_widgets(self):
        self.response_name.pack()


if __name__ == '__main__':
    app = TemperatureConverter()
    app.mainloop()
