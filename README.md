# 🎮 CodeCraft Academy

> 8-16 yaş arası çocuklara kodlama, algoritma, hata ayıklama, veri analizi ve dijital güvenlik öğreten interaktif eğitim oyunu

<img width="1920" height="892" alt="image" src="https://github.com/user-attachments/assets/8ab35d25-fdd4-4c3e-92e0-2d353e2b7652" />
<img width="1920" height="886" alt="image" src="https://github.com/user-attachments/assets/e5f8039f-18bd-4f87-9ed9-0eebee55d6f8" />
<img width="1920" height="882" alt="image" src="https://github.com/user-attachments/assets/9d8c88ad-293e-4e83-8dd4-267bbe2058f0" />
<img width="1920" height="896" alt="image" src="https://github.com/user-attachments/assets/1bceac0f-861d-45f7-ae7b-ed3057f561fc" />
<img width="1920" height="892" alt="image" src="https://github.com/user-attachments/assets/57006980-8fae-43a8-85c1-0054e708424c" />

**CodeCraft Academy**, çocuklara temel programlama kavramlarını oyun formatında öğreten Python tabanlı bir masaüstü uygulamasıdır. Farklı istasyonlarda sorular çözerek puanlar kazanabilir ve başarı rozetleri alabilirsiniz.

---

## 📋 İçindekiler

