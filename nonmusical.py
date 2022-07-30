from mido import Message, MidiFile, MidiTrack, MetaMessage
from random import randint, gauss,choices
from  instrument_data import best_in_family,fam_weights,families

def on_off_sequence(length,max_chord):
    #generates a sequence of random chords, always starting with ons. 
    out = []
    while (len(out) <length):
        chord_len = randint(1,max_chord)
        if 2*chord_len + len(out) > length:
            chord_len = (length - len(out))//2
        for i in range(1,-1,-1):
            for _ in range(chord_len):
                out.append(i)
    return out

def generate_nonmusical(path,max_chord=4,num_messages=256):
    mid = MidiFile(type = 1)

    track = MidiTrack()
    mid.tracks.append(track)
    bpm = int(gauss(500000,20000))
    track.append(MetaMessage(type="set_tempo",tempo=bpm,time=0))
    for idx, instrument in (enumerate(best_in_family)):
        track.append(Message(type="program_change",program=instrument[0],channel=idx))

    #this is a pretty arbitrary range but is unlikely to matter much. 
    track_vol = randint(100,120)
    message_sequence = on_off_sequence(num_messages,max_chord)
    #builds 
    open_notes = []
    for j in message_sequence:
        if j == 1:
            #generates random notes, but we store each note so that we can close notes when they're opened
            #the usage of the .pop method means that notes that are opened first are also closed first, which isn't perfect but it's a solid appoximation
            my_channel = choices(list(fam_weights.keys()),weights=list(fam_weights.values()),k=1)[0]
            my_channel = (families.index(my_channel))
            #these aren't a simple random selection because, for example, piano, is used a lot more than bird sound FX 4
            my_note = min(max(int(gauss(64,24)),0),127)
            note_params = {
                "type":"note_on",
                "note":(my_note),
                "velocity":min(int(gauss(track_vol,5)),127),
                "time":int(max(gauss(240,150),0)),
                "channel":my_channel
                }
            open_notes.append((my_note,my_channel))
            track.append(Message(**note_params))
        else:
            open_note = open_notes.pop(0)
            off_params ={
                "type":"note_off",
                "note":open_note[0],
                "velocity":0,
                "time":20,
                "channel":open_note[1]
                }
            track.append(Message(**off_params))
    mid.save(path)

def generate_n_nonmusicals(path,n,kwargs):
    for i in range(n):
        print(f"file {i+1} done")
        generate_nonmusical(fr"{path}\nonmusical{i+1}.mid",**kwargs)

