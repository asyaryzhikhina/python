import json


with open('C:\\Users\\Albert\\Desktop\\py\\6\\rna_codon_table.json') as f:
    

class SequenceError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
    
    def __str__(self) -> str:
        return f'{self.message}'

class Sequence(object):
    seq_type = None
    types = set(['DNA', 'RNA', 'Protein']) # all possible sequence types
    _prot_acids = set(rnacodontable.values())
    _dna_nucls = set(['A', 'T', 'C', 'G'])
    _rna_nucls = set(['A', 'U', 'C', 'G'])

    def __init__(self, file_name: str) -> None:
        """
        Input:
        - file_name : FASTA file with sequence_name, sequence_type and 
        the sequence itself

        Output: None
        """
        self.file_name = file_name   
        self.seq_types, self.seq   = self._parse(file_name)
        #self.trans_dna = self.transcribe()

        
    def _parse(self, file_name: str) -> tuple[str, str]:
        """
        Input:
        - file_name : FASTA file with sequence_name, sequence_type and 
        the sequence itself

        Output: A tuple with (sequence, sequence_type)
        """
        
        with open(self.file_name, "r") as file:
            lines = file.readlines()
            sequence = ""
            sequence_type = ""

            for i, line in enumerate(lines):
                line = line.strip()
                if ">" in line:
                     sequence_type = line.split()[1]
                     sequence = lines[i+1].strip()  
                     break  

        return (sequence_type, sequence)
    
    def _check(self, string: str) -> bool:
        """
        Input:
        - string : sequence from FASTA file

        Output: A boolean value (True or False)
        """

        if self.seq_types not in self.types:
            return False

        if self.seq_types == 'Protein':
            for i in self.seq:
                if i not in self._prot_acids:
                    return False
            
        elif self.seq_types == 'DNA':
            for i in self.seq:
                if i not in self._dna_nucls:
                    return False
            
        elif self.seq_types == 'RNA':
            for i in self.seq:
                if i not in self._rna_nucls:
                    return False
            
        else: 
             return False 

        return True
    
    def hamming_distance(self, sequence, string2: str) -> int:
        """
        Input:
        - sequence : another sequence of nucleotides

        Output: number of different letters 
        between sequence_attribute and given string sequence
        """

        count = 0
        if len(self.sequence) != len(string2):
            raise ValueError("Строки разной длины")
        else:
            for i in range(min(len(self.sequence), len(string2))):
                if self.sequence[i] != string2[i]:
                    count += 1
        count += abs(len(self.sequence) - len(string2))
        return(count)
    
    def count_nucleotides(self) -> None:
        """
        Input: None

        Output: None
        """
        raise NameError
    
    def to_protein(self) -> None:
        """
        Input: None

        Output: None
        """
        raise NameError
    
    def transcribe(self) -> None:
        """
        Input: None

        Output: None
        """
        raise NameError

class DNA(Sequence):
    _type = 'DNA'
    def count_nucleotides(self) -> dict:
        """
        Input: None

        Output:
        - a dictionary with keys 'A', 'T', 'G', 'C' and their 
        corresponding amounts in sequence_attribute. 
        {'A': count_A, 'T': count_T, 'G': count_G, 'C': count_C}
        """
        count_A : int = self.seq.count('A')
        count_T : int = self.seq.count('T')
        count_G : int = self.seq.count('G')
        count_C : int = self.seq.count('C')
        return{'A': count_A, 'T': count_T, 'G': count_G, 'C': count_C}
    
    def complement_dna(self) -> str:
        """
        Input: None

        Output: a NEW string, where all 'A's were changed to 'T's
        and vice versa, all 'C's changed to 'G's and vice versa
        """
        complement_dna = self.seq
        complement_dna = complement_dna.replace('A', '1')
        complement_dna = complement_dna.replace('T', 'A')
        complement_dna = complement_dna.replace('C', '3')
        complement_dna = complement_dna.replace('G', 'C')
        complement_dna = complement_dna.replace('1', 'T')
        complement_dna = complement_dna.replace('3', 'G')
        return(complement_dna)
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def transcribe(self) -> str:
        """
        Input: None

        Output: a NEW string, where all 'T's were changed to 'U's
        """
        transcribe_dna = self.seq.replace('T', 'U')
        return(transcribe_dna)
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def to_protein(self) -> str:
        """
        Input: None

        Output: a NEW string, where all nucleotides are replaced with codons
        """
        trans_dna = self.seq.replace('T', 'U')

        if 'AUG' not in trans_dna:
            raise ValueError("Start codon not found")
        codons = []
    
    
        index = trans_dna.index('AUG')
        for i in range(index+3, len(trans_dna), 3):
            codon = trans_dna[i:i+3]
            codons.append(rnacodontable[codon])
    
            if codon in ["UAA", "UAG", "UGA"]:
                break

        if "Stop" in codons:
           codons.remove("Stop")


        index += 3

        return (codons)

        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def restriction_slices(self) -> int:
        """
        Input: None

        Output: number of slices by EcoRI restrictase
        """

