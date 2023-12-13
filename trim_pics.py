def process_markdown_file(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            lines = input_file.readlines()

        # Filter lines containing images and lines starting with "【"
        lines = [line for line in lines if not line.startswith('![]') and not line.startswith('【') and not line.startswith('[')]

        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.writelines(lines)

        print(f"文件 {input_file_path} 处理成功！副本保存在 {output_file_path}")
    except Exception as e:
        print(f"处理文件 {input_file_path} 时出错：{e}")

# Replace with your file
input_file_path = 'original.md'
output_file_path = 'trimed.md'
process_markdown_file(input_file_path, output_file_path)
