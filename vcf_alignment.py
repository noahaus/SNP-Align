import os # use in order to call commands from the terminal script is called in
import glob

list_of_files = glob.glob('*.filtered.vcf')
#initialize our data structure
genome_map = {}
vcf_map = {}
name = ""
name_arr = []
name_arr.append('reference')
ref = ""
alt = ""
position = ""
vcf_list = []
info = []
#choose a file
for file in list_of_files:
    #extract the position, and then map it to the isolate name and nucleotide at that position.
    #name
    name = file.replace(".filtered.vcf","")
    name_arr.append(name)
    # position
    vcf = open(file,'r')
    #collect all the snp info in one file
    for line in vcf:
        if line.startswith('#'):
            continue
        else:
            info = line.split("\t")
            position = info[1]
            ref = info[3]
            alt = info[4]
            if len(ref) > 1 or len(alt) > 1:
                continue
            else:
                if genome_map.get(position,-1) == -1:
                    genome_map[position] = {}
                    genome_map.get(position)["reference"] = ref
                    genome_map.get(position)[name] = alt
                else:
                    genome_map.get(position)[name] = alt

sequence = ""
for name in name_arr:
    print(">{}".format(name))
    for k,v in sorted(genome_map.items()):
        if genome_map.get(k).get(name,"reference") == "reference":
            sequence = sequence + genome_map.get(k).get("reference")
        else:
            sequence = sequence + genome_map.get(k).get(name)
    print("{}".format(sequence))
    sequence = ""
