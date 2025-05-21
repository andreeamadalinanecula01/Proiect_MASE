from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

AREA_TYPE = (
    (0,"Protejata"),
    (1,"Neprotejata")
)

class ArieNaturala(models.Model):
    nume_arie = models.CharField(max_length=200)
    tip_arie = models.IntegerField(choices=AREA_TYPE)
    judet_arie = models.CharField(max_length=200)
    localitate_arie = models.CharField(max_length=200)
    descriere = RichTextUploadingField(blank=True, null=True)  # descriere nouă
    imagine = models.ImageField(upload_to='arii/', blank=True, null=True)  # imagine
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = "Arii Naturale"

    def __str__(self):
        return self.nume_arie

class DateGeografice(models.Model):
    arie_naturala = models.OneToOneField(ArieNaturala, on_delete=models.CASCADE)
    body = RichTextUploadingField()

    class Meta:
        verbose_name_plural = "Date Geografice"
class DateHidrografice(models.Model):
    arie_naturala = models.OneToOneField(ArieNaturala, on_delete=models.CASCADE)
    body = RichTextUploadingField()

    class Meta:
        verbose_name_plural = "Date Hidrografice"

class DateSpeologice(models.Model):
    arie_naturala = models.OneToOneField(ArieNaturala, on_delete=models.CASCADE)
    body = RichTextUploadingField()

    class Meta:
        verbose_name_plural = "Date Speologice"

class DateForestiere(models.Model):
    arie_naturala = models.OneToOneField(ArieNaturala, on_delete=models.CASCADE)
    body = RichTextUploadingField()

    class Meta:
        verbose_name_plural = "Date Forestiere"


class DateBiodiversitate(models.Model):
    arie_naturala = models.OneToOneField(ArieNaturala, on_delete=models.CASCADE)
    body = RichTextUploadingField()

    class Meta:
        verbose_name_plural = "Date Biodiversitate"

class Post(models.Model):
            title = models.CharField(max_length=200)
            body = RichTextUploadingField()
            author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
            updated_on = models.DateTimeField(auto_now=True)
            created_on = models.DateTimeField(auto_now_add=True)
            cover_image = models.ImageField(upload_to='images/', blank=True, null=True)
            status = models.IntegerField(choices=STATUS, default=0)
            arie_naturala = models.ForeignKey(ArieNaturala, on_delete=models.DO_NOTHING, limit_choices_to={'status': 1})

            class Meta:
                ordering = ['-created_on']

            def __str__(self):
                return self.title

class Discussion(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    arie_discutie = models.ForeignKey(ArieNaturala, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='comments')
    body = RichTextUploadingField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.created_at}'

class Petition(models.Model):
    arie_naturala = models.ForeignKey(ArieNaturala, on_delete=models.CASCADE)
    titlu = models.CharField(max_length=200)
    campanie_initiata_de = models.CharField(max_length=100)
    text_petitie = RichTextUploadingField()

class Signature(models.Model):
    petition = models.ForeignKey(Petition, on_delete=models.CASCADE)
    nume = models.CharField(max_length=100)
    prenume = models.CharField(max_length=100)
    adresa_email = models.EmailField()
    judet = models.CharField(max_length=100)
    numar_telefon = models.CharField(max_length=15)
 
 
