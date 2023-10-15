class DNA:
    def __init__(self, string):
        self.string = string

    def count_nucleotides(self):
        adenine = len(self.string.split('A')) - 1
        thymine = len(self.string.split('T')) - 1
        cytosine = len(self.string.split('C')) - 1
        guanine = len(self.string.split('G')) - 1
        return {'A': adenine, 'T': thymine, 'C': cytosine, 'G': guanine}

    def transcribe(self):
        return 'U'.join(self.string.split('T')) 

    def complement_dna(self):
        string = self.string
        string = 'a'.join(string.split('T'))
        string = 't'.join(string.split('A'))
        string = 'c'.join(string.split('G'))
        string = 'g'.join(string.split('C'))
        return string.upper()
    
    def distance(self, s2):
        x = 0
        if len(s2) == len(self.string):
            for i in range(len(self.string)):
                if list(self.string)[i] != list(s2)[i]:
                    x += 1
            return x
        else:
            return 'Длины строк не равны'
                  

class RNA(object):
    def __init__(self, string):
        self.string = string


    def transcribe(self):
        return 'T'.join(self.string.split('U'))
    
Lactase = RNA('CCGAAGCAUUCG')
print(Lactase.transcribe())
GFP = DNA('TTTTTAAACGCG')
print(GFP.count_nucleotides())
print(GFP.complement_dna())

