import pypdf

def extract_text_from_pdf(pdf_path):
    try:
        reader = pypdf.PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    pdf_path = "G ROSHNI PROFFESIONAL RESUME.pdf"
    content = extract_text_from_pdf(pdf_path)
    with open("resume_text.txt", "w", encoding="utf-8") as f:
        f.write(content)
    print("Extraction complete. Check resume_text.txt")
