from bleak import BleakScanner, BleakClient

class BLEDeviceReader:
    def __init__(self, on_data_received, scan_duration=5, use_bdaddr=False):
        self.service_uuid = "000000ff-0000-1000-8000-00805f9b34fb"
        self.characteristic_uuid = "0000ff01-0000-1000-8000-00805f9b34fb"
        self.on_data_received = on_data_received
        self.scan_duration = scan_duration
        self.use_bdaddr = use_bdaddr
        self.client = None

    async def scan_and_connect(self):
        print("Scanning for devices, please wait...")
        devices = await BleakScanner.discover(duration=self.scan_duration)

        for device in devices:
            if self.service_uuid in device.metadata.get("uuids", []):
                print(f"Found target device: {device}")
                self.client = BleakClient(device.address)
                await self.connect_and_start_listening()
                return

        print("No target device found.")

    async def connect_and_start_listening(self):
        try:
            await self.client.connect()
            print("Connected to the device.")
            await self.start_listening_for_data()
        except Exception as e:
            print(f"Failed to connect or listen for data: {e}")

    async def start_listening_for_data(self):
        while True:
            if self.client and self.client.is_connected:
                value = await self.client.read_gatt_char(self.characteristic_uuid)
                self.on_data_received(value)
                # await asyncio.sleep(1)  # Adjust the sleep time as necessary
            else:
                print("Disconnected, stopping data listening.")
                break

    def on_data_received_default(self, data):
        # Default data received handler if none is provided
        print(f"Data received: {data}")

