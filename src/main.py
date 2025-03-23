import sys
import os

# Bir üst klasöre çık, sonra 'ui' klasörüne git
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'ui')))

from main_window import MainWindow  # Doğru modül adı ile içe aktar

import customtkinter as ctk

def main():
    # Uygulama penceresini oluştur
    ctk.set_appearance_mode("dark")  # Karanlık mod (Opsiyonel)
    ctk.set_default_color_theme("blue")  # Varsayılan tema

    # Ana pencereyi oluştur
    root = ctk.CTk()

    # MainWindow sınıfını çağır
    window = MainWindow(root)

    # Uygulamayı çalıştır
    root.mainloop()

if __name__ == "__main__":
    main()