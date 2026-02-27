from sqladmin import ModelView
from db.models import TextBlock

class TextBlockView(ModelView, model=TextBlock):
    name_plural = "Текст на сайте"

    column_list = [
        TextBlock.textblock_id,
        TextBlock.title,
        TextBlock.body,
        TextBlock.slug,
        TextBlock.created_at,
        TextBlock.updated_at,
    ]

    form_excluded_columns = [
        TextBlock.textblock_id,
        TextBlock.created_at,
        TextBlock.updated_at,
    ]


    column_labels = {
        TextBlock.slug: "Краткое название",
    }

    form_create_fields = [
        TextBlock.title,
        TextBlock.body,
        TextBlock.slug,
    ]

    form_edit_fields = [
        TextBlock.title,
        TextBlock.body,
        TextBlock.slug,
    ]

    column_editable_list = []

    column_searchable_list = [TextBlock.title, TextBlock.slug]

    column_sortable_list = [TextBlock.title, TextBlock.slug]

