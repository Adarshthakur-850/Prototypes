import os

project_root = "mini-log-analytics"

structure = {
    "frontend": {
        "src": [],
    },
    "backend": [],
    "prometheus": [],
    "grafana": [],
    "kubernetes": {
        "deployments": [],
        "services": [],
        "configmaps": [],
    }
}

def create_structure(base_path, struct):
    for key, value in struct.items():
        if key != "":
            dir_path = os.path.join(base_path, key)
            os.makedirs(dir_path, exist_ok=True)
            if isinstance(value, dict):
                create_structure(dir_path, value)

if __name__ == "__main__":
    os.makedirs(project_root, exist_ok=True)
    create_structure(project_root, structure)
    print(f"Project structure created at {os.path.abspath(project_root)}")
