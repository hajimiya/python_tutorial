from pathlib import Path

folder = Path("practice_data")
folder.mkdir(exist_ok=True)
file_path = folder / "hello.txt"
file_path.write_text("Written using pathlib.", encoding="utf-8")
print(file_path.read_text(encoding="utf-8"))
print("Exists:", file_path.exists())
print("File name:", file_path.name)
