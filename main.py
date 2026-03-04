from fastapi import FastAPI
from mysite.api import user_profile, category, auth
from mysite.admin.setup import setup_admin



wildberies_app = FastAPI(title='Wildberies-AI15')
wildberies_app.include_router(user_profile.user_router)
wildberies_app.include_router(category.category_router)
wildberies_app.include_router(auth.auth_router)

setup_admin(wildberies_app)









