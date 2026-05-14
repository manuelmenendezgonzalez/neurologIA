import importlib
import platform
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent

IMPORT_NAMES = {
    "pandas": "pandas",
    "numpy": "numpy",
    "scipy": "scipy",
    "statsmodels": "statsmodels",
    "scikit-learn": "sklearn",
    "imbalanced-learn": "imblearn",
    "joblib": "joblib",
    "matplotlib": "matplotlib",
    "seaborn": "seaborn",
    "plotly": "plotly",
    "kaleido": "kaleido",
    "jupyter": "jupyter",
    "ipykernel": "ipykernel",
    "nbconvert": "nbconvert",
    "nbformat": "nbformat",
    "jsonschema": "jsonschema",
    "referencing": "referencing",
    "rpds-py": "rpds",
    "papermill": "papermill",
    "python-pptx": "pptx",
    "fpdf2": "fpdf",
    "xlsxwriter": "xlsxwriter",
    "openpyxl": "openpyxl",
    "tabulate": "tabulate",
    "jinja2": "jinja2",
    "streamlit": "streamlit",
    "pyyaml": "yaml",
    "pyalex": "pyalex",
    "biopython": "Bio",
    "habanero": "habanero",
    "bibtexparser": "bibtexparser",
    "langchain": "langchain",
}


def load_requirements():
    reqs = []
    for raw_line in (ROOT / "requirements.txt").read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        reqs.append(line)
    return reqs


def find_quarto():
    candidates = [
        shutil.which("quarto"),
        shutil.which("quarto.cmd"),
        Path.home() / "AppData" / "Local" / "Apps" / "Quarto" / "bin" / "quarto.exe",
        Path("C:/Program Files/Quarto/bin/quarto.exe"),
    ]
    for candidate in candidates:
        if not candidate:
            continue
        path = Path(candidate)
        if path.exists():
            return path
    return None


def run_command(command):
    try:
        completed = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
        )
        return True, completed.stdout.strip() or completed.stderr.strip()
    except Exception as exc:
        return False, str(exc)


def check_python_packages():
    missing = []
    for req in load_requirements():
        module_name = IMPORT_NAMES.get(req, req.replace("-", "_"))
        try:
            importlib.import_module(module_name)
        except Exception:
            missing.append(req)
    return missing


def check_course_files():
    required_paths = [
        ROOT / "requirements.txt",
        ROOT / "GUIA_ALUMNOS.md",
        ROOT / "Set_Alzheimer" / "base_datos_alzheimer.csv",
        ROOT / "Set_Alzheimer" / "alzheimer_utils.py",
        ROOT / "Set_Alzheimer" / "preguntas_ejercicios_ALZ.md",
        ROOT / "Set_Alzheimer" / "Soluciones_y_Ejemplos" / "generar_datos_alzheimer.py",
    ]
    return [str(path.relative_to(ROOT)) for path in required_paths if not path.exists()]


def python_is_free_threaded():
    executable_name = Path(sys.executable).name.lower()
    version_tag = getattr(sys, "abiflags", "")
    return executable_name.endswith("t.exe") or "t" in version_tag


def main():
    print("NeuroIA environment check")
    print("=" * 32)
    print(f"Python: {sys.version.split()[0]}")
    print(f"Executable: {sys.executable}")
    print(f"Platform: {platform.system()} {platform.release()}")
    print()

    if python_is_free_threaded():
        print("Python build: NOT RECOMMENDED")
        print("Use standard python.exe, not the free-threaded python3.13t.exe build.")
    else:
        print("Python build: OK")

    missing_packages = check_python_packages()
    print()
    if missing_packages:
        print("Python packages: MISSING")
        for pkg in missing_packages:
            print(f" - {pkg}")
    else:
        print("Python packages: OK")

    missing_files = check_course_files()
    print()
    if missing_files:
        print("Course files: MISSING")
        for path in missing_files:
            print(f" - {path}")
    else:
        print("Course files: OK")

    ok_jupyter, out_jupyter = run_command(["jupyter", "--version"])
    print()
    if ok_jupyter:
        print("Jupyter: OK")
        print(out_jupyter.splitlines()[0])
    else:
        print("Jupyter: MISSING OR BROKEN")
        print(out_jupyter)

    quarto_path = find_quarto()
    print()
    if quarto_path:
        ok_quarto, out_quarto = run_command([str(quarto_path), "--version"])
        if ok_quarto:
            print("Quarto: OK")
            print(f"Path: {quarto_path}")
            print(f"Version: {out_quarto}")
        else:
            print("Quarto: FOUND BUT NOT RUNNABLE")
            print(f"Path: {quarto_path}")
            print(out_quarto)
    else:
        ok_quarto = False
        print("Quarto: MISSING")
        print("Install from https://quarto.org/docs/download/")

    print()
    print("Windows note for Exercise 17:")
    print("If Quarto tries to use python3.13t.exe, set QUARTO_PYTHON to your standard python.exe first.")

    if missing_packages or missing_files or not ok_jupyter or not ok_quarto or python_is_free_threaded():
        print()
        print("Overall status: NOT READY")
        raise SystemExit(1)

    print()
    print("Overall status: READY")


if __name__ == "__main__":
    main()
