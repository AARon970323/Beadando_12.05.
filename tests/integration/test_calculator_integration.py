import os
import tempfile
from calculator.calculator import Calculator

def test_save_to_file():
    c = Calculator()
    tmp = tempfile.NamedTemporaryFile(delete=False)
    tmp.close()

    c.save_result_to_file(10, tmp.name)

    with open(tmp.name, "r", encoding="utf-8") as f:
        data = f.read().strip()

    assert data == "10"

    os.remove(tmp.name)
