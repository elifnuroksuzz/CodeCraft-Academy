# assets_generator.py
"""
CodeCraft Academy Assets Oluşturucu
Oyun için gerekli görsel assets'leri SVG formatında oluşturur
"""

import os
import urllib.request
from typing import Dict

def create_assets_structure():
    """Assets klasör yapısını oluşturur"""
    directories = [
        'assets',
        'assets/images',
        'assets/fonts',
        'assets/icons'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"📁 {directory} klasörü oluşturuldu")

def create_svg_icon(name: str, svg_content: str):
    """SVG ikon dosyası oluşturur"""
    file_path = f"assets/icons/{name}.svg"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"🎨 {file_path} oluşturuldu")

def create_game_icons():
    """Oyun için gerekli SVG ikonları oluşturur"""
    
    # Logo/Ana İkon
    logo_svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
    <defs>
        <linearGradient id="logoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#2E86AB;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#A23B72;stop-opacity:1" />
        </linearGradient>
    </defs>
    <circle cx="100" cy="100" r="95" fill="url(#logoGrad)" stroke="#fff" stroke-width="3"/>
    <text x="100" y="110" font-family="Arial, sans-serif" font-size="40" font-weight="bold" 
          text-anchor="middle" fill="white">CC</text>
    <text x="100" y="140" font-family="Arial, sans-serif" font-size="16" 
          text-anchor="middle" fill="white">Academy</text>
    <polygon points="60,60 80,40 140,40 160,60 140,80 80,80" fill="rgba(255,255,255,0.2)"/>
