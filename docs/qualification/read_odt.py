import zipfile
import xml.etree.ElementTree as ET
import sys

def extract_text_from_odt(file_path):
    with zipfile.ZipFile(file_path, 'r') as zf:
        content = zf.read('content.xml')
    
    root = ET.fromstring(content)
    text_content = []
    
    # Iterate through all elements and extract text
    for elem in root.iter():
        if elem.tag.endswith('}p') or elem.tag.endswith('}h'):
            text = "".join(elem.itertext())
            if text:
                text_content.append(text)
                
    return "\n".join(text_content)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        text = extract_text_from_odt(sys.argv[1])
        print(text)
