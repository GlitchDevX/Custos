from typing import Literal
class ValidationResult:
    type result_code = Literal[
        "OK",
        "FORMAT_INVALID",
        "DISPOSABLE",
        "NO_SERVER",
        "NO_ADDRESS",
    ]
    
    def __init__(self, passed, code: result_code, text):
        self.passed = passed
        self.code = code
        self.text = text
