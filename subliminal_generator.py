import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext, messagebox
from gtts import gTTS
from pydub import AudioSegment
import os
import tempfile
from pygame import mixer
import threading
import shutil

class SubliminalGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Subliminal Generator")
        self.root.geometry("800x700")
        
        # Variables
        self.background_music = None
        self.background_music_path = None
        self.voice_volume = tk.DoubleVar(value=0.3)  # Default voice volume (30%)
        self.fade_in = tk.DoubleVar(value=0)  # Fade in duration in seconds
        self.fade_out = tk.DoubleVar(value=0)  # Fade out duration in seconds
        self.reverb = tk.DoubleVar(value=0)  # Reverb effect (0-1)
        self.temp_audio_path = None
        self.temp_dir = None
        
        # Initialize pygame mixer
        try:
            mixer.init()
        except Exception as e:
            messagebox.showerror("Chyba", f"Chyba při inicializaci zvuku: {str(e)}")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Affirmations input
        ttk.Label(self.root, text="Zadejte afirmace (jedna na řádek):").pack(pady=5)
        self.affirmations_text = scrolledtext.ScrolledText(self.root, height=10)
        self.affirmations_text.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
        # Effects frame
        effects_frame = ttk.LabelFrame(self.root, text="Audio efekty")
        effects_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Fade in/out
        ttk.Label(effects_frame, text="Fade in (sekundy):").grid(row=0, column=0, padx=5, pady=5)
        ttk.Scale(effects_frame, from_=0, to=5, variable=self.fade_in, orient=tk.HORIZONTAL).grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(effects_frame, text="Fade out (sekundy):").grid(row=1, column=0, padx=5, pady=5)
        ttk.Scale(effects_frame, from_=0, to=5, variable=self.fade_out, orient=tk.HORIZONTAL).grid(row=1, column=1, padx=5, pady=5)
        
        # Reverb effect
        ttk.Label(effects_frame, text="Reverb:").grid(row=2, column=0, padx=5, pady=5)
        ttk.Scale(effects_frame, from_=0, to=1, variable=self.reverb, orient=tk.HORIZONTAL).grid(row=2, column=1, padx=5, pady=5)
        
        # Background music selection
        ttk.Label(self.root, text="Zvukový podkres:").pack(pady=5)
        self.music_frame = ttk.Frame(self.root)
        self.music_frame.pack(fill=tk.X, padx=10)
        
        self.music_path_label = ttk.Label(self.music_frame, text="Žádný soubor vybrán")
        self.music_path_label.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(self.music_frame, text="Vybrat hudbu", command=self.select_background_music).pack(side=tk.RIGHT)
        
        # Voice volume control
        ttk.Label(self.root, text="Hlasitost hlasu:").pack(pady=5)
        self.volume_scale = ttk.Scale(self.root, from_=0, to=1, variable=self.voice_volume, orient=tk.HORIZONTAL)
        self.volume_scale.pack(fill=tk.X, padx=10)
        
        # Preview and save buttons
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=10)
        
        self.preview_button = ttk.Button(button_frame, text="Náhled nahrávky", command=self.preview_audio, state=tk.DISABLED)
        self.preview_button.pack(side=tk.LEFT, padx=5)
        
        self.save_button = ttk.Button(button_frame, text="Uložit nahrávku", command=self.save_audio, state=tk.DISABLED)
        self.save_button.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(button_frame, text="Vygenerovat nahrávku", command=self.generate_subliminal).pack(side=tk.LEFT, padx=5)
    
    def select_background_music(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Audio files", "*.mp3 *.wav")]
        )
        if file_path:
            self.background_music_path = file_path
            self.music_path_label.config(text=os.path.basename(file_path))
    
    def apply_effects(self, audio):
        # Apply fade in
        if self.fade_in.get() > 0:
            audio = audio.fade_in(int(self.fade_in.get() * 1000))
        
        # Apply fade out
        if self.fade_out.get() > 0:
            audio = audio.fade_out(int(self.fade_out.get() * 1000))
        
        # Apply reverb (simple implementation)
        if self.reverb.get() > 0:
            reverb_strength = int(self.reverb.get() * 100)
            reverb_audio = audio - reverb_strength
            reverb_audio = reverb_audio.set_frame_rate(44100)
            audio = audio.overlay(reverb_audio, position=100)
        
        return audio
    
    def generate_subliminal(self):
        # Get affirmations
        affirmations = self.affirmations_text.get("1.0", tk.END).strip().split("\n")
        if not affirmations or not affirmations[0]:
            messagebox.showerror("Chyba", "Zadejte prosím alespoň jednu afirmaci.")
            return
        
        try:
            # Create temporary directory if it doesn't exist
            if self.temp_dir is None:
                self.temp_dir = tempfile.mkdtemp()
            
            # Generate speech for each affirmation
            voice_segments = []
            for i, affirmation in enumerate(affirmations):
                if affirmation.strip():
                    tts = gTTS(text=affirmation, lang='cs')
                    temp_file = os.path.join(self.temp_dir, f"affirmation_{i}.mp3")
                    tts.save(temp_file)
                    voice_segments.append(AudioSegment.from_mp3(temp_file))
            
            # Combine all voice segments
            combined_voice = sum(voice_segments)
            
            # Adjust voice volume
            voice_volume_db = -20 * (1 - self.voice_volume.get())
            combined_voice = combined_voice + voice_volume_db
            
            # Process background music if selected
            if self.background_music_path:
                try:
                    background = AudioSegment.from_file(self.background_music_path)
                    
                    # Reduce background music volume by 10dB
                    background = background - 10
                    
                    # Loop background music to match voice length
                    if len(background) < len(combined_voice):
                        loops_needed = len(combined_voice) // len(background) + 1
                        background = background * loops_needed
                    
                    # Trim background to match voice length
                    background = background[:len(combined_voice)]
                    
                    # Mix voice and background
                    final_audio = background.overlay(combined_voice)
                except Exception as e:
                    messagebox.showerror("Chyba", f"Chyba při zpracování hudby: {str(e)}")
                    return
            else:
                final_audio = combined_voice
            
            # Apply effects
            final_audio = self.apply_effects(final_audio)
            
            # Save to temporary file
            self.temp_audio_path = os.path.join(self.temp_dir, "preview.mp3")
            final_audio.export(self.temp_audio_path, format="mp3")
            
            # Enable preview and save buttons
            self.preview_button.config(state=tk.NORMAL)
            self.save_button.config(state=tk.NORMAL)
            
            messagebox.showinfo("Úspěch", "Nahrávka byla úspěšně vygenerována! Můžete si ji poslechnout nebo uložit.")
            
        except Exception as e:
            messagebox.showerror("Chyba", f"Došlo k chybě při generování nahrávky: {str(e)}")
    
    def preview_audio(self):
        if self.temp_audio_path and os.path.exists(self.temp_audio_path):
            try:
                # Stop any currently playing audio
                mixer.music.stop()
                # Load and play the new audio
                mixer.music.load(self.temp_audio_path)
                mixer.music.play()
            except Exception as e:
                messagebox.showerror("Chyba", f"Chyba při přehrávání: {str(e)}")
    
    def save_audio(self):
        if self.temp_audio_path and os.path.exists(self.temp_audio_path):
            output_path = filedialog.asksaveasfilename(
                defaultextension=".mp3",
                filetypes=[("MP3 files", "*.mp3")]
            )
            
            if output_path:
                try:
                    # Copy the temporary file to the selected location
                    shutil.copy2(self.temp_audio_path, output_path)
                    messagebox.showinfo("Úspěch", "Nahrávka byla úspěšně uložena!")
                except Exception as e:
                    messagebox.showerror("Chyba", f"Chyba při ukládání: {str(e)}")
    
    def __del__(self):
        # Clean up temporary directory when the application is closed
        if self.temp_dir and os.path.exists(self.temp_dir):
            try:
                shutil.rmtree(self.temp_dir)
            except:
                pass

if __name__ == "__main__":
    root = tk.Tk()
    app = SubliminalGenerator(root)
    root.mainloop() 