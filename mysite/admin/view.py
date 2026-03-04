from sqladmin import ModelView
from mysite.db.models import UserProfile, Category, Product


class UserProfileView(ModelView, model=UserProfile):
    column_list = [UserProfile.id, UserProfile.username, UserProfile.phone_number]

class CategoryView(ModelView, model=Category):
    column_list = [Category.category_name]

class ProductView(ModelView, model=Product):
    column_list = [Product.id, Product.product_name]
