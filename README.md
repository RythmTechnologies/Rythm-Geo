# Rythm Geo

Rythm Geo, dünya genelindeki ülkeler, eyaletler ve şehirler hakkında veri sağlayan bir coğrafi veri API'sidir. Bu API, çeşitli uygulamalar ve analizler için kullanılabilir. Hem tam veri setini hem de belirli sorgulara dayalı verileri döndürme yeteneğine sahiptir.

## Özellikler

- Tüm ülke, eyalet ve şehirleri listeleme
- Belirli bir ülke, eyalet veya şehir için veri getirme
- JSON formatında veri döndürme
- Kolay kullanılabilir RESTful API

## Kullanım

API'yi kullanmak için, aşağıdaki uç noktaları kullanabilirsiniz:

### Tüm Verileri Getirme


Bu uç nokta, tüm ülke, eyalet ve şehir verilerini döndürür.

### Belirli Bir Sorguya Dayalı Veri Getirme

Belirli bir ülke, eyalet veya şehir için veri getirmek için aşağıdaki sorgu parametrelerini kullanabilirsiniz:

- **Ülkeye göre arama:** `api/v1/geo/?country=Turkey`
- **Eyalete göre arama:** `api/v1/geo/?state=Adana`
- **Şehire göre arama:** `api/v1/geo/?city=Istanbul`

### Tüm Veriyi Getirme

Tüm ülke, eyalet ve şehir verilerini getirmek için aşağıdaki uç noktayı kullanabilirsiniz:

- **Tüm veriyi getirme:** `api/v1/geo/all/`

Bu uç nokta, tüm ülke, eyalet ve şehirlerin verilerini döndürecektir.

## Katkıda Bulunanlar

- CoderMungan - [GitHub](https://github.com/codermungan)
- MelihCiray - [GitHub](https://github.com/mciray)

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.
