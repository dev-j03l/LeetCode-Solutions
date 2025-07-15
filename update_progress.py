import os
import matplotlib.pyplot as plt

DIFFICULTY_FOLDERS = ["easy", "medium", "hard"]
ASSETS_DIR = "assets"
IMAGE_PATH = os.path.join(ASSETS_DIR, "progress.png")
README_PATH = "README.md"

def count_problems():
    counts = {}
    for level in DIFFICULTY_FOLDERS:
        folder = os.path.join(level)
        if os.path.exists(folder):
            counts[level] = len([
                d for d in os.listdir(folder)
                if os.path.isdir(os.path.join(folder, d)) and not d.startswith(".")
            ])
        else:
            counts[level] = 0
    return counts

def generate_pie_chart(counts):
    labels = []
    sizes = []

    for key, count in counts.items():
        if count > 0:
            labels.append(f"{key.capitalize()} ({count})")
            sizes.append(count)

    if not sizes:
        print("⚠️ No problems found to plot.")
        return

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("LeetCode Progress by Difficulty")
    plt.axis("equal")

    os.makedirs(ASSETS_DIR, exist_ok=True)
    plt.savefig(IMAGE_PATH, bbox_inches='tight')
    plt.close()

    print(f"✅ Pie chart saved to {IMAGE_PATH}")

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

    print("✅ README.md updated with latest progress chart.")

def main():
    counts = count_problems()
    generate_pie_chart(counts)
    update_readme()

if __name__ == "__main__":
    main()
