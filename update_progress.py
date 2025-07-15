import os
import matplotlib.pyplot as plt

DIFFICULTIES = ["easy", "medium", "hard"]
LANGUAGES = ["python", "java"]
LANGUAGE_FILES = {
    "python": "solution.py",
    "java": "Solution.java"
}
ASSETS_DIR = "assets"
README_PATH = "README.md"


def count_solutions():
    counts = {diff: {lang: 0 for lang in LANGUAGES} for diff in DIFFICULTIES}
    totals = {"python": 0, "java": 0}
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
                    totals[lang] += 1
                    total += 1

    return counts, totals, total


def generate_stacked_bar(counts):
    python_counts = [counts[d]["python"] for d in DIFFICULTIES]
    java_counts = [counts[d]["java"] for d in DIFFICULTIES]
    x = range(len(DIFFICULTIES))

    plt.figure(figsize=(8, 5))
    plt.bar(x, python_counts, label="Python", color="#4CAF50")
    plt.bar(x, java_counts, bottom=python_counts, label="Java", color="#2196F3")
    plt.xticks(x, [d.capitalize() for d in DIFFICULTIES])
    plt.ylabel("Problems Solved")
    plt.title("Solved Problems by Difficulty & Language")
    plt.legend()
    plt.tight_layout()

    path = os.path.join(ASSETS_DIR, "progress_difficulty_language.png")
    plt.savefig(path)
    plt.close()
    print(f"✅ Bar chart saved to {path}")


def generate_pie_chart(counts):
    labels = []
    sizes = []

    for d in DIFFICULTIES:
        total_d = counts[d]["python"] + counts[d]["java"]
        if total_d > 0:
            labels.append(f"{d.capitalize()} ({total_d})")
            sizes.append(total_d)

    if not sizes:
        print("⚠️ No data for pie chart.")
        return

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title("Problem Distribution by Difficulty")
    plt.axis("equal")

    path = os.path.join(ASSETS_DIR, "pie_difficulty.png")
    plt.savefig(path)
    plt.close()
    print(f"✅ Pie chart saved to {path}")


def generate_language_bar(total_by_lang):
    langs = list(total_by_lang.keys())
    values = list(total_by_lang.values())
    colors = ["#4CAF50" if lang == "python" else "#2196F3" for lang in langs]

    plt.figure(figsize=(6, 4))
    plt.bar(langs, values, color=colors)
    plt.ylabel("Problems Solved")
    plt.title("Problems Solved by Language")
    for i, v in enumerate(values):
        plt.text(i, v + 0.2, str(v), ha='center')
    plt.tight_layout()

    path = os.path.join(ASSETS_DIR, "bar_language.png")
    plt.savefig(path)
    plt.close()
    print(f"✅ Language bar chart saved to {path}")


def update_readme():
    if not os.path.exists(README_PATH):
        print("⚠️ README.md not found. Skipping update.")
        return

    lines = []
    with open(README_PATH, "r") as f:
        lines = f.readlines()

    section_start = "## 📊 Problem Distribution"
    charts = [
        "![By Difficulty and Language](assets/progress_difficulty_language.png)",
        "![By Difficulty (Pie)](assets/pie_difficulty.png)",
        "![By Language](assets/bar_language.png)",
    ]

    new_section = [f"\n{section_start}\n"] + [c + "\n" for c in charts]
    new_lines = []
    inside_old_section = False

    for line in lines:
        if section_start in line:
            inside_old_section = True
            continue
        if inside_old_section and line.startswith("!["):
            continue
        if inside_old_section and not line.startswith("!["):
            inside_old_section = False
        new_lines.append(line)

    new_lines += new_section

    with open(README_PATH, "w") as f:
        f.writelines(new_lines)

    print("✅ README.md updated with all charts.")


def print_summary(counts, totals, total):
    print(f"\n🧮 Total Problems Solved: {total}")
    for diff in DIFFICULTIES:
        py = counts[diff]["python"]
        java = counts[diff]["java"]
        total_diff = py + java
        print(f"{diff.capitalize():<6}: Python: {py}, Java: {java}, Total: {total_diff}")
    print(f"\n🔤 Language Totals: Python: {totals['python']}, Java: {totals['java']}")


def main():
    os.makedirs(ASSETS_DIR, exist_ok=True)
    counts, lang_totals, total = count_solutions()
    print_summary(counts, lang_totals, total)
    generate_stacked_bar(counts)
    generate_pie_chart(counts)
    generate_language_bar(lang_totals)
    update_readme()


if __name__ == "__main__":
    main()
