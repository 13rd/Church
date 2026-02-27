from sqladmin import Admin
from api.admin.news import NewsAdmin
from api.admin.textblock import TextBlockView



def register_admin_views(admin: Admin):
    admin.add_view(NewsAdmin)
    admin.add_view(TextBlockView)