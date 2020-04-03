import random
from typing import List

def generate_password(length: int = 4) -> str:
    words = read_all("./common_words_en.txt")
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
    except:
        print("error read")

    return result

if __name__ == "__main__":
    print(generate_password())
