#!/usr/bin/python
import psycopg2
def connect_to_db():
    try:
        from sqlalchemy import schema, types, Table, column, String
        from sqlalchemy.engine import create_engine
        from sqlalchemy.orm import sessionmaker
        from sqlalchemy.sql import select
        metadata = schema.MetaData()
        import psycopg2
        engine=create_engine("postgresql://root:postgres@localhost:5432/testdb")
        connection=engine.connect()
        engine.echo=True
        metadata.bind=engine
        return engine,metadata,connection
    except Exception, e:
        print e
