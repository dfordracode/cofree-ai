import sys

print("=" * 60)
print("Python Environment Test")
print("=" * 60)

print(f"Python Version : {sys.version}")

packages = [
    "numpy",
    "pandas",
    "scipy",
    "matplotlib",
    "sklearn",
    "pymatgen",
    "matminer",
    "mp_api",
    "ase",
    "optuna",
    "plotly",
    "shap",
]

for package in packages:
    try:
        __import__(package)
        print(f"[PASS] {package}")
    except Exception as e:
        print(f"[FAIL] {package}")
        print(e)

print("=" * 60)