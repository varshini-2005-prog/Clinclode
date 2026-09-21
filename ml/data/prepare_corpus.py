from pathlib import Path
import json
import random

INPUT_DIR = Path("data/mtsamples")
OUTPUT_DIR = Path("data/gold_charts")

random.seed(42)


def load_documents():
    documents = []

    for path in INPUT_DIR.glob("*.txt"):
        text = path.read_text(encoding="utf-8").strip()

        if text:
            documents.append({
                "id": path.stem,
                "text": text
            })

    return documents


def split_documents(documents):
    random.shuffle(documents)

    total = len(documents)
    train_end = int(total * 0.8)
    val_end = int(total * 0.9)

    return {
        "train": documents[:train_end],
        "validation": documents[train_end:val_end],
        "test": documents[val_end:]
    }


def save_splits(splits):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for name, documents in splits.items():
        output_file = OUTPUT_DIR / f"{name}.json"

        output_file.write_text(
            json.dumps(documents, indent=2),
            encoding="utf-8"
        )


if __name__ == "__main__":
    documents = load_documents()
    splits = split_documents(documents)
    save_splits(splits)

    print(f"Loaded documents: {len(documents)}")
    print(f"Train: {len(splits['train'])}")
    print(f"Validation: {len(splits['validation'])}")
    print(f"Test: {len(splits['test'])}")
