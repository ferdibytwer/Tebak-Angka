import tkinter as tk
from tkinter import messagebox
import random
import pygame
import os
import sys

def resource_path(relative_path):
    # Mengatasi path saat dibundel ke .exe
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class TebakAngkaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Game Tebak Angka")
        self.root.geometry("500x500")

        self.bg_image = tk.PhotoImage(file=resource_path("resource/bg.png"))  # Gambar latar
        
        # Memuat gambar untuk tombol musik
        self.mulai_icon = tk.PhotoImage(file=resource_path("resource/ikon-s-mulai.png")).subsample(13,13)  # Gambar untuk tombol "Mulai"
        self.berhenti_icon = tk.PhotoImage(file=resource_path("resource/ikon-s-berhenti.png")).subsample(13,13)  # Gambar untuk tombol "Berhenti"

        pygame.mixer.init()
        pygame.mixer.music.load(resource_path("resource/backsound.mp3"))  # Musik yang dimuat
        pygame.mixer.music.play(-1, 0.0)  # -1 berarti musik diputar terus-menerus
        self.music_on = True  # Menandakan musik sedang aktif

        # Memuat suara klik tombol
        self.button_click_sound = pygame.mixer.Sound(resource_path("resource/button-click.mp3"))

        self.angka = None
        self.batas = None
        self.tries = 0
        self.max_tries = 5
        self.histori = []

        self.layer1()

    def play_button_click_sound(self):
        self.button_click_sound.play()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def buat_background(self, frame):
        bg_label = tk.Label(frame, image=self.bg_image)
        bg_label.place(relwidth=1, relheight=1)
    
    def toggle_musik(self):
        self.play_button_click_sound()  # Tambahkan suara klik
        if self.music_on:
            pygame.mixer.music.stop()  # Hentikan musik
            self.btn_music.config(image=self.berhenti_icon)  # Ganti ikon tombol jadi "🔇"
            self.music_on = False  # Status musik jadi off
        else:
            pygame.mixer.music.play(-1, 0.0)  # Putar musik kembali
            self.btn_music.config(image=self.mulai_icon)  # Ganti ikon tombol jadi "🎵"
            self.music_on = True  # Status musik jadi on

    def layer1(self):
        self.clear_window()
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill="both")
        self.buat_background(frame)

        # Tombol toggle musik
        self.btn_music = tk.Button(frame, image=self.mulai_icon, command=self.toggle_musik, bd=0)
        self.btn_music.place(relx=0.97, rely=0.03, anchor="ne")

        content = tk.Frame(frame, bg="#ffffff", bd=1, relief="ridge")
        content.place(relx=0.5, rely=0.5, anchor="center")

        inner = tk.Frame(content, bg="#ffffff")
        inner.pack(padx=30, pady=30)

        tk.Label(inner, text="🎯 Game Tebak Angka", font=("Helvetica", 28, "bold"),
                bg="#ffffff", fg="#003366").pack(pady=(0, 30))

        tk.Button(inner, text="Mulai Game", font=("Helvetica", 14),
                bg="#4CAF50", fg="white", width=20, command=lambda: [self.play_button_click_sound(), self.layer2()]).pack(pady=10)

        tk.Button(inner, text="Keluar", font=("Helvetica", 14),
                bg="#f44336", fg="white", width=20, command=lambda: [self.play_button_click_sound(), self.root.destroy()]).pack(pady=10)

    def layer2(self):
        self.clear_window()
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill="both")
        self.buat_background(frame)

        # Tombol toggle musik
        self.btn_music = tk.Button(frame, image=self.mulai_icon, command=self.toggle_musik, bd=0)
        self.btn_music.place(relx=0.97, rely=0.03, anchor="ne")

        content = tk.Frame(frame, bg="#ffffff", bd=2, relief="ridge")
        content.place(relx=0.5, rely=0.5, anchor="center")

        inner = tk.Frame(content, bg="#ffffff")
        inner.pack(padx=30, pady=30)

        tk.Label(inner, text="Pilih Tingkat Kesulitan", font=("Helvetica", 18, "bold"),
                bg="#ffffff", fg="#800040").pack(pady=(0, 20))

        tk.Button(inner, text="Mudah (1-100)", bg="#98fb98", width=20, font=("Helvetica", 12),
                command=lambda: [self.play_button_click_sound(), self.mulai_game(100)]).pack(pady=8)

        tk.Button(inner, text="Sedang (1-500)", bg="#87ceeb", width=20, font=("Helvetica", 12),
                command=lambda: [self.play_button_click_sound(), self.mulai_game(500)]).pack(pady=8)

        tk.Button(inner, text="Sulit (1-1000)", bg="#dda0dd", width=20, font=("Helvetica", 12),
                command=lambda: [self.play_button_click_sound(), self.mulai_game(1000)]).pack(pady=8)

    def mulai_game(self, batas):
        self.angka = random.randint(1, batas)
        self.batas = batas
        self.tries = 0
        self.histori = []
        self.layer3()

    def layer3(self):
        self.clear_window()
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill="both")
        self.buat_background(frame)

        # Tombol toggle musik
        self.btn_music = tk.Button(frame, image=self.mulai_icon, command=self.toggle_musik, bd=0)
        self.btn_music.place(relx=0.97, rely=0.03, anchor="ne")

        content = tk.Frame(frame, bg="#ffffff", bd=2, relief="ridge")
        content.place(relx=0.5, rely=0.5, anchor="center")

        inner = tk.Frame(content, bg="#ffffff")
        inner.pack(padx=30, pady=30)

        tk.Label(inner, text=f"Tebak angka antara 1 dan {self.batas}",
                font=("Helvetica", 16), bg="#ffffff").pack(pady=(0, 15))

        self.input_tebakan = tk.Entry(inner, font=("Helvetica", 14), justify="center")
        self.input_tebakan.pack(pady=5)
        self.input_tebakan.bind("<Return>", lambda event: [self.play_button_click_sound(), self.cek_tebakan()])

        tk.Button(inner, text="Tebak", bg="#2196f3", fg="white", font=("Helvetica", 12),
                command=lambda: [self.play_button_click_sound(), self.cek_tebakan()]).pack(pady=10)

        self.label_info = tk.Label(inner, text="", font=("Helvetica", 12), bg="#ffffff", fg="#333")
        self.label_info.pack(pady=5)

        self.label_histori = tk.Label(inner, text="Histori Tebakan:\n-", font=("Helvetica", 12),
                                    justify="left", bg="#ffffff")
        self.label_histori.pack(pady=10)

        self.btn_main_lagi = tk.Button(inner, text="Main Lagi", font=("Helvetica", 12),
                                    bg="#4caf50", fg="white", command=lambda: [self.play_button_click_sound(), self.layer2()])
        self.btn_keluar = tk.Button(inner, text="Keluar", font=("Helvetica", 12),
                                    bg="#f44336", fg="white", command=lambda: [self.play_button_click_sound(), self.root.destroy()])

        self.btn_main_lagi.pack_forget()
        self.btn_keluar.pack_forget()

    def cek_tebakan(self):
        try:
            tebakan = int(self.input_tebakan.get())
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid!")
            return

        self.tries += 1
        self.histori.append(tebakan)
        self.input_tebakan.delete(0, tk.END)

        if tebakan == self.angka:
            self.label_info.config(text="🎉 Tebakan Anda BENAR!")
            self.selesai()
        elif self.tries >= self.max_tries:
            self.label_info.config(text=f"😢 Anda kalah! Angka yang benar adalah : {self.angka}")
            self.selesai()
        elif tebakan < self.angka:
            self.label_info.config(text="Tebakan terlalu rendah.")
        else:
            self.label_info.config(text="Tebakan terlalu tinggi.")

        self.label_histori.config(text="Histori Tebakan:\n" + ', '.join(map(str, self.histori)))

    def selesai(self):
        self.btn_main_lagi.pack(pady=5)
        self.btn_keluar.pack(pady=5)

# Jalankan Aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    app = TebakAngkaApp(root)
    root.mainloop()