- [✨ Özellikler](#-özellikler)
- [🎪 Eğitim İstasyonları](#-eğitim-istasyonları)
- [🛠️ Teknoloji](#️-teknoloji)
- [🚀 Kurulum](#-kurulum)
- [🎮 Nasıl Oynanır](#-nasıl-oynanır)
- [📁 Proje Yapısı](#-proje-yapısı)
- [💻 Sistem Gereksinimleri](#-sistem-gereksinimleri)
- [🤝 Katkıda Bulunma](#-katkıda-bulunma)
- [📄 Lisans](#-lisans)
- [📞 İletişim](#-iletişim)

---

## ✨ Özellikler

### 🎯 **Temel Özellikler**
- **5 Farklı İstasyon** - Algoritma, hata ayıklama, veri analizi, mantık ve güvenlik
- **15+ Soru** - Her istasyonda yaş grubuna uygun sorular
- **Skor Sistemi** - Doğru cevaplar için puan kazanma
- **Rozet Sistemi** - Başarı seviyelerine göre rozetler
- **PDF Sertifika** - Tamamlanan modüller için sertifika oluşturma

### 🎨 **Kullanıcı Deneyimi**
- **Tkinter GUI** - Basit ve kullanıcı dostu arayüz
- **Yaş Uygun İçerik** - 8-16 yaş grubu için tasarlanmış sorular
- **Offline Çalışma** - İnternet bağlantısı gerektirmez
- **Çoklu Platform** - Windows, macOS ve Linux desteği

---

## 🎪 Eğitim İstasyonları

### 🧩 **Algorithm Explorer**
Algoritma temel kavramları ve problem çözme adımlarını öğrenin
- Algoritma nedir?
- Problem çözme teknikleri
- Adım adım düşünme

### 🐛 **Bug Hunter**
Kod hatalarını bulma ve düzeltme becerilerini geliştirin
- Farklı hata türleri
- Debug teknikleri
- Kod inceleme alışkanlıkları

### 📊 **Data Detective**
Temel veri analizi ve yorumlama becerilerini keşfedin
- Veri türleri
- Basit veri analizi
- Grafik okuma

### 🧠 **Logic Builder**
Mantıksal düşünme ve karar verme yapılarını öğrenin
- Koşullu ifadeler (IF-ELSE)
- Mantıksal operatörler (AND, OR)
- Döngü kavramları

### 🛡️ **Tech Safety**
Dijital dünyada güvenli kalma yöntemlerini öğrenin
- Güvenli şifre oluşturma
- Phishing farkındalığı
- Dijital güvenlik temelleri

---

## 🛠️ Teknoloji

**Kullanılan Teknolojiler:**
- **Python 3.8+** - Ana programlama dili
- **Tkinter** - GUI framework (Python ile birlikte gelir)
- **JSON** - Soru ve skor verilerinin depolanması

---

## 🚀 Kurulum

### **Ön Gereksinimler**
- Python 3.8 veya üstü
- Tkinter (çoğu Python kurulumunda varsayılan olarak gelir)

### **Kurulum Adımları**

1. **Projeyi indirin**
```bash
git clone https://github.com/elifnuroksuzz/CodeCraft-Academy.git
cd CodeCraft-Academy
```

2. **Gerekli paketleri yükleyin**
```bash
pip install -r requirements.txt
```

3. **Oyunu başlatın**
```bash
python main.py
```

### **Sorun Giderme**
```bash
# Tkinter yoksa (Ubuntu/Debian için)
sudo apt-get install python3-tk

# macOS için
brew install python-tk
```

---

## 🎮 Nasıl Oynanır

1. **Oyuncu Adı Girişi** - Adınızı girin ve oyuna başlayın
2. **İstasyon Seçimi** - 5 farklı eğitim alanından birini seçin  
3. **Soruları Cevaplayın** - Her istasyonda 3 soru yanıtlayın
4. **Puanınızı Görün** - Doğru cevaplara göre puan kazanın
5. **Rozet Kazanın** - Başarı seviyenize göre rozet alın
6. **Sertifika İndirin** - Başarılı modüller için PDF sertifika

---

## 📁 Proje Yapısı

```
CodeCraft-Academy/
├── main.py              # Ana başlatıcı dosya
├── config.py            # Oyun yapılandırma ayarları
├── game_engine.py       # Oyun mantığı ve motor
├── ui_manager.py        # Kullanıcı arayüz yönetimi
├── question_bank.py     # Soru bankası ve veri yönetimi
├── score_system.py      # Skor ve rozet sistemi
├── assets_generator.py  # SVG ikon ve grafik oluşturucu
├── requirements.txt     # Python paket gereksinimleri
├── data/               # Soru verileri ve skorlar (JSON)
├── assets/             # Görseller, fontlar ve kaynaklar
└── certificates/       # Oluşturulan PDF sertifikalar
```

---

## 💻 Sistem Gereksinimleri

**Minimum Sistem Gereksinimleri:**
- **İşletim Sistemi:** Windows 10, macOS 10.14+, Linux Ubuntu 18.04+
- **Python:** 3.8 veya üstü
- **RAM:** 4GB
- **Disk Alanı:** 200MB

---

## 🤝 Katkıda Bulunma

Bu projeye katkıda bulunmak isterseniz:

1. Bu repository'yi fork edin
2. Yeni bir feature branch oluşturun:
   ```bash
   git checkout -b feature/yeni-ozellik
   ```
3. Değişikliklerinizi commit edin:
   ```bash
   git commit -m "✨ Yeni özellik eklendi"
   ```
4. Branch'inizi push edin:
   ```bash
   git push origin feature/yeni-ozellik
   ```
5. Pull Request oluşturun

### **Katkı Alanları**
- Yeni sorular ekleme
- Arayüz geliştirmeleri
- Bug düzeltmeleri
- Dokümantasyon iyileştirmeleri
- Yeni dil desteği

---

## 📄 Lisans

Bu proje MIT License ile lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

```
MIT License

Copyright (c) 2024 Elif Nur Öksüz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software.
```

---

## 📞 İletişim

**Elif Nur Öksüz**

- 🌐 **GitHub:** [@elifnuroksuzz](https://github.com/elifnuroksuzz)
- 📧 **Email:** [elifnuroksuz4@gmail.com](mailto:elifnuroksuz4@gmail.com)  
- 💼 **LinkedIn:** [elifnuroksuz](https://www.linkedin.com/in/elifnuroksuz/)

---

<div align="center">

**⭐ Bu projeyi beğendiyseniz yıldızlamayı unutmayın!**

🐛 **Hata bulursanız veya öneriniz varsa** [Issues sayfası](https://github.com/elifnuroksuzz/CodeCraft-Academy/issues) üzerinden bize ulaşın.

🚀 **Projeyi fork'layın ve kendi özelliklerinizi ekleyin!**

</div>
