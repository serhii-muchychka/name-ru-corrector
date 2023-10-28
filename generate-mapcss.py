import codecs

with codecs.open("ua-name-ru.validator.mapcss", mode="w", encoding="utf-8") as mapcss_file:
  with codecs.open("ua-name-ru.validator.mapcss.head.txt", encoding="utf-8") as head_file:
    mapcss_file.write(head_file.read())

  with codecs.open("translations.txt", encoding='utf-8') as translations_file:
    for line in translations_file:
      name_uk, name_ru = line.strip().split(';', 2)
      pattern = '''way[highway]["name:ru"][inside("UA")][name="{0}"]["name:ru"!="{1}"],
relation[type=associatedStreet]["name:ru"][inside("UA")][name="{0}"]["name:ru"!="{1}"] {{
  throwWarning: tr("У назві «{0}» name:ru повинен бути «{1}» замість «{{1}}»", "{{1.value}}");
  group: tr("Російська назва не відповідає правилам перекладу власних назв");
  fixAdd: "name:ru={1}";
}}
'''
      mapcss_file.write(pattern.format(name_uk, name_ru))
