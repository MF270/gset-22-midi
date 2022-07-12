from cv2 import repeat
from mido import Message, MidiFile, MidiTrack
from instrument_data import best_in_family,int_classify_inst
from pathlib import Path


def remove_duplicate_tracks(mf:MidiFile):
    #duplicate tracks could mess with the reduction to a single track, this deals with those.
    message_numbers = []
    duplicates = []
    for track in mf.tracks:
        if len(track) in message_numbers:
            duplicates.append(track)
        else:
            message_numbers.append(len(track))
    for track in duplicates:
        mf.tracks.remove(track)

def slice_into_segments(mf:MidiFile,num_messages:int,output:str):
    if len(mf.tracks) > 1:
        raise Exception("Make sure your MIDI file has only one track")
    #we want to make sure we're only dealing with a single track, otherwise slicing is hard
    song_name = Path(mf.filename).stem

    if not Path(rf"{output}\{song_name}").exists():
        Path(rf"{output}\{song_name}").mkdir(parents=True)

    track = MidiTrack()
    newMidi = MidiFile()
    newMidi.tracks.append(track)
    x=1
    #x keeps track of the number of the file we're on. This is probably not the perfect way to do it but it's easy.
    repeat_messages = []
    #repeat messages will only come before notes, describing the instruments as well as the tempo
    for message in mf.tracks[0]:
        if message.type in ("note_on","note_off"):
            break
        else:
            repeat_messages.append(message)
    idx = 0
    track.extend(repeat_messages)
    for message in (mf.tracks[0]):
        if (message.type not in ("note_on","note_off")):
            continue
        #we only want to worry about notes on or off.
        track.append(message)
        idx +=1
        #should take every n notes, but just in case there are non-note messages between the notes, so idx has to be separate from the idx of the message
        if idx % num_messages == 0 and idx != 0:
            newMidi.save(rf"{output}\{song_name}\{x}.mid")
            #when we're done, we save the file and reset the track/file
            x+=1
            newMidi = MidiFile()
            track = MidiTrack()
            newMidi.tracks.append(track)
            track.extend(repeat_messages)
            #repeat_messages are needed in every file for them to sound right
        if len(mf.tracks[0]) - (idx + 1) < num_messages:
            break

def clean_on_off(mf:MidiFile):
    #all we need to do here is remove the note_on messages with vel 0, this could confuse the network
    #for some reason, some midi files on the internet use note_on messages with velocity 0, this standardizes that
    for track in mf.tracks:
        for idx,message in enumerate(track):
            if message.type == "note_on" and message.velocity == 0:
                new_message = message.__dict__
                new_message["type"] = "note_off"
                track[idx] = Message(**new_message)

def reduce_tracks(mf:MidiFile):
    instruments = set()
    tempofound = False
    final_track = MidiTrack()
    #this uses the most common instrument for each family in the entire dataset which allows us to easily reduce the number of instruments to 16
    #withoug losing *too* much information about the way the song sounds
    for idx,fam in enumerate(best_in_family):
        final_track.append(Message(type="program_change",program=fam[0],channel=idx))

    #first we note every instrument used on the track
    for idx,track in enumerate(mf.tracks):
        for message in track:
            if message.type == "program_change":
                instruments.add((idx,message.channel,message.program))
            if message.type == "set_tempo" and not(tempofound):
                final_track.append(message)
                tempofound = True
    #then we translate to the most popular in their family
    for idx,track in enumerate(mf.tracks):
        for message in track:
            if message.type in ("note_on","note_off"):
                new_message = message.__dict__
                #messages are mutable but mido convention suggests only working with copies, and the dictionary form is a good intermediary.
                new_channel = [i[2] for i in instruments if (i[0] == idx and message.channel == i[1])]
                #this categorizes the family of the instrument and therefore its channel
                if len(new_channel) == 0:
                    continue
                new_message["channel"] = int_classify_inst(new_channel[0])
                #then we edit its channel
                final_track.append(Message(**new_message))
    mf.tracks = []
    mf.tracks.append(final_track)

def process_file(path:str,output:str,num_messages:int):
    mf = MidiFile(path)
    clean_on_off(mf)
    remove_duplicate_tracks(mf)
    reduce_tracks(mf)
    slice_into_segments(mf,num_messages,output)

def process_dir(dir,output,num_messages):
    for p in Path(dir).glob("**/*.mid"):
        process_file(str(p),output,num_messages)

if __name__=="__main__":
    process_file(r"C:\PythonPrograms\gset\midi\clean_midi\Earth, Wind & Fire\September (bonus track).1.mid",r"C:\PythonPrograms\gset\midi\sliced_midi",256)