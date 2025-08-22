# ui_manager.py
import tkinter as tk
from tkinter import ttk, font, messagebox
from typing import Callable, Optional, List, Dict
import random
from config import GameConfig

class UIManager:
    """Kullanıcı arayüzü yönetimi için ana class"""
    
    def __init__(self):
        self.root = None
        self.current_frame = None
        self.callback_functions = {}
        self._setup_styles()
    
    def _setup_styles(self):
        """UI stillerini ayarlar"""
        self.fonts = {
            'title': ('Arial', 24, 'bold'),
            'heading': ('Arial', 18, 'bold'),
            'normal': ('Arial', 12),
            'button': ('Arial', 14, 'bold'),
            'small': ('Arial', 10)
        }
        
        self.colors = GameConfig.COLORS.copy()
        self.colors.update({
            'TEXT': '#FFFFFF',
            'BUTTON_TEXT': '#FFFFFF',
            'CARD_BG': '#FFFFFF',
            'CARD_TEXT': '#333333'
        })
    
    def create_main_window(self) -> tk.Tk:
        """Ana pencereyi oluşturur"""
        self.root = tk.Tk()
        self.root.title(GameConfig.GAME_TITLE)
        self.root.geometry(f"{GameConfig.WINDOW_WIDTH}x{GameConfig.WINDOW_HEIGHT}")
        self.root.configure(bg=self.colors['BACKGROUND'])
        
        # Pencereyi tam ekran yap ve merkeze al
        self.root.state('zoomed')  # Windows için tam ekran
        
        # ESC ile çıkış
        self.root.bind('<Escape>', lambda e: self.root.quit())
        
        return self.root
    
    def clear_frame(self):
        """Mevcut frame'i temizler"""
        if self.current_frame:
            self.current_frame.destroy()
    
    def create_gradient_frame(self, parent: tk.Widget) -> tk.Frame:
        """Gradient arka planlı frame oluşturur"""
        frame = tk.Frame(parent, bg=self.colors['BACKGROUND'])
        frame.pack(fill='both', expand=True)
        return frame
    
    def create_card(self, parent: tk.Widget, width: int = 400, height: int = 300) -> tk.Frame:
        """Modern card stili frame oluşturur"""
        card = tk.Frame(
            parent,
            bg=self.colors['CARD_BG'],
            relief='raised',
            bd=2,
            padx=20,
            pady=20
        )
        card.configure(width=width, height=height)
        return card
    
    def create_styled_button(self, parent: tk.Widget, text: str, command: Callable, 
                           color: str = 'PRIMARY', width: int = 20) -> tk.Button:
        """Stilize edilmiş buton oluşturur"""
        button = tk.Button(
            parent,
            text=text,
            command=command,
            bg=self.colors[color],
            fg=self.colors['BUTTON_TEXT'],
            font=self.fonts['button'],
            relief='flat',
            padx=20,
            pady=10,
            width=width,
            cursor='hand2'
        )
        
        # Hover efekti
        button.bind('<Enter>', lambda e: button.configure(bg=self._darken_color(self.colors[color])))
        button.bind('<Leave>', lambda e: button.configure(bg=self.colors[color]))
        
        return button
    
    def _darken_color(self, color: str) -> str:
        """Rengi koyulaştırır (hover efekti için)"""
        # Basit renk koyulaştırma
        color_map = {
            self.colors['PRIMARY']: '#1E5F7A',
            self.colors['SUCCESS']: '#D1362F',
            self.colors['WARNING']: '#E69A26',
            self.colors['INFO']: '#D1560F'
        }
        return color_map.get(color, color)
    
    def show_welcome_screen(self, start_callback: Callable):
        """Hoş geldin ekranını gösterir"""
        self.clear_frame()
        self.current_frame = self.create_gradient_frame(self.root)
        
        # Ana container
        main_container = tk.Frame(self.current_frame, bg=self.colors['BACKGROUND'])
        main_container.pack(expand=True, fill='both')
        
        # Başlık
        title_label = tk.Label(
            main_container,
            text="🚀 CodeCraft Academy",
            font=self.fonts['title'],
            bg=self.colors['BACKGROUND'],
            fg=self.colors['TEXT']
        )
        title_label.pack(pady=(100, 20))
        
        # Alt başlık
        subtitle_label = tk.Label(
            main_container,
            text="Kodlama Dünyasına Hoş Geldin!",
            font=self.fonts['heading'],
            bg=self.colors['BACKGROUND'],
            fg=self.colors['TEXT']
        )
        subtitle_label.pack(pady=(0, 50))
        
        # İsim girişi card'ı
        input_card = self.create_card(main_container, width=500, height=200)
        input_card.pack(pady=20)
        
        # İsim label
        name_label = tk.Label(
            input_card,
            text="Adını gir:",
            font=self.fonts['normal'],
            bg=self.colors['CARD_BG'],
            fg=self.colors['CARD_TEXT']
        )
        name_label.pack(pady=(20, 10))
        
        # İsim entry
        self.name_entry = tk.Entry(
            input_card,
            font=self.fonts['normal'],
            width=30,
            justify='center'
        )
        self.name_entry.pack(pady=10)
        self.name_entry.focus()
        
        # Başla butonu
        start_button = self.create_styled_button(
            input_card,
            "🎮 Maceraya Başla!",
            lambda: self._handle_start(start_callback),
            'SUCCESS',
            width=25
        )
        start_button.pack(pady=20)
        
        # Enter tuşu ile başlama
        self.name_entry.bind('<Return>', lambda e: self._handle_start(start_callback))
    
    def _handle_start(self, start_callback: Callable):
        """Başla butonuna basıldığında çalışır"""
        player_name = self.name_entry.get().strip()
        if not player_name:
            messagebox.showwarning("Uyarı", "Lütfen adınızı girin!")
            return
        
        start_callback(player_name)
    
    def show_station_screen(self, station_name: str, station_index: int, total_stations: int, 
                           start_station_callback: Callable):
        """İstasyon tanıtım ekranını gösterir"""
        self.clear_frame()
        self.current_frame = self.create_gradient_frame(self.root)
        
        # Ana container
        main_container = tk.Frame(self.current_frame, bg=self.colors['BACKGROUND'])
        main_container.pack(expand=True, fill='both')
        
        # İlerleme göstergesi
        progress_text = f"İstasyon {station_index + 1}/{total_stations}"
        progress_label = tk.Label(
            main_container,
            text=progress_text,
            font=self.fonts['small'],
            bg=self.colors['BACKGROUND'],
            fg=self.colors['TEXT']
        )
        progress_label.pack(pady=(50, 10))
        
        # İstasyon başlığı
        station_title = tk.Label(
            main_container,
            text=f"🎯 {station_name}",
            font=self.fonts['title'],
            bg=self.colors['BACKGROUND'],
            fg=self.colors['TEXT']
        )
        station_title.pack(pady=20)
        
        # İstasyon açıklaması card'ı
        info_card = self.create_card(main_container, width=600, height=300)
        info_card.pack(pady=30)
        
        # İstasyon bilgisi
        station_info = self._get_station_info(station_name)
        info_label = tk.Label(
            info_card,
            text=station_info,
            font=self.fonts['normal'],
            bg=self.colors['CARD_BG'],
            fg=self.colors['CARD_TEXT'],
            wraplength=550,
            justify='center'
        )
        info_label.pack(pady=20)
        
        # Hazır mısın sorusu
        ready_label = tk.Label(
            info_card,
            text="3 soru seni bekliyor. Hazır mısın?",
            font=self.fonts['heading'],
            bg=self.colors['CARD_BG'],
            fg=self.colors['CARD_TEXT']
        )
        ready_label.pack(pady=20)
        
        # Başla butonu
        start_button = self.create_styled_button(
            info_card,
            "▶️ İstasyonu Başlat",
            start_station_callback,
            'INFO',
            width=25
        )
        start_button.pack(pady=20)
    
    def _get_station_info(self, station_name: str) -> str:
        """İstasyon bilgilerini döndürür"""
        station_info = {
            "Algorithm Explorer": "Algoritma dünyasına yolculuk! Problem çözme adımlarını öğrenecek ve mantık kurma becerilerini geliştireceksin.",
            "Bug Hunter": "Hata avcılığı zamanı! Kodlardaki hataları bulup düzeltmeyi öğreneceksin. Debugging ustası olmaya hazır mısın?",
            "Data Detective": "Veri dedektifliği! Bilgileri analiz etmeyi ve verilerden anlam çıkarmayı keşfedeceksin.",
            "Logic Builder": "Mantık kurucusu! IF-ELSE, döngüler ve mantıksal operatörlerle düşünme becerilerini geliştireceksin.",
            "Tech Safety": "Teknoloji güvenliği! Dijital dünyada kendini nasıl koruyacağını öğreneceksin."
        }
        return station_info.get(station_name, "Bu istasyonda yeni şeyler öğreneceksin!")
    
    def show_question_screen(self, question_text: str, options: List[str], question_num: int, 
                           total_questions: int, answer_callback: Callable, hint: str = ""):
        """Soru ekranını gösterir"""
        self.clear_frame()
        self.current_frame = self.create_gradient_frame(self.root)
        
        # Ana container
        main_container = tk.Frame(self.current_frame, bg=self.colors['BACKGROUND'])
        main_container.pack(expand=True, fill='both')
        
        # Soru numarası
        question_num_label = tk.Label(
            main_container,
            text=f"Soru {question_num}/{total_questions}",
            font=self.fonts['small'],
            bg=self.colors['BACKGROUND'],
            fg=self.colors['TEXT']
        )
        question_num_label.pack(pady=(50, 10))
        
        # Soru card'ı
        question_card = self.create_card(main_container, width=800, height=500)
        question_card.pack(pady=20)
        
        # Soru metni
        question_label = tk.Label(
            question_card,
            text=question_text,
            font=self.fonts['heading'],
            bg=self.colors['CARD_BG'],
            fg=self.colors['CARD_TEXT'],
            wraplength=750,
            justify='center'
        )
        question_label.pack(pady=(30, 40))
        
        # Şıklar için frame
        options_frame = tk.Frame(question_card, bg=self.colors['CARD_BG'])
        options_frame.pack(pady=20)
        
        # Şık butonları
        option_colors = ['PRIMARY', 'SUCCESS', 'WARNING', 'INFO']
        for i, option in enumerate(options):
            color = option_colors[i % len(option_colors)]
            option_button = self.create_styled_button(
                options_frame,
                f"{chr(65 + i)}) {option}",
                lambda idx=i: answer_callback(idx),
                color,
                width=40
            )
            option_button.pack(pady=8, padx=20)
        
        # Hint varsa göster
        if hint:
            hint_label = tk.Label(
                question_card,
                text=f"💡 İpucu: {hint}",
                font=self.fonts['small'],
                bg=self.colors['CARD_BG'],
                fg='#666666',
                wraplength=750
            )
            hint_label.pack(pady=(20, 10))
    
    def show_result_screen(self, is_correct: bool, correct_answer: str, 
                          continue_callback: Callable, game_over_callback: Optional[Callable] = None):
        """Sonuç ekranını gösterir"""
        self.clear_frame()
        self.current_frame = self.create_gradient_frame(self.root)
        
        # Ana container
        main_container = tk.Frame(self.current_frame, bg=self.colors['BACKGROUND'])
        main_container.pack(expand=True, fill='both')
        
        # Sonuç card'ı
        result_card = self.create_card(main_container, width=600, height=400)
        result_card.pack(expand=True)
        
        if is_correct:
            # Doğru cevap
            result_icon = "🎉"
            result_text = "Tebrikler! Doğru cevap!"
            result_color = self.colors['SUCCESS']
            button_text = "▶️ Devam Et"
            callback = continue_callback
        else:
            # Yanlış cevap
            result_icon = "❌"
            result_text = "Üzgünüm, yanlış cevap!"
            result_color = self.colors['WARNING']
            button_text = "🏠 Ana Menüye Dön"
            callback = game_over_callback or continue_callback
        
        # Sonuç ikonu ve metni
        result_label = tk.Label(
            result_card,
            text=f"{result_icon}\n{result_text}",
            font=self.fonts['title'],
            bg=self.colors['CARD_BG'],
            fg=result_color
        )
        result_label.pack(pady=50)
        
        # Doğru cevap göster
        correct_label = tk.Label(
            result_card,
            text=f"Doğru cevap: {correct_answer}",
            font=self.fonts['normal'],
            bg=self.colors['CARD_BG'],
            fg=self.colors['CARD_TEXT']
        )
        correct_label.pack(pady=20)
        
        # Devam butonu
        continue_button = self.create_styled_button(
            result_card,
            button_text,
            callback,
            'INFO' if is_correct else 'WARNING',
            width=25
        )
        continue_button.pack(pady=30)
        
        # 3 saniye sonra otomatik devam (sadece doğru cevaplarda)
        if is_correct:
            self.root.after(3000, callback)
    
    def show_loading_screen(self, message: str = "Yükleniyor..."):
        """Yükleme ekranını gösterir"""
        self.clear_frame()
        self.current_frame = self.create_gradient_frame(self.root)
        
        # Loading container
        loading_container = tk.Frame(self.current_frame, bg=self.colors['BACKGROUND'])
        loading_container.pack(expand=True)
        
        # Loading ikonu (dönen yıldız efekti)
        loading_label = tk.Label(
            loading_container,
            text="⭐",
            font=('Arial', 48),
            bg=self.colors['BACKGROUND'],
            fg=self.colors['TEXT']
        )
        loading_label.pack(pady=50)
        
        # Loading mesajı
        message_label = tk.Label(
            loading_container,
            text=message,
            font=self.fonts['heading'],
            bg=self.colors['BACKGROUND'],
            fg=self.colors['TEXT']
        )
        message_label.pack(pady=20)
        
        # Basit animasyon
        self._animate_loading(loading_label)
    
    def _animate_loading(self, label: tk.Label):
        """Loading animasyonu"""
        stars = ["⭐", "🌟", "✨", "💫"]
        current = getattr(self, '_loading_frame', 0)
        label.configure(text=stars[current % len(stars)])
        self._loading_frame = current + 1
        
        # 500ms sonra tekrar çağır
        self.root.after(500, lambda: self._animate_loading(label))

# Test fonksiyonu
def test_ui():
    """UI sistemini test eder"""
    ui = UIManager()
    root = ui.create_main_window()
    
    def dummy_callback(*args):
        print(f"Callback çağırıldı: {args}")
    
    # Hoş geldin ekranını göster
    ui.show_welcome_screen(dummy_callback)
    
    root.mainloop()

if __name__ == "__main__":
    test_ui()