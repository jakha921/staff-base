# Create your models here.
from datetime import date

from django.db import models


class Employee(models.Model):
    full_name = models.CharField("FISH (passport buycha)", max_length=255, help_text="Familiya Ism Sharif")
    date_of_birth = models.DateField("Tug'ilgan sana")

    phone_number = models.CharField("Telefon raqami", max_length=20)
    # email = models.EmailField("Elektron pochta")
    residential_address = models.TextField("Yashash manzili")
    registration_address = models.TextField("Ro'yhatdan o'tgan manzili")

    position = models.CharField("Lavozim", max_length=255)
    department = models.CharField("Kafedra/bo'lim", max_length=255)

    EDUCATION_LEVELS = [
        ('secondary_special', 'O\'rta maxsus'),
        ('secondary', 'O\'rta'),
        ('higher', 'Oliy'),
    ]
    education_level = models.CharField("Ta'lim darajasi", max_length=20, choices=EDUCATION_LEVELS)
    specialty = models.CharField("Mutaxassislik", max_length=255)
    educational_institution = models.CharField("O'quv yurti", max_length=255)
    graduation_year = models.IntegerField("Bitirgan yil", blank=True, null=True)
    photo = models.ImageField("Rasm", upload_to='photos/', blank=True, null=True)

    ACADEMIC_LEVEL = [
        ('bachelor', 'Bakalavr'),
        ('master', 'Magistr'),
        ('phd', 'PhD'),
        ('dsc', 'DsC')
    ]

    academic_degree = models.CharField('Ilmiy daraja', max_length=200, blank=True, null=True, choices=ACADEMIC_LEVEL)

    SCIENTIFIC_TITLE_LEVEL = [
        ("teacher_trainee", "o'qituvchisi stajyor"),
        ("teacher_assistant", "o'qituvchisi(assistent)"),
        ("senior_teacher", "katta o'qituvchis"),
        ("dotsent", "dotsent"),
        ("professor", "professor"),
    ]

    scientific_title = models.CharField('Ilmiy unvon', max_length=255, blank=True, null=True,
                                        choices=SCIENTIFIC_TITLE_LEVEL)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Xodim"
        verbose_name_plural = "Xodimlar"


class ProfessionalExperience(models.Model):
    employee = models.ForeignKey(Employee, related_name='professional_experiences', on_delete=models.CASCADE)
    company_name = models.CharField("Oldingi ish joyi", max_length=255)
    position = models.CharField("Lavozim", max_length=255)
    description = models.TextField("Vazifalar", blank=True, null=True)

    start_date = models.DateField("Boshlanish sanasi")
    end_date = models.DateField("Tugash sanasi", blank=True, null=True)

    class Meta:
        verbose_name = "Professional tajriba"
        verbose_name_plural = "Professional tajribalar"


class Publication(models.Model):
    employee = models.ForeignKey(Employee, related_name='publications', on_delete=models.CASCADE)
    title = models.CharField("Nomi", max_length=255)
    date = models.DateField("Sana")
    description = models.TextField("Tavsif", blank=True, null=True)

    class Meta:
        verbose_name = "Publikatsiya"
        verbose_name_plural = "Publikatsiyalar"


class Skill(models.Model):
    employee = models.ForeignKey(Employee, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField("Malaka va ko'nikmalar", max_length=255)

    class Meta:
        verbose_name = "Ko'nikma"
        verbose_name_plural = "Ko'nikmalar"


class Award(models.Model):
    employee = models.ForeignKey(Employee, related_name='awards', on_delete=models.CASCADE)
    title = models.CharField("Mukofot", max_length=255)
    date = models.DateField("Sana")
    description = models.TextField("Tavsif", blank=True, null=True)

    class Meta:
        verbose_name = "Mukofot"
        verbose_name_plural = "Mukofotlar"


class Certificate(models.Model):
    employee = models.ForeignKey(Employee, related_name='certificates', on_delete=models.CASCADE)
    title = models.CharField("Sertifikat", max_length=255)
    date = models.DateField("Sana")
    description = models.TextField("Tavsif", blank=True, null=True)

    class Meta:
        verbose_name = "Sertifikat"
        verbose_name_plural = "Sertifikatlar"


class Conference(models.Model):
    employee = models.ForeignKey(Employee, related_name='conferences', on_delete=models.CASCADE)
    title = models.CharField("Konferensiya/seminar nomi", max_length=255)
    date = models.DateField("Sana")
    description = models.TextField("Tavsif", blank=True, null=True)

    class Meta:
        verbose_name = "Konferensiya/seminar"
        verbose_name_plural = "Konferensiyalar/seminarlar"


class OrganizationMembership(models.Model):
    employee = models.ForeignKey(Employee, related_name='organization_memberships', on_delete=models.CASCADE)
    organization_name = models.CharField("Tashkilot nomi", max_length=255)
    role = models.CharField("Rol", max_length=255)

    class Meta:
        verbose_name = "Tashkilot a'zosi"
        verbose_name_plural = "Tashkilot a'zolari"


class PersonalDetail(models.Model):
    employee = models.ForeignKey(Employee, related_name='personal_details', on_delete=models.CASCADE)
    hobby = models.CharField("Hobbi va qiziqishlar", max_length=255, blank=True, null=True)
    social_media = models.URLField("Ijtimoiy tarmoqlar", blank=True, null=True)

    class Meta:
        verbose_name = "Shaxsiy ma'lumot"
        verbose_name_plural = "Shaxsiy ma'lumotlar"


class FamilyMember(models.Model):

    family_relation = [
        # turmush o'rtog'i, farzandi
        ('turmush', 'Turmush o\'rtog\'im'),
        ('farzand', 'Farzandim'),
    ]

    employee = models.ForeignKey(Employee, related_name='family_members', on_delete=models.CASCADE)
    full_name = models.CharField("FISH (oila a'zosi)", max_length=255, help_text="Familiya Ism Sharif (passport buycha)")
    dob = models.DateField("Tug'ilgan sana")
    relationship = models.CharField("Qarindoshlik", max_length=20, choices=family_relation, default='turmush')

    class Meta:
        verbose_name = "Oila a'zosi"
        verbose_name_plural = "Oila a'zolari"

    @property
    def age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))

    def age_display(self):
        return self.age
    age_display.short_description = 'Yosh'