import os
import re
import matplotlib.pyplot as plt
from collections import Counter, defaultdict
from datetime import datetime

DIFFICULTIES = ["easy", "medium", "hard"]
LANGUAGES = {"python": "solution.py", "java": "Solution.java"}
ASSETS_DIR = "assets"
README_PATH = "README.md"


def ensure_assets():
    os.makedirs(ASSETS_DIR, exist_ok=True)


def extract_tags(readme_path):
    if not os.path.exists(readme_path):
        return []
    with open(readme_path, "r") as f:
        for line in f:
            if line.lower().startswith("**tags:**"):
                tags = line.split("**Tags:**", 1)[-1].strip()
                return [tag.strip() for tag in tags.split(",")]
    return []


def collect_data():
    lang_counts = {d: {"python": 0, "java": 0} for d in DIFFICULTIES}
    lang_totals = {"python": 0, "java": 0}
    date_counter = Counter()
    tag_counter = Counter()
    total = 0

    for diff in DIFFICULTIES:
        if not os.path.exists(diff):
            continue
        for problem in os.listdir(diff):
            problem_path = os.path.join(diff, problem)
            solution_path = os.path.join(problem_path, "solution")
            readme_path = os.path.join(problem_path, "README.md")
            if not os.path.isdir(solution_path):
                continue

            counted = False
            modified_date = datetime.fromtimestamp(
                os.path.getmtime(solution_path)
            ).strftime("%Y-%m-%d")

            for lang, file in LANGUAGES.items():
                if os.path.exists(os.path.join(solution_path, file)):
                    lang_counts[diff][lang] += 1
                    lang_totals[lang] += 1
                    if not counted:
                        date_counter[modified_date] += 1
                        counted = True
                    total += 1

            for tag in extract_tags(readme_path):
                tag_counter[tag] += 1

    return lang_counts, lang_totals, date_counter, tag_counter, total


def generate_difficulty_language_chart(lang_counts):
    python = [lang_counts[d]["python"] for d in DIFFICULTIES]
    java = [lang_counts[d]["java"] for d in DIFFICULTIES]
    x = range(len(DIFFICULTIES))

    plt.figure(figsize=(8, 5))
    plt.bar(x, python, label="Python", color="#4CAF50")
    plt.bar(x, java, bottom=python, label="Java", color="#2196F3")
    plt.xticks(x, [d.capitalize() for d in DIFFICULTIES])
    plt.ylabel("Problems Solved")
    plt.title("Solved Problems by Difficulty & Language")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{ASSETS_DIR}/progress_difficulty_language.png")
    plt.close()


def generate_pie_chart(lang_counts):
    total_per_diff = [lang_counts[d]["python"] + lang_counts[d]["java"] for d in DIFFICULTIES]
    labels = [f"{d.capitalize()} ({n})" for d, n in zip(DIFFICULTIES, total_per_diff) if n > 0]
    sizes = [n for n in total_per_diff if n > 0]

    if not sizes:
        return

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title("Problem Distribution by Difficulty")
    plt.axis("equal")
    plt.savefig(f"{ASSETS_DIR}/pie_difficulty.png")
    plt.close()


def generate_language_bar(lang_totals):
    langs = list(lang_totals.keys())
    counts = list(lang_totals.values())
    colors = ["#4CAF50", "#2196F3"]

    plt.figure(figsize=(6, 4))
    plt.bar(langs, counts, color=colors)
    for i, v in enumerate(counts):
        plt.text(i, v + 0.2, str(v), ha="center")
    plt.title("Problems Solved by Language")
    plt.tight_layout()
    plt.savefig(f"{ASSETS_DIR}/bar_language.png")
    plt.close()


def generate_timeline_chart(date_counter):
    if not date_counter:
        return

    dates = sorted(date_counter)
    daily_counts = [date_counter[d] for d in dates]
    cumulative = []
    total = 0
    for c in daily_counts:
        total += c
        cumulative.append(total)

    plt.figure(figsize=(10, 4))
    plt.plot(dates, cumulative, marker="o", label="Cumulative")
    plt.bar(dates, daily_counts, alpha=0.5, label="Daily")
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Problems")
    plt.title("Problems Solved Over Time")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{ASSETS_DIR}/progress_timeline.png")
    plt.close()


def generate_tag_chart(tag_counter):
    if not tag_counter:
        return
    tags, counts = zip(*tag_counter.most_common())
    plt.figure(figsize=(10, 5))
    plt.bar(tags, counts, color="#ff9800")
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Count")
    plt.title("Problem Tags Frequency")
    plt.tight_layout()
    plt.savefig(f"{ASSETS_DIR}/tag_frequency.png")
    plt.close()


def update_readme():
    charts = [
        ("![By Difficulty & Language](assets/progress_difficulty_language.png)\n"),
        ("![By Difficulty Pie](assets/pie_difficulty.png)\n"),
        ("![By Language](assets/bar_language.png)\n"),
        ("![Timeline](assets/progress_timeline.png)\n"),
        ("![Tag Frequency](assets/tag_frequency.png)\n"),
    ]

    section_title = "## 📊 Problem Distribution"
    new_section = ["\n", section_title + "\n"] + charts

    if not os.path.exists(README_PATH):
        with open(README_PATH, "w") as f:
            f.writelines(new_section)
        return

    with open(README_PATH, "r") as f:
        lines = f.readlines()

    inside = False
    result = []
    for line in lines:
        if section_title in line:
            inside = True
            continue
        if inside and line.startswith("!["):
            continue
        if inside and not line.startswith("!["):
            inside = False
        result.append(line)

    result += new_section

    with open(README_PATH, "w") as f:
        f.writelines(result)


def print_summary(lang_counts, lang_totals, total):
    print(f"\n✅ Total Problems Solved: {total}")
    for d in DIFFICULTIES:
        py = lang_counts[d]["python"]
        java = lang_counts[d]["java"]
        print(f"{d.capitalize():<6}: Python: {py}, Java: {java}, Total: {py + java}")
    print(f"\nLanguages: Python: {lang_totals['python']} | Java: {lang_totals['java']}\n")


def main():
    ensure_assets()
    lang_counts, lang_totals, dates, tags, total = collect_data()
    print_summary(lang_counts, lang_totals, total)
    generate_difficulty_language_chart(lang_counts)
    generate_pie_chart(lang_counts)
    generate_language_bar(lang_totals)
    generate_timeline_chart(dates)
    generate_tag_chart(tags)
    update_readme()
    print("📊 All charts updated in assets/ and README.md\n")


if __name__ == "__main__":
    main()
