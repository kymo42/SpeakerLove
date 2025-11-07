# Voice Isolator - File Structure & Usage Guide

## Main Application Files

### 🎯 **To Get Started:**
1. **QUICK_START.md** - Read this first (5 minute overview)
2. **run.bat** - Double-click to launch the application
3. **list_devices.py** - Run to see your audio devices

### 📖 **For Detailed Help:**
- **SETUP.md** - Complete setup with troubleshooting
- **README.md** - Full technical documentation
- **FILES_GUIDE.md** - This file

---

## File-by-File Description

### Program Files (Core Application)

| File | Purpose |
|------|---------|
| `voice_isolator.py` | Main application with GUI - the core program |
| `run.bat` | Double-click to start Voice Isolator |
| `setup.bat` | Installs required Python packages |
| `list_devices.py` | Lists all audio devices (helps identify correct device IDs) |
| `config.json` | Stores your settings (auto-created after first run) |
| `requirements.txt` | List of Python packages needed |

### Documentation Files

| File | When to Use |
|------|------------|
| **QUICK_START.md** | First time? Read this (5 minutes) |
| **SETUP.md** | Need detailed setup instructions? Read this |
| **README.md** | Want full technical details? Read this |
| **FILES_GUIDE.md** | Lost? You're reading it now! |

---

## Getting Started (3 Steps)

### Step 1: Read Quick Start
```
Open: QUICK_START.md
Time: 5 minutes
Result: Understand what you need
```

### Step 2: Setup Prerequisites
```
Task: Install VB-Audio VoiceMeeter
Link: https://vb-audio.com/Voicemeeter/
Time: 5 minutes
Important: Restart PC after install
```

### Step 3: Run the Application
```
Double-click: run.bat
Or run: python voice_isolator.py
Result: GUI application launches
```

---

## Common Tasks

### "I want to see my audio devices"
```bash
python list_devices.py
```
This shows you which device numbers to use.

### "I want to start the app"
```
Double-click: run.bat
```
Or from command prompt:
```bash
python voice_isolator.py
```

### "I want to reinstall packages"
```bash
setup.bat
```

### "I want to adjust settings manually"
1. Stop the application
2. Edit: `config.json`
3. Restart the application

### "I want more information"
- **Quick overview**: QUICK_START.md
- **Setup help**: SETUP.md  
- **Technical details**: README.md

---

## Typical Workflow

```
1. Open QUICK_START.md
   ↓
2. Install VoiceMeeter (if not already)
   ↓
3. Double-click run.bat
   ↓
4. Select your devices in the GUI
   ↓
5. Click "Start Voice Isolation"
   ↓
6. Adjust sliders until happy
   ↓
7. Set Discord/Teams/Zoom to use output device
   ↓
8. Test with a friend - they should hear only your voice!
```

---

## Configuration (config.json)

After first run, a file called `config.json` is created. It looks like:

```json
{
  "mic_device": 50,
  "speaker_device": 42,
  "output_device": 6,
  "chunk_size": 2048,
  "sample_rate": 44100,
  "subtraction_strength": 1.0,
  "delay_compensation": 0
}
```

**You can edit these values** to fine-tune performance:
- Lower chunk_size = lower latency but higher CPU
- Adjust subtraction_strength = 0.5 to 2.0 (1.0 is default)
- delay_compensation = 0 to 1000 (for timing adjustment)

---

## Troubleshooting Quick Reference

| Problem | Solution |
|---------|----------|
| Can't find speaker loopback | Install VoiceMeeter, restart PC |
| Speaker audio still comes through | Increase subtraction_strength slider |
| Your voice is quiet | Decrease subtraction_strength slider |
| No output audio | Check device selection, check app microphone settings |
| High CPU usage | Increase chunk_size in config.json |
| Latency too high | Decrease chunk_size in config.json |

For more help: See **SETUP.md**

---

## File Locations

```
C:\Users\0\VoiceIsolator\
├── voice_isolator.py          (Main app - DO NOT DELETE)
├── run.bat                     (Launch button - Double-click)
├── setup.bat                   (Package installer)
├── list_devices.py             (Device finder)
├── requirements.txt            (Package list)
├── config.json                 (Auto-created, stores settings)
├── QUICK_START.md              (Start here!)
├── SETUP.md                    (Detailed setup)
├── README.md                   (Full documentation)
└── FILES_GUIDE.md              (This file)
```

---

## Quick Reference Commands

### Launch the application
```bash
run.bat
# or
python voice_isolator.py
```

### List your audio devices
```bash
python list_devices.py
```

### Reinstall Python packages
```bash
setup.bat
```

### Check Python is installed
```bash
python --version
```

---

## Next Steps

1. ✅ You've found this guide
2. → Open **QUICK_START.md** next
3. → Then install **VoiceMeeter**
4. → Then run **run.bat**
5. → Then follow the GUI

---

## Need Help?

**Something not working?**
1. Check **SETUP.md** troubleshooting section
2. Run: `python list_devices.py` to verify devices
3. Make sure VoiceMeeter is installed
4. Verify device selection in the GUI
5. Try adjusting the sliders

**Want more info?**
- Read **README.md** for technical details
- Read **SETUP.md** for complete setup guide

---

## Summary

This is a **Voice Isolator** - it removes everything your speakers output from your microphone input. Simple mathematics does the heavy lifting!

**All you need to do:**
1. Install VoiceMeeter
2. Double-click run.bat
3. Select devices
4. Adjust sliders
5. Use in Discord/Teams/Zoom
6. Enjoy clean voice without speaker audio!

---

**Questions? See SETUP.md or README.md for comprehensive guides!**
