from mido import Message, MidiFile, MidiTrack
from random import randint, gauss, choices,choice
from  instrument_data import instrument_weights_usable

def generate_nonmusical(path,num_tracks=4,num_instruments=3,num_messages=16):
    mid = MidiFile(type = 1)

    track = MidiTrack()
    mid.tracks.append(track)
    
    
    track.append(Message(type="note_on",note=64,velocity=120,time=0,channel=1))
    track.append(Message(type="note_on",note=68,velocity=120,time=30,channel=2))

    mid.save(path)

def generate_n_nonmusicals(path,n,kwargs):
    for i in range(n):
        print(f"file {i+1} done")
        generate_nonmusical(fr"{path}\nonmusical{i+1}.mid",**kwargs)

if __name__ == "__main__":
    generate_n_nonmusicals(r"C:\PythonPrograms\gset\midi\tests",1,{"num_tracks":1,"num_instruments":3,"num_messages":1})