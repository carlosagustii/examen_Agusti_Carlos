from typing import Literal
from pydantic import BaseModel, ConfigDict, Field, field_validator


class Entrada(BaseModel):
    model_config = ConfigDict(extra="forbid") 
    id_paquete: str = Field(min_length=1 ) 
    peso_kg: float = Field(ge=0, le=30)
    distancia_km: float = Field(ge=0, le=200)

    @field_validator("id_paquete", mode="before") 
    @classmethod
    def quitar_espacios(cls, value):
            if isinstance(value, str):
                return value.strip()
            return value
    pass


class Salida(BaseModel):
    id_paquete: str = Field(min_length=1)
    categoria: Literal['normal', 'urgente']
    confianza: float = Field(ge=0, le=1)
    pass


