# Voice Isolator - Complete Setup Guide

## What Is This?

**Voice Isolator** is for gamers who use **speakers instead of headsets** and want to:
- Remove game/speaker audio from their microphone
- Transmit only their voice to teammates
- Avoid hearing their own voice through speakers (no echo)

## Who Should Use This?

✅ **Good Use Case:**
- Playing at home with minimal ambient noise
- Using speakers instead of headsets
- Want clean team communication
- Tired of hearing yourself in voice chat

❌ **NOT Recommended For:**
- Public/noisy environments (coffee shops, libraries)
- Situations with lots of background noise
- If you prefer headsets
- Mobile/laptop with open mics nearby

## System Requirements

- Windows 10 or 11
- Microphone
- Speakers
- Internet connection (for setup only)

## Step-by-Step Setup

### Phase 1: Install VoiceMeeter (CRITICAL!)

VoiceMeeter is free software that creates virtual audio devices Voice Isolator needs.

1. Go to: https://vb-audio.com/Voicemeeter/
2. Click "Download"
3. Run the installer
4. **RESTART YOUR PC** (important!)

After restart, VoiceMeeter will be installed and ready.

### Phase 2: Download Voice Isolator

**Option A - Use the .exe (Easiest):**
1. Download `voice_isolator.exe`
2. Save it somewhere convenient (Desktop, Documents, etc.)
3. Double-click to run (no installation needed!)

**Option B - Use Python:**
1. Install Python 3.7+ from python.org
2. Download `voice_isolator.py`
3. Open command prompt
4. Run: `python voice_isolator.py`

### Phase 3: Configure Windows Audio Routing

This step tells Windows to send game audio through VoiceMeeter.

**For Windows 11:**

1. Click Start → Settings
2. Go to: System → Sound
3. Scroll down → Click "Volume mixer"
4. Click "App volume and device preferences"
5. Find your game or browser
6. Under "Output device" → Select "VoiceMeeter Virtual Input"
7. Repeat for ANY app that plays sound (Discord, Spotify, YouTube, etc.)

**For Windows 10:**

1. Right-click speaker icon in taskbar
2. Click "Open Sound settings"
3. Click "Volume mixer"
4. Find your game/app
5. Change output device to "VoiceMeeter Virtual Input"

### Phase 4: Configure VoiceMeeter

1. Click Start → Search "VoiceMeeter"
2. Open VoiceMeeter
3. Look for "Hardware Out 1" section
4. Change dropdown to your speakers (e.g., "Speakers (Audioengine)")
5. Your game audio should now play through speakers

### Phase 5: Run Voice Isolator

1. Run `voice_isolator.exe` (or `python voice_isolator.py`)
2. The GUI will appear

### Phase 6: Select Audio Devices

You need to select THREE devices:

**1. Your Microphone:**
- Look for something like: "Microphone (Sound Blaster...)"
- Pick the one you actually use
- Click on it to select

**2. Game/Speaker Audio (Loopback):**
- This captures what's playing through speakers
- Look for:
  - "What U Hear (Sound Blaster...)" ← Try this first
  - "Stereo Mix (Conexant...)" ← Try this second
  - "Input (Voicemeeter...)" ← Try this if above don't work
- Click one to select

**3. Output (Virtual Microphone) - IMPORTANT:**
- This is where your CLEAN voice goes
- Look for: "Voicemeeter Input" or similar Voicemeeter option
- **DO NOT select your physical speakers!**
- This prevents you from hearing your own voice

### Phase 7: Start Voice Isolation

1. Click the big green button: "START - Begin Voice Isolation"
2. Wait a moment...
3. Status should change to **GREEN "RUNNING"**
4. If RED error: Try different device combinations

### Phase 8: Set Your Game/Discord Microphone

Now tell Discord/your game to use the Voicemeeter device for input:

**Discord:**
1. Discord Settings → Voice & Video
2. Microphone: Select the SAME Voicemeeter device from Phase 6
3. Microphone Volume: Adjust to comfortable level
4. Click "Check Microphone" to test

**In-Game Voice Chat:**
1. Game Settings → Audio → Microphone
2. Select the SAME Voicemeeter device
3. Adjust microphone volume

