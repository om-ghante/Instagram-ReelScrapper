import tkinter as tk
from tkinter import messagebox
import yt_dlp

def download_reel():
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Please enter a URL")
        return
    
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'reel_%(id)s.%(ext)s',
            'quiet': True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            messagebox.showinfo("Success", f"✅ Downloaded: {info['title']}.{info['ext']}")
    except Exception as e:
        messagebox.showerror("Error", f"❌ Failed: {str(e)}")

# Create main window
root = tk.Tk()
root.title("Instagram Reel Downloader")

# Set window size and center it
window_width = 400
window_height = 150
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# URL Entry
tk.Label(root, text="Enter Instagram Reel URL:").pack(pady=(10, 0))
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5, padx=10)

# Download Button
download_btn = tk.Button(root, text="Download", command=download_reel)
download_btn.pack(pady=10)

# Run the application
root.mainloop()