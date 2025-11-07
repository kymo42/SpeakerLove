#!/usr/bin/env python3
"""
Diagnostic tool to find working microphone and loopback combinations
"""

import sounddevice as sd
import numpy as np

print("="*80)
print("VOICE ISOLATOR DIAGNOSTIC TOOL")
print("="*80)
print()

devices = sd.query_devices()

print("STEP 1: Find Microphone Input Devices")
print("-" * 80)

mics = []
for i, dev in enumerate(devices):
    if dev['max_input_channels'] > 0:
        # Filter for likely microphones (not outputs, not loopback)
        name = dev['name'].lower()
        if any(keyword in name for keyword in ['mic', 'audio', 'capture', 'input']):
            if not any(keyword in name for keyword in ['output', 'out', 'speaker', 'voicemeeter']):
                mics.append(i)
                print(f"  [{i}] {dev['name']}")
                print(f"      Input channels: {dev['max_input_channels']}, Latency: {dev['default_low_input_latency']*1000:.1f}ms")

print()
print("STEP 2: Find Voicemeeter Input/Loopback Devices")
print("-" * 80)

loopbacks = []
for i, dev in enumerate(devices):
    name = dev['name'].lower()
    if 'voicemeeter' in name and 'in' in name and dev['max_input_channels'] > 0:
        loopbacks.append(i)
        print(f"  [{i}] {dev['name']}")
        print(f"      Input channels: {dev['max_input_channels']}, Latency: {dev['default_low_input_latency']*1000:.1f}ms")

print()
print("STEP 3: Find Output Devices")
print("-" * 80)

outputs = []
for i, dev in enumerate(devices):
    if dev['max_output_channels'] > 0:
        name = dev['name'].lower()
        if not any(keyword in name for keyword in ['voicemeeter', 'virtual']):
            outputs.append(i)
            print(f"  [{i}] {dev['name']}")
            print(f"      Output channels: {dev['max_output_channels']}, Latency: {dev['default_low_output_latency']*1000:.1f}ms")

print()
print("="*80)
print("RECOMMENDED COMBINATION:")
print("="*80)

if mics and loopbacks and outputs:
    print(f"Microphone:       [{mics[0]}] (First real microphone)")
    print(f"Loopback/Input:   [{loopbacks[0]}] (Voicemeeter input)")
    print(f"Output Device:    [{outputs[0]}] (Speakers)")
    print()
    print("Try this combination in Voice Isolator")
    print()
    print("If that doesn't work, try each Voicemeeter option:")
    for i, lb in enumerate(loopbacks[:5]):
        print(f"  Option {i+1}: [{lb}]")
else:
    print("Error: Not enough devices found!")
    if not mics:
        print("  - No microphones found")
    if not loopbacks:
        print("  - No Voicemeeter inputs found")
    if not outputs:
        print("  - No output devices found")

print()
print("="*80)
print("DETAILED DEVICE LIST:")
print("="*80)

for i, dev in enumerate(devices):
    in_ch = dev['max_input_channels']
    out_ch = dev['max_output_channels']
    if in_ch > 0 or out_ch > 0:
        print(f"[{i}] {dev['name']}")
        if in_ch > 0:
            print(f"    INPUT: {in_ch} channels")
        if out_ch > 0:
            print(f"    OUTPUT: {out_ch} channels")

print()
print("="*80)
