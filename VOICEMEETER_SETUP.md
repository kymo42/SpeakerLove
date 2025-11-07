# VoiceMeeter Configuration Guide

## Current Situation
✓ VoiceMeeter is installed  
✓ You can select Voicemeeter devices in Voice Isolator  
✓ Stereo Mix / other loopback is NOT available

This is **PERFECT** - VoiceMeeter IS the loopback you need!

---

## How VoiceMeeter Works

VoiceMeeter creates **virtual audio routing**. Think of it like this:

```
Applications (Discord, YouTube, Music)
           ↓
    VoiceMeeter (routes audio)
           ↓
    Your Physical Speakers
           ↓
    Microphone picks it up
```

**Voice Isolator captures what VoiceMeeter is playing**, then removes it from your microphone.

---

## The Setup You Need

### Part 1: Configure VoiceMeeter

1. **Open VoiceMeeter** (find it in Start menu or taskbar)

2. You'll see this interface:
```
┌─────────────────────────────────────┐
│  VoiceMeeter Control Panel          │
├─────────────────────────────────────┤
│  LEFT SIDE (Inputs):                │
│  • Hardware In 1 (your microphone)  │
│  • Hardware In 2                    │
│  • Virtual Input                    │
│                                     │
│  MIDDLE (Main Mix & Aux):           │
│  • A1, A2, A3 (outputs)             │
│  • B1, B2 (aux outputs)             │
│                                     │
│  RIGHT SIDE (Outputs):              │
│  • Hardware Out 1 (speakers)        │
│  • VoiceMeeter Aux Output           │
│  • VoiceMeeter VAIO 3               │
└─────────────────────────────────────┘
```

3. **Set Hardware Out 1** to your speakers:
   - Look for dropdown under "Hardware Out 1"
   - Select your speaker device (Audioengine, Sound Blaster, etc.)

4. **Critical**: Route applications through VoiceMeeter:
   - In Windows Volume Mixer (Settings → Sound → Volume mixer)
   - For EACH app (Discord, YouTube, etc.)
   - Set output to: **VoiceMeeter Virtual Input**

---

## Voice Isolator Setup

With VoiceMeeter routing audio:

### Device Selection in Voice Isolator:

```
Microphone:        [Your real microphone]
                   Example: [1] Microphone (Sound Blaster)

Speaker Loopback:  [Voicemeeter input device]
                   Example: [15] Voicemeeter In 1
                   OR:      [56] Voicemeeter In 1 (VB-Audio...)

Output:            [Any output device]
                   Example: [6] Speakers (Audioengine HD3)
```

---

## Step-by-Step VoiceMeeter Configuration

### Step 1: Set Physical Outputs
```
In VoiceMeeter:

Hardware Out 1:
  └─ Click dropdown
  └─ Select: Your speakers (e.g., "Audioengine HD3")

This makes your speakers work with VoiceMeeter
```

### Step 2: Route Apps to VoiceMeeter
```
In Windows Settings:

1. Open: Settings → Sound → Volume mixer → Advanced

2. For EACH application (Discord, Chrome, Spotify, etc.):
   - Find the app name
   - Click dropdown next to it
   - Select: VoiceMeeter Virtual Input
   - This sends app audio TO VoiceMeeter

3. Now VoiceMeeter receives all your app audio
```

### Step 3: VoiceMeeter Sends to Speakers
```
In VoiceMeeter:

Click "A1" button (at bottom of faders)
└─ This enables output to Hardware Out 1 (your speakers)

Now:
YouTube → VoiceMeeter → Hardware Out 1 → Your Speakers
```

### Step 4: Voice Isolator Captures From VoiceMeeter
```
When you start Voice Isolator:

Speaker Loopback: [15] Voicemeeter In 1 (or similar)
└─ This CAPTURES what VoiceMeeter is playing
└─ Voice Isolator removes it from microphone

Microphone: [1] Your actual microphone
└─ Picks up: Your voice + Voicemeeter audio

Result: Clean voice output
```

---

## The Complete Flow

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  Discord, YouTube, Spotify, etc. (Applications)        │
│              ↓                                          │
│        [Set to: VoiceMeeter Virtual Input]             │
│              ↓                                          │
│        VoiceMeeter (Audio Router)                       │
│              ↓                                          │
│        [A1 output enabled]                             │
│              ↓                                          │
│        Hardware Out 1 → Your Speakers                  │
│              ↓                                          │
│        Room/Air                                         │
│              ↓                                          │
│        Your Microphone (picks up everything)            │
│    ┌────────────────────────────────────────┐          │
│    │ Contains:                              │          │
│    │ • Your voice                           │          │
│    │ • Speaker audio (from VoiceMeeter)    │          │
│    │ • Room noise                           │          │
│    └────────────────────────────────────────┘          │
│              ↓                                          │
│    Voice Isolator captures TWO streams:               │
│    1. Microphone input (your voice + speaker audio)   │
│    2. VoiceMeeter input (speaker audio being played)  │
│              ↓                                          │
│    Math: Clean Voice = Mic - VoiceMeeter Audio        │
│              ↓                                          │
│    Output Device (Virtual Microphone)                  │
│              ↓                                          │
│    Discord/Teams/Zoom (receives ONLY your voice)      │
│              ↓                                          │
│    Friends hear: CLEAN VOICE (no background audio!)   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## Device Selection for Your System

Based on your device list, use these:

