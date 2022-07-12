_instrument_weights={'Bright Acoustic Piano':3608953,'Vibraphone':2794843,'Clavi':2509916,'Soprano Sax':1265537,'Music Box':637622,
'FX 4 (atmosphere)':414586,'Harpsichord':285851,'Bird Tweet':164036,'Pad 4 (choir)':154818,
'Pad 6 (metallic)':139902,
'FX 5 (brightness)':138601,
'FX 3 (crystal)':132273,
'Guitar harmonics':99798,
'Acoustic Grand Piano':96703,
'Breath Noise':63158,
'Acoustic Bass':57114,
'Recorder':42114,
'FX 6 (goblins)':34612,
'Synth Bass 1':27951,
'Guitar Fret Noise':24575,
'Drawbar Organ':22029,
'Electric Grand Piano':19830,
'Honky-tonk Piano':12419,
'Percussive Organ':9752,
'Pad 7 (halo)':7547,
'Electric Piano 2':6955,
'Celesta':6879,
'Reverse Cymbal':5938,
'Alto Sax':5794,
'Clarinet':3679,
'Synth Bass 2':3097,
'Baritone Sax':2892,
'Lead 5 (charang)':2438,
'Tenor Sax':2002,
'Synth Voice':1847,
'Xylophone':1796,
'Contrabass':1397,
'Electric Piano 1':1275,
'Pad 5 (bowed)':1232,
'Dulcimer':1054,
'English Horn':1019,
'Lead 7 (fifths)':968,
'SynthStrings 1':894,
'Piccolo':768,
'Flute':729,
'Bassoon':697,
'SynthBrass 2':674,
'String Ensemble 1':510,
'Pad 1 (new age)':480,
'Lead 1 (square)':454,
'Oboe':343,
'Gunshot':284,
'Pad 8 (sweep)':265,
'String Ensemble 2':260,
'French Horn':230,
'Lead 2 (sawtooth)':210,
'Applause':164,
'Harmonica':136,
'Orchestra Hit':125,
'Lead 6 (voice)':109,
'Banjo':104,
'Trumpet':91,
'Tango Accordion':87,
'Marimba':70,
'Electric Bass (finger)':58,
'Sitar':57,
'SynthBrass 1':55,
'Telephone Ring':55,
'Timpani':43,
'FX 1 (rain)':41,
'Blown Bottle':36,
'FX 8 (sci-fi)':34,
'Reed Organ':32,
'Distortion Guitar':31,
'Fretless Bass':30,
'Violin':27,
'FX 2 (soundtrack)':27,
'Voice Oohs':25,
'Tubular Bells':24,
'Tinkle Bell':24,
'Lead 3 (calliope)':22,
'Muted Trumpet':21,
'Slap Bass 1':20,
'Electric Guitar (jazz)':18,
'Ocarina':18,
'Seashore':17,
'Glockenspiel':16,
'Lead 4 (chiff)':16,
'Accordion':15,
'Acoustic Guitar (nylon)':15,
'Tuba':13,
'Lead 8 (bass + lead)':13,
'Electric Bass (pick)':12,
'Pad 3 (polysynth)':12,
'Overdriven Guitar':11,
'Acoustic Guitar (steel)':10,
'Rock Organ':9,
'Church Organ':9,
'Shakuhachi':8,
'Whistle':8,
'Pad 2 (warm)':8,
'Choir Aahs':7,
'Electric Guitar (clean)':6,
'Electric Guitar (muted)':6,
'Slap Bass 2':6,
'Shanai':5,
'Woodblock':5,
'Melodic Tom':5,
'Viola':4,
'Cello':4,
'SynthStrings 2':4,
'Brass Section':4,
'FX 7 (echoes)':4,
'Fiddle':4,
'Pizzicato Strings':3,
'Shamisen':3,
'Trombone':2,
'Pan Flute':2,
'Tremolo Strings':1,
'Koto':1,
'Bag pipe':1,
'Agogo':1,
'Synth Drum':1,
'Helicopter':1}
#loaded from an analysis of every single midi file in the database of ~20k
instrument_names = {
    0:'Acoustic Grand Piano', 1:'Bright Acoustic Piano',
2:'Electric Grand Piano',3:'Honky-tonk Piano',4:'Electric Piano 1',
5:'Electric Piano 2',6:'Harpsichord',7:'Clavi',8:'Celesta',9:'Glockenspiel',10:'Music Box',
11:'Vibraphone',12:'Marimba',13:'Xylophone',14:'Tubular Bells',15:'Dulcimer',16:'Drawbar Organ',
17:'Percussive Organ',18:'Rock Organ',19:'Church Organ',20:'Reed Organ',21:'Accordion',
22:'Harmonica',23:'Tango Accordion',24:'Acoustic Guitar (nylon)',25:'Acoustic Guitar (steel)',
26:'Electric Guitar (jazz)',27:'Electric Guitar (clean)',28:'Electric Guitar (muted)',29:'Overdriven Guitar',
30:'Distortion Guitar',31:'Guitar harmonics',32:'Acoustic Bass',33:'Electric Bass (finger)',34:'Electric Bass (pick)',
35:'Fretless Bass',36:'Slap Bass 1',37:'Slap Bass 2',38:'Synth Bass 1',39:'Synth Bass 2',40:'Violin',
41:'Viola',42:'Cello',43:'Contrabass',44:'Tremolo Strings',45:'Pizzicato Strings',46:'Orchestral Harp',
47:'Timpani',48:'String Ensemble 1',49:'String Ensemble 2',50:'SynthStrings 1',51:'SynthStrings 2',52:'Choir Aahs',
53:'Voice Oohs',54:'Synth Voice',55:'Orchestra Hit',56:'Trumpet',57:'Trombone',58:'Tuba',59:'Muted Trumpet',
60:'French Horn',61:'Brass Section',62:'SynthBrass 1',63:'SynthBrass 2',64:'Soprano Sax',65:'Alto Sax',
66:'Tenor Sax',67:'Baritone Sax',68:'Oboe',69:'English Horn',70:'Bassoon',71:'Clarinet',72:'Piccolo',
73:'Flute',74:'Recorder',75:'Pan Flute',76:'Blown Bottle',77:'Shakuhachi',78:'Whistle',
79:'Ocarina',80:'Lead 1 (square)',81:'Lead 2 (sawtooth)',82:'Lead 3 (calliope)',83:'Lead 4 (chiff)',
84:'Lead 5 (charang)',85:'Lead 6 (voice)',86:'Lead 7 (fifths)',87:'Lead 8 (bass + lead)',
88:'Pad 1 (new age)',89:'Pad 2 (warm)',90:'Pad 3 (polysynth)',91:'Pad 4 (choir)',92:'Pad 5 (bowed)',
93:'Pad 6 (metallic)',94:'Pad 7 (halo)',95:'Pad 8 (sweep)',96:'FX 1 (rain)',97:'FX 2 (soundtrack)',98:'FX 3 (crystal)',
99:'FX 4 (atmosphere)',100:'FX 5 (brightness)',101:'FX 6 (goblins)',102:'FX 7 (echoes)',103:'FX 8 (sci-fi)',
104:'Sitar',105:'Banjo',106:'Shamisen',107:'Koto',108:'Kalimba',109:'Bag pipe',110:'Fiddle',111:'Shanai',
112:'Tinkle Bell',113:'Agogo',114:'Steel Drums',115:'Woodblock',116:'Taiko Drum',117:'Melodic Tom',118:'Synth Drum',
119:'Reverse Cymbal',120:'Guitar Fret Noise',121:'Breath Noise',122:'Seashore',123:'Bird Tweet',124:'Telephone Ring',
125:'Helicopter',126:'Applause',127:'Gunshot'}
#sourced from the general MIDI 1 specification
#https://www.midi.org/specifications-old/item/gm-level-1-sound-set
names_instruments = {v:k for (k,v) in instrument_names.items()}

