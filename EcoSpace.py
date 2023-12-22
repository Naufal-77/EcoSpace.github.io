import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.configure(bg='white')
window.geometry('800x300')
window.resizable(0,0)
window.title('EcoSpace Planner')

# Declare global variables
frame_kalkulasi = None
tab_kalkulasi = None
tombol_kembali = None
frame_parameter = None
tab_parameter = None

def load_image(path, max_width, max_height):
    img = Image.open(path)

    # Resize the image if it's too big
    img.thumbnail((max_width, max_height), resample=Image.ANTIALIAS)

    img = ImageTk.PhotoImage(img)
    return img

# Provide the absolute path to your JPG image
img_path = 'C:/Users/HP/Downloads/isometric-futuristic-skyscrapers-infographics-with-shopping-business-centers-skyscraper-other-elemen/RTH_ui.jpg'

# Set maximum width and height for resizing
max_width = 375
max_height = 300

img = load_image(img_path, max_width, max_height)

img_label = tk.Label(window, image=img, bg='white')
img_label.image = img
img_label.grid(row=0, column=3, rowspan=6, padx=10, pady=5, sticky='nswe')

# Function to calculate the green area
def hitung_luas_lahan_hijau(total_luas, persentase_lahan_hijau):
    lahan_hijau = (persentase_lahan_hijau / 100) * total_luas
    return lahan_hijau

def tab_hijau():
    global frame_kalkulasi, tab_kalkulasi, tombol_kembali

    # Check if objects exist before destroying
    if frame_parameter:
        frame_parameter.destroy()
    if tab_parameter:
        tab_parameter.destroy()

    frame_kalkulasi = tk.Frame(window, bg='lightgreen')
    frame_kalkulasi.grid(row=0, column=3, rowspan=6,columnspan=2, sticky='nswe')

    # grid configure
    frame_kalkulasi.columnconfigure((0,1,2),weight=1)
    frame_kalkulasi.rowconfigure((0,1,2,3,4,5),weight=1)
    frame_kalkulasi.rowconfigure(4,weight=5)

    tab_kalkulasi = tk.Label(frame_kalkulasi, text='\tKalkulator Lahan Hijau', bg='lightgreen', font=('helvetica', 16, 'bold'))
    tab_kalkulasi.grid(row=0, column=0,columnspan=2, pady=10, sticky='n')

    tombol_kembali = tk.Button(frame_kalkulasi, text='back', font=('helvetica', 12), fg='white', bg='blue', command=kembali)
    tombol_kembali.grid(row=5, column=2, padx=5, pady=5, sticky='se')

    # Label dan widget
    panjang_kalkulasi_label = tk.Label(frame_kalkulasi, text='Panjang Lahan (m):',bg='lightgreen')
    panjang_kalkulasi_label.grid(row=1,column=0, padx=10, pady=5, sticky='w')

    panjang_kalkulasi_entry = tk.Entry(frame_kalkulasi)
    panjang_kalkulasi_entry.grid(row=1,column=1,padx=10, pady=5, sticky='w')

    lebar_kalkulasi_label = tk.Label(frame_kalkulasi, text='Lebar Lahan (m):',bg='lightgreen')
    lebar_kalkulasi_label.grid(row=2,column=0,padx=10, pady=5, sticky='w')

    lebar_kalkulasi_entry = tk.Entry(frame_kalkulasi)
    lebar_kalkulasi_entry.grid(row=2,column=1,padx=10, pady=5, sticky='w')

    persentase_kalkulasi_label = tk.Label(frame_kalkulasi, text='Persentase Lahan Hijau (%):',bg='lightgreen')
    persentase_kalkulasi_label.grid(row=3,column=0,padx=10, pady=5, sticky='w')

    persentase_kalkulasi_entry = tk.Entry(frame_kalkulasi)
    persentase_kalkulasi_entry.grid(row=3,column=1,padx=10, pady=5, sticky='w')

    hasil_label = tk.Label(frame_kalkulasi, text='Hasil akan ditampilkan disini',font=('Helvetica',12),fg='black',bg='lightgreen')
    hasil_label.grid(row=5,column=0,columnspan=2, pady=20, sticky='nswe')

    # Function to perform the calculation
    def hitung_luas_dan_lahan_hijau():
        panjang_lahan = float(panjang_kalkulasi_entry.get())
        lebar_lahan = float(lebar_kalkulasi_entry.get())

        total_luas = panjang_lahan * lebar_lahan

        persentase_lahan_hijau = float(persentase_kalkulasi_entry.get())

        lahan_hijau_hasil = hitung_luas_lahan_hijau(total_luas, persentase_lahan_hijau)

        hasil_label.config(text=f"Luas lahan anda: {total_luas:.2f} m^2 \n Lahan hijau minimal yang diperlukan: {lahan_hijau_hasil:.2f} m^2")

    # Button to trigger the calculation
    tombol_hitung = tk.Button(frame_kalkulasi, text="Hitung", bg='#4CAF50', fg='white', font=('Helvetica', 12), command=hitung_luas_dan_lahan_hijau)
    tombol_hitung.grid(row=4, column=0,columnspan=2, padx=10, pady=5, sticky='n')

