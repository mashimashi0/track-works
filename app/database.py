from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ✅ MySQL に変更
# 例: root / パスワードなし / ローカル の場合
DATABASE_URL = "mysql+pymysql://root:hogehoge1234@127.0.0.1:3306/recipes_db"
engine = create_engine(DATABASE_URL, echo=True, future=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
