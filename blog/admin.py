from django.contrib import admin
from .models import Post, Comment , AppRegs ,Category,MultiStepFormModel,MultiStepFormModelBr
from import_export.admin import ImportExportModelAdmin

# admin.site.register(Post)
@admin.register(Post)
@admin.register(AppRegs)
@admin.register(Category)
@admin.register(MultiStepFormModel)
@admin.register(MultiStepFormModelBr)


class PostImportExport(ImportExportModelAdmin):
    pass


# admin.site.register(Comment)
@admin.register(Comment)
class CommentImportExport(ImportExportModelAdmin):
    pass
