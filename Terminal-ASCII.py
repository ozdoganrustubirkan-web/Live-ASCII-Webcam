import cv2
import numpy as np
import os
import time

# 1. ASCII Karakter Seti (Koyudan Açığa)
ASCII_CHARS = '@%#*+=-:. ' 
MAX_CHARS = len(ASCII_CHARS)

# 2. Renk Kodları
# Karakter Rengi: Siyah (\033[30m)
# Arka Plan Rengi: Beyaz (\033[47m)
# Terminal rengini sıfırlama kodu
RESET_COLOR = "\033[0m"

# Siyah karakter rengi kodu
BLACK_TEXT = "\033[30m"
# Beyaz arka plan rengi kodu
WHITE_BACKGROUND = "\033[47m"

# 3. Ayarlar
DOWNSCALE_FACTOR = 8 
FRAME_RATE = 0.05     

# 4. Görüntüyü Siyah-Beyaz ASCII'ye Çeviren Fonksiyon
def convert_image_to_ascii_bw(frame):
    # Görüntüyü gri tonlamaya çevir
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Boyutu küçült
    resized_frame = cv2.resize(gray_frame, 
                               (gray_frame.shape[1] // DOWNSCALE_FACTOR, 
                                gray_frame.shape[0] // DOWNSCALE_FACTOR), 
                               interpolation=cv2.INTER_AREA)

    # 0-255 parlaklık değerlerini 0-MAX_CHARS arası bir indekse dönüştür
    pixel_indices = (resized_frame / (255 / (MAX_CHARS - 1))).astype(np.uint8)
    
    ascii_output = []
    
    # İlk önce tüm çıktıya beyaz arka plan kodunu ekle
    # Bu, çıktının başlangıcında terminalin arka planını beyaza ayarlar.
    output_prefix = WHITE_BACKGROUND
    
    for row in pixel_indices:
        line = []
        for char_idx in row:
            # Karakteri seç
            char = ASCII_CHARS[char_idx]
            
            # Siyah renk kodunu ve karakteri birleştir
            colored_char = BLACK_TEXT + char
            line.append(colored_char)
            
        # Satırı birleştir. Reset kodu satırın sonuna gitmeli.
        ascii_output.append(''.join(line))
        
    # Tüm çıktıya beyaz arka planı uygula ve sonunda resetle
    return output_prefix + '\n'.join(ascii_output) + RESET_COLOR

# 5. Kamera Başlatma
def run_live_ascii_bw():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Hata: Kamera açılamadı.")
        return

    try:
        while True:
            ret, frame = cap.read()
            
            if not ret:
                print("Kare okunamadı, çıkılıyor.")
                break
            
            # Siyah-Beyaz ASCII'ye çevir
            ascii_art = convert_image_to_ascii_bw(frame)
            
            # Terminali temizle
            os.system('cls' if os.name == 'nt' else 'clear') 
            
            # ASCII çıktısını yazdır
            print(ascii_art)
            
            # Çıkış tuşu kontrolü
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
            time.sleep(FRAME_RATE)

    finally:
        cap.release()
        cv2.destroyAllWindows()
        print("\nASCII Sanat görüntüsü kapatıldı." + RESET_COLOR)

# Kodu çalıştırma
if __name__ == '__main__':
    run_live_ascii_bw()