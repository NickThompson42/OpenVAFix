import os

# Define the directory structure
structure = {
    "backend": ["ai_ocr", "automation", "integrations", "verification", "db", "models", "tests"],
    "frontend": ["dashboard", "auth", "api", "tests"],
    "deployment": ["docker", "k8s", "CI-CD", "security", "logs", "monitoring"],
    "docs": ["roadmap.md", "api-docs.md", "tech-stack.md", "installation.md", "contribution.md", "media", "advocacy"],
    "scripts": [],
    ".github": ["workflows", "ISSUE_TEMPLATE.md", "PULL_REQUEST_TEMPLATE.md", "CODE_OF_CONDUCT.md"],
}

# Root files
root_files = ["README.md", "LICENSE", "CONTRIBUTING.md", "CHANGELOG.md", "ROADMAP.md"]

# Function to create directories and files
def create_structure():
    for parent, subdirs in structure.items():
        os.makedirs(parent, exist_ok=True)
        for sub in subdirs:
            path = os.path.join(parent, sub)
            if ".md" in sub:
                with open(path, "w") as f:
                    f.write(f"# {sub.replace('.md', '').replace('-', ' ').title()}\n\n")
            else:
                os.makedirs(path, exist_ok=True)
    
    # Create root files
    for file in root_files:
        with open(file, "w") as f:
            f.write(f"# {file.replace('.md', '').title()}\n\n")
    
    print("✅ Repository structure created successfully.")

if __name__ == "__main__":
    create_structure()
