# question_bank.py
import json
import random
from typing import List, Dict, Optional
from config import GameConfig

class Question:
    """Tek bir soruyu temsil eden clean class"""
    
    def __init__(self, text: str, options: List[str], correct_index: int, hint: str = ""):
        self.text = text
        self.options = options
        self.correct_index = correct_index
        self.hint = hint
    
    def is_correct(self, selected_index: int) -> bool:
        """Verilen cevabın doğru olup olmadığını kontrol eder"""
        return selected_index == self.correct_index
    
    def get_correct_answer(self) -> str:
        """Doğru cevabı döndürür"""
        return self.options[self.correct_index]

class QuestionBank:
    """Tüm soruları yöneten ana class"""
    
    def __init__(self):
        self.questions = self._load_questions()
    
    def _load_questions(self) -> Dict[str, List[Question]]:
        """Soruları JSON'dan yükler veya varsayılan soruları oluşturur"""
        try:
            with open('data/questions.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                return self._convert_to_question_objects(data)
        except FileNotFoundError:
            print("Soru dosyası bulunamadı, varsayılan sorular oluşturuluyor...")
            return self._create_default_questions()
    
    def _convert_to_question_objects(self, data: Dict) -> Dict[str, List[Question]]:
        """JSON verisini Question objelerine çevirir"""
        questions = {}
        for station, question_list in data.items():
            questions[station] = []
            for q in question_list:
                question = Question(
                    text=q['text'],
                    options=q['options'],
                    correct_index=q['correct_index'],
                    hint=q.get('hint', '')
                )
                questions[station].append(question)
        return questions
    
    def _create_default_questions(self) -> Dict[str, List[Question]]:
        """Varsayılan soruları oluşturur"""
        default_questions = {
            'algorithm_explorer': [
                Question(
                    "Algoritma nedir?",
                    ["Bir problem çözme adımları dizisi", "Bir programlama dili", "Bir bilgisayar oyunu", "Bir matematik işlemi"],
                    0,
                    "Adım adım yapılacak işlemlerin sırası"
                ),
                Question(
                    "Hangi sıralama algoritması daha hızlıdır?",
                    ["Bubble Sort", "Quick Sort", "Sleep Sort", "Random Sort"],
                    1,
                    "Böl ve fethet mantığı kullanan algoritma"
                ),
                Question(
                    "Pseudocode ne işe yarar?",
                    ["Kod yazmak için", "Algoritma tasarlamak için", "Hata bulmak için", "Program çalıştırmak için"],
                    1,
                    "Algoritmanın mantığını yazma yöntemi"
                )
            ],
            'bug_hunter': [
                Question(
                    "Bug (hata) nedir?",
                    ["Programda istenmeyen davranış", "Bilgisayar virüsü", "Antivirus programı", "Oyun karakteri"],
                    0,
                    "Kodun beklenmedik şekilde çalışması"
                ),
                Question(
                    "Debug ne demektir?",
                    ["Program yazmak", "Hata aramak ve düzeltmek", "Kod silmek", "Program yüklemek"],
                    1,
                    "Hataları bulup düzeltme işlemi"
                ),
                Question(
                    "Syntax error nedir?",
                    ["Mantık hatası", "Yazım kuralları hatası", "Çalışma zamanı hatası", "Performans sorunu"],
                    1,
                    "Kodun yazım kurallarına uymaması"
                )
            ],
            'data_detective': [
                Question(
                    "Veri (Data) nedir?",
                    ["Sadece sayılar", "Bilgi parçacıkları", "Program kodları", "Bilgisayar dosyaları"],
                    1,
                    "İşlenebilir bilgi parçaları"
                ),
                Question(
                    "Hangi veri tipi en fazla yer kaplar?",
                    ["Integer", "String", "Boolean", "Video"],
                    3,
                    "Görsel içerik en fazla yer kaplar"
                ),
                Question(
                    "Veri analizi nedir?",
                    ["Veri silmek", "Veriden anlam çıkarmak", "Veri kopyalamak", "Veri yazmak"],
                    1,
                    "Verilerden desenleri ve bilgileri çıkarma"
                )
            ],
            'logic_builder': [
                Question(
                    "AND operatörü ne zaman TRUE döner?",
                    ["Hiçbir zaman", "Her zaman", "Her iki koşul da doğruysa", "Bir koşul doğruysa"],
                    2,
                    "İki koşulun da sağlanması gerekir"
                ),
                Question(
                    "IF-ELSE yapısı neye yarar?",
                    ["Döngü oluşturmak", "Koşullu işlem yapmak", "Fonksiyon tanımlamak", "Değişken oluşturmak"],
                    1,
                    "Koşula bağlı farklı işlemler yapma"
                ),
                Question(
                    "Loop (döngü) nedir?",
                    ["Tek seferlik işlem", "Tekrarlayan işlem", "Koşullu işlem", "Rastgele işlem"],
                    1,
                    "Aynı işlemi birden fazla kez yapma"
                )
            ],
            'tech_safety': [
                Question(
                    "Güçlü şifre hangi özelliklere sahip olmalı?",
                    ["Sadece harfler", "Büyük-küçük harf, sayı ve sembol karışımı", "Sadece sayılar", "Doğum tarihi"],
                    1,
                    "Karmaşık kombinasyon daha güvenli"
                ),
                Question(
                    "Phishing nedir?",
                    ["Balık tutma", "Bilgi çalma tuzağı", "Oyun oynama", "Program yazma"],
                    1,
                    "Sahte sitelerle bilgi çalma yöntemi"
                ),
                Question(
                    "İki faktörlü doğrulama nedir?",
                    ["İki şifre kullanma", "Ek güvenlik katmanı", "İki bilgisayar kullanma", "İki kişi ile giriş"],
                    1,
                    "Şifreye ek olarak SMS/kod doğrulaması"
                )
            ]
        }
        
        # Varsayılan soruları JSON olarak kaydet
        self._save_questions_to_json(default_questions)
        return default_questions
    
    def _save_questions_to_json(self, questions: Dict[str, List[Question]]):
        """Soruları JSON formatında kaydeder"""
        import os
        
        # data klasörünü oluştur
        os.makedirs('data', exist_ok=True)
        
        # Question objelerini dict'e çevir
        json_data = {}
        for station, question_list in questions.items():
            json_data[station] = []
            for q in question_list:
                json_data[station].append({
                    'text': q.text,
                    'options': q.options,
                    'correct_index': q.correct_index,
                    'hint': q.hint
                })
        
        # JSON dosyasına yaz
        with open('data/questions.json', 'w', encoding='utf-8') as file:
            json.dump(json_data, file, ensure_ascii=False, indent=2)
    
    def get_random_questions(self, station_name: str, count: int = 3) -> List[Question]:
        """Belirtilen istasyon için rastgele sorular döndürür"""
        station_key = station_name.lower().replace(' ', '_')
        
        if station_key in self.questions:
            station_questions = self.questions[station_key]
            if len(station_questions) >= count:
                return random.sample(station_questions, count)
            else:
                return station_questions.copy()  # Tüm soruları döndür
        
        return []  # Eğer istasyon bulunamazsa boş liste döndür
    
    def get_station_question_count(self, station_name: str) -> int:
        """Belirtilen istasyondaki toplam soru sayısını döndürür"""
        station_key = station_name.lower().replace(' ', '_')
        if station_key in self.questions:
            return len(self.questions[station_key])
        return 0