import pandas as pd
import customtkinter as ctk
from tkinter import ttk, messagebox

def load_csv(file_path):
    try:
        data = pd.read_csv(file_path).head(100)
        return data
    except Exception as e:
        messagebox.showerror("Error", f"Error loading file: {e}")
        return None

def display_data(data, tree):
    tree.delete(*tree.get_children())


    tree["columns"] = list(data.columns)
    tree["show"] = "headings"

    for col in data.columns:
        tree.heading(col, text=col)
        tree.column(col, width=120, anchor="center")

    for index, row in data.iterrows():
        tree.insert("", "end", values=list(row))

def apply_darkmode_to_treeview(tree):
    style = ttk.Style()
    style.theme_use("clam")

    style.configure("Treeview",
                    background="#2E2E2E",
                    foreground="white",
                    fieldbackground="#2E2E2E",
                    rowheight=25)
    style.configure("Treeview.Heading",
                    background="#333333",
                    foreground="white",
                    font=("Arial", 10, "bold"))
    style.map("Treeview",
              background=[("selected", "#4CAF50")],
              foreground=[("selected", "white")])

def sort_data(data, tree, sort_column, ascending):
    try:
        sorted_data = data.sort_values(by=sort_column, ascending=ascending)
        display_data(sorted_data, tree)
    except Exception as e:
        messagebox.showerror("Error", f"Error sorting data: {e}")

def filter_data(data, tree):
    filter_window = ctk.CTkToplevel()
    filter_window.title("Filter Data")

    ctk.CTkLabel(filter_window, text="Select column to filter by:").pack(pady=5)
    filter_column = ctk.StringVar()
    filter_column.set(data.columns[0])

    column_menu = ctk.CTkOptionMenu(filter_window, variable=filter_column, values=list(data.columns))
    column_menu.pack(pady=5)

    ctk.CTkLabel(filter_window, text="Enter value to filter:").pack(pady=5)
    filter_value = ctk.CTkEntry(filter_window)
    filter_value.pack(pady=5)

    def apply_filter():
        value = filter_value.get()
        column = filter_column.get()
        try:
            filtered_data = data[data[column].astype(str).str.contains(value, case=False, na=False)]
            display_data(filtered_data, tree)
        except Exception as e:
            messagebox.showerror("Error", f"Error filtering data: {e}")

    ctk.CTkButton(filter_window, text="Apply Filter", command=apply_filter).pack(pady=10)

    filter_window.transient()
    filter_window.grab_set()
    filter_window.wait_window()

def main():
    #Przykładowy dataset
    file_path = './src/assets/social_media_entertainment_data.csv'
    data = load_csv(file_path)
    if data is None:
        return

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.title("CSViewer")
    root.geometry("900x600")
    root.iconbitmap("./src/assets/icon.ico")

    frame = ctk.CTkFrame(root)
    frame.pack(pady=10, padx=10, fill="both", expand=True)

    tree = ttk.Treeview(frame)

    x_scrollbar = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
    x_scrollbar.pack(side="bottom", fill="x")

    y_scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    y_scrollbar.pack(side="right", fill="y")

    tree.configure(xscroll=x_scrollbar.set, yscroll=y_scrollbar.set)
    tree.pack(side="left", fill="both", expand=True)

    apply_darkmode_to_treeview(tree)

    display_data(data, tree)

    def sort_file():
        sort_window = ctk.CTkToplevel(root)
        sort_window.title("Sort Options")

        ctk.CTkLabel(sort_window, text="Select column to sort by:").pack(pady=5)
        sort_column = ctk.StringVar()
        sort_column.set(data.columns[0])

        column_menu = ctk.CTkOptionMenu(sort_window, variable=sort_column, values=list(data.columns))
        column_menu.pack(pady=5)

        ascending = ctk.BooleanVar(value=True)
        ctk.CTkCheckBox(sort_window, text="Sort in ascending order", variable=ascending).pack(pady=5)

        def apply_sort():
            sort_data(data, tree, sort_column.get(), ascending.get())

        ctk.CTkButton(sort_window, text="Sort", command=apply_sort).pack(pady=10)

        sort_window.transient()
        sort_window.grab_set()
        sort_window.wait_window()

    button_frame = ctk.CTkFrame(root)
    button_frame.pack(pady=10)

    sort_button = ctk.CTkButton(button_frame, text="Sort Data", command=sort_file)
    sort_button.grid(row=0, column=0, padx=5)

    filter_button = ctk.CTkButton(button_frame, text="Filter Data", command=lambda: filter_data(data, tree))
    filter_button.grid(row=0, column=1, padx=5)

    exit_button = ctk.CTkButton(button_frame, text="Exit", command=root.quit, fg_color="red")
    exit_button.grid(row=0, column=2, padx=5)

    root.mainloop()

if __name__ == "__main__":
    main()
