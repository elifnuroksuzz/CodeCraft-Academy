# config.py
class GameConfig:
    # Oyun Temel Ayarları
    GAME_TITLE = "CodeCraft Academy"
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 800
    
    # İstasyon Ayarları
    TOTAL_STATIONS = 5
    QUESTIONS_PER_STATION = 3
    
    # Oyuncu Hakları
    MAX_LIVES = 2
    JOKER_RIGHTS = 2
    
    # İstasyon İsimleri
    STATIONS = [
        "Algorithm Explorer",
        "Bug Hunter", 
        "Data Detective",
        "Logic Builder",
        "Tech Safety"
    ]
    
    # Renkler
    COLORS = {
        'PRIMARY': '#2E86AB',
        'SUCCESS': '#F24236', 
        'WARNING': '#F6AE2D',
        'INFO': '#F26419',
        'BACKGROUND': '#A23B72'
    }
    
    # Rozetler
    BADGES = {
        'GOLD': {'min_score': 90, 'name': 'Kodlama Ustası'},
        'SILVER': {'min_score': 70, 'name': 'Algoritma Uzmanı'}, 
        'BRONZE': {'min_score': 50, 'name': 'Mantık Kurucusu'},
        'PARTICIPATION': {'min_score': 0, 'name': 'Cesur Öğrenci'}
    }