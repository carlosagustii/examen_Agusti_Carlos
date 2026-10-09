import csv
from pathlib import Path
import joblib
from .contracts import Entrada, Salida


def leer_csv(ruta: Path) -> list[Entrada]:
    lista_entradas: list[Entrada] = []
    try:
        with open(ruta, mode='r', encoding='utf-8') as archivo:
            lector_csv = csv.DictReader(archivo)
            for fila in lector_csv:
                lista_entradas.append(fila)
    except BaseException as e:
        print(f"Error {e}")
    return lector_csv


def preprocesar(entrada: Entrada) -> list[float]:
    lista_salida=list[float]
    lista_salida.append(entrada["peso_kg"].round(1))
    lista_salida.append(entrada["distancia_km"])
    return lista_salida


def cargar_modelo(ruta: Path):
    joblib.load(ruta)


def predecir(entrada: Entrada, modelo) -> Salida:
    prediccion = modelo.predict_proba(entrada)
    return prediccion


def guardar_csv(resultados: list[Salida], ruta: Path) -> None:
    # TODO
    raise NotImplementedError


def ejecutar(entrada: Path, modelo: Path, salida: Path) -> None:
    # TODO
    raise NotImplementedError


if __name__ == "__main__":
    ejecutar(
        Path("data/raw/paquetes.csv"),
        Path("models/modelo.joblib"),
        Path("resultados.csv"),
    )
