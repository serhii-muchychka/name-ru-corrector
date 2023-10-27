import codecs

mapcss_file  = codecs.open("ua-name-ru.validator.mapcss", mode="w", encoding="utf8")

head = '''meta {
  title: "name:ru for streets in Ukraine";
  description: "Check and fix name:ru for streets in Ukraine";
  author: "Serhii Muchychka";
  min-josm-version: "11424"; /* due to territory selectors */
  baselanguage: "uk";
}
meta[lang=uk] {
  title: "name:ru для вулиць в Україні";
  description: "Перевірка й коригування name:ru для вулиць в Україні. Приклади виправлень: Красная улица» -> Червоная улица», Пограничная улица» -> Прикордонная улица»";
}
'''
mapcss_file.write(head);

translations_file = open("translations.txt", encoding='utf-8')
for line in translations_file:
  name_uk, name_ru = line.strip().split(';', 2)
  pattern = '''way[highway]["name:ru"][inside("UA")][name="{0}"]["name:ru"!="{1}"],
relation[type=associatedStreet]["name:ru"][inside("UA")][name="{0}"]["name:ru"!="{1}"] {{
  throwWarning: tr(
    "У назві «{0}» name:ru повинен бути «{1}» замість «{{1}}»",
    "{{1.value}}"
  );
  group: tr("Російська назва не відповідає правилам перекладу власних назв");
  fixAdd: "name:ru={1}";
}}
'''
  mapcss_file.write(pattern.format(name_uk, name_ru))
