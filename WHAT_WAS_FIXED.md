# What Was Fixed

## The Problem

You got this error:
```
Failed to start audio streams: Error opening Inputstream:Invalid Device [PaErrorCode-9996]
```

**Root Cause**: The device IDs saved in `config.json` from previous selections were invalid or no longer available. Device IDs can change after reboot, or if a device wasn't properly selected.

---

## The Solution

### 1. **Improved Device Validation**
   - Added `validate_device()` function to check if devices exist BEFORE trying to use them
   - Better error messages that tell you exactly which device failed
   - Validates that:
     - Device ID is within valid range
     - Device has the right input/output channels
     - Device is accessible

### 2. **Better Error Handling**
   - Catches exceptions during stream creation
   - Provides detailed error messages
   - Stops cleanly without hanging

### 3. **Cleared Old Configuration**
   - Deleted old `config.json` with invalid device numbers
   - Fresh start with no cached bad settings

### 4. **Improved Device Display**
   - Device dropdowns now show: `[ID] Device Name`
   - Easy to see the exact device number to use
   - Auto-detection of loopback devices

### 5. **Better Default Selection**
   - GUI tries to intelligently select:
     - First available microphone
     - First available loopback device
     - First available output device
   - You can override manually if needed

### 6. **Verbose Output**
   - Prints to console what's happening
   - Shows which devices were selected
   - Helps debug if something goes wrong

---

## Code Changes

### New Function: `validate_device()`
```python
def validate_device(device_id, input_device=True):
    """Validate that a device exists and is accessible"""
    # Checks if device exists
    # Checks if it has the right channels
    # Returns True/False
```

### Improved Error Handling
```python
# Before: Generic error
raise ValueError("Audio stream failed")

# After: Specific error with device info
if not validate_device(self.config.mic_device):
    raise ValueError(f"Invalid microphone device: {self.config.mic_device}")
```

### Better Device Selection
```python
# Extract device ID from GUI string "[1] Device Name"
mic_idx = int(mic_str.split(']')[0].strip('['))

# Validate before use
if not validate_device(mic_idx, input_device=True):
    raise ValueError(f"Device {mic_idx} is not a valid input device")
```

---

## What To Do Now

### Step 1: Run the Fixed Version
```bash
python voice_isolator.py
```

### Step 2: Device Selection
The GUI will show devices with their IDs:
```
Microphone:        [1] Microphone (Sound Blaster...)
Speaker Loopback:  [15] Voicemeeter In 1 (...)
Output Virtual:    [6] Speakers (Audioengine...)
```

### Step 3: Select All Three
- **Microphone**: A real microphone input device
- **Speaker Loopback**: A loopback device (Voicemeeter or Stereo Mix)
- **Output**: Where clean voice goes

### Step 4: Start
Click "Start Voice Isolation"

If you get an error:
1. Read the error message
2. It will tell you which device is wrong
3. Try a different device
4. Click "Start" again

---

## Device Selection Guide

### Microphone - Pick ONE of these:
```
[1] Microphone (Sound Blaster Audigy 5/Rx)
[3] Headset Microphone (Oculus Virt...)
[13] Microphone (Sound Blaster Audigy 5/Rx)
[32] Microphone (Sound Blaster Audigy 5/Rx)
[43] Microphone (Conexant HD Audio capture)
[50] Microphone (SB Audigy 5/Rx [5FC0])
```
**NOT Voicemeeter, NOT Output, NOT Speakers**

### Speaker Loopback - Pick ONE of these:
```
[15] Voicemeeter In 1 (VB-Audio Voicemeeter VAIO)
[42] Stereo Mix (Conexant HD Stereo Mix)
[46] Voicemeeter Input (VB-Audio Voicemeeter VAIO)
[49] Voicemeeter AUX Input (VB-Audio Voicemeeter VAIO)
```
**These are the "loopback" devices** (marked with `<- LIKELY LOOPBACK`)

### Output - Pick ANY of these:
```
[5] Microsoft Sound Mapper - Output
[6] Speakers (Audioengine HD3)
[17] Primary Sound Driver
[20] Speakers (Audioengine HD3)
[25] SPDIF Out (Sound Blaster Audigy 5/Rx)
```
**Any output device works**

---

## If It Still Doesn't Work

### Check Device Availability
Run this to see current devices:
```bash
python list_devices.py
```

Look for:
- A real microphone (Conexant, Audigy, headset, etc.)
- A loopback device (Voicemeeter, Stereo Mix, WHAT U HEAR)
- Any speakers output

### Reboot If Needed
Device IDs can change. If devices are different:
1. Run `list_devices.py` again
2. Note the new device numbers
3. Select them in Voice Isolator
4. Try again

### Manual Configuration
If GUI selection doesn't work, you can edit `config.json`:
```json
{
  "mic_device": 1,
  "speaker_device": 15,
  "output_device": 6,
  "chunk_size": 2048,
  "sample_rate": 44100,
  "subtraction_strength": 1.0,
  "delay_compensation": 0
}
```

Then run: `python voice_isolator.py`

---

## Technical Details

### Why Device Numbers Are Important
- Device 0 might be "Microsoft Sound Mapper" (alias for default)
- Device 1 might be "Microphone (Sound Blaster)"
- Device 15 might be "Voicemeeter In 1"
- Each number points to a SPECIFIC audio device

### Why Numbers Can Change
1. **Reboot**: Windows re-enumerates devices
2. **Plugging in USB**: New device changes numbering
3. **Installing new audio driver**: Changes device order
4. **Disabling device in settings**: Removes it from list

### How Fix Prevents This
- New validation checks if device still exists
- Clear error message if device doesn't exist
- GUI refreshes device list each time it starts
- You select from currently available devices

---

## Summary

**Old behavior**: Used stale device IDs → Error  
**New behavior**: Validates devices exist → Clear error messages → Lets you pick valid ones

**Result**: No more cryptic PaErrorCode errors. Instead:
- Device not found → Tells you which one
- Try different device → Easy UI to switch
- Success → Isolation works!

---

## Next Steps

1. **Read**: FIX_AND_RUN.txt (quick start guide)
2. **Run**: `python voice_isolator.py`
3. **Select**: Microphone → Loopback → Output
4. **Click**: "Start Voice Isolation"
5. **Test**: Play audio, speak into mic
6. **Adjust**: Strength slider until right
7. **Use**: Set Discord/Teams/Zoom to output device
8. **Enjoy**: Clean voice!

---

**Questions?** See SETUP.md troubleshooting section or README.md for technical details.
