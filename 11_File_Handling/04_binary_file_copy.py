# Binary mode is useful for copying bytes from files such as images and PDFs.
# Use a small file for this practice example.
source = "sample.txt"
destination = "sample_copy.txt"
with open(source, "rb") as src, open(destination, "wb") as dst:
    dst.write(src.read())
print("Copied:", destination)
