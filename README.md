# BLE Device Reader

### Bu proje, BLE (Bluetooth Low Energy) cihazlarından asenkron olarak veri okumak için bir Python scriptidir. BLEDeviceReader sınıfı aracılığıyla, belirtilen servis UUID'leri üzerinden BLE cihazlarına bağlanır ve bu cihazlardan veri okuma işlemleri gerçekleştirir.

# Özellikler

### There is some ways for you to know what kind of augments you could able to do with this repository.

- BLE cihazlarını tarar ve belirtilen servis UUID'lerine göre filtreler.
- Filtrelenen cihazlara bağlanır.
- Belirtilen karakteristiklerden veri okur.
- Okunan verileri işlemek için kullanıcı tanımlı bir callback fonksiyonu çağırır.

# Gerekli Kütüphaneleri Kurun

```
pip install -r requirements.txt
```

# Kullanım

```
python read_example.py
```

# Örnek Callback Fonksiyonu

Okunan verileri işlemek için bir callback fonksiyonu tanımlamanız gerekmektedir. Örnek bir callback fonksiyonu:

```
def handle_data_received(data):
    value = bytearray(data)[0]  # İlk byte'ı al
    print(f"Received Data: {value}")
```


# Projelere Entregrasyon
```
# asyncio kütüphanesi, Python'da asenkron programlama için kullanılır.
# Bu kütüphane, özellikle ağ işlemleri ve zaman uyumsuz görevler gibi bloke edici işlemler için kullanışlıdır.

import asyncio

# ConnectButton modülünden BLEDeviceReader sınıfını içe aktarır.
# Bu sınıf, belirli bir BLE cihazına bağlanmak, servisler ve karakteristikler üzerinden veri okumak için gerekli işlevselliği sağlar.

from ConnectButton import BLEDeviceReader
```