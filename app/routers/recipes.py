from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import schemas, crud
from typing import Union

router = APIRouter(prefix="/recipes", tags=["Recipes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=schemas.RecipeListResponse)
def list_recipes(db: Session = Depends(get_db)):
    recipes = crud.get_recipes(db)
    return {"recipes": recipes}

@router.get("/{id}", response_model=schemas.RecipeDetailsResponse)
def get_recipe(id: str, db: Session = Depends(get_db)):
    recipe = crud.get_recipe(db, id)
    if not recipe:
        raise HTTPException(status_code=404, detail="Not found")
    return {
        "message": "Recipe details by id",
        "recipe": [recipe]  # リストとして返す
    }

@router.post("/", response_model=Union[schemas.RecipeCreateResponse, schemas.RecipeCreateErrorResponse])
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    try:
        # 必須フィールドのチェック（空文字はNG、0はOK）
        empty_str_fields = any(
            isinstance(getattr(recipe, f), str) and getattr(recipe, f).strip() == ""
            for f in ("title", "making_time", "serves", "ingredients")
        )
        if empty_str_fields or recipe.cost is None:
            err = schemas.RecipeCreateErrorResponse(
                message="Recipe creation failed!",
                required="title, making_time, serves, ingredients, cost"
            )
            return JSONResponse(status_code=200, content=err)

        created_recipe = crud.create_recipe(db, recipe)
        return {
            "message": "Recipe successfully created!",
            "recipe": [created_recipe]
        }

    except Exception:
        err = schemas.RecipeCreateErrorResponse(
            message="Recipe creation failed!",
            required="title, making_time, serves, ingredients, cost"
        )
        return JSONResponse(status_code=200, content=err)

@router.patch("/{id}", response_model=schemas.RecipeUpdateResponse)
def update_recipe(id: str, recipe: schemas.RecipeUpdate, db: Session = Depends(get_db)):
    updated = crud.update_recipe(db, id, recipe)
    if not updated:
        return HTTPException(
                status_code=404,
                message="Not found!"
        )
    return {
        "message": "Recipe successfully updated!",
        "recipe": [updated]  # リストとして返す
    }

@router.delete("/{id}")
def delete_recipe(id: str, db: Session = Depends(get_db)):
    ok = crud.delete_recipe(db, id)
    if not ok:
        return HTTPException(
                status_code=404,
                message="No Recipe found"
        )
    return {  "message": "Recipe successfully removed!" }
