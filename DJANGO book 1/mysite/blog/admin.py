from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "slug",
        "author",
        "publish",
        "status",
    ]  # отображаемы поля списка постов
    list_filter = [
        "status",
        "created",
        "publish",
        "author",
    ]  # правая боковая панель, позволяет фильтровать по полям
    search_fields = [
        "title",
        "body",
    ]  # строка поиска. Список полей по которым можно выполнять поиск
    prepopulated_fields = {
        "slug": ("title",)
    }  # при вводе поля title, поле slug заполняется автоматически
    raw_id_fields = ["author"]  # поисковый виджет по полю
    date_hierarchy = "publish"  # навигационные ссылки для навигации по иерархии дат
    ordering = [
        "status",
        "publish",
    ]  # правая боковая панель, критерии сортировки по умолчанию
