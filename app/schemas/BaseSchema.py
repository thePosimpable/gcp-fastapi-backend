from pydantic import BaseModel
from humps import camelize

def to_camel(val: str):
	return camelize(val)

class BaseSchema(BaseModel):
	class Config:
		orm_mode = True
		alias_generator = to_camel
		allow_population_by_field_name = True
		extra = 'ignore'