from mido import MidiFile,MidiTrack,Message,MetaMessage
from pathlib import Path
import csv
from processing import process_dir

def midi_to_csv(path,output,num_messages,name=None):
    mf = MidiFile(path,clip=True)
    if name is None:
        name = str(Path(path).parents[0]).split("\\")[-1]
    if not Path(rf"{output}\{name}").exists():
        Path(rf"{output}\{name}").mkdir(parents=True)
    #make room for the file
    messages = 0
    with open(rf"{output}\{name}\{Path(path).stem}.csv","w",newline="") as csv_out:
        note_writer = csv.writer(csv_out,delimiter=',')
        for track in mf.tracks:
            for message in track:
                #just transcribe every note, but ignore message changes because those are gonna be standardized
                if message.type == "set_tempo":
                    note_writer.writerow([message.tempo])
                elif message.type in ("note_on","note_off"):
                    message_info = [int(message.type=="note_on"),message.channel,message.note,message.velocity,message.time]
                    note_writer.writerow(message_info)
                    messages += 1
        if messages != num_messages:
            return
        #need to make sure that there are actually the right number of messages, otherwise ML breaks. So don't actually write the file if there aren't


def csv_dir(path,output,num_messages):
    for idx,p in enumerate(Path(path).glob("**/*.mid")):
        print(f"processed file {idx}")
        midi_to_csv(str(p),output,num_messages)

def midi_dir_to_csv(midi_path,midi_out,num_messages,csv_out):
    process_dir(midi_path,midi_out,num_messages)
    csv_dir(midi_out,csv_out,num_messages)

def csv_to_midi(path,output):
    mf = MidiFile()
    track = MidiTrack()
    mf.tracks.append(track)

    with open(path,"r",newline="") as csv_data:
        reader = csv.reader(csv_data,delimiter=",")
        for line in reader:
            if len(line) == 1:
                track.append(MetaMessage(type="set_tempo",tempo=int(line[0])))
            else:
                note_params = {
                    "type":("note_on" if int(line[0]) == 1 else "note_off"),
                    "note":int(line[2]),
                    "velocity":int(line[3]),
                    "time":int(line[4]),
                    "channel":int(line[1])
                    }
                track.append(Message(**note_params))
    mf.save(rf"{output}\{Path(path).stem}.mid")

if __name__ == "__main__":
    csv_dir(r"C:\PythonPrograms\gset\midi\nonmusicals",r"C:\PythonPrograms\gset\midi\csv",256)