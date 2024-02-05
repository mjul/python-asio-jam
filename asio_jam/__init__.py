import sounddevice as sd


def enumerate_devices():
    print("Looking for ASIO devices...")
    apis = sd.query_hostapis()
    asio_apis = [a for a in apis if a['name'] == 'ASIO']
    asio_devices_nums = set([n for a in asio_apis for n in a['devices']])

    print("ASIO devices found", sorted(asio_devices_nums))

    devices = sd.query_devices()

    for i, d in enumerate(devices):
        if i in asio_devices_nums:
            print(f"Device {i}: {d['name']}", d)


if __name__ == "__main__":
    enumerate_devices()