### Phase 9: Test

This is the moment of truth!

1. Start your game
2. Play some game audio (background music, effects, etc.)
3. Speak into your microphone
4. Listen to your speakers - you should **NOT hear yourself**
5. Ask a teammate: "Do you hear my voice?"
6. They should hear: **Only your voice, no game audio**

If this works → **Success!** 🎉

If not → See troubleshooting below

## Troubleshooting

### Problem: Can't find loopback device in dropdown

**Solution:**
1. Make sure VoiceMeeter is fully installed
2. Restart Voice Isolator
3. Click "Refresh Devices"
4. Try enabling "Stereo Mix":
   - Settings → Sound → Recording tab
   - Right-click "Stereo Mix" → Enable
   - Refresh Voice Isolator

### Problem: Game audio not playing through speakers

**Solution:**
1. Make sure you set game output to "VoiceMeeter Virtual Input" in Volume Mixer
2. Check VoiceMeeter Hardware Out 1 is set to your speakers
3. Open VoiceMeeter and check "A1" button is enabled

### Problem: Still hearing your own voice through speakers

**Solution:**
1. Check Output device in Voice Isolator is a **Voicemeeter option** (NOT speakers!)
2. If already correct, try a different Voicemeeter option
3. Make sure Discord/Game is set to the same Voicemeeter device

### Problem: Voice Isolator won't start (RED error)

**Solution:**
1. Click "Refresh Devices"
2. Try different Loopback option (if [33] fails, try [114], etc.)
3. Try different Output option
4. Make sure all three dropdowns have selections

### Problem: Teammates still hear game audio

**Solution:**
1. Increase the "Subtraction Strength" slider (drag right)
2. Try values: 1.2 → 1.5 → 2.0
3. Test each and ask teammates if improvement

### Problem: Your voice is too quiet

**Solution:**
1. Decrease the "Subtraction Strength" slider (drag left)
2. Try: 0.8 → 0.5
3. Check microphone volume in Windows Sound settings

## Device Selection Guide

Your system will show different device numbers. Here's what to look for:

### Good Microphone Options:
- `Microphone (Sound Blaster...)`
- `Microphone (Conexant...)`
- `Microphone (SB Audigy...)`
- `Microphone (Audio capture)`

### Good Loopback Options:
- `"What U Hear" (Sound Blaster...)`
- `Stereo Mix (Conexant...)`
- `Input (Voicemeeter...)`

### Good Output Options:
- `Voicemeeter Input`
- `Voicemeeter AUX Input`
- `Voicemeeter In 1/2/3/etc.`

**Avoid selecting:**
- Physical speakers for Output (that causes echo!)
- Multiple options of same device

## Fine-Tuning

Once it's working, you can adjust:

**Subtraction Strength:**
- **Lower (0.5)** = Less game audio removal, your voice louder
- **Normal (1.0)** = Default, works for most
- **Higher (2.0)** = Maximum game audio removal

Experiment to find what works best for your game!

## Tips & Tricks

1. **Test in quiet room first** - Easier to debug
2. **Don't shout into mic** - Causes distortion
3. **Adjust one setting at a time** - Easier to see what helps
4. **Different games may need different settings** - Adjust slider as needed
5. **Leave it running during gaming session** - Don't stop/start multiple times

## Uninstallation

Simply delete the .exe or folder. No registry changes or system files modified.

## Common Questions

**Q: Do I need to run this every time I game?**
A: Yes, start it before gaming, stop when done.

**Q: Can I minimize it while gaming?**
A: Yes, minimize the window. It will keep running.

**Q: Will this work with consoles?**
A: No, only PC with speakers.

**Q: Does this work offline?**
A: Yes, setup needs internet but usage doesn't.

**Q: Can I use this for streaming?**
A: Yes! Set your streaming software's mic to the Voicemeeter device.

## Getting Help

If setup isn't working:

1. Re-read "Troubleshooting" section
2. Check all three devices are selected and green
3. Verify VoiceMeeter is installed
4. Try a different combination of devices
5. Restart Voice Isolator and try again

---

**You're ready to game with clean voice communication!** 🎮🎤
