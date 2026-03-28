import tkinter as tk
from tkinter import messagebox, scrolledtext
import requests
from bs4 import BeautifulSoup


# -------- Scraping Function --------
def scrape_headings():
    url = url_entry.get()

    if not url:
        messagebox.showwarning("Input Error", "Please enter a website URL")
        return

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        headings = soup.find_all(['h1', 'h2', 'h3'])

        output_area.delete(1.0, tk.END)

        if headings:
            output_area.insert(tk.END, "--- Extracted Headings ---\n\n")
            for i, heading in enumerate(headings, 1):
                output_area.insert(
                    tk.END, f"{i}. {heading.text.strip()}\n"
                )
        else:
            output_area.insert(tk.END, "No headings found.")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch website:\n{e}")


# -------- GUI Window --------
root = tk.Tk()
root.title("Web Scraper GUI")
root.geometry("600x450")

# Title Label
title_label = tk.Label(root, text="Website Heading Scraper",
                       font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# URL Entry
tk.Label(root, text="Enter Website URL:").pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Scrape Button
scrape_btn = tk.Button(root, text="Scrape Headings",
                       command=scrape_headings,
                       bg="lightblue")
scrape_btn.pack(pady=10)

# Output Area
output_area = scrolledtext.ScrolledText(root, width=70, height=18)
output_area.pack(padx=10, pady=10)

# Run App
root.mainloop()