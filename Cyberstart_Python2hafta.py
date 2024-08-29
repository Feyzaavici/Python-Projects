# 1. Adım: Noktaların Tanımlanması
noktalar = [(1, 2), (4, 6), (5, 7), (8, 9), (3, 3)]  # Örnek noktalar

# 2. Adım: Öklid Mesafesi Fonksiyonu
def oklidMesafesi(nokta1, nokta2):
    x1, y1 = nokta1
    x2, y2 = nokta2
    mesafe = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5  # Öklid mesafesi formülü
    return mesafe

# 3. Adım: Mesafelerin Hesaplanması
mesafeler = []  # Mesafeleri saklamak için bir liste

for i in range(len(noktalar)):
    for j in range(i + 1, len(noktalar)):  # Aynı çiftleri tekrar hesaplamamak için 'j' 'i+1'den başlar
        mesafe = oklidMesafesi(noktalar[i], noktalar[j])
        mesafeler.append(mesafe)

# 4. Adım: Minimum Mesafenin Bulunması
min_mesafe = min(mesafeler)  # 'mesafeler' listesindeki minimum mesafeyi bulur

# Sonucu yazdır
print("Noktalar arasındaki minimum Öklid mesafesi:", min_mesafe)
