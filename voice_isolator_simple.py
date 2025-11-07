"""
Voice Isolator - SIMPLIFIED VERSION
Real-time speaker output removal from microphone
"""

import numpy as np
import threading
import queue
from collections import deque
import tkinter as tk
from tkinter import ttk, messagebox
import sounddevice as sd
import json
import os

class VoiceIsolator:
    """Core audio processing engine"""
    
    def __init__(self, mic_device, speaker_device, output_device, sample_rate=44100, chunk_size=2048):
        self.mic_device = mic_device
        self.speaker_device = speaker_device
        self.output_device = output_device
        self.sample_rate = sample_rate
        self.chunk_size = chunk_size
        
        self.running = False
        self.enabled = False
        self.subtraction_strength = 1.0
        self.delay_compensation = 0
        
        self.audio_queue = queue.Queue(maxsize=5)
        self.speaker_queue = queue.Queue(maxsize=5)
        
        self.mic_stream = None
        self.speaker_stream = None
        self.output_stream = None
        
    def _mic_callback(self, indata, frames, time, status):
        """Microphone input callback"""
        try:
            audio = indata[:, 0] if indata.ndim > 1 else indata
            try:
                self.audio_queue.put_nowait(audio.copy().astype(np.float32))
            except queue.Full:
                pass
        except Exception as e:
            print(f"Mic callback error: {e}")
    
    def _speaker_callback(self, indata, frames, time, status):
        """Speaker loopback callback"""
        try:
            audio = indata[:, 0] if indata.ndim > 1 else indata
            try:
                self.speaker_queue.put_nowait(audio.copy().astype(np.float32))
            except queue.Full:
                pass
        except Exception as e:
            print(f"Speaker callback error: {e}")
    
    def _output_callback(self, outdata, frames, time, status):
        """Output callback"""
        try:
            try:
                processed = self.audio_queue.get(timeout=0.01)
                if outdata.ndim == 1:
                    outdata[:] = processed[:len(outdata)]
                else:
                    outdata[:, 0] = processed[:len(outdata)]
            except queue.Empty:
                outdata[:] = 0
        except Exception as e:
            print(f"Output error: {e}")
            outdata[:] = 0
    
    def process_audio(self):
        """Main processing loop"""
        speaker_buffer = deque(maxlen=self.sample_rate)
        
        while self.running:
            try:
                mic_audio = self.audio_queue.get(timeout=0.1)
                
                # Get latest speaker audio
                try:
                    while True:
                        speaker_audio = self.speaker_queue.get_nowait()
                        speaker_buffer.append(speaker_audio)
                except queue.Empty:
                    pass
                
                if self.enabled and len(speaker_buffer) > 0:
                    # Combine speaker buffer
                    speaker_combined = np.concatenate(list(speaker_buffer))
                    
                    # Align lengths
                    min_len = min(len(mic_audio), len(speaker_combined))
                    mic_audio = mic_audio[:min_len]
                    speaker_combined = speaker_combined[:min_len]
                    
                    # Subtract
                    cleaned = mic_audio - (speaker_combined * self.subtraction_strength)
                    cleaned = np.tanh(cleaned)
                else:
                    cleaned = mic_audio
                
                try:
                    self.audio_queue.put_nowait(cleaned)
                except queue.Full:
                    pass
                    
            except queue.Empty:
                continue
            except Exception as e:
                print(f"Error: {e}")
    
    def start(self):
        """Start audio streams"""
        try:
            print(f"Starting with: Mic={self.mic_device}, Speaker={self.speaker_device}, Output={self.output_device}")
            
            self.mic_stream = sd.InputStream(
                device=self.mic_device,
                samplerate=self.sample_rate,
                channels=1,
                blocksize=self.chunk_size,
                callback=self._mic_callback
            )
            self.mic_stream.start()
            
            self.speaker_stream = sd.InputStream(
                device=self.speaker_device,
                samplerate=self.sample_rate,
                channels=1,
                blocksize=self.chunk_size,
                callback=self._speaker_callback
            )
            self.speaker_stream.start()
            
            self.output_stream = sd.OutputStream(
                device=self.output_device,
                samplerate=self.sample_rate,
                channels=1,
                blocksize=self.chunk_size,
                callback=self._output_callback
            )
            self.output_stream.start()
            
            self.running = True
            threading.Thread(target=self.process_audio, daemon=True).start()
            
            print("✓ Started successfully")
            return True
            
        except Exception as e:
            print(f"Start error: {e}")
            messagebox.showerror("Error", f"Failed to start:\n{e}")
            self.stop()
            return False
    
    def stop(self):
        """Stop audio"""
        self.running = False
        for stream in [self.mic_stream, self.speaker_stream, self.output_stream]:
            if stream:
                try:
                    stream.stop()
                    stream.close()
                except:
                    pass
        print("✓ Stopped")


