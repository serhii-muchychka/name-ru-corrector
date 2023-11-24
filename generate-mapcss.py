import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--translations', default='translations/translations.txt', type=argparse.FileType(encoding='utf-8'))
parser.add_argument('-o', '--output', default='ua-name-ru.validator.mapcss', type=argparse.FileType(mode='w', encoding='utf-8'))
parsed_args = parser.parse_args()

with open('ua-name-ru.validator.mapcss.head.txt', encoding='utf-8') as head_file:
  parsed_args.output.write(head_file.read())

for line in parsed_args.translations:
  name_uk, name_ru = line.strip().split(';', 2)
  pattern = '''*["name:ru"][name="{0}"]["name:ru"!="{1}"].base_condition {{
  throwWarning: tr("У назві «{0}» name:ru повинен бути «{1}» замість «{{0}}»", "{{0.value}}");
  group: tr("Російська назва не відповідає правилам перекладу власних назв");
  fixAdd: "name:ru={1}";
}}
'''
  parsed_args.output.write(pattern.format(name_uk, name_ru))
