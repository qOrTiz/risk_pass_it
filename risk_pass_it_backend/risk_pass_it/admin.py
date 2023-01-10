from django.contrib import admin

from .models import *




admin.site.register(Probability_Impact)
admin.site.register(Probability)
admin.site.register(Impact)
admin.site.register(Department_Objective)
admin.site.register(Department_Goal)
admin.site.register(Department_Object)

@admin.register(Risk)
class RiskAdmin(admin.ModelAdmin):
    list_display = ('id', 'risk_name', 'risk_object')
    list_filter = ('risk_name', 'risk_object')
    #raw_id_fields = ('category', 'subcategory')
    search_fields = ('risk_name', 'risk_object', 'departament__text', 'departament_goal__text', 'department_object__text', 'risk_description')
    #list_editable = ('price', 'quantity')
    save_on_top = True
    save_as = True
    fieldsets = (
        ('Основные настройки риска', {
            'fields': (('risk_name', 'risk_object',),)
        }),
        ('Настройки департаментов', {
            'fields': ('departament', 'departament_goal', 'department_object')
        }),
        ('Настройки оценки риска', {
            'fields': ('probability', 'impact')
        }),
        ('Настройки', {
            'fields': ('risk_description', 'probability_max', 'risk_owner', 'registration_date')
        }),
    )




admin.site.register(Final_assessment_of_effectiveness)
admin.site.register(Reduce_Probability)
#admin.site.register(Precondition_Outcome)
admin.site.register(Priority_Countermeasure)
admin.site.register(Implementation_Status)
admin.site.register(End_Countermeasure_Implementation)

@admin.register(Countermeasures)
class CountermeasuresAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'countermeasure_coordinator')
    list_filter = ('name', 'countermeasure_coordinator')
    #raw_id_fields = ('category', 'subcategory')
    search_fields = ('name', 'countermeasure_coordinator', 'description')
    list_display_links = ('id', 'name')
    #list_editable = ('price', 'quantity')
    save_on_top = True
    save_as = True
    # fieldsets = (
    #     ('Основные настройки риска', {
    #         'fields': (('risk_name', 'risk_object',),)
    #     }),
    #     ('Настройки департаментов', {
    #         'fields': ('departament', 'departament_goal', 'department_object')
    #     }),
    #     ('Настройки оценки риска', {
    #         'fields': ('probability', 'impact')
    #     }),
    #     ('Настройки', {
    #         'fields': ('risk_description', 'probability_max', 'risk_owner', 'registration_date')
    #     }),
    # )


admin.site.register(Material_Damage)
admin.site.register(Immaterial_Damage)
#admin.site.register(Precondition_Outcome)
admin.site.register(Legal_Relevance)
admin.site.register(Risk_response_strategie)
admin.site.register(Risk_manager)

@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'risk_id')
    list_filter = ('id', 'risk_id')
    #raw_id_fields = ('category', 'subcategory')
    search_fields = ('id', )
    list_display_links = ('id', 'risk_id')
    #list_editable = ('price', 'quantity')
    save_on_top = True
    save_as = True


@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    list_display = ('id', 'risk_id', 'assessment_id', 'countermeasures_id')
    list_filter = ('id', 'risk_id__risk_name')
    #raw_id_fields = ('category', 'subcategory')
    search_fields = ('id', )
    list_display_links = ('id', 'risk_id')
    #list_editable = ('price', 'quantity')
    save_on_top = True
    save_as = True