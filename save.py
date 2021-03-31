import csv

def save_to_file(term, result_db):
  file = open(f"{term}.csv", mode="w", encoding="utf-8")
  writer = csv.writer(file)
  writer.writerow(["title","company","link"])

  for i in result_db:
    writer.writerow(list(i.values()))
  return