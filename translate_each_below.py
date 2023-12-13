import json
import requests
import re

# change this to your own key   
apikey = "KEY"


def translate(sentence, src_lan, tgt_lan):
    if not sentence:
        return ""

    url = 'https://api.niutrans.com/NiuTransServer/translation'
    data = {"from": src_lan, "to": tgt_lan, "apikey": apikey, "src_text": sentence}
    res = requests.post(url, data=data)
    
    # Add this print statement to see the API response
    print(res.text)
    
    res_dict = json.loads(res.text)
    if "tgt_text" in res_dict:
        result = res_dict['tgt_text']
    else:
        result = str(res)  # Convert Response object to string
    return result


def translate_md_file(file_path, src_lan, tgt_lan, output_file_path='translated_output.md'):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    translated_lines = []
    in_code_block = False

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for line in lines:
            line = line.strip()
            if not line:
                # Ignore empty lines
                continue


            if line.startswith("```"):
                in_code_block = not in_code_block
                translated_lines.append(line)
                output_file.write(f"{line}\n")
            elif in_code_block:
                # If in a code block, keep the line unchanged
                translated_lines.append(line)
                output_file.write(f"{line}\n")
            elif line.strip().startswith("|") and line.strip().endswith("|"):
                # Skip translation for lines in tables
                translated_lines.append(line)
                output_file.write(f"{line}\n")
            elif line.startswith("#"):
                # Translate headers and remove * symbols
                header_text = ' '.join(line.split()[1:]).replace('*', '').strip()
                translated_header = translate(header_text, src_lan, tgt_lan)
                translated_lines.append(f"{line} ({translated_header})")
                output_file.write(f"{line} ({translated_header})\n")
            elif re.match(r'^\d+\.', line):
                # Translate lines starting with numeric indices
                index, rest = re.match(r'^(\d+\.)\s*(.*)', line).groups()
                translated_text = translate(rest, src_lan, tgt_lan)
                translated_lines.append(f"{index} {translated_text}")
                output_file.write(f"{line}\n {translated_text}\n")
            elif line.startswith(">"):
                # Handle lines inside blockquotes
                translated_text = translate(line[1:], src_lan, tgt_lan)
                translated_lines.append(f">{translated_text}")
                output_file.write(f">{line}\n>{translated_text}\n")
            else:
                # Translate other text
                translated_text = translate(line, src_lan, tgt_lan)
                output_file.write(f"{line}\n {translated_text}\n")

    print(f"Translation completed. Results saved in '{output_file_path}'.")

if __name__ == "__main__":
    translate_md_file('original.md', 'auto', 'en', 'translated.md')
