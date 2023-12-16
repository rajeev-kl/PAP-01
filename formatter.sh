isort . --skip __init__.py
black . --line-length 120
tree -a -I '.git|.vscode|__pycache__|run|static_cdn|static' > dir.tree
pipenv graph > graph.txt