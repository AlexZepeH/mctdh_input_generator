class VibronicCouplingTerm:
    def __init__(self, coefficient: str, electronic_state: int, label):
        self.coefficient = coefficient
        self.electronic_state = electronic_state
        self.label = label

    def to_string_with_index(self, label_to_index: dict[str, int]) -> str:
        return f"{self.coefficient}    |{self.electronic_state} S{self.electronic_state}&1 |{label_to_index} q"
