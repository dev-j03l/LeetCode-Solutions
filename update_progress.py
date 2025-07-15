import os
import matplotlib.pyplot as plt

DIFFICULTIES = ["easy", "medium", "hard"]
LANGUAGES = ["python", "java"]
LANGUAGE_FILES = {
    "python": "solution.py",
    "java": "Solution.java"
}
ASSETS_DIR = "assets"
IMAGE_PATH = os.path.join(ASSETS_DIR, "progress.png")
README_PATH = "README.md"


def count_solutions():
    counts = {diff: {lang: 0 for lang in LANGUAGES} for diff in DIFFICULTIES}
    total = 0

    for diff in DIFFICULTIES:
        if not os.path.exists(diff):
            continue

        for problem in os.listdir(diff):
            problem_path = os.path.join(diff, problem, "solution")
            if not os.path.isdir(problem_path):
                continue

            for lang, filename in LANGUAGE_FILES.items():
                file_path = os.path.join(problem_path, filename)
                if os.path.isfile(file_path):
                    counts[diff][lang] += 1
                    total += 1

    return counts, total


def generate_bar_chart(counts):
    labels = [d.capitalize() for d in DIFFICULTIES]
    python_counts = [counts[d]["python"] for d in DIFFICULTIES]
    java_counts = [counts[d]["java"] for d in DIFFICULTIES]

    x = range(len(DIFFICULTIES))

    plt.figure(figsize=(8, 5))
    plt.bar(x, python_counts, label="Python", color="#4CAF50")
    plt.bar(x, java_counts, bottom=python_counts, label="Java", color="#2196F3")

    plt.xticks(x, labels)
    plt.ylabel("Problems Solved")
    plt.title("LeetCode Progress by Difficulty and Language")
    plt.legend()
    plt.tight_layout()

    os.makedirs(ASSETS_DIR, exist_ok=True)
    plt.savefig(IMAGE_PATH)
    plt.close()

    print(f"✅ Graph saved to {IMAGE_PATH}")


def update_readme():
    if not os.path.exists(README_PATH):
        print("⚠️ README.md not found. Skipping update.")
        return

    with open(README_PATH, "r") as f:
        lines = f.readlines()

    image_line = "![Progress](assets/progress.png)\n"
    found = False
    new_lines = []

    for line in lines:
        if "assets/progress.png" in line:
            new_lines.append(image_line)
            found = True
        else:
            new_lines.append(line)

    if not found:
        new_lines.append("\n## 📊 Problem Distribution\n")
        new_lines.append(image_line)

    with open(README_PATH, "w") as f:
        f.writelines(new_lines)

    print("✅ README.md updated.")


def print_summary(counts, total):
    print(f"\n🧮 Total Problems Solved: {total}")
    for diff in DIFFICULTIES:
        py = counts[diff]["python"]
        java = counts[diff]["java"]
        total_diff = py + java
        print(f"{diff.capitalize():<6}: Python: {py}, Java: {java}, Total: {total_diff}")
    print()


def main():
    counts, total = count_solutions()
    print_summary(counts, total)
    generate_bar_chart(counts)
    update_readme()


if __name__ == "__main__":
    main()
