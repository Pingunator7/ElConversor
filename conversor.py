import tkinter as tk
from tkinter import ttk, messagebox

class CurrencyConverter:
    def __init__(self, master):
        self.master = master
        master.title("Conversor de Monedas")
        master.geometry("800x600")  
        master.resizable(False, False)
        master.configure(bg='#e0f7fa')

 
        self.conversion_rates = {
            "USD": {
                "EUR": 0.92,
                "GBP": 0.79,
                "NIO": 36.60,  
                "CNY": 7.25,   
                "MXN": 18.00,  
                "USD": 1.0
            },
            "EUR": {
                "USD": 1.09,
                "GBP": 0.86,
                "NIO": 40.00,  
                "CNY": 7.90,   
                "MXN": 19.60,  
                "EUR": 1.0
            },
            "GBP": {
                "USD": 1.27,
                "EUR": 1.16,
                "NIO": 46.50,  
                "CNY": 9.20,   
                "MXN": 22.80,  
                "GBP": 1.0
            },
            "NIO": {
                "USD": 1/36.60,
                "EUR": 1/40.00,
                "GBP": 1/46.50,
                "CNY": (1/36.60) * 7.25,  
                "MXN": (1/36.60) * 18.00,  
                "NIO": 1.0
            },
            "CNY": {
                "USD": 1/7.25,
                "EUR": 1/7.90,
                "GBP": 1/9.20,
                "NIO": (1/7.25) * 36.60,  
                "MXN": (1/7.25) * 18.00,  
                "CNY": 1.0
            },
            "MXN": {
                "USD": 1/18.00,
                "EUR": 1/19.60,
                "GBP": 1/22.80,
                "NIO": (1/18.00) * 36.60,  
                "CNY": (1/18.00) * 7.25,  
                "MXN": 1.0
            }
        }

        self.create_widgets()

    def create_widgets(self):
        
        main_frame = ttk.Frame(self.master, padding="20 20 20 20", style='TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True)

         
        style = ttk.Style()
        style.configure('TFrame', background='#e0f7fa')
        style.configure('TLabel', background='#e0f7fa', font=('Arial', 10))
        style.configure('TButton', font=('Arial', 10, 'bold'), background='#00796b', foreground='white')
        style.map('TButton', background=[('active', '#004d40')])
        style.configure('TCombobox', font=('Arial', 10))
        style.configure('TEntry', font=('Arial', 10))

        
        amount_label = ttk.Label(main_frame, text="Monto a convertir:", style='TLabel')
        amount_label.grid(row=0, column=0, pady=10, sticky=tk.W)

        self.amount_entry = ttk.Entry(main_frame, width=30)
        self.amount_entry.grid(row=0, column=1, pady=10, padx=5, sticky=tk.EW)

         
        all_currencies = ["USD", "EUR", "GBP", "NIO", "CNY", "MXN"]

        
        from_currency_label = ttk.Label(main_frame, text="De:", style='TLabel')
        from_currency_label.grid(row=1, column=0, pady=10, sticky=tk.W)

        self.from_currency_combo = ttk.Combobox(main_frame,
                                                values=all_currencies,
                                                state="readonly", width=27)
        self.from_currency_combo.set("USD")
        self.from_currency_combo.grid(row=1, column=1, pady=10, padx=5, sticky=tk.EW)

         
        to_currency_label = ttk.Label(main_frame, text="A:", style='TLabel')
        to_currency_label.grid(row=2, column=0, pady=10, sticky=tk.W)

        self.to_currency_combo = ttk.Combobox(main_frame,
                                              values=all_currencies,
                                              state="readonly", width=27)
        self.to_currency_combo.set("EUR")
        self.to_currency_combo.grid(row=2, column=1, pady=10, padx=5, sticky=tk.EW)

        
        convert_button = ttk.Button(main_frame, text="Convertir", command=self.convert_currency, style='TButton')
        convert_button.grid(row=3, column=0, columnspan=2, pady=20)

         
        self.result_label = ttk.Label(main_frame, text="Resultado: ", style='TLabel', font=('Arial', 12, 'bold'))
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

         
        main_frame.grid_columnconfigure(1, weight=1)

    def convert_currency(self):
        try:
            amount = float(self.amount_entry.get())
            from_currency = self.from_currency_combo.get()
            to_currency = self.to_currency_combo.get()

            if from_currency not in self.conversion_rates or to_currency not in self.conversion_rates[from_currency]:
                messagebox.showerror("Error de conversión", "Moneda no soportada o tasa de conversión no definida.")
                return

            converted_amount = amount * self.conversion_rates[from_currency][to_currency]

            self.result_label.config(text=f"Resultado: {converted_amount:.2f} {to_currency}")

        except ValueError:
            messagebox.showerror("Error de entrada", "Por favor, ingresa un monto numérico válido.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()


