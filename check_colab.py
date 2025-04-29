import nbformat

notebook_path = "translation_RAG_opt.ipynb"

try:
    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
    print("Notebook is valid.")
except Exception as e:
    print(f"Notebook validation failed: {e}")