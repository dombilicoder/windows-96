# 💾 Windows 96 — Gelişmiş Discord Müzik & Moderasyon Botu

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/discord.py-v2.0+-blueviolet?style=for-the-badge" alt="Discord.py">
  <img src="https://img.shields.io/badge/Lavalink-Wavelink-orange?style=for-the-badge" alt="Wavelink">
  <img src="https://img.shields.io/badge/Render-Deployed-brightgreen?style=for-the-badge&logo=render&logoColor=white" alt="Render">
</p>

---

Eski günlerin nostaljik esintisini Discord sunucunuza taşıyan, **bir coZ projesi** olarak geliştirilmiş yüksek performanslı bir Discord botu. Gelişmiş Lavalink entegrasyonu sayesinde kesintisiz müzik deneyimi sunarken, akıllı ve dinamik arayüzüyle sohbet kirliliğinin önüne geçer.

## ✨ Öne Çıkan Özellikler

* 🎵 **Canlı ve Dinamik Müzik Paneli:** Şarkı başladığında açılan özel embed arayüzü, 3 saniyede bir güncellenen ilerleme çubuğu (progress bar) ile şarkının anlık durumunu gösterir. Şarkı bittiğinde panel otomatik olarak yeşile döner ve sayaç son saniyeye kilitlenir.
* 👥 **Footer Entegrasyonu:** Şarkıyı isteyen kullanıcının ismi ve profil fotoğrafı, paneli bozmayacak şekilde şık bir biçimde alt bilgi (footer) alanında çözümlenir.
* 🤫 **Sessiz Komut Yapısı:** `w.dur`, `w.devam`, `w.ses` ve `w.sar` gibi yönetim komutları kullanıldığında chatte ekstra mesaj kirliliği yaratmaz; kullanıcının yazdığı mesajı silerek doğrudan ana paneli manipüle eder.
* 🧹 **Akıllı Moderasyon (`w.sil`):** Kanaldaki mesajları toplu olarak temizler. İşlem bittiğinde gönderdiği onay mesajını 3 saniye sonra otomatik olarak imha eder.
* 📡 **7/24 Kesintisiz Yayın (Render Ready):** İçerisinde barındırdığı hafif `aiohttp` web sunucusu sayesinde Render.com gibi bulut platformlarında uyku moduna geçmeden 7/24 aktif kalabilir.

## 🛠️ Komutlar

### 🔹 Müzik Komutları
* `w.oynat <şarkı adı / url>`: Belirtilen şarkıyı arar ve sıraya ekleyerek oynatır.
* `w.dur`: Şarkıyı duraklatır (Sessiz komut).
* `w.devam`: Şarkıyı sürdürür (Sessiz komut).
* `w.sar <saniye>`: Şarkıyı belirtilen süre kadar ileri sarar.
* `w.geç`: Çalan şarkıyı atlayarak sıradakine geçer.
* `w.ses <0-500>`: Botun ses seviyesini ayarlar ve paneli anlık günceller (Sessiz komut).
* `w.sıra`: Aktif müzik sırasını listeler.
* `w.bitir`: Müziği tamamen kapatır ve botu kanaldan ayırır.

### 🔹 Moderasyon & Genel
* `w.sil <miktar>`: Belirtilen miktarda mesajı kanaldan temizler (Maks: 100).
* `w.yardım`: Sistem yardım menüsünü şık bir embed ile gösterir.
* `w.emoji`: Sunucudaki emojileri ID'leri ile listeler.

## 🚀 Kurulum ve Dağıtım

### 1. Gereksinimler
Projenin çalışması için bilgisayarınızda veya sunucunuzda bir **Lavalink** sunucusunun aktif olması gerekmektedir.

### 2. Çevresel Değişkenler (.env)
Ana dizinde bir `.env` dosyası oluşturun ve aşağıdaki verileri doldurun:
```env
DISCORD_TOKEN=BOT_TOKENINIZ
VOICE_CHANNEL_ID=SABIT_SES_KANALI_ID
LAVALINK_HOST=LAVALINK_IP_ADRESI
LAVALINK_PORT=LAVALINK_PORTU
LAVALINK_PASSWORD=LAVALINK_SIFRESI
LAVALINK_SECURE=false