class ElectronicOperatorFactory:
    def __init__(self, num_states: int):
        self.num_states = num_states
    
    def validate_indices(self, m: int, n:int):
        if not (1 <= m <= self.num_states) or not (1 <= n <= self.num_states):
            raise ValueError(f"n and m must be in range 1 to {self.num_states}")
        
    def Smn(self, m: int, n:int) -> str:
        self.validate_indices(m,n)
        return f"S{m}&{n}"
    
    def Zmn(self, m: int, n: int) -> str:
        self.validate_indices(m, n)
        return f"Z{m}&{n}"
    
    def identity(self) -> str:
        return "1"
    

def generate_all_Smn_terms(factory, el_label, coefficient="1.0"):
    terms = []
    for m in range(1, factory.num_states + 1):
        for n in range(1, factory.num_states + 1):
            op = factory.Smn(m, n)
            terms.append((coefficient, [(el_label, op)]))
    return terms

def generate_all_Zmn_terms(factory, el_label, coefficient="1.0"):
    terms = []
    for m in range(1, factory.num_states + 1):
        for n in range(1, factory.num_states + 1):
            op = factory.Zmn(m, n)
            terms.append((coefficient, [(el_label, op)]))
    return terms
