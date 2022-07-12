from mido import MidiFile
from pathlib import Path
import csv
from processing import process_dir

def midi_to_csv(path,output,name=None):
    mf = MidiFile(path)
    if name is None:
        name = str(Path(path).parents[0]).split("\\")[-1]
    if not Path(rf"{output}\{name}").exists():
        Path(rf"{output}\{name}").mkdir(parents=True)

    with open(rf"{output}\{name}\{Path(path).stem}.csv","w",newline="") as csv_out:
        note_writer = csv.writer(csv_out,delimiter=',')
        for track in mf.tracks:
            for message in track:
                if message.type == "set_tempo":
                    note_writer.writerow([message.tempo])
                elif message.type in ("note_on","note_off"):
                    message_info = [int(message.type=="note_on"),message.channel,message.note,message.velocity,message.time]
                    note_writer.writerow(message_info)


def csv_dir(path,output):
    for p in Path(path).glob("**/*.mid"):
        midi_to_csv(str(p),output)

def midi_dir_to_csv(midi_path,midi_out,num_messages,csv_out):
    process_dir(midi_path,midi_out,num_messages)
    csv_dir(midi_out,csv_out)
if __name__=="__main__":
    midi_to_csv(r"C:\PythonPrograms\gset\midi\sliced_midi\Dancing Queen.1\18.mid",r"C:\PythonPrograms\gset\midi\csv")
