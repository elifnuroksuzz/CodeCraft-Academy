# game_engine.py
import tkinter as tk
from typing import List, Optional
import random
from config import GameConfig
from question_bank import QuestionBank, Question
from score_system import ScoreManager, PlayerScore, BadgeSystem
from ui_manager import UIManager

class GameState:
    """Oyun durumunu takip eden class"""
    
    def __init__(self):
        self.player_name = ""
        self.current_station = 0
        self.current_question = 0
        self.station_questions = []
        self.station_correct_answers = 0
        self.lives_remaining = GameConfig.MAX_LIVES
        self.jokers_remaining = GameConfig.JOKER_RIGHTS
        self.is_game_over = False
        self.is_game_completed = False

class GameEngine:
    """Ana oyun motoru - tüm oyun akışını yönetir"""
    
    def __init__(self):
        self.ui_manager = UIManager()
        self.question_bank = QuestionBank()
        self.score_manager = ScoreManager()
        self.game_state = GameState()
        self.root = None
        
        print("🎮 CodeCraft Academy başlatılıyor...")
        self._validate_system()
    
    def _validate_system(self):
        """Sistem bileşenlerini kontrol eder"""
        try:
            # Soru bankasını kontrol et
            total_questions = 0
            for station in GameConfig.STATIONS:
                count = self.question_bank.get_station_question_count(station)
                total_questions += count
                if count < GameConfig.QUESTIONS_PER_STATION:
                    print(f"⚠️ {station} istasyonunda yeterli soru yok ({count}/{GameConfig.QUESTIONS_PER_STATION})")
            
            print(f"✅ Toplam {total_questions} soru yüklendi")
            print(f"✅ {len(GameConfig.STATIONS)} istasyon hazır")
            
        except Exception as e:
            print(f"❌ Sistem kontrolü başarısız: {e}")
            raise
    
    def start_game(self):
        """Oyunu başlatır"""
        print("🚀 Oyun başlatılıyor...")
        
        # Ana pencereyi oluştur
        self.root = self.ui_manager.create_main_window()
        
        # Hoş geldin ekranını göster
        self.show_welcome_screen()
        
        # Ana döngüyü başlat
        self.root.mainloop()
    
    def show_welcome_screen(self):
        """Hoş geldin ekranını gösterir"""
        self.ui_manager.show_welcome_screen(self.on_game_start)
    
    def on_game_start(self, player_name: str):
        """Oyuncu adını alıp oyunu başlatır"""
        print(f"👤 Oyuncu: {player_name}")
        
        # Oyun durumunu sıfırla
        self.game_state = GameState()
        self.game_state.player_name = player_name
        
        # Score manager'da yeni oturum başlat
        self.score_manager.start_new_session(player_name)
        
        # İlk istasyonu başlat
        self.start_next_station()
    
    def start_next_station(self):
        """Bir sonraki istasyonu başlatır"""
        if self.game_state.current_station >= len(GameConfig.STATIONS):
            # Tüm istasyonlar tamamlandı
            self.complete_game()
            return
        
        # Mevcut istasyon bilgilerini al
        station_name = GameConfig.STATIONS[self.game_state.current_station]
        station_index = self.game_state.current_station
        
        print(f"🎯 İstasyon başlatılıyor: {station_name}")
        
        # İstasyon sorularını hazırla
        self.prepare_station_questions(station_name)
        
        # İstasyon tanıtım ekranını göster
        self.ui_manager.show_station_screen(
            station_name,
            station_index,
            len(GameConfig.STATIONS),
            self.start_station_questions
        )
    
    def prepare_station_questions(self, station_name: str):
        """İstasyon sorularını hazırlar"""
        # Rastgele sorular seç
        questions = self.question_bank.get_random_questions(
            station_name,
            GameConfig.QUESTIONS_PER_STATION
        )
        
        if not questions:
            print(f"❌ {station_name} için soru bulunamadı!")
            # Fallback: dummy soru oluştur
            questions = [Question(
                "Bu istasyon henüz hazır değil. Test sorusu?",
                ["Evet", "Hayır", "Belki", "Bilmiyorum"],
                0,
                "Bu sadece bir test sorusu"
            )]
        
        self.game_state.station_questions = questions
        self.game_state.current_question = 0
        self.game_state.station_correct_answers = 0
        
        print(f"📝 {len(questions)} soru hazırlandı")
    
    def start_station_questions(self):
        """İstasyon sorularını başlatır"""
        self.show_next_question()
    
    def show_next_question(self):
        """Bir sonraki soruyu gösterir"""
        if self.game_state.current_question >= len(self.game_state.station_questions):
            # İstasyon tamamlandı
            self.complete_station()
            return
        
        # Mevcut soruyu al
        question = self.game_state.station_questions[self.game_state.current_question]
        question_num = self.game_state.current_question + 1
        total_questions = len(self.game_state.station_questions)
        
        print(f"❓ Soru {question_num}/{total_questions}: {question.text}")
        
        # Soru ekranını göster
        self.ui_manager.show_question_screen(
            question.text,
            question.options,
            question_num,
            total_questions,
            self.on_answer_selected,
            question.hint
        )
    
    def on_answer_selected(self, selected_index: int):
        """Oyuncu cevap seçtiğinde çalışır"""
        question = self.game_state.station_questions[self.game_state.current_question]
        is_correct = question.is_correct(selected_index)
        correct_answer = question.get_correct_answer()
        
        print(f"📋 Seçilen: {question.options[selected_index]}")
        print(f"✅ Doğru: {correct_answer}")
        print(f"🎯 Sonuç: {'Doğru' if is_correct else 'Yanlış'}")
        
        if is_correct:
            self.handle_correct_answer()
        else:
            self.handle_wrong_answer()
        
        # Sonuç ekranını göster
        self.ui_manager.show_result_screen(
            is_correct,
            correct_answer,
            self.on_result_continue,
            self.on_game_over if not is_correct else None
        )
    
    def handle_correct_answer(self):
        """Doğru cevap işlemlerini yapar"""
        self.game_state.station_correct_answers += 1
        self.game_state.current_question += 1
        print(f"🎉 Doğru! Toplam doğru: {self.game_state.station_correct_answers}")
    
    def handle_wrong_answer(self):
        """Yanlış cevap işlemlerini yapar"""
        self.game_state.lives_remaining -= 1
        print(f"💔 Yanlış! Kalan can: {self.game_state.lives_remaining}")
        
        if self.game_state.lives_remaining <= 0:
            self.game_state.is_game_over = True
            print("💀 Oyun bitti!")
    
    def on_result_continue(self):
        """Sonuç ekranından devam edildiğinde çalışır"""
        if self.game_state.is_game_over:
            self.end_game()
        else:
            self.show_next_question()
    
    def on_game_over(self):
        """Oyun bittiğinde çalışır"""
        self.end_game()
    
    def complete_station(self):
        """İstasyonu tamamlar"""
        station_name = GameConfig.STATIONS[self.game_state.current_station]
        total_questions = len(self.game_state.station_questions)
        correct_answers = self.game_state.station_correct_answers
        
        print(f"🏁 İstasyon tamamlandı: {station_name}")
        print(f"📊 Sonuç: {correct_answers}/{total_questions}")
        
        # Score manager'a sonucu ekle
        self.score_manager.add_station_result(
            station_name,
            total_questions,
            correct_answers
        )
        
        # Bir sonraki istasyona geç
        self.game_state.current_station += 1
        
        # Yükleme ekranı göster ve sonraki istasyona geç
        self.ui_manager.show_loading_screen("Sonraki istasyon hazırlanıyor...")
        self.root.after(2000, self.start_next_station)
    
    def complete_game(self):
        """Oyunu başarıyla tamamlar"""
        self.game_state.is_game_completed = True
        print("🎊 Oyun başarıyla tamamlandı!")
        
        # Final skorunu hesapla
        final_score = self.score_manager.calculate_final_score()
        
        # Skoru kaydet
        self.score_manager.save_score(final_score)
        
        # Başarı ekranını göster
        self.show_victory_screen(final_score)
    
    def show_victory_screen(self, final_score: PlayerScore):
        """Zafer ekranını gösterir"""
        self.ui_manager.clear_frame()
        frame = self.ui_manager.create_gradient_frame(self.root)
        
        # Container
        container = tk.Frame(frame, bg=self.ui_manager.colors['BACKGROUND'])
        container.pack(expand=True)
        
        # Başarı card'ı
        victory_card = self.ui_manager.create_card(container, width=700, height=500)
        victory_card.pack(pady=50)
        
        # Başlık
        title = tk.Label(
            victory_card,
            text="🎉 TEBRİKLER! 🎉",
            font=self.ui_manager.fonts['title'],
            bg=self.ui_manager.colors['CARD_BG'],
            fg=self.ui_manager.colors['SUCCESS']
        )
        title.pack(pady=20)
        
        # Rozet ve mesaj
        badge_emoji = BadgeSystem.get_badge_emoji(final_score.badge)
        badge_message = BadgeSystem.get_congratulations_message(final_score.badge)
        
        badge_label = tk.Label(
            victory_card,
            text=f"{badge_emoji} {final_score.badge}",
            font=self.ui_manager.fonts['heading'],
            bg=self.ui_manager.colors['CARD_BG'],
            fg=self.ui_manager.colors['CARD_TEXT']
        )
        badge_label.pack(pady=10)
        
        message_label = tk.Label(
            victory_card,
            text=badge_message,
            font=self.ui_manager.fonts['normal'],
            bg=self.ui_manager.colors['CARD_BG'],
            fg=self.ui_manager.colors['CARD_TEXT'],
            wraplength=600
        )
        message_label.pack(pady=10)
        
        # Skor bilgileri
        score_text = f"""
        🎯 Final Skor: {final_score.score} puan
        ✅ Doğru Cevap: {final_score.correct_answers}/{final_score.total_questions}
        📊 Başarı Oranı: %{final_score.get_accuracy():.1f}
        🏆 Tamamlanan İstasyon: {final_score.completed_stations}/{GameConfig.TOTAL_STATIONS}
        """
        
        score_label = tk.Label(
            victory_card,
            text=score_text,
            font=self.ui_manager.fonts['normal'],
            bg=self.ui_manager.colors['CARD_BG'],
            fg=self.ui_manager.colors['CARD_TEXT'],
            justify='left'
        )
        score_label.pack(pady=20)
        
        # Çıkış butonu
        exit_button = self.ui_manager.create_styled_button(
            victory_card,
            "🏠 Oyundan Çık",
            self.exit_game,
            'PRIMARY',
            width=20
        )
        exit_button.pack(pady=20)
    
    def end_game(self):
        """Oyunu sonlandırır (başarısız)"""
        print("🔚 Oyun sonlandırıldı")
        
        # Kısmi skor hesapla
        if self.game_state.current_station > 0 or self.game_state.station_correct_answers > 0:
            partial_score = self.score_manager.calculate_final_score()
            self.score_manager.save_score(partial_score)
        
        # Game over ekranı
        self.show_game_over_screen()
    
    def show_game_over_screen(self):
        """Oyun bitti ekranını gösterir"""
        self.ui_manager.clear_frame()
        frame = self.ui_manager.create_gradient_frame(self.root)
        
        # Container
        container = tk.Frame(frame, bg=self.ui_manager.colors['BACKGROUND'])
        container.pack(expand=True)
        
        # Game over card
        game_over_card = self.ui_manager.create_card(container, width=600, height=400)
        game_over_card.pack(pady=100)
        
        # Başlık
        title = tk.Label(
            game_over_card,
            text="😔 Oyun Bitti",
            font=self.ui_manager.fonts['title'],
            bg=self.ui_manager.colors['CARD_BG'],
            fg=self.ui_manager.colors['WARNING']
        )
        title.pack(pady=30)
        
        # Mesaj
        message = tk.Label(
            game_over_card,
            text="Üzülme! Öğrenmek bir süreç.\nTekrar denemeye ne dersin?",
            font=self.ui_manager.fonts['normal'],
            bg=self.ui_manager.colors['CARD_BG'],
            fg=self.ui_manager.colors['CARD_TEXT'],
            justify='center'
        )
        message.pack(pady=20)
        
        # Butonlar
        button_frame = tk.Frame(game_over_card, bg=self.ui_manager.colors['CARD_BG'])
        button_frame.pack(pady=30)
        
        retry_button = self.ui_manager.create_styled_button(
            button_frame,
            "🔄 Tekrar Dene",
            self.restart_game,
            'SUCCESS',
            width=15
        )
        retry_button.pack(side='left', padx=10)
        
        exit_button = self.ui_manager.create_styled_button(
            button_frame,
            "🚪 Çık",
            self.exit_game,
            'WARNING',
            width=15
        )
        exit_button.pack(side='left', padx=10)
    
    def restart_game(self):
        """Oyunu yeniden başlatır"""
        print("🔄 Oyun yeniden başlatılıyor...")
        self.game_state = GameState()
        self.score_manager.clear_current_session()
        self.show_welcome_screen()
    
    def exit_game(self):
        """Oyundan çıkar"""
        print("👋 Görüşürüz!")
        if self.root:
            self.root.quit()

# Main fonksiyonu
def main():
    """Ana fonksiyon"""
    try:
        game = GameEngine()
        game.start_game()
    except KeyboardInterrupt:
        print("\n👋 Oyun kapatıldı")
    except Exception as e:
        print(f"❌ Beklenmeyen hata: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()