from sqladmin import ModelView

from db.models import News


class NewsAdmin(ModelView, model=News):
    name = "Новость"
    name_plural = "Новости"
    icon = "fa-solid fa-newspaper"

    column_list = [
        News.news_id,
        News.title,
        News.body,
        News.image_link,
        News.created_at,
        News.updated_at,
        News.is_active,
    ]

    form_excluded_columns = [
        News.news_id,
        News.created_at,
        News.updated_at,
    ]

    column_labels = {
        News.news_id: "Идентификатор новости",
        News.title: "Заголовок",
        News.body: "Текст",
        News.image_link: "Картинка новости",
        News.created_at: "Дата создания",
        News.updated_at: "Дата обновления",
        News.is_active: "Активно",
    }

    column_default_sort = [(News.created_at, True)]

    form_create_fields = [
        News.title,
        News.body,
        News.image_link,
        News.is_active,
    ]

    form_edit_fields = [
        News.title,
        News.body,
        News.image_link,
        News.is_active,
    ]

    column_editable_list = [News.is_active]

    column_searchable_list = [News.title]

    column_sortable_list = [News.title, News.created_at, News.updated_at]

    form_args = {
        "title": {
            "label": "Заголовок новости",
            "render_kw": {
                "placeholder": "Введите заголовок...",
                "style": "width: 100%; max-width: 800px;",
            },
        },
        "body": {
            "label": "Текст новости",
            "render_kw": {
                "placeholder": "Введите текст новости...",
                "rows": 15,
                "style": "width: 100%; max-width: 1000px;",
            },
        },
        "image_link": {
            "label": "Ссылка на изображение",
            "render_kw": {
                "placeholder": "https://...",
                "style": "width: 100%; max-width: 600px;",
            },
        },
    }

    form_widget_args = {
        "body": {
            "class": "form-control textarea-resizable",
        },
    }



