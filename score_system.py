# score_system.py
import json
import os
from datetime import datetime
from typing import List, Dict, Optional
from dataclasses import dataclass
from config import GameConfig

@dataclass
class PlayerScore:
    """Oyuncu skor bilgilerini tutan clean data class"""
    name: str
    score: int
    badge: str
    completed_stations: int
    total_questions: int
    correct_answers: int
    date: str
    
    def get_accuracy(self) -> float:
        """Doğruluk yüzdesini hesaplar"""
        if self.total_questions == 0:
            return 0.0
        return (self.correct_answers / self.total_questions) * 100

class ScoreManager:
    """Skor yönetimi için ana class"""
    
    def __init__(self):
        self.scores_file = 'data/scores.json'
        self.current_session = None
        self._ensure_data_directory()
    
    def _ensure_data_directory(self):
        """Data klasörünün var olduğundan emin olur"""
        os.makedirs('data', exist_ok=True)
    
    def start_new_session(self, player_name: str):
        """Yeni oyun oturumu başlatır"""
        self.current_session = {
            'player_name': player_name,
            'score': 0,
            'completed_stations': 0,
            'total_questions': 0,
            'correct_answers': 0,
            'start_time': datetime.now().isoformat()
        }
    
    def add_station_result(self, station_name: str, questions_answered: int, correct_count: int):
        """İstasyon sonucunu oturuma ekler"""
        if not self.current_session:
            raise ValueError("Aktif oturum bulunamadı. Önce start_new_session() çağırın.")
        
        # Station puanını hesapla (her doğru cevap 20 puan)
        station_score = correct_count * 20
        
        # Bonus puanlar
        if correct_count == questions_answered:  # Tüm sorular doğru
            station_score += 10  # Mükemmellik bonusu
        
        # Oturumu güncelle
        self.current_session['score'] += station_score
        self.current_session['completed_stations'] += 1
        self.current_session['total_questions'] += questions_answered
        self.current_session['correct_answers'] += correct_count
        
        print(f"✅ {station_name}: {correct_count}/{questions_answered} doğru, +{station_score} puan")
    
    def calculate_final_score(self) -> PlayerScore:
        """Final skoru hesaplar ve PlayerScore objesi döndürür"""
        if not self.current_session:
            raise ValueError("Aktif oturum bulunamadı.")
        
        # Tamamlama bonusu
        if self.current_session['completed_stations'] == GameConfig.TOTAL_STATIONS:
            self.current_session['score'] += 50  # Oyunu bitirme bonusu
            print("🎉 Oyunu tamamlama bonusu: +50 puan!")
        
        # Rozet belirleme
        badge = self._calculate_badge(self.current_session['score'])
        
        # PlayerScore objesi oluştur
        final_score = PlayerScore(
            name=self.current_session['player_name'],
            score=self.current_session['score'],
            badge=badge,
            completed_stations=self.current_session['completed_stations'],
            total_questions=self.current_session['total_questions'],
            correct_answers=self.current_session['correct_answers'],
            date=datetime.now().strftime("%Y-%m-%d %H:%M")
        )
        
        return final_score
    
    def _calculate_badge(self, score: int) -> str:
        """Skora göre rozet belirler"""
        for badge_key, badge_info in GameConfig.BADGES.items():
            if score >= badge_info['min_score']:
                return badge_info['name']
        
        # En düşük rozeti döndür
        return GameConfig.BADGES['PARTICIPATION']['name']
    
    def save_score(self, player_score: PlayerScore):
        """Skoru kalıcı olarak kaydeder"""
        scores = self._load_all_scores()
        
        # Yeni skoru ekle
        score_dict = {
            'name': player_score.name,
            'score': player_score.score,
            'badge': player_score.badge,
            'completed_stations': player_score.completed_stations,
            'total_questions': player_score.total_questions,
            'correct_answers': player_score.correct_answers,
            'accuracy': round(player_score.get_accuracy(), 1),
            'date': player_score.date
        }
        
        scores.append(score_dict)
        
        # Skora göre sırala (yüksekten düşüğe)
        scores.sort(key=lambda x: x['score'], reverse=True)
        
        # Dosyaya kaydet
        with open(self.scores_file, 'w', encoding='utf-8') as file:
            json.dump(scores, file, ensure_ascii=False, indent=2)
        
        print(f"💾 Skor kaydedildi: {player_score.name} - {player_score.score} puan")
    
    def _load_all_scores(self) -> List[Dict]:
        """Tüm skorları dosyadan yükler"""
        try:
            with open(self.scores_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("⚠️ Skor dosyası bozuk, yeni dosya oluşturuluyor...")
            return []
    
    def get_top_scores(self, limit: int = 10) -> List[Dict]:
        """En yüksek skorları döndürür"""
        scores = self._load_all_scores()
        return scores[:limit]
    
    def get_player_rank(self, player_score: int) -> int:
        """Oyuncunun sırasını hesaplar"""
        scores = self._load_all_scores()
        rank = 1
        
        for score in scores:
            if score['score'] > player_score:
                rank += 1
            else:
                break
        
        return rank
    
    def get_session_summary(self) -> Dict:
        """Mevcut oturum özetini döndürür"""
        if not self.current_session:
            return {}
        
        accuracy = 0
        if self.current_session['total_questions'] > 0:
            accuracy = (self.current_session['correct_answers'] / 
                       self.current_session['total_questions']) * 100
        
        return {
            'player_name': self.current_session['player_name'],
            'current_score': self.current_session['score'],
            'completed_stations': self.current_session['completed_stations'],
            'total_stations': GameConfig.TOTAL_STATIONS,
            'correct_answers': self.current_session['correct_answers'],
            'total_questions': self.current_session['total_questions'],
            'accuracy': round(accuracy, 1)
        }
    
    def clear_current_session(self):
        """Mevcut oturumu temizler"""
        self.current_session = None

class BadgeSystem:
    """Rozet sistemi için yardımcı class"""
    
    @staticmethod
    def get_badge_emoji(badge_name: str) -> str:
        """Rozet adına göre emoji döndürür"""
        badge_emojis = {
            'Kodlama Ustası': '🥇',
            'Algoritma Uzmanı': '🥈',
            'Mantık Kurucusu': '🥉',
            'Cesur Öğrenci': '🎖️'
        }
        return badge_emojis.get(badge_name, '🏅')
    
    @staticmethod
    def get_badge_color(badge_name: str) -> str:
        """Rozet adına göre renk döndürür"""
        badge_colors = {
            'Kodlama Ustası': '#FFD700',      # Altın
            'Algoritma Uzmanı': '#C0C0C0',   # Gümüş
            'Mantık Kurucusu': '#CD7F32',    # Bronz
            'Cesur Öğrenci': '#4169E1'       # Mavi
        }
        return badge_colors.get(badge_name, '#808080')
    
    @staticmethod
    def get_congratulations_message(badge_name: str) -> str:
        """Rozet için tebrik mesajı döndürür"""
        messages = {
            'Kodlama Ustası': "🎉 Mükemmel! Sen gerçek bir kodlama ustasısın!",
            'Algoritma Uzmanı': "👏 Harika! Algoritma dünyasında uzmanlaştın!",
            'Mantık Kurucusu': "💪 Güzel! Mantık kurma becerilerin gelişiyor!",
            'Cesur Öğrenci': "🌟 Aferin! Öğrenmeye devam etme cesaretini gösterdin!"
        }
        return messages.get(badge_name, "🎈 Tebrikler! Yeni şeyler öğrendin!")

# Test fonksiyonu
def test_score_system():
    """Skor sistemini test eder"""
    print("🧪 Skor sistemi test ediliyor...")
    
    # Score manager oluştur
    score_manager = ScoreManager()
    
    # Test oturumu başlat
    score_manager.start_new_session("Test Oyuncusu")
    
    # Test station sonuçları ekle
    score_manager.add_station_result("Algorithm Explorer", 3, 3)
    score_manager.add_station_result("Bug Hunter", 3, 2)
    score_manager.add_station_result("Data Detective", 3, 3)
    score_manager.add_station_result("Logic Builder", 3, 1)
    score_manager.add_station_result("Tech Safety", 3, 2)
    
    # Final skoru hesapla
    final_score = score_manager.calculate_final_score()
    print(f"Final Skor: {final_score}")
    
    # Badge emoji test
    emoji = BadgeSystem.get_badge_emoji(final_score.badge)
    message = BadgeSystem.get_congratulations_message(final_score.badge)
    print(f"Rozet: {emoji} {final_score.badge}")
    print(f"Mesaj: {message}")

if __name__ == "__main__":
    test_score_system()