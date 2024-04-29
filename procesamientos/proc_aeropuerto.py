import csv
import pathlib

def categorize_elevation(elevation):
    if elevation <= 131:
        return 'bajo'
    elif 131 < elevation <= 903:
        return 'medio'
    else:
        return 'alto'

def process_airports_dataset():

    airports_dataset_path = pathlib.Path("./datasets/ar-airports.csv")
    cities_dataset_path = pathlib.Path("./datasets/ar.csv")
    output_path = pathlib.Path("./custom_datasets/processed_airports.csv")

    city_province_mapping = {}

    with open(cities_dataset_path, mode='r', encoding='utf-8') as cities_file:
        cities_reader = csv.DictReader(cities_file)
        for row in cities_reader:
            city_province_mapping[row['city']] = row['admin_name']

    with open(airports_dataset_path, mode='r', encoding='utf-8') as airports_file, \
            open(output_path, mode='w', encoding='utf-8', newline='') as output_file:
        airports_reader = csv.DictReader(airports_file)
        header = airports_reader.fieldnames + ['elevation_name', 'prov_name']
        writer = csv.DictWriter(output_file, fieldnames=header)
        writer.writeheader()
        
        for row in airports_reader:

            elevation_str = row['elevation_ft']
            elevation_category = categorize_elevation(float(elevation_str)) if elevation_str else 'Desconocido'
            row['elevation_name'] = elevation_category

            city = row['municipality']  #agarro el municipio para buscarlo en las ciudades
            province = city_province_mapping.get(city, "--" + row["region_name"]) #se pone la provincia si se encontro la ciudad por medio del municipio sino mando el dato region_name
            row['prov_name'] = province

            writer.writerow(row)

process_airports_dataset()