def tab_biru():
    global frame_parameter, tab_parameter, tombol_kembali

    # Check if objects exist before destroying
    if frame_kalkulasi:
        frame_kalkulasi.destroy()
    if tab_kalkulasi:
        tab_kalkulasi.destroy()

    frame_parameter = tk.Frame(window, bg='lightblue')
    frame_parameter.grid(row=0, column=3, rowspan=6, columnspan=2, sticky='nswe')

    # grid configure
    frame_parameter.columnconfigure((0, 1, 2), weight=1)
    frame_parameter.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
    frame_parameter.rowconfigure(4, weight=5)

    tab_parameter = tk.Label(frame_parameter, text='\tParameter Lahan Hijau', bg='lightblue', font=('helvetica', 16, 'bold'))
    tab_parameter.grid(row=0, column=0, columnspan=2, pady=10, sticky='n')

    label_luas_lahan = tk.Label(frame_parameter, text='Luas Lahan (m^2): ', bg='lightblue', font=('helvetica', 12))
    label_luas_lahan.grid(row=2, column=0, padx=10, pady=5, sticky='w')

    luas_lahan_entry = tk.Entry(frame_parameter)
    luas_lahan_entry.grid(row=2, column=1, padx=10, pady=5, sticky='w')

    luas_hijau_label = tk.Label(frame_parameter, text='Luas Lahan Hijau (m^2):', bg='lightblue', font=('helvetica', 12))
    luas_hijau_label.grid(row=3, column=0, padx=10, pady=5, sticky='w')

    luas_hijau_entry = tk.Entry(frame_parameter)
    luas_hijau_entry.grid(row=3, column=1, padx=10, pady=5, sticky='w')

    hasil_label = tk.Label(frame_parameter, text='', font=('Helvetica', 12), fg='black', bg='lightblue')
    hasil_label.grid(row=5, column=0, columnspan=2, pady=20, sticky='nswe')

    # Function to perform the calculation
    def hitung_parameter_lahan_hijau():
        luas_lahan = float(luas_lahan_entry.get())
        luas_lahan_hijau = float(luas_hijau_entry.get())

        persentase_lahan_hijau = (luas_lahan_hijau / luas_lahan) * 100

        if persentase_lahan_hijau > 30:
            hasil = 'Sangat Baik'
        elif persentase_lahan_hijau > 20:
            hasil = 'Cukup'
        elif persentase_lahan_hijau > 10:
            hasil = 'Kurang'
        else:
            hasil = 'Sangat Kurang'

        hasil_label.config(text=f"Persentase Lahan Hijau: {persentase_lahan_hijau:.2f}%\nPenilaian: {hasil}")

    # Button to trigger the calculation
    tombol_hitung = tk.Button(frame_parameter, text="Hitung", bg='#4CAF50', fg='white', font=('Helvetica', 12),
                              command=hitung_parameter_lahan_hijau)
    tombol_hitung.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky='n')

    tombol_kembali = tk.Button(frame_parameter, text='back', font=('helvetica', 12), fg='white', bg='blue',
                               command=kembali)
    tombol_kembali.grid(row=5, column=2, padx=5, pady=5, sticky='se')

def kembali():
    global frame_kalkulasi, frame_parameter, tombol_kembali

    # Check if objects exist before destroying
    if frame_kalkulasi:
        frame_kalkulasi.destroy()
    if frame_parameter:
        frame_parameter.destroy()
    if tombol_kembali:
        tombol_kembali.destroy()
    main_tab()


def main_tab():
    label_judul = tk.Label(window, bg='white', text='SELAMAT DATANG\n DI ECOSPACE PLANNER:\nKALKULASI DAN EVALUASI RTH', font=('Garamond', 16, 'bold'))
    label_judul.grid(row=0, column=0, columnspan=3, pady=20, sticky='nswe')
    window.columnconfigure((0, 1, 2), weight=1)
    window.columnconfigure(3,weight=10)
    window.rowconfigure((0, 1, 2), weight=1)

    tombol_kalkulasi = tk.Button(window, text="Kalkulasi", bg='#4CAF50', fg='white', font=('Helvetica', 12), command=tab_hijau)
    tombol_parameter = tk.Button(window, text="Parameter", bg='#4CAF50', fg='white', font=('Helvetica', 12), command=tab_biru)

    tombol_kalkulasi.grid(row=1, column=0, padx=10, pady=5, sticky='ne')
    tombol_parameter.grid(row=1, column=2, padx=10, pady=5, sticky='nw')

    tagline = tk.Label(window,text='Transformasi Kota Anda Menuju Ruang Hijau yang Berkelanjutan',font=('helvetica',8),bg='white')
    tagline.grid(row=2,column=0,columnspan=3,sticky='nswe')
main_tab()
window.mainloop()