import os
import shutil

# Define the updated file structure
structure = {
    "backend": ["ocr", "nlp", "api", "db", "models", "tests"],
    "frontend": ["dashboard", "api", "auth", "tests"],
    "deployment": ["docker", "k8s", "CI-CD", "security", "logs", "monitoring"],
    "docs": ["STRATEGY.md", "roadmap.md", "api-docs.md", "tech-stack.md", "installation.md", "contribution.md", "media", "advocacy"],
    "scripts": [],
    ".github": ["workflows", "ISSUE_TEMPLATE.md", "PULL_REQUEST_TEMPLATE.md", "CODE_OF_CONDUCT.md"],
}

# Root files that need to be in place
root_files = ["README.md", "LICENSE", "CONTRIBUTING.md", "CHANGELOG.md", "ROADMAP.md"]

# Function to create directories and files
def create_structure():
    for parent, subdirs in structure.items():
        os.makedirs(parent, exist_ok=True)
        for sub in subdirs:
            path = os.path.join(parent, sub)
            if ".md" in sub:  # Create markdown documentation files
                with open(path, "w") as f:
                    f.write(f"# {sub.replace('.md', '').replace('-', ' ').title()}\n\n")
            else:
                os.makedirs(path, exist_ok=True)

    # Create root files
    for file in root_files:
        if not os.path.exists(file):
            with open(file, "w") as f:
                f.write(f"# {file.replace('.md', '').title()}\n\n")

    print("✅ Repository structure updated successfully.")

# Function to clean up incorrect directories
def clean_old_structure():
    remove_dirs = [
        "backend/ai_ocr", "backend/automation", "backend/integrations", "backend/verification"
    ]
    for d in remove_dirs:
        if os.path.exists(d):
            shutil.rmtree(d)
            print(f"🗑️ Removed old directory: {d}")

if __name__ == "__main__":
    clean_old_structure()
    create_structure()
