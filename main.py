import csv

#1-Carga en memoria el archivo sample_grocery.csv, eso se convierte efectivamente en tu fuente de datos.
    
# data = [{'name': 'John Doe', 'age': 30}, {'name': 'Jane Doe', 'age': 25}]
def write_list_of_dicts_to_csv(filename, data):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def read_csv_to_dict(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)
    
#2-Carga en memoria el archivo grocery_batch_1.csv y compara las filas de grocery_batch_1.csv con sample_grocery.csv
    #Si el articulo no existe en tu fuente de datos agregalo.
    #Si el articulo ya existe en la fuente de datos incrementa su valor de cantidad por la suma de ambas cantidades.
def merge_and_update_data(main_data, new_data):
    for new_row in new_data:
        match_found = False
        for main_row in main_data:
            if new_row['SKU'] == main_row['SKU']:
                main_row['Quantity'] = str(int(main_row['Quantity']) + int(new_row['Quantity']))
                match_found = True
                break
        if not match_found:
            main_data.append(new_row)
    return main_data

def main():
    main_data = read_csv_to_dict('sample_grocery.csv')
    new_data = read_csv_to_dict('grocery_batch_1.csv')
    main_data = merge_and_update_data(main_data, new_data)

    #3-Guarda la fuente de datos final en un archivo llamado grocery_db.csv al terminar el punto 2.
    write_list_of_dicts_to_csv('grocery_db.csv', main_data)

if __name__ == '__main__':
    main()
