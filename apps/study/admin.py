from django.contrib import admin
from apps.study.models import Category, Study, StudyBlog, University, UniversityImages
from modeltranslation.admin import TranslationAdmin


class UniversityImagesInline(admin.TabularInline):
    model = UniversityImages
    extra = 1


class UniversityAdmin(TranslationAdmin):
    inlines = [UniversityImagesInline]
    list_display = ('id', 'title', 'created_at')
    readonly_fields = ('created_at',)


class CategoryAdmin(TranslationAdmin):
    pass


class StudyAdmin(TranslationAdmin):
    pass


class StudyBlogAdmin(TranslationAdmin):
    pass


admin.site.register(University, UniversityAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Study, StudyAdmin)
admin.site.register(StudyBlog, StudyBlogAdmin)
