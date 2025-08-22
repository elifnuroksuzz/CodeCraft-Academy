# main.py
"""
CodeCraft Academy - Ana Başlatıcı
Çocuklara kodlama ve teknoloji okuryazarlığı öğreten interaktif eğitim oyunu

Kullanım: python main.py
"""

import sys
import os
import tkinter as tk
from tkinter import messagebox
import traceback

# Proje dizinini Python path'ine ekle
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_dir)

def check_dependencies():
    """Gerekli bağımlılıkları kontrol eder"""
    missing_modules = []
    
    try:
        import tkinter
    except ImportError:
        missing_modules.append("tkinter")
    
    try:
        import json
    except ImportError:
        missing_modules.append("json")
    
    if missing_modules:
        error_msg = f"Eksik modüller: {', '.join(missing_modules)}\n"
        error_msg += "Lütfen Python kurulumunuzu kontrol edin."
        print(f"❌ {error_msg}")
        return False
    
    return True

def check_project_structure():
    """Proje dosya yapısını kontrol eder"""
    required_files = [
        'config.py',
        'question_bank.py', 
        'score_system.py',
        'ui_manager.py',
        'game_engine.py'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        error_msg = f"Eksik dosyalar: {', '.join(missing_files)}\n"
        error_msg += "Lütfen tüm proje dosyalarının mevcut olduğundan emin olun."
        print(f"❌ {error_msg}")
        return False
    
    # Data klasörünü oluştur
    if not os.path.exists('data'):
        os.makedirs('data')
        print("📁 Data klasörü oluşturuldu")
    
    # Certificates klasörünü oluştur
    if not os.path.exists('certificates'):
        os.makedirs('certificates')
        print("📁 Certificates klasörü oluşturuldu")
    
    return True

def setup_logging():
    """Basit logging sistemi kurar"""
    import logging
    
    # Log klasörünü oluştur
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # Log formatını ayarla
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('logs/game.log', encoding='utf-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    return logging.getLogger(__name__)

def show_startup_info():
    """Başlangıç bilgilerini gösterir"""
    print("=" * 60)
    print("🚀 CodeCraft Academy")
    print("=" * 60)
    print("📚 Kodlama ve Teknoloji Okuryazarlığı Eğitim Oyunu")
    print("👥 Hedef Kitle: 8-16 yaş arası öğrenciler")
    print("🎯 5 İstasyon, 15+ Soru, Skor ve Rozet Sistemi")
    print("=" * 60)
    print()

def show_controls_info():
    """Kontrol bilgilerini gösterir"""
    print("🎮 KONTROLLER:")
    print("   • ESC tuşu: Oyundan çık")
    print("   • Enter tuşu: Devam et (bazı ekranlarda)")
    print("   • Mouse: Butonlara tıklama")
    print()

def create_desktop_shortcut():
    """Masaüstü kısayolu oluşturur (Windows için)"""
    try:
        import winshell
        from win32com.client import Dispatch
        
        desktop = winshell.desktop()
        path = os.path.join(desktop, "CodeCraft Academy.lnk")
        target = os.path.join(project_dir, "main.py")
        
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = sys.executable
        shortcut.Arguments = f'"{target}"'
        shortcut.WorkingDirectory = project_dir
        shortcut.IconLocation = target
        shortcut.save()
        
        print("🔗 Masaüstü kısayolu oluşturuldu")
    except ImportError:
        pass  # Windows değil ya da gerekli modüller yok
    except Exception as e:
        print(f"⚠️ Kısayol oluşturulamadı: {e}")

def handle_exception(exc_type, exc_value, exc_traceback):
    """Global exception handler"""
    if issubclass(exc_type, KeyboardInterrupt):
        print("\n👋 Oyun kullanıcı tarafından kapatıldı")
        return
    
    error_msg = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    print(f"❌ Beklenmeyen hata:\n{error_msg}")
    
    # Tkinter varsa hata dialogu göster
    try:
        root = tk.Tk()
        root.withdraw()  # Ana pencereyi gizle
        
        messagebox.showerror(
            "CodeCraft Academy - Hata",
            f"Beklenmeyen bir hata oluştu:\n\n{exc_value}\n\n"
            "Lütfen oyunu yeniden başlatmayı deneyin.\n"
            "Sorun devam ederse geliştiriciye başvurun."
        )
        root.destroy()
    except:
        pass  # Tkinter kullanamıyoruz

def run_game():
    """Ana oyun fonksiyonu"""
    try:
        # Game engine'i import et ve başlat
        from game_engine import GameEngine
        
        print("🎮 Oyun motoru başlatılıyor...")
        game = GameEngine()
        
        print("✅ Sistem hazır! Oyun başlıyor...")
        print("🎯 İyi eğlenceler!\n")
        
        # Oyunu başlat
        game.start_game()
        
    except ImportError as e:
        print(f"❌ Modül import hatası: {e}")
        print("Lütfen tüm proje dosyalarının mevcut olduğundan emin olun.")
        return False
    
    except Exception as e:
        print(f"❌ Oyun başlatma hatası: {e}")
        traceback.print_exc()
        return False
    
    return True

def main():
    """Ana fonksiyon"""
    # Global exception handler'ı ayarla
    sys.excepthook = handle_exception
    
    # Başlangıç bilgilerini göster
    show_startup_info()
    
    # Sistem kontrollerini yap
    print("🔍 Sistem kontrolleri...")
    
    if not check_dependencies():
        input("Devam etmek için Enter'a basın...")
        return 1
    
    if not check_project_structure():
        input("Devam etmek için Enter'a basın...")
        return 1
    
    print("✅ Tüm kontroller başarılı!")
    print()
    
    # Logging sistemini kur
    logger = setup_logging()
    logger.info("CodeCraft Academy başlatılıyor")
    
    # Kontrol bilgilerini göster
    show_controls_info()
    
    # Masaüstü kısayolu oluştur (opsiyonel)
    create_desktop_shortcut()
    
    # Oyunu çalıştır
    try:
        success = run_game()
        
        if success:
            logger.info("Oyun başarıyla tamamlandı")
            print("👋 Tekrar görüşmek üzere!")
        else:
            logger.error("Oyun hata ile sonlandı")
            return 1
            
    except KeyboardInterrupt:
        logger.info("Oyun kullanıcı tarafından durduruldu")
        print("\n👋 Görüşürüz!")
    
    except Exception as e:
        logger.error(f"Beklenmeyen hata: {e}")
        print(f"❌ Beklenmeyen hata: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    
    # Windows'ta konsol penceresini açık tut
    if os.name == 'nt' and exit_code != 0:
        input("\nBir tuşa basın...")
    
    sys.exit(exit_code)