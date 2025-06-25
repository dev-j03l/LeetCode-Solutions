import os
import argparse
import requests
import re
from bs4 import BeautifulSoup
from difflib import get_close_matches

GRAPHQL_URL = "https://leetcode.com/graphql"

# Step 1: Get all problems from LeetCode
def fetch_all_problems():
    query = {
        "operationName": "problemsetQuestionList",
        "variables": {
            "categorySlug": "",
            "limit": 2000,
            "skip": 0,
            "filters": {}
        },
        "query": """
        query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
            problemsetQuestionList: questionList(
                categorySlug: $categorySlug
                limit: $limit
                skip: $skip
                filters: $filters
            ) {
                totalNum
                data {
                    questionFrontendId
                    title
                    titleSlug
                    difficulty
                }
            }
        }
        """
    }

    res = requests.post(GRAPHQL_URL, json=query)

    if res.status_code != 200:
        print(f"Error: Received HTTP {res.status_code}")
        print(res.text)
        return []

    try:
        data = res.json()
        return data['data']['problemsetQuestionList']['data']
    except Exception as e:
        print(f"Failed to parse GraphQL response: {e}")
        print("Response content:")
        print(res.text)
        return []


# Step 2: Fuzzy match input
def match_problem(user_input, problems):
    user_input = user_input.lower().replace('.', ' ').replace('-', ' ').replace('_', ' ')
    matches = []

    for p in problems:
        text = f"{p['questionFrontendId']} {p['title']}".lower().replace('-', ' ')
        matches.append((text, p))

    keys = [t[0] for t in matches]
    best_match = get_close_matches(user_input, keys, n=1, cutoff=0.5)

    if not best_match:
        return None
    return dict(matches)[best_match[0]]

# Step 3: Fetch full problem content by slug
def fetch_problem_details(slug):
    query = {
        "operationName": "questionData",
        "variables": {"titleSlug": slug},
        "query": """
        query questionData($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                content
                difficulty
                title
                titleSlug
                questionFrontendId
            }
        }
        """
    }

    res = requests.post(GRAPHQL_URL, json=query)
    return res.json()['data']['question']

# Step 4: Convert HTML to Markdown
def html_to_markdown(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text("\n")

# Step 5: Create file structure
def kebab_case(s):
    return s.lower().replace(" ", "-").replace("'", "")

def create_problem_files(problem):
    number = problem['questionFrontendId']
    title = problem['title']
    slug = problem['titleSlug']
    difficulty = problem['difficulty'].lower()
    url = f"https://leetcode.com/problems/{slug}/"
    description = html_to_markdown(problem['content'])

    folder_name = f"{number}-{kebab_case(title)}"
    base_path = os.path.join(difficulty, folder_name)

    if os.path.exists(base_path):
        print(f"Folder '{base_path}' already exists.")
        return

    os.makedirs(os.path.join(base_path, "solution"))

    readme = f"""# {number}. {title}

**Difficulty:** {difficulty.capitalize()}  
**Link:** [{url}]({url})

## Problem Description

{description}
"""

    with open(os.path.join(base_path, "README.md"), "w") as f:
        f.write(readme)

    with open(os.path.join(base_path, "solution", "solution.py"), "w") as f:
        f.write("""class Solution:
    def method_name(self, *args):
        pass
""")

    print(f"✅ Created: {base_path}/")

# Main script
def main():
    parser = argparse.ArgumentParser(description="Create LeetCode problem folder from fuzzy input.")
    parser.add_argument("query", type=str, help="Problem ID or title (e.g. '1.twosum', '42', 'binary tree max path')")
    args = parser.parse_args()

    print("🔍 Fetching problems...")
    problems = fetch_all_problems()
    matched = match_problem(args.query, problems)

    if not matched:
        print("No matching problem found.")
        return

    print(f"Matched: {matched['questionFrontendId']}. {matched['title']} [{matched['difficulty']}]")
    details = fetch_problem_details(matched['titleSlug'])
    create_problem_files(details)

if __name__ == "__main__":
    main()
