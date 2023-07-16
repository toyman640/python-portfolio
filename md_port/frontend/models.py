from django.db import models

# Create your models here.

class FirstQuote(models.Model):
  id = models.AutoField(primary_key=True)
  first_name = models.CharField(max_length=100, verbose_name='Name')
  first_quote = models.TextField(blank=True, verbose_name='First Quote')

  def __str__(self):
    return self.first_name
    
  class Meta:  
    verbose_name_plural = 'Quote'


class Awards(models.Model):
  id = models.AutoField(primary_key=True)
  award_name = models.CharField(max_length=100, verbose_name='Award Name')
  award_org =  models.CharField(max_length=100, verbose_name='Organization/Body')
  year = models.IntegerField(verbose_name='Year')
  org_image = models.ImageField(verbose_name='Body logo', upload_to='uploads/')

  def __str__(self):
    return self.award_name

  class Meta:  
    verbose_name_plural = 'Award Name'


class Testimonials(models.Model):
  id = models.AutoField(primary_key=True)
  test_name = models.CharField(max_length=100, verbose_name='Name')
  title = models.CharField(max_length=100, verbose_name='title/position')
  message = models.TextField(blank=True, verbose_name='message')
  test_image = models.ImageField(verbose_name='Image', upload_to='uploads/')

  def __str__(self):
    return self.test_name

  class Meta:  
    verbose_name_plural = 'Testimonial name'

class Projects(models.Model):
  id = models.AutoField(primary_key=True)
  project_title = models.CharField(max_length=100, verbose_name='Project title')
  project_date = models.IntegerField(verbose_name='Project date')
  project_description = models.TextField(blank=True, verbose_name='message')
  test_image1 = models.ImageField(verbose_name='Image1', upload_to='uploads/')
  test_image2 = models.ImageField(verbose_name='Image2', upload_to='uploads/')
  test_image3 = models.ImageField(verbose_name='Image3', upload_to='uploads/')

  def __str__(self):
    return self.project_title

  class Meta:  
    verbose_name_plural = 'Project title'



class Message(models.Model):
  id = models.AutoField(primary_key=True)
  msg_name = models.CharField(max_length=100, verbose_name='Name')
  email = models.EmailField(max_length=100, verbose_name='Email')
  subject = models.CharField(max_length=100, verbose_name='Subject')
  message = models.TextField(blank=True, verbose_name='Message')

  def __str__(self):
    return self.email

  class Meta:  
    verbose_name_plural = 'Email'

class Article(models.Model):
  id = models.AutoField(primary_key=True)
  art_titile = models.CharField(max_length=100, verbose_name='Article title')
  post = models.TextField(blank=True, verbose_name='Post')
  art_image = models.ImageField(verbose_name='Image3', upload_to='uploads/')

  def __str__(self):
    return self.art_titile

  class Meta:
    verbose_name_plural = "Article Title"






