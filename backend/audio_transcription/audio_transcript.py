import aubio
import numpy as np
import subprocess

class AudioTranscripter:
    def __init__(self, filename):
        aubio_pitch = subprocess.getoutput("aubio pitch temp_song/" + str(filename)).split()
        aubio_beat = subprocess.getoutput("aubio onset temp_song/" + str(filename)).split()
        self.filename = filename
        self.pitch = {}
        self.beat = {}
        self.tempo = subprocess.getoutput("aubio tempo temp_song/" + str(filename))

        i = 0
        while i < len(aubio_pitch):
            timestamp = "{:.2f}".format(float(aubio_pitch[i]))
            freq = float(aubio_pitch[i + 1])
            if freq > 0:
                if not timestamp in self.pitch:
                    self.pitch[timestamp] = freq
            i += 2
        i = 0
        while i < len(aubio_beat):
            timestamp = "{:.2f}".format(float(aubio_beat[i]))
            if not timestamp in self.beat:
                self.beat[timestamp] = 1
            i += 1
    
    def convert(self):
        musical_score = []
        for timestamp in self.beat:
            if timestamp in self.pitch:
                freq = self.pitch[timestamp]
                letter_note = aubio.freq2note(freq)
                musical_score.append((timestamp, letter_note))
        return (self.filename, self.tempo, musical_score)