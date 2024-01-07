import tkinter as tk
import random

def suit_tangan(pilihan_pengguna):
    pilihan_computer = random.choice(["Gunting", "Batu", "Kertas"])
    label_hasil.config(text=f"Pilihan Komputer: {pilihan_computer}")

    if pilihan_pengguna == pilihan_computer:
        hasil = "Seru, Seri!"
    elif (
        (pilihan_pengguna == "Batu" and pilihan_computer == "Gunting") or
        (pilihan_pengguna == "Gunting" and pilihan_computer == "Kertas") or
        (pilihan_pengguna == "Kertas" and pilihan_computer == "Batu")
    ):
        hasil = "Anda Menang !"
    else:
        hasil = "Anda Kalah :("

    label_hasil.config(text=f"Hasil: {hasil}")

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Suit Tangan")

# Membuat label dan tombol
label_instruksi = tk.Label(root, text="Pilih satu: Gunting, Batu, atau Kertas")
label_instruksi.pack(pady=10)

tombol_batu = tk.Button(root, text="Gunting", command=lambda: suit_tangan("Gunting"))
tombol_batu.pack(side=tk.LEFT, padx=10)

tombol_gunting = tk.Button(root, text="Batu", command=lambda: suit_tangan("Batu"))
tombol_gunting.pack(side=tk.LEFT, padx=10)

tombol_kertas = tk.Button(root, text="Kertas", command=lambda: suit_tangan("Kertas"))
tombol_kertas.pack(side=tk.LEFT, padx=10)

label_hasil = tk.Label(root, text="Hasil: ")
label_hasil.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()
 