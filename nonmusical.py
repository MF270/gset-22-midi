from mido import Message, MidiFile, MidiTrack
from random import randint, gauss, choices,choice,sample
from  instrument_data import instrument_weights_usable

def on_off_sequence(length,max_chord):
    out = []
    while (len(out) <length):
        chord_len = randint(1,max_chord)
        if chord_len + len(out) > length:
            chord_len = length - len(out)
        for i in range(1,-1,-1):
            for _ in range(chord_len):
                out.append(i)
    return out







def generate_nonmusical(path,max_chord=4,num_instruments=3,num_notes=16):
    mid = MidiFile(type = 1)

    track = MidiTrack()
    instruments = choices(list(instrument_weights_usable.keys()),weights=list(instrument_weights_usable.values()),k=3)
    mid.tracks.append(track)

    for idx,instrument in enumerate(instruments):
        track.append(Message('program_change', program=instrument, time=0,channel=idx))

    track_vol = randint(100,120)
    mult_messages = [on_off_sequence(2*num_notes,max_chord) for _ in range(num_instruments)]
    
    for i in range(len(instruments)):
        open_notes = []
        seq = mult_messages[i]
        for j in seq:
            if j == 1:
                my_note = min(max(int(gauss(64,24)),0),127)
                note_params = {
                    "type":"note_on",
                    "note":(my_note),
                    "velocity":min(int(gauss(track_vol,5)),127),
                    "time":int(max(gauss(240,150),0)),
                    "channel":i
                    }
                open_notes.append(my_note)
                track.append(Message(**note_params))
            else:
                off_params ={
                    "type":"note_off",
                    "note":(open_notes.pop(0)),
                    "velocity":0,
                    "time":20,
                    "channel":i
                    }
                track.append(Message(**off_params))

    mid.save(path)

def generate_n_nonmusicals(path,n,kwargs):
    for i in range(n):
        print(f"file {i+1} done")
        generate_nonmusical(fr"{path}\nonmusical{i+1}.mid",**kwargs)

if __name__ == "__main__":
    generate_n_nonmusicals(r"C:\PythonPrograms\gset\midi\nonmusicals",1000,{"max_chord":4,"num_instruments":3,"num_notes":16})
    