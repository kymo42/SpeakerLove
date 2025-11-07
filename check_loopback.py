import sounddevice as sd

devices = sd.query_devices()

print('REAL LOOPBACK DEVICES (2+ input channels, 0 output):')
print('='*80)

for i, dev in enumerate(devices):
    # Real loopback: has input channels but NO output channels
    if dev['max_input_channels'] >= 2 and dev['max_output_channels'] == 0:
        print(f'[{i}] {dev["name"]}')
        print(f'    INPUT: {dev["max_input_channels"]} channels')
        print()

print()
print('MICROPHONES (input only, typically 1-2 channels):')
print('='*80)

for i, dev in enumerate(devices):
    if dev['max_input_channels'] in [1, 2] and dev['max_output_channels'] == 0:
        name_lower = dev['name'].lower()
        if any(k in name_lower for k in ['microphone', 'mic', 'capture']):
            print(f'[{i}] {dev["name"]}')
            print(f'    INPUT: {dev["max_input_channels"]} channels')
            print()
