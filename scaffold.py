import os

project_root = "BharatTranslate"

structure = {
    "frontend": {
        "public": ["index.html"],
        "src": {
            "components": [
                "LanguageSelector.jsx",
                "TextInput.jsx",
                "TranslationOutput.jsx",
                "VoiceInput.jsx",
                "Navbar.jsx",
            ],
            "pages": ["Home.jsx", "History.jsx", "Settings.jsx"],
            "services": ["api.js"],
            "utils": ["languageList.js"],
            "": ["App.jsx", "main.jsx", "index.css"],
        },
        "": ["package.json", "tailwind.config.js"],
    },
    "backend": {
        "app": {
            "api": ["routes_translate.py", "routes_detect.py", "routes_history.py"],
            "core": ["config.py", "logging.py"],
            "models": ["load_model.py", "inference.py", "tokenizer.py"],
            "services": [
                "translation_service.py",
                "language_service.py",
                "cache_service.py",
            ],
            "schemas": ["translation_schema.py", "language_schema.py"],
            "db": ["database.py", "models.py"],
            "": ["main.py", "dependencies.py"],
        },
        "": ["requirements.txt", "Dockerfile"],
    },
    "ml": {
        "data": {
            "raw": [],
            "processed": [],
            "": ["datasets.md"],
        },
        "preprocessing": ["clean_text.py", "tokenizer.py", "build_dataset.py"],
        "training": ["train.py", "fine_tune.py", "config.yaml"],
        "evaluation": ["bleu_score.py", "rouge_score.py", "metrics.py"],
        "models": {
            "saved_models": [],
        },
        "notebooks": ["experiments.ipynb"],
    },
    "deployment": {
        "docker": ["docker-compose.yml", "nginx.conf"],
        "kubernetes": [
            "backend-deployment.yaml",
            "frontend-deployment.yaml",
            "service.yaml",
        ],
        "ci-cd": ["github-actions.yml"],
    },
    "monitoring": {
        "prometheus": ["prometheus.yml"],
        "grafana": ["dashboards.json"],
        "logs": [],
    },
    "tests": {"backend": [], "frontend": [], "ml": []},
    "docs": ["architecture.md", "api_docs.md", "setup_guide.md"],
    "": [".env", ".gitignore", "README.md", "LICENSE"],
}

def create_structure(base_path, struct):
    for key, value in struct.items():
        if key != "":
            dir_path = os.path.join(base_path, key)
            os.makedirs(dir_path, exist_ok=True)
            if isinstance(value, dict):
                create_structure(dir_path, value)
            elif isinstance(value, list):
                for item in value:
                    open(os.path.join(dir_path, item), "a").close()
        else:
            if isinstance(value, list):
                for item in value:
                    open(os.path.join(base_path, item), "a").close()

if __name__ == "__main__":
    os.makedirs(project_root, exist_ok=True)
    create_structure(project_root, structure)
    print(f"Project structure created at {os.path.abspath(project_root)}")
