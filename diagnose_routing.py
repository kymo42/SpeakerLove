"""
Diagnose audio routing issue
"""

import sounddevice as sd

devices = sd.query_devices()

print("ANALYZING YOUR AUDIO ROUTING")
print("="*80)
print()

# Show all OUTPUT devices
print("OUTPUT DEVICES (Where audio can be sent to):")
print("-"*80)

for i, dev in enumerate(devices):
    if dev['max_output_channels'] > 0:
        print(f"[{i}] {dev['name']}")
        print(f"    Output channels: {dev['max_output_channels']}")

print()
print()

# Show what each output is likely connected to
print("DEVICE ROUTING ANALYSIS:")
print("="*80)
print()

print("When Voice Isolator outputs to a device, it goes to:")
print()

output_devices = {
    13: "Microsoft Sound Mapper - Output",
    116: "Speakers (Conexant HD Audio output)",
    125: "Speakers (Audioengine HD3)",
}

for device_id, name in output_devices.items():
    # Find the device
    if device_id < len(devices):
        dev = devices[device_id]
        print(f"Device [{device_id}] {dev['name']}")
        print(f"  Connected to: Your physical SPEAKERS")
        print(f"  What happens: Audio plays through your speakers")
        print()

print()
print("THE ISSUE:")
print("="*80)
print()
print("If you select output device [13] (Microsoft Sound Mapper),")
print("Voice Isolator sends the PROCESSED voice to your speakers.")
print()
print("This is actually CORRECT behavior for what you want!")
print()
print("The issue is: You don't want Voice Isolator's OUTPUT going to speakers.")
print("You want it to go to a VIRTUAL MICROPHONE that Discord uses.")
print()
print()
print("SOLUTION:")
print("="*80)
print()
print("You need a VIRTUAL MICROPHONE device that:")
print("  1. Voice Isolator sends clean voice TO")
print("  2. Discord/Game receives FROM")
print("  3. Is NOT connected to your speakers")
print()
print("Options:")
print("  A) Create a Virtual Audio Cable (software)")
print("  B) Use VoiceMeeter Virtual Microphone")
print("  C) Use Windows built-in virtual microphone (if available)")
print()
