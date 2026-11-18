from pypdf import PdfReader
from backend.constants import DATA_PATH


def extract_text_from_pdf(path) -> str:
    all_text = ""

    reader = PdfReader(path) # create a PdfReader object
    for page in reader.pages: # loop throough the pages
        text = page.extract_text() # extract the text from the page
        if text: # check if the text is not empty
            all_text += text + "\n" # add the text to the all_text variable - concatinted - later we can export or open it as a txt file

    return all_text

def export_txt(text, path):
    with open(path, "w") as f:
        f.write(text)

if __name__ == "__main__":
    for pdf_path in DATA_PATH.glob("*.pdf"): # loop through all pdf files in the data folder
        pdf_text = extract_text_from_pdf(pdf_path) # extract the text from the pdf file 

        filename = pdf_path.stem + ".txt" # GET the FILENAME without the extension and add .txt

        export_txt(pdf_text, DATA_PATH / filename) # EXPORT the TEXT to a txt file in the data folder
   

    #uv run pdfs_to_text.py from main folder to run this script
    # data from ddfs are exported to data folder as txt files