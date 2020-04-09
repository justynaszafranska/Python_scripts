from os import path

def czytajfasta(plik): #plik to zmienna formalna, nie musi miec odpowiednika w danych
    lista_nazw=[]
    lista_index=[]
    lista_sekw=[]
    sekwencja=''
    fasta=open(plik, 'r')
    dane=fasta.read()
    fasta.close()
    dane=dane.splitlines()
    for wiersz in dane:
        if wiersz[0]=='>':  #pierwszy znak z ciagu znakow
            info=wiersz.split('|')  #dzieli na nowy wyraz po znaku |
            nr=info[1]
            nazwa=info[-1]
            lista_nazw.append(nazwa)
            lista_index.append(nr)
            if sekwencja!='':
                lista_sekw.append(sekwencja)
            sekwencja=''
        else:
            sekwencja=sekwencja+wiersz
    lista_sekw.append(sekwencja)
    return lista_nazw, lista_index, lista_sekw

plik=input('Podaj nazwe pliku: ')

if path.isfile(plik): #zmienna globalna, nie pokaze jej program
    #wywołujemy funkcje czytania
    nazwy1, indexy1, sekwencje1=czytajfasta(plik)
else:
    print('Nie ma takiego pliku')


#WYNIK:
##Podaj nazwe pliku: FASTA/test1.fasta
##>>> sekwencje
##['MRMRGRRLLPIILSLLLIVLLSLCYFSNHLRDSSQSRKNGFLLHLPLETKRNPSNPNTPLSNLLNLTDFHYLLASNVCRKAKRELLVTSYAGHDALRSAHRQAIPQSKLEEMGLRRVFLLAALPSREHFISQDQLASEQNRFGDLLQGNFIEDYRNLSYKHVMGLKWVSEECKKQAKFIIKLDDDIIYDVFHLRRYLETLEVREPGLATSSTLLSGYVLDAKPPIRLRANKWYVSKKEYPQALYPAYLSGWLYVTNVPTAERIVAEAERMSFFWIDDTWLTGVVRTRLGIPLERHNDWFSANAEFIDCCVRDLKKHNYECEYSVGPNGGDDRLLVEFLHNVEKCYFDECVKRPVGKSLKETCLAAAKSRPPKHGFPEIKALRLR']
##>>> nazwy
##[' (AE003417) EG:BACR37P7.1 gene product [Drosophila melanogaster]']
##>>> indexy
##['7290019']

from os import path

def czytajfasta(plik): #plik to zmienna formalna, nie musi miec odpowiednika w danych
    lista_nazw=[]
    lista_index=[]
    lista_sekw=[]
    sekwencja=''
    fasta=open(plik, 'r')
    dane=fasta.read()
    fasta.close()
    dane=dane.splitlines()
    for wiersz in dane:
        if wiersz[0]=='>':
            info=wiersz.split('|')
            nr=info[1]
            nazwa=info[-1]
            lista_nazw.append(nazwa)
            lista_index.append(nr)
            if sekwencja!='':
                lista_sekw.append(sekwencja)
            sekwencja=''
        else:
            sekwencja=sekwencja+wiersz
    lista_sekw.append(sekwencja)
    return lista_nazw, lista_index, lista_sekw
lista_sekw=[]
plik=input('Podaj nazwe pliku: ')
plik1=input('Podaj nazwe pliku: ')
if path.isfile(plik): #zmienna globalna, nie pokaze jej program
    #wywołujemy funkcje czytania
    nazwy1, indexy1, sekwencje1=czytajfasta(plik)
    nazwy2, indexy2, sekwencje2=czytajfasta(plik1)
else:
    print('Nie ma takiego pliku')

WYNIK:
Podaj nazwe pliku: FASTA/test1.fasta
Podaj nazwe pliku: FASTA/test2.fasta

>>> sekwencje1
['MRMRGRRLLPIILSLLLIVLLSLCYFSNHLRDSSQSRKNGFLLHLPLETKRNPSNPNTPLSNLLNLTDFHYLLASNVCRKAKRELLVTSYAGHDALRSALYPAYLSGWLYVTNVPTAECTCLAAAKSRPPKHGFPEIKALRLR']
>>> sekwencje2
['MTDFVELMNSMSSTFNSDCATSTAEGGTLLNLNLAEDKTLKWRNLANNQFASKEKKHKDKEEEERKEARNQEEIEDIKALLADVVDAAAVKLEEEEAQNAEKVEPHTKCEIEEEGRKEMEYDQDVAKQDSEMEKKQNG
