import os
import re
import sys

def remove_comments(content):
    # Pattern to capture strings (so we don't remove # inside them) or comments
    pattern = r"(\".*?\"|\'.*?\')|(#.*)"
    
    def replace(match):
        if match.group(1):
            return match.group(1) # It's a string, keep it
        return "" # It's a comment, remove it

    lines = content.split('\n')
    new_lines = []
    for line in lines:
        # Simple removal of full line comments (most common in my generations)
        stripped = line.strip()
        if stripped.startswith('#'):
            continue
        
        # Initial check for inline comments using simple split if no quotes
        if '#' in line and '"' not in line and "'" not in line:
            line = line.split('#')[0].rstrip()
            
        new_lines.append(line)
        
    return '\n'.join(new_lines)

def process_directory(directory):
    if not os.path.exists(directory):
        print(f"Directory not found: {directory}")
        return

    print(f"Processing {directory}...")
    for root, dirs, files in os.walk(directory):
        # Skip venv
        if '.venv' in root:
            continue
            
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    new_content = remove_comments(content)
                    
                    # Remove multiple empty lines
                    new_content = re.sub(r'\n\s*\n', '\n\n', new_content)
                    
                    if content != new_content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Cleaned {file}")
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    dirs = [
        "Real-Time Object Detection",
        "Multi-Language Chatbot",
        "Stock Price Prediction"
    ]
    base_path = "d:\\lpu\\project ml"
    
    for d in dirs:
        process_directory(os.path.join(base_path, d))