```
Microphone:
  [1] Microphone (Sound Blaster Audigy 5/Rx)
  [13] Microphone (Sound Blaster Audigy 5/Rx)
  [32] Microphone (Sound Blaster Audigy 5/Rx)
  [50] Microphone (SB Audigy 5/Rx)
  
  Pick any ONE of these (your actual microphone)

Speaker Loopback (VoiceMeeter options):
  [15] Voicemeeter In 1 (VB-Audio Voicemeeter VAIO)
  [46] Voicemeeter Input (VB-Audio Voicemeeter VAIO)
  [49] Voicemeeter AUX Input (VB-Audio Voicemeeter VAIO)
  [56] Voicemeeter In 1 (VB-Audio...) - 48kHz version
  [59] Voicemeeter Input (VB-Audio...) - 48kHz version
  [62] Voicemeeter AUX Input (VB-Audio...) - 48kHz version
  
  Pick ANY ONE - they all work!
  (Lower latency ones marked "3.0ms" are best)

Output (where clean voice goes):
  [5] Microsoft Sound Mapper - Output
  [6] Speakers (Audioengine HD3)
  [13] Microsoft Sound Mapper - Output
  [17] Primary Sound Driver
  [20] Speakers (Audioengine HD3)
  
  Pick any speakers device
```

---

## Recommended Configuration

**Start with this:**
```
Microphone:        [1] Microphone (Sound Blaster Audigy 5/Rx)
Speaker Loopback:  [56] Voicemeeter In 1 (VB-Audio...) [48000Hz, 2ms latency - BEST]
Output:            [6] Speakers (Audioengine HD3)
```

**If that doesn't work, try:**
```
Microphone:        [50] Microphone (SB Audigy 5/Rx)
Speaker Loopback:  [15] Voicemeeter In 1 (VB-Audio...)
Output:            [20] Speakers (Audioengine HD3)
```

---

## Testing the Setup

### Test 1: VoiceMeeter Audio Flow
1. Open VoiceMeeter
2. Play YouTube in browser
3. Set YouTube output to: VoiceMeeter Virtual Input (in Volume Mixer)
4. You should hear YouTube through your speakers
5. If yes: VoiceMeeter is routing correctly ✓

### Test 2: Voice Isolator Captures
1. Start Voice Isolator with your device selection
2. Click "Start Voice Isolation"
3. Play YouTube
4. Speak into microphone
5. Adjust "Subtraction Strength" slider
6. You should hear ONLY your voice (no YouTube) ✓

### Test 3: Discord Test
1. Start Voice Isolator
2. Open Discord and set input to output device
3. Have friend join voice channel
4. Play YouTube through speakers
5. Speak into microphone
6. Friend should hear ONLY your voice ✓

---

## Troubleshooting

### YouTube/Music Not Playing
**Problem:** App audio not coming through speakers

**Solution:**
1. Check Windows Volume Mixer (Settings → Sound → Volume mixer → Advanced)
2. For the app, set output to: VoiceMeeter Virtual Input
3. In VoiceMeeter, enable "A1" output button
4. Test again

### Still Hearing Background Audio
**Problem:** Speaker audio coming through to Discord

**Solution:**
1. Increase "Subtraction Strength" slider to 1.5-2.0
2. Make sure VoiceMeeter is actually playing audio (test with YouTube)
3. Check that you selected the right Voicemeeter input in Voice Isolator

### No Audio in VoiceMeeter
**Problem:** VoiceMeeter shows no activity

**Solution:**
1. Restart VoiceMeeter
2. Check Hardware Out 1 is set to your speakers
3. Make sure apps are set to VoiceMeeter Virtual Input
4. Check Volume Mixer settings

### Wrong Device Selected
**Problem:** Voice Isolator shows error when starting

**Solution:**
1. Run: `python list_devices.py`
2. Find a Voicemeeter device (has "Voicemeeter" in name)
3. Use that [ID] number in Speaker Loopback dropdown
4. Try starting again

---

## Quick Setup Checklist

- [ ] VoiceMeeter is installed
- [ ] VoiceMeeter Hardware Out 1 = Your speakers
- [ ] YouTube/apps set to "VoiceMeeter Virtual Input" in Volume Mixer
- [ ] VoiceMeeter A1 button is ON (enabled)
- [ ] Voice Isolator Microphone = Real microphone [1]
- [ ] Voice Isolator Speaker Loopback = Voicemeeter In [15 or 56 or 62]
- [ ] Voice Isolator Output = Speakers [6 or 20]
- [ ] Voice Isolator "Start" button shows "RUNNING (GREEN LIGHT)"
- [ ] Discord/Teams/Zoom set to Voice Isolator output device
- [ ] Test: YouTube + Voice = Only voice transmitted ✓

---

## Advanced Tips

### Lower Latency
Use Voicemeeter devices marked with lowest latency:
- 2.0ms devices are best (marked "Voicemeeter In 1 48000Hz")
- 3.0ms devices are also good
- Avoid 90ms+ devices (high latency)

### Lower CPU Usage
- Use 44100Hz devices instead of 48000Hz if available
- In Voice Isolator config.json, increase chunk_size to 4096

### Better Audio Quality
- Use 48000Hz devices (marked 48000Hz in device list)
- In Voice Isolator config.json, set: "sample_rate": 48000

---

## Summary

You have VoiceMeeter - that's **perfect**!

The setup is:
1. ✓ Apps play audio → VoiceMeeter
2. ✓ VoiceMeeter sends to your speakers
3. ✓ Your mic picks up the speaker audio
4. ✓ Voice Isolator captures from Voicemeeter input
5. ✓ Voice Isolator subtracts it from microphone
6. ✓ Result: Clean voice only!

**Next step:** Configure VoiceMeeter following steps above, then start Voice Isolator!

---

**Questions?** See SETUP.md or README.md for more details.
