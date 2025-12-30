def count_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return len(f.readlines())


def count_words(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return len(f.read().split())


if __name__ == "__main__":
    path = "example.txt"
    print("Lines:", count_lines(path))
    print("Words:", count_words(path))
