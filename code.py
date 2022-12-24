import tkinter as tk
import tkinter.messagebox as messagebox

def upgrade_pc():
    messagebox.showinfo("Upgrade PC", "It looks like your PC is outdated and in need of an upgrade. Please consider upgrading to a newer model to improve performance and security.")

root = tk.Tk()
root.withdraw()
upgrade_pc()
