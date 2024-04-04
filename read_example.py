# asyncio kütüphanesi, Python'da asenkron programlama için kullanılır.
# Bu kütüphane, özellikle ağ işlemleri ve zaman uyumsuz görevler gibi bloke edici işlemler için kullanışlıdır.
import asyncio

# ConnectButton modülünden BLEDeviceReader sınıfını içe aktarır.
# Bu sınıf, belirli bir BLE cihazına bağlanmak, servisler ve karakteristikler üzerinden veri okumak için gerekli işlevselliği sağlar.
from ConnectButton import BLEDeviceReader

# Alınan veriyi işleyen bir fonksiyon tanımlanır.
# Bu fonksiyon, BLE cihazından okunan ham veriyi (bytearray formatında) alır,
# ve ilgilenilen ilk byte'ı çıkararak ekrana yazdırır.


def handle_data_received(data):
    # Gelen veriyi bytearray'a çevirip ilk byte'ı alır
    value = bytearray(data)[0]
    # Alınan değeri ekrana yazdırır
    print(f"Received Data: {value}")


# BLEDeviceReader sınıfının bir örneğini oluşturur ve veri alındığında çağrılacak fonksiyon olarak
# handle_data_received fonksiyonunu kullanır. Bu, BLE cihazından veri okunduğunda
# handle_data_received fonksiyonunun otomatik olarak çağrılmasını sağlar.
# Ayrıca, cihaz adını eldiven üzerindeki etiketle eşleşecek şekilde ayarlayın.
reader = BLEDeviceReader(
    on_data_received=handle_data_received, device_name="BUTON_1")

# Asenkron bir şekilde reader nesnesinin scan_and_connect metodunu çalıştırır.
# Bu metod, öncelikle çevredeki BLE cihazlarını tarar, ardından belirli bir cihaza bağlanır
# ve sürekli olarak veri okuma işlemini gerçekleştirir.
# Bu işlem, asyncio kütüphanesi ile yönetilen bir asenkron döngü içinde gerçekleşir.
asyncio.run(reader.scan_and_connect())
