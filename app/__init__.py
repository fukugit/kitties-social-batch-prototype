import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = 'postgresql+pg8000://{user}:{password}@{host}/{name}'.format(**{
    'user': 'postgres.zvuhoviybhrsppmznzmk',
    'password': 'dSqJfrLHJucwLFtY',
    'host': 'aws-0-ap-northeast-1.pooler.supabase.com:6543',
    'name': 'postgres'
})

# データベースエンジンの作成（PostgreSQLの例）
DATABASE_URI = SQLALCHEMY_DATABASE_URI
engine = create_engine(DATABASE_URI)

# 基底クラスの作成
Base = declarative_base()
Base.metadata.create_all(bind=engine)

# セッションの設定
SessionLocal = sessionmaker(bind=engine)