class GUI:
    """Simple GUI"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Isolator - Speaker Output Remover")
        self.root.geometry("600x500")
        
        self.isolator = None
        
        # Title
        ttk.Label(root, text="Voice Isolator", font=("Arial", 14, "bold")).pack(pady=10)
        ttk.Label(root, text="Real-time speaker audio removal").pack()
        
        # Devices frame
        dev_frame = ttk.LabelFrame(root, text="Select Audio Devices", padding=10)
        dev_frame.pack(fill=tk.BOTH, padx=10, pady=10)
        
        ttk.Label(dev_frame, text="Microphone:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.mic_var = tk.StringVar()
        self.mic_combo = ttk.Combobox(dev_frame, textvariable=self.mic_var, state="readonly", width=50)
        self.mic_combo.grid(row=0, column=1, sticky=tk.W)
        
        ttk.Label(dev_frame, text="Speaker Loopback:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.speaker_var = tk.StringVar()
        self.speaker_combo = ttk.Combobox(dev_frame, textvariable=self.speaker_var, state="readonly", width=50)
        self.speaker_combo.grid(row=1, column=1, sticky=tk.W)
        
        ttk.Label(dev_frame, text="Output Device:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.output_var = tk.StringVar()
        self.output_combo = ttk.Combobox(dev_frame, textvariable=self.output_var, state="readonly", width=50)
        self.output_combo.grid(row=2, column=1, sticky=tk.W)
        
        # Control frame
        ctrl_frame = ttk.LabelFrame(root, text="Controls", padding=10)
        ctrl_frame.pack(fill=tk.BOTH, padx=10, pady=10)
        
        self.start_btn = ttk.Button(ctrl_frame, text="Start Voice Isolation", command=self.toggle)
        self.start_btn.pack(fill=tk.X, pady=10)
        
        self.status_label = ttk.Label(ctrl_frame, text="Status: STOPPED", foreground="red", font=("Arial", 11, "bold"))
        self.status_label.pack()
        
        # Settings frame
        set_frame = ttk.LabelFrame(root, text="Settings", padding=10)
        set_frame.pack(fill=tk.BOTH, padx=10, pady=10)
        
        ttk.Label(set_frame, text="Subtraction Strength:").grid(row=0, column=0, sticky=tk.W)
        self.strength_var = tk.DoubleVar(value=1.0)
        ttk.Scale(set_frame, from_=0.5, to=2.0, variable=self.strength_var, command=self.update_strength).grid(row=0, column=1, sticky=tk.EW)
        self.strength_label = ttk.Label(set_frame, text="1.0")
        self.strength_label.grid(row=0, column=2, padx=5)
        
        # Buttons
        ttk.Button(root, text="Refresh Devices", command=self.refresh_devices).pack(pady=5)
        
        self.refresh_devices()
    
    def refresh_devices(self):
        """Load and display devices"""
        try:
            devices = sd.query_devices()
            
            mics = []
            speakers = []
            outputs = []
            
            for i, dev in enumerate(devices):
                name_lower = dev['name'].lower()
                
                # Microphones
                if dev['max_input_channels'] > 0 and any(k in name_lower for k in ['microphone', 'mic', 'capture']):
                    mics.append(f"[{i}] {dev['name']}")
                
                # Loopback/Input devices (must have INPUT channels)
                if dev['max_input_channels'] > 0 and any(k in name_lower for k in ['input (', 'voicemeeter', 'stereo mix', 'what u hear']):
                    speakers.append(f"[{i}] {dev['name']}")
                
                # Output devices
                if dev['max_output_channels'] > 0:
                    outputs.append(f"[{i}] {dev['name']}")
            
            self.mic_combo['values'] = mics
            self.speaker_combo['values'] = speakers
            self.output_combo['values'] = outputs
            
            if mics:
                self.mic_combo.current(0)
            if speakers:
                self.speaker_combo.current(0)
            if outputs:
                self.output_combo.current(0)
            
            print(f"Found {len(mics)} mics, {len(speakers)} loopbacks, {len(outputs)} outputs")
            
        except Exception as e:
            messagebox.showerror("Error", f"Device refresh failed: {e}")
    
    def update_strength(self, value):
        """Update strength display and value"""
        val = float(value)
        self.strength_label.config(text=f"{val:.2f}")
        if self.isolator:
            self.isolator.subtraction_strength = val
    
    def toggle(self):
        """Start/stop"""
        if not self.isolator or not self.isolator.running:
            try:
                mic_str = self.mic_combo.get()
                speaker_str = self.speaker_combo.get()
                output_str = self.output_combo.get()
                
                if not all([mic_str, speaker_str, output_str]):
                    messagebox.showerror("Error", "Select all three devices")
                    return
                
                mic_id = int(mic_str.split('[')[1].split(']')[0])
                speaker_id = int(speaker_str.split('[')[1].split(']')[0])
                output_id = int(output_str.split('[')[1].split(']')[0])
                
                self.isolator = VoiceIsolator(mic_id, speaker_id, output_id)
                self.isolator.subtraction_strength = self.strength_var.get()
                
                if self.isolator.start():
                    self.isolator.enabled = True
                    self.start_btn.config(text="Stop Voice Isolation")
                    self.status_label.config(text="Status: RUNNING", foreground="green")
                else:
                    self.isolator = None
                    
            except Exception as e:
                messagebox.showerror("Error", f"Failed to start: {e}")
        else:
            self.isolator.enabled = False
            self.isolator.stop()
            self.isolator = None
            self.start_btn.config(text="Start Voice Isolation")
            self.status_label.config(text="Status: STOPPED", foreground="red")


if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()
