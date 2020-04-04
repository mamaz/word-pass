import fire
from .generator import generate_password

def main():
    fire.Fire(generate_password)

if __name__ == "__main__":
    main()