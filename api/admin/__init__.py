from sqladmin import Admin
from api.admin.news import NewsAdmin


def register_admin_views(admin: Admin):
    admin.add_view(NewsAdmin)