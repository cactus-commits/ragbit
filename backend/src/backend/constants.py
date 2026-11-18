from pathlib import Path

DATA_PATH = Path(__file__).parents[1] / "data" # parent = parents[0] dvs. hoppar upp en folder, parents[1] = hoppar upp två folder
VECTOR_DATABASE_PATH = Path(__file__).parents[1] / "knowledge_base" 

if __name__ == "__main__":
    print(DATA_PATH)