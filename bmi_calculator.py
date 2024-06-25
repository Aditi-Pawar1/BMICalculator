import tkinter as tk
from tkinter import messagebox           

try:            
    import matplotlib.pyplot as plt 
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
except ImportError as e:
    plt = None
    FigureCanvasTkAgg = None
    messagebox.showerror("Error", f"Matplotlib import error: {e}. Please install matplotlib.")

class BMI_Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.root.geometry("600x400")  # Set initial window size
        
        self.label_weight = tk.Label(root, text="Weight (kg):", font=("Arial", 16))
        self.label_weight.pack(pady=10)

        self.entry_weight = tk.Entry(root, font=("Arial", 14))
        self.entry_weight.pack()

        self.label_height = tk.Label(root, text="Height (m):", font=("Arial", 16))
        self.label_height.pack(pady=10)

        self.entry_height = tk.Entry(root, font=("Arial", 14))
        self.entry_height.pack()

        self.calculate_button = tk.Button(root, text="Calculate BMI", command=self.calculate_bmi, font=("Arial", 14))
        self.calculate_button.pack(pady=20)

        self.result_label = tk.Label(root, text="", font=("Arial", 18, "bold"))
        self.result_label.pack()

        # History
        self.history = []
        self.history_button = tk.Button(root, text="View History", command=self.view_history, font=("Arial", 14))
        self.history_button.pack(pady=10)

        # Trend Analysis
        self.trend_button = tk.Button(root, text="View Trend", command=self.view_trend, font=("Arial", 14))
        self.trend_button.pack(pady=10)

    def calculate_bmi(self):
        try:
            weight = float(self.entry_weight.get())
            height = float(self.entry_height.get())
            bmi = weight / (height ** 2)
            bmi_result = f"Your BMI is: {bmi:.2f}"
            self.result_label.config(text=bmi_result)
            self.history.append(bmi)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values.")

    def view_history(self):
        if self.history:
            messagebox.showinfo("BMI History", f"BMI History:\n{', '.join(map(str, self.history))}")
        else:
            messagebox.showinfo("BMI History", "No BMI history yet.")

    def view_trend(self):
        if plt and FigureCanvasTkAgg:
            if self.history:
                plt.figure(figsize=(10, 8)) 
                plt.plot(self.history, marker='o')
                plt.title('BMI Trend Analysis', fontsize=18)
                plt.xlabel('Measurement', fontsize=14)
                plt.ylabel('BMI', fontsize=14)
                plt.grid(True)
                plt.tight_layout()

                # Display plot in tkinter window
                fig_canvas = FigureCanvasTkAgg(plt.gcf(), master=self.root)
                fig_canvas.draw()
                fig_canvas.get_tk_widget().pack()

                # Button to close trend analysis
                close_button = tk.Button(self.root, text="Close Trend Analysis", command=lambda: plt.close(), font=("Arial", 14))
                close_button.pack(pady=10)
            else:
                messagebox.showinfo("BMI Trend", "No data to analyze.")
        else:
            messagebox.showerror("Error", "Matplotlib is not properly installed or configured.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BMI_Calculator(root)
    root.mainloop()