class RNA(Sequence):
    _type = 'RNA'
    def count_nucleotides(self) -> dict:
        """
        Input: None

        Output:
        - a dictionary with keys 'A', 'U', 'G', 'C' and their 
        corresponding amounts in sequence_attribute. 
        {'A': count_A, 'U': count_U, 'G': count_G, 'C': count_C}
        """
        count_A : int = self.seq.count('A')
        count_U : int = self.seq.count('U')
        count_G : int = self.seq.count('G')
        count_C : int = self.seq.count('C')
        return{'A': count_A, 'U': count_U, 'G': count_G, 'C': count_C}
    
    def transcribe(self) -> str:
        """
        Input: None

        Output: a NEW string, where all 'U's were changed to 'T's
        """
        transcribe_rna = self.seq.replace('U', 'T')
        return(transcribe_rna)
    
    def to_protein(self) -> str:
        """
        Input: None

        Output: a NEW string, where all nucleotides are replaced with codons
        """
        if 'AUG' not in self.seq:
            raise ValueError("Start codon not found")
        codons = []
    
    
        index = self.seq.index('AUG')
        for i in range(index+3, len(self.seq), 3):
            codon = self.seq[i:i+3]
            codons.append(rnacodontable[codon])
    
            if codon in ["UAA", "UAG", "UGA"]:
                break

        if "Stop" in codons:
           codons.remove("Stop")


        index += 3

        return (codons)
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

class Protein(Sequence):
    _type = 'Protein'
    _pos_acids = set(['K', 'R', 'H'])
    _neg_acids = set(['D', 'E'])
    def count_amino_acids(self) -> dict:
        """
        Input: None

        Output:
        - a dictionary with amino acids as keys and their corresponding
        amounts in sequence_attribute
        {'A': count_A, 'U': count_U, 'G': count_G, 'C': count_C ...}
        """
        count_A : int = self.seq.count('A')
        count_R : int = self.seq.count('R')
        count_N : int = self.seq.count('N')
        count_D : int = self.seq.count('D')
        count_C : int = self.seq.count('C')
        count_Q : int = self.seq.count('Q')
        count_E : int = self.seq.count('E')
        count_G : int = self.seq.count('G')
        count_H : int = self.seq.count('H')
        count_I : int = self.seq.count('I')
        count_L : int = self.seq.count('L')
        count_K : int = self.seq.count('K')
        count_M : int = self.seq.count('M')
        count_F : int = self.seq.count('F')
        count_P : int = self.seq.count('P')
        count_S : int = self.seq.count('S')
        count_T : int = self.seq.count('T')
        count_V : int = self.seq.count('V')
        count_Y : int = self.seq.count('Y')
        count_W : int = self.seq.count('W')
        return{'A': count_A, 'R': count_R, 'N': count_N, 'D': count_D, 'C': count_C, 'Q': count_Q, 'G': count_G, 'E': count_E, 
        'H': count_H, 'I': count_I, 'L': count_L, 'K': count_K, 'M': count_M, 'F': count_F, 'P': count_P, 'S': count_S, 
        'T': count_T, 'W': count_W, 'Y': count_Y, 'V': count_V}
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def to_protein(self) -> str:
        """
        Input: None

        Output:
        - sequence of amino acids
        {'A': count_A, 'U': count_U, 'G': count_G, 'C': count_C ...}
        """
        return(self.seq)
    
    def charge(self) -> int:
        """
        Input: None

        Output:
        - resulting charge of sequence
        """

        charge = 0

        for i in self.seq:
            if i in self._pos_acids:
               charge += 1
            elif i in self._neg_acids:
                 charge -= 1
        return (charge)
