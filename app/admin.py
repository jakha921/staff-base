from django.contrib import admin

from .models import (
    Employee, ProfessionalExperience, Publication, Skill, Award,
    Certificate, Conference, OrganizationMembership, PersonalDetail, FamilyMember
)


# Register your models here.

# change the default admin site header
admin.site.site_header = "Xodimlar bazasi"
admin.site.site_title = "Xodimlar bazasi"
admin.site.index_title = "Xodimlar bazasi"

class ProfessionalExperienceInline(admin.StackedInline):
    model = ProfessionalExperience
    extra = 0


class PublicationInline(admin.StackedInline):
    model = Publication
    extra = 0


class SkillInline(admin.StackedInline):
    model = Skill
    extra = 0


class AwardInline(admin.StackedInline):
    model = Award
    extra = 0


class CertificateInline(admin.StackedInline):
    model = Certificate
    extra = 0


class ConferenceInline(admin.StackedInline):
    model = Conference
    extra = 0


class OrganizationMembershipInline(admin.StackedInline):
    model = OrganizationMembership
    extra = 0


class PersonalDetailInline(admin.StackedInline):
    model = PersonalDetail
    extra = 0


class FamilyMemberInline(admin.StackedInline):
    model = FamilyMember
    extra = 0
    fields = ('full_name', 'dob', 'age_display', 'relationship')
    readonly_fields = ('age_display',)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'date_of_birth', 'position', 'department', 'education_level')
    search_fields = ('full_name', 'position', 'department')
    inlines = [
        # ProfessionalExperienceInline,
        # PublicationInline,
        # SkillInline,
        # AwardInline,
        # CertificateInline,
        # ConferenceInline,
        # OrganizationMembershipInline,
        # PersonalDetailInline,
        FamilyMemberInline,
    ]


admin.site.register(Employee, EmployeeAdmin)
