import csv
import pathlib

def use_aeropuerto():
    aeropuerto_path = pathlib.Path("./custom_datasets/processed_airports.csv")
    with open (aeropuerto_path, mode='r', encoding= 'utf-8') as read_aeropuerto:
        reader_aeropuerto = csv.DictReader(read_aeropuerto.readlines())
    return reader_aeropuerto

def use_lagos():
    lagos_path = pathlib.Path("./custom_datasets/lagos_arg.csv")
    with open (lagos_path, mode='r', encoding= 'utf-8') as read_lagos:
        reader_lagos = csv.DictReader(read_lagos.readlines())
    return reader_lagos

def use_conectividad():
    conectividad_path = pathlib.Path("./custom_datasets/Conectividad_Internet.csv")
    with open (conectividad_path, mode='r', encoding= 'utf-8') as read_conectividad:
        reader_conectividad = csv.DictReader(read_conectividad.readlines())
    return reader_conectividad

def use_resumen_adaptado():
    resumen_adaptado_path = pathlib.Path("./custom_datasets/c2022_tp_c_resumen_adaptado.csv")
    with open (resumen_adaptado_path, mode='r', encoding= 'utf-8') as read_resumen_adaptado:
        reader_resumen_adaptado = csv.DictReader(read_resumen_adaptado.readlines())
    return reader_resumen_adaptado

def use_ar():
    ar_path = pathlib.Path("./datasets/ar.csv")
    with open ( ar_path, mode='r', encoding= 'utf-8') as read_ar:
        reader_ar = csv.DictReader(read_ar.readlines())
    return reader_ar