# IMDb Top 250 Film Web Scraping ve Analiz Projesi

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)

Bu proje, IMDb'nin Top 250 film listesindeki filmlere ait detaylı verileri Python ve Selenium kullanarak çekmek, bu verileri temizlemek ve Power BI ile görselleştirerek analiz etmek amacıyla geliştirilmiştir.

---

###  Proje Hakkında

Projenin temel amacı, web scraping tekniklerini kullanarak dinamik bir web sitesinden veri toplama, toplanan veriyi işleme ve anlamlı sonuçlar çıkarmak için görselleştirme adımlarını içeren bütüncül bir veri projesi deneyimi sunmaktır.

**Toplanan Veriler:**
*   Film Adı
*   Yayın Yılı
*   Süre
*   IMDb Puanı
*   Puanlama Sayısı
*   Yorum Sayısı
*   Film Türleri
*   Yönetmen(ler)
*   Senarist(ler)
*   Ülke
*   Bütçe ve Hasılat (varsa)

Veriler çekildikten sonra bir Excel dosyasına kaydedilmiş, ardından Power BI'da detaylı analizler ve görselleştirmeler yapılmıştır.

---

### Kullanılan Teknolojiler

*   **Veri Kazıma:** Python, Selenium
*   **Veri İşleme:** Pandas
*   **Veri Depolama:** Excel
*   **Veri Görselleştirme ve Analiz:** Power BI

---

### 📄 Proje Raporları

Projenin teknik adımlarını, veri hazırlama sürecini ve analiz bulgularını içeren detaylı raporlara aşağıdaki linklerden ulaşabilirsiniz:

*   [**Proje Raporu:**](./reports/Proje_Raporu.pdf) Projenin motivasyonunu, hedeflerini, veri toplama ve işleme adımlarını açıklar.
*   [**Analiz ve Görselleştirme Raporu:**](./reports/Analiz_ve_Gorsellestirme_Raporu.pdf) Power BI ile oluşturulan grafikler üzerinden yapılan detaylı analizleri ve çıkarımları içerir.

---

### 📊 Analizden Öne Çıkan Bulgular

*   **Puan ve Sıralama İlişkisi:** Film puanı ile listedeki sıralama arasında çok güçlü bir negatif korelasyon (-0.84) bulunmaktadır. Puan arttıkça sıralama iyileşmektedir.
*   **Türlerin Hakimiyeti:** "Drama", Top 250 listesinde açık ara en çok temsil edilen film türüdür.
*   **Sürelerin Dağılımı:** Filmlerin büyük çoğunluğu 110-140 dakika aralığında yoğunlaşmaktadır. "2 saatlik" film süresi, listenin standardı gibi görünmektedir.
*   **Coğrafi Dağılım:** Liste, büyük ölçüde ABD yapımı filmlerden (195 film) oluşmaktadır. Bu durum Hollywood'un sinema endüstrisindeki baskın konumunu göstermektedir.
*   **Öne Çıkan Yönetmen ve Senaristler:** Christopher Nolan, hem yönetmen (8 film) hem de senarist (9 film) olarak listede en çok eseri bulunan isimdir.
