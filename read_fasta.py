from os import path

def readfasta(plik):
    name_list=[]
    index_list=[]
    seq_list=[]
    sequence=''
    fasta=open(plik, 'r')
    data=fasta.read()
    fasta.close()
    data=data.splitlines()
    for line in data:
        if line[0]=='>':  #first sign
            info=line.split('|')  #divides into a new word by character |
            nr=info[1]
            name=info[-1]
            name_list.append(name)
            index_list.append(nr)
            if sequence!='':
                seq_list.append(sequence)
            sequence=''
        else:
            sequence=sequence+line
    seq_list.append(sequence)
    return name_list, index_list, seq_list

plik=input('Please enter file name: ')

if path.isfile(plik): #global variable
    #reading function
    names1, indexes1, sequences1=readfasta(plik)
else:
    print('File does not exist')


#RESULTS:
##Please enter file name: FASTA/test1.fasta
##>>> sequences
##['MRMRGRRLLPIILSLLLIVLLSLCYFSNHLRDSSQSRKNGFLLHLPLETKRNPSNPNTPLSNLLNLTDFHYLLASNVCRKAKRELLVTSYAGHDALRSAHRQAIPQSKLEEMGLRRVFLLAALPSREHFISQDQLASEQNRFGDLLQGNFIEDYRNLSYKHVMGLKWVSEECKKQAKFIIKLDDDIIYDVFHLRRYLETLEVREPGLATSSTLLSGYVLDAKPPIRLRANKWYVSKKEYPQALYPAYLSGWLYVTNVPTAERIVAEAERMSFFWIDDTWLTGVVRTRLGIPLERHNDWFSANAEFIDCCVRDLKKHNYECEYSVGPNGGDDRLLVEFLHNVEKCYFDECVKRPVGKSLKETCLAAAKSRPPKHGFPEIKALRLR']
##>>> names
##[' (AE003417) EG:BACR37P7.1 gene product [Drosophila melanogaster]']
##>>> indexes
##['7290019']

from os import path

def readfasta(plik): 
    name_list=[]
    index_list=[]
    seq_list=[]
    sequence=''
    fasta=open(plik, 'r')
    data=fasta.read()
    fasta.close()
    data=data.splitlines()
    for line in data:
        if line[0]=='>':
            info=line.split('|')
            nr=info[1]
            name=info[-1]
            name_list.append(name)
            index_list.append(nr)
            if sequence!='':
                seq_list.append(sequence)
            sequence=''
        else:
            sequence=sequence+line
    seq_list.append(sequence)
    return name_list, index_list, seq_list
seq_list=[]
plik=input('Please enter file name: ')
plik1=input('Please enter file name: ')
if path.isfile(plik): 
    #reading function
    names1, indexes1, sequences1=readfasta(plik)
    names2, indexes2, sequences2=readfasta(plik1)
else:
    print('File does not exist')
