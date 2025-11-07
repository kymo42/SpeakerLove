import sounddevice as sd

devices = sd.query_devices()

print("ALL DEVICES WITH INPUT CHANNELS:")
print("="*80)

for i, dev in enumerate(devices):
    if dev['max_input_channels'] > 0:
        print(f"[{i}] {dev['name']}")
        print(f"    INPUT: {dev['max_input_channels']} channels, OUTPUT: {dev['max_output_channels']} channels")
