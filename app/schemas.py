from pydantic import BaseModel
from datetime import datetime

class RecipeBase(BaseModel):
    title: str
    making_time: str
    serves: str
    ingredients: str
    cost: int

class RecipeCreate(RecipeBase):
    pass

class RecipeUpdate(BaseModel):
    title: str | None = None
    making_time: str | None = None
    serves: str | None = None
    ingredients: str | None = None
    cost: int | None = None

class Recipe(BaseModel):
    id: int
    title: str
    making_time: str
    serves: str
    ingredients: str
    cost: int

    class Config:
        orm_mode = True

class RecipeWithTimestamp(Recipe):
    created_at: datetime
    updated_at: datetime

class RecipeCreateResponse(BaseModel):
    message: str
    recipe: list[RecipeWithTimestamp]

class RecipeCreateErrorResponse(BaseModel):
    message: str
    required: str

class RecipeListResponse(BaseModel):
    recipes: list[Recipe]

class RecipeDetailsResponse(BaseModel):
    message: str
    recipe: list[Recipe]

class RecipeUpdateResponse(BaseModel):
    message: str
    recipe: list[Recipe]