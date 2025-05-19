import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext, messagebox
from gtts import gTTS
from pydub import AudioSegment
import os
import tempfile

class SubliminalGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Subliminal Generator")
        self.root.geometry("800x600")
        
        # Variables
        self.background_music = None
        self.background_music_path = None
        self.voice_volume = tk.DoubleVar(value=0.3)  # Default voice volume (30%)
        
        self.create_widgets()
    
    def create_widgets(self):
        # Affirmations input
        ttk.Label(self.root, text="Zadejte afirmace (jedna na řádek):").pack(pady=5)
        self.affirmations_text = scrolledtext.ScrolledText(self.root, height=10)
        self.affirmations_text.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
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
        
        # Generate button
        ttk.Button(self.root, text="Vygenerovat nahrávku", command=self.generate_subliminal).pack(pady=20)
    
    def select_background_music(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Audio files", "*.mp3 *.wav")]
        )
        if file_path:
            self.background_music_path = file_path
            self.music_path_label.config(text=os.path.basename(file_path))
    
    def generate_subliminal(self):
        # Get affirmations
        affirmations = self.affirmations_text.get("1.0", tk.END).strip().split("\n")
        if not affirmations or not affirmations[0]:
            messagebox.showerror("Chyba", "Zadejte prosím alespoň jednu afirmaci.")
            return
        
        # Create temporary directory
        with tempfile.TemporaryDirectory() as temp_dir:
            # Generate speech for each affirmation
            voice_segments = []
            for i, affirmation in enumerate(affirmations):
                if affirmation.strip():
                    tts = gTTS(text=affirmation, lang='cs')
                    temp_file = os.path.join(temp_dir, f"affirmation_{i}.mp3")
                    tts.save(temp_file)
                    voice_segments.append(AudioSegment.from_mp3(temp_file))
            
            # Combine all voice segments
            combined_voice = sum(voice_segments)
            
            # Adjust voice volume
            combined_voice = combined_voice - (20 * (1 - self.voice_volume.get()))
            
            # Process background music if selected
            if self.background_music_path:
                background = AudioSegment.from_file(self.background_music_path)
                
                # Loop background music to match voice length
                if len(background) < len(combined_voice):
                    loops_needed = len(combined_voice) // len(background) + 1
                    background = background * loops_needed
                
                # Trim background to match voice length
                background = background[:len(combined_voice)]
                
                # Mix voice and background
                final_audio = background.overlay(combined_voice)
            else:
                final_audio = combined_voice
            
            # Save the final audio
            output_path = filedialog.asksaveasfilename(
                defaultextension=".mp3",
                filetypes=[("MP3 files", "*.mp3")]
            )
            
            if output_path:
                final_audio.export(output_path, format="mp3")
                messagebox.showinfo("Úspěch", "Nahrávka byla úspěšně vygenerována!")

if __name__ == "__main__":
    root = tk.Tk()
    app = SubliminalGenerator(root)
    root.mainloop() 