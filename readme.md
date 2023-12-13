# 说明 (Description)
## 文件1: trim_pics.py (File 1: trim_pics. py)
这是一个用于处理 Markdown 文件的 Python 脚本，名为 `trim_pics.py`。该脚本的目的是去除 Markdown 文件中包含图片的行，并过滤以 "【"、"[" 开头的行。
 This is a Python script for processing the Markdown file, named ` trim_pics. py '. The purpose of this script is to remove lines from the Markdown file that contain pictures and filter lines that begin with "" "," [".
### 使用方法 (Usage)
1. 将待处理的 Markdown 文件放置在与脚本相同的目录下，例如命名为 `original.md`。
 Place the Markdown file to be processed in the same directory as the script, for example, named ` original.md '.
2. 运行 `trim_pics.py` 脚本，它将生成一个新的 Markdown 文件，例如 `trimed.md`，其中不包含图片行和以 "【"、"[" 开头的行。
 Run the ` trim_pics. py ` script, which generates a new Markdown file, such as ` trimed. md `, which does not contain the picture lines and lines beginning with "" "," [".
## 文件2: translate_each_below.py (File 2: translate_each_below. py)
这是一个用于翻译 Markdown 文件的 Python 脚本，名为 `translate_each_below.py`。脚本使用 NiuTrans API 进行翻译，并具有处理数字序号、引用块、表格以及代码块的逻辑。
 This is a Python script for translating the Markdown file, called ` translate_each_below. py '. Scripts are translated using the NiuTrans API and have logic to handle numeric ordinal numbers, reference blocks, tables, and code blocks.
在翻译时，脚本会将源语言和目标语言的文本排列在一起，以便更清晰地展示翻译前后的对应关系。对于表格和代码块，不做翻译。
 When translating, the script arranges the text in the source language and the target language together to show the correspondence before and after translation more clearly. For tables and code blocks, do not translate.
### 使用方法 (Usage)
1. 将待翻译的 Markdown 文件放置在与脚本相同的目录下，例如命名为 `original.md`。
 Place the Markdown file to be translated in the same directory as the script, for example, named ` original.md '.
2. 运行 `translate_each_below.py` 脚本，它将生成一个新的翻译后的 Markdown 文件，例如 `translated.md`。
 Run the ` translate_each_below. py ` script, which generates a new translated Markdown file, such as ` translated.md '.