instrument_weights_usable = {names_instruments[k]:v for k,v in _instrument_weights.items()}
families = ["Piano", "Chromatic Percussion", "Organ", "Guitar", "Bass", 
"Strings", "Ensemble", "Brass", "Reed", "Pipe", "Synth Lead", "Synth Pad", "Synth Effects", "Ethnic", "Percussive", "Sound Effects"]


#will return the family name in a string
def classify_inst(inst:int) -> str:
    ranges = [list(range((8*i),(8*(i+1)))) for i in range(16)]
    families = ["Piano", "Chromatic Percussion", "Organ", "Guitar", "Bass", 
    "Strings", "Ensemble", "Brass", "Reed", "Pipe", "Synth Lead", "Synth Pad", "Synth Effects", "Ethnic", "Percussive", "Sound Effects"]
    classifications = {j:i for i,j in zip(ranges,families)}
    for j,i in classifications.items():
        if inst in i:
            return j


def int_classify_inst(inst):
    families = ["Piano", "Chromatic Percussion", "Organ", "Guitar", "Bass", 
"Strings", "Ensemble", "Brass", "Reed", "Pipe", "Synth Lead", "Synth Pad", "Synth Effects", "Ethnic", "Percussive", "Sound Effects"]
    return families.index(classify_inst(inst))

best_in_family = [max(([(inst,count,fam) for inst,count in instrument_weights_usable.items() if classify_inst(inst) == fam]),key=lambda x: x[1])for fam in families]
#hacky list comprehension that will give the best in each family

def give_best_inst(inst:int) -> tuple:
    look_for = classify_inst(inst)
    for idx,x in enumerate(best_in_family):
        if x[2] == look_for:
            return (idx,x[0])
            #returns idx of best instrumnet in a family