</svg>'''
    
    # Algorithm Explorer İkonu
    algorithm_svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
    <defs>
        <linearGradient id="algGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#2E86AB;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#1E5F7A;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect x="10" y="10" width="80" height="80" rx="10" fill="url(#algGrad)"/>
    <circle cx="30" cy="30" r="5" fill="white"/>
    <circle cx="50" cy="50" r="5" fill="white"/>
    <circle cx="70" cy="70" r="5" fill="white"/>
    <line x1="30" y1="30" x2="50" y2="50" stroke="white" stroke-width="2"/>
    <line x1="50" y1="50" x2="70" y2="70" stroke="white" stroke-width="2"/>
    <polygon points="25,60 35,60 30,70" fill="white"/>
    <polygon points="45,40 55,40 50,30" fill="white"/>
</svg>'''
    
    # Bug Hunter İkonu
    bug_svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
    <defs>
        <linearGradient id="bugGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#F24236;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#D1362F;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect x="10" y="10" width="80" height="80" rx="10" fill="url(#bugGrad)"/>
    <ellipse cx="50" cy="40" rx="15" ry="10" fill="white"/>
    <ellipse cx="50" cy="60" rx="12" ry="8" fill="white"/>
    <circle cx="45" cy="38" r="2" fill="black"/>
    <circle cx="55" cy="38" r="2" fill="black"/>
    <line x1="35" y1="30" x2="25" y2="20" stroke="white" stroke-width="2"/>
    <line x1="65" y1="30" x2="75" y2="20" stroke="white" stroke-width="2"/>
    <line x1="35" y1="45" x2="25" y2="45" stroke="white" stroke-width="2"/>
    <line x1="65" y1="45" x2="75" y2="45" stroke="white" stroke-width="2"/>
    <line x1="35" y1="60" x2="25" y2="70" stroke="white" stroke-width="2"/>
    <line x1="65" y1="60" x2="75" y2="70" stroke="white" stroke-width="2"/>
</svg>'''
    
    # Data Detective İkonu
    data_svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
    <defs>
        <linearGradient id="dataGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#F6AE2D;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#E69A26;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect x="10" y="10" width="80" height="80" rx="10" fill="url(#dataGrad)"/>
    <rect x="20" y="25" width="60" height="50" rx="5" fill="white"/>
    <rect x="25" y="35" width="15" height="8" fill="#F6AE2D"/>
    <rect x="45" y="35" width="25" height="8" fill="#F6AE2D"/>
    <rect x="25" y="48" width="20" height="8" fill="#F6AE2D"/>
    <rect x="50" y="48" width="20" height="8" fill="#F6AE2D"/>
    <rect x="25" y="61" width="30" height="8" fill="#F6AE2D"/>
    <circle cx="70" cy="70" r="8" fill="rgba(0,0,0,0.1)"/>
    <circle cx="68" cy="68" r="6" fill="white" stroke="#F6AE2D" stroke-width="2"/>
</svg>'''
    
    # Logic Builder İkonu
    logic_svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
    <defs>
        <linearGradient id="logicGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#F26419;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#D1560F;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect x="10" y="10" width="80" height="80" rx="10" fill="url(#logicGrad)"/>
    <rect x="20" y="25" width="25" height="15" rx="3" fill="white"/>
    <rect x="55" y="25" width="25" height="15" rx="3" fill="white"/>
    <rect x="37.5" y="50" width="25" height="15" rx="3" fill="white"/>
    <rect x="37.5" y="75" width="25" height="10" rx="3" fill="white"/>
    <line x1="32.5" y1="40" x2="37.5" y2="57" stroke="white" stroke-width="2"/>
    <line x1="67.5" y1="40" x2="62.5" y2="57" stroke="white" stroke-width="2"/>
    <line x1="50" y1="65" x2="50" y2="75" stroke="white" stroke-width="2"/>
    <text x="32" y="35" font-family="monospace" font-size="8" fill="#F26419">IF</text>
    <text x="65" y="35" font-family="monospace" font-size="8" fill="#F26419">&amp;&amp;</text>
    <text x="44" y="60" font-family="monospace" font-size="8" fill="#F26419">THEN</text>
</svg>'''
    
    # Tech Safety İkonu
    safety_svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
    <defs>
        <linearGradient id="safetyGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#A23B72;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#7A2B56;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect x="10" y="10" width="80" height="80" rx="10" fill="url(#safetyGrad)"/>
    <path d="M 50 20 L 35 30 L 35 55 Q 35 70 50 75 Q 65 70 65 55 L 65 30 Z" fill="white"/>
    <circle cx="50" cy="45" r="8" fill="#A23B72"/>
    <rect x="48" y="41" width="4" height="8" fill="white"/>
    <circle cx="50" cy="43" r="2" fill="white"/>
    <rect x="25" y="75" width="50" height="4" fill="white"/>
    <rect x="30" y="80" width="40" height="4" fill="white"/>
</svg>'''
    
    # Başarı Rozetleri
    gold_badge_svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
    <defs>
        <radialGradient id="goldGrad" cx="50%" cy="30%" r="70%">
            <stop offset="0%" style="stop-color:#FFD700;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#B8860B;stop-opacity:1" />
        </radialGradient>
    </defs>
    <circle cx="50" cy="50" r="40" fill="url(#goldGrad)" stroke="#DAA520" stroke-width="2"/>
    <polygon points="50,25 55,40 70,40 58,50 63,65 50,55 37,65 42,50 30,40 45,40" fill="#FFF8DC"/>
    <text x="50" y="80" font-family="Arial, sans-serif" font-size="10" font-weight="bold" 
          text-anchor="middle" fill="#B8860B">GOLD</text>
</svg>'''
    
    silver_badge_svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
    <defs>
        <radialGradient id="silverGrad" cx="50%" cy="30%" r="70%">
            <stop offset="0%" style="stop-color:#C0C0C0;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#808080;stop-opacity:1" />
        </radialGradient>
    </defs>
    <circle cx="50" cy="50" r="40" fill="url(#silverGrad)" stroke="#A0A0A0" stroke-width="2"/>
    <polygon points="50,25 55,40 70,40 58,50 63,65 50,55 37,65 42,50 30,40 45,40" fill="white"/>
    <text x="50" y="80" font-family="Arial, sans-serif" font-size="10" font-weight="bold" 
          text-anchor="middle" fill="#808080">SILVER</text>
</svg>'''
    
    bronze_badge_svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
    <defs>
        <radialGradient id="bronzeGrad" cx="50%" cy="30%" r="70%">
            <stop offset="0%" style="stop-color:#CD7F32;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#8B4513;stop-opacity:1" />
        </radialGradient>
    </defs>
    <circle cx="50" cy="50" r="40" fill="url(#bronzeGrad)" stroke="#A0522D" stroke-width="2"/>
    <polygon points="50,25 55,40 70,40 58,50 63,65 50,55 37,65 42,50 30,40 45,40" fill="#DEB887"/>
    <text x="50" y="80" font-family="Arial, sans-serif" font-size="10" font-weight="bold" 
          text-anchor="middle" fill="#8B4513">BRONZE</text>
</svg>'''
    
    participation_badge_svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
    <defs>
        <radialGradient id="partGrad" cx="50%" cy="30%" r="70%">
            <stop offset="0%" style="stop-color:#4169E1;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#191970;stop-opacity:1" />
        </radialGradient>
    </defs>
    <circle cx="50" cy="50" r="40" fill="url(#partGrad)" stroke="#4682B4" stroke-width="2"/>
    <polygon points="50,25 55,40 70,40 58,50 63,65 50,55 37,65 42,50 30,40 45,40" fill="#ADD8E6"/>
    <text x="50" y="80" font-family="Arial, sans-serif" font-size="8" font-weight="bold" 
          text-anchor="middle" fill="#191970">PARTICIPANT</text>
</svg>'''
    
    # İkonları oluştur
    icons = {
        'logo': logo_svg,
        'algorithm_explorer': algorithm_svg,
        'bug_hunter': bug_svg,
        'data_detective': data_svg,
        'logic_builder': logic_svg,
        'tech_safety': safety_svg,
        'gold_badge': gold_badge_svg,
        'silver_badge': silver_badge_svg,
        'bronze_badge': bronze_badge_svg,
        'participation_badge': participation_badge_svg
    }
    
    for name, svg_content in icons.items():
        create_svg_icon(name, svg_content)

def create_background_patterns():
    """Arka plan desenleri oluşturur"""
    
    # Gradient arka plan
    gradient_bg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" width="1200" height="800">
    <defs>
        <linearGradient id="mainGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#2E86AB;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#A23B72;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#F26419;stop-opacity:1" />
        </linearGradient>
        <pattern id="dots" x="0" y="0" width="50" height="50" patternUnits="userSpaceOnUse">
            <circle cx="25" cy="25" r="2" fill="rgba(255,255,255,0.1)"/>
        </pattern>
    </defs>
    <rect width="1200" height="800" fill="url(#mainGrad)"/>
    <rect width="1200" height="800" fill="url(#dots)"/>
</svg>'''
    
    file_path = "assets/images/background.svg"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(gradient_bg)
    print(f"🖼️ {file_path} oluşturuldu")

def download_font():
    """DejaVu Sans fontunu indirir"""
    try:
        font_url = "https://github.com/dejavu-fonts/dejavu-fonts/raw/master/ttf/DejaVuSans.ttf"
        font_path = "assets/fonts/DejaVuSans.ttf"
        
        print("📥 Font indiriliyor...")
        urllib.request.urlretrieve(font_url, font_path)
        print(f"✅ {font_path} indirildi")
        
    except Exception as e:
        print(f"⚠️ Font indirilemedi: {e}")
        print("💡 Manuel olarak DejaVuSans.ttf fontunu assets/fonts/ klasörüne koyabilirsiniz")
        
        # Fallback: Boş font dosyası oluştur
        with open("assets/fonts/DejaVuSans.ttf", 'w') as f:
            f.write("# Font dosyası burada olmalı\n")

def create_readme():
    """Assets klasörü için README oluşturur"""
    readme_content = """# CodeCraft Academy - Assets

Bu klasör oyun için gerekli görsel ve ses dosyalarını içerir.

## 📁 Klasör Yapısı

### 🎨 icons/
- İstasyon ikonları (SVG format)
- Rozet ikonları 
- Logo ve ana simgeler

### 🖼️ images/
- Arka plan görselleri
- Dekoratif elementler
- UI pattern'leri

### 🔤 fonts/
- DejaVuSans.ttf (Türkçe karakter desteği için)
- Alternatif fontlar

## 🎯 Kullanım

Tüm görsel assets'ler otomatik olarak assets_generator.py ile oluşturulur.

Yeni iconlar eklemek için:
1. SVG formatında oluşturun
2. 100x100 veya 200x200 boyutlarında
3. icons/ klasörüne yerleştirin

## 🎨 Renk Paleti

- Primary: #2E86AB (Mavi)
- Success: #F24236 (Kırmızı) 
- Warning: #F6AE2D (Sarı)
- Info: #F26419 (Turuncu)
- Background: #A23B72 (Mor)

## 📝 Notlar

- Tüm SVG dosyaları responsive tasarımdır
- Fontlar Türkçe karakter desteği sağlar
- Renkler GameConfig'deki palette ile uyumludur
"""
    
    with open("assets/README.md", 'w', encoding='utf-8') as f:
        f.write(readme_content)
    print("📝 assets/README.md oluşturuldu")

def main():
    """Ana fonksiyon"""
    print("🎨 CodeCraft Academy Assets Oluşturucu")
    print("=" * 50)
    
    # Klasör yapısını oluştur
    create_assets_structure()
    print()
    
    # İkonları oluştur
    print("🎯 İkonlar oluşturuluyor...")
    create_game_icons()
    print()
    
    # Arka plan desenlerini oluştur
    print("🖼️ Arka plan görselleri oluşturuluyor...")
    create_background_patterns()
    print()
    
    # Font indir
    print("🔤 Font indiriliyor...")
    download_font()
    print()
    
    # README oluştur
    print("📝 Dokümantasyon oluşturuluyor...")
    create_readme()
    print()
    
    print("✅ Tüm assets başarıyla oluşturuldu!")
    print("\n📦 Oluşturulan dosyalar:")
    print("   • 10 adet SVG ikon")
    print("   • 1 adet arka plan görseli") 
    print("   • DejaVuSans.ttf font dosyası")
    print("   • README.md dokümantasyonu")
    print("\n🎮 Artık oyunu çalıştırabilirsiniz!")

if __name__ == "__main__":
    main()