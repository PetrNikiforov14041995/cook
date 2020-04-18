def cook_book(reading):
    with open('recept.txt', encoding='utf-8') as f:
      while True:
        book = f.readline()
        if not book:
          break
        if book.strip() != "":
          reading[book.strip()] = []
          read = int(f.readline().strip())

          for i in range(read):
            ingr = f.readline().strip().split(' | ')
            reading[book.strip()].append({"ingridient_name": ingr[0], "quantity": int(ingr[1]), "measure": ingr[2]})


def get_shop_list_by_dishes(dishes, person_count, reading):
  order = {}
  for d in dishes:
    for ingr in reading[d]:
      if ingr ["ingridient_name"] not in order.keys():
        order[ingr["ingridient_name"]] = {"measure": ingr["measure"], "quantity": ingr["quantity"] * person_count}
      else:
        order[ingr["ingridient_name"]]["quantity"] += ingr["quantity"] * person_count
  return order

def main():
  reading = {}
  cook_book(reading)
  print(reading)
  print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, reading))

if __name__ == "__main__":
  main()  
