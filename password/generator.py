import random
import sys
from pathlib import Path
from typing import List

def generate_password(length: int = 4) -> str:
    path = str(Path(__file__).parent) + "/common_words_en.txt"
    words = read_all(path)

    password = ""
    for i in range(0, length):
        password += random.choice(words) + " "

    return password

def read_all(file_path: str) -> List[str]:
    result = []
    line = ""
    try:
        with open(file_path, "r") as file:
            line = file.readline()
            while line:
                result.append(line.replace("\n", ""))
                line = file.readline()
        return result
    except:
        print("error read file", sys.exc_info()[0])

if __name__ == "__main__":
    print(generate_password())
