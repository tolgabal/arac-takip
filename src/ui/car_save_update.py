import customtkinter as ctk
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..', 'controllers')))
from controllers.arac_controller import AracRepository
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..', 'models')))
from models.entity.arac import Arac


class CarSaveUpdate:
    
    def __init__(self,root, arac : Arac = None):
        self.root = root
        self.root.geometry("700x400")
        self.root.title("Araç Ekleme/Güncelleme")
        self.a = arac
        
        # 🎨 Yeni renkler
        self.bg_color = "#35374B"
        self.sidebar_color = "#344955"
        self.button_color = "#50727B"
        self.hover_color = "#78A083"
        self.text_color = "#FFFFFF"
        
        self.root.configure(bg = self.bg_color)
        
        self.main_frame = ctk.CTkFrame(self.root, fg_color = self.bg_color)
        self.main_frame.pack(fill = "both", expand = True)
        