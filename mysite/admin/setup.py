from .view import CategoryView, UserProfileView, ProductView
from sqladmin import Admin
from fastapi import FastAPI
from mysite.db.database import engine

def setup_admin(app: FastAPI):
    admin = Admin(app, engine=engine)
    admin.add_view(CategoryView)
    admin.add_view(UserProfileView)
    admin.add_view(ProductView)


