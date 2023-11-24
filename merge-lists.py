import argparse
import warnings

from colorama import init, Fore

# Initializes Colorama
init(autoreset=True)

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--add", type=argparse.FileType(encoding="utf-8"), required=True)
parser.add_argument("-t", "--to", type=argparse.FileType(mode='r+', encoding="utf-8"), default="translations/translations.txt")
parsed_args = parser.parse_args()

from_map = {}
for line in parsed_args.add:
  name_uk, name_ru = line.strip().split(';', 2)
  from_map[name_uk]=name_ru

to_map = {}
for line in parsed_args.to:
  name_uk, name_ru = line.strip().split(';', 2)
  to_map[name_uk]=name_ru

print(to_map.keys())

for name_uk in from_map:
  name_ru = from_map[name_uk]

  if name_uk not in to_map.keys():
    to_map[name_uk] = name_ru
  else:
    old_name_ru = to_map[name_uk]
    if name_ru != old_name_ru:
      print(Fore.RED + "duplicate key:", name_uk, '\nold:', old_name_ru, '\nnew:', name_ru)

parsed_args.to.seek(0)
parsed_args.to.truncate()

for name_uk in sorted(to_map):
  parsed_args.to.write(name_uk)
  parsed_args.to.write(';')
  parsed_args.to.write(to_map[name_uk])
  parsed_args.to.write('\n')

#print(to_map)
