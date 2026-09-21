from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(unique=True)
    def __str__(self): return self.name

class Person(models.Model):
    name = models.CharField(max_length=160)
    image = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    def __str__(self): return self.name

class Content(models.Model):
    TYPES=[('movie','Movie'),('show','TV Show'),('anime','Anime'),('live','Live')]
    title=models.CharField(max_length=255); slug=models.SlugField(unique=True); content_type=models.CharField(max_length=20,choices=TYPES)
    description=models.TextField(); poster=models.URLField(blank=True); backdrop=models.URLField(blank=True); trailer=models.URLField(blank=True); video_url=models.URLField(blank=True)
    year=models.PositiveIntegerField(null=True,blank=True); duration=models.CharField(max_length=50,blank=True); rating=models.DecimalField(max_digits=3,decimal_places=1,default=0)
    language=models.CharField(max_length=80,blank=True); country=models.CharField(max_length=100,blank=True); quality=models.CharField(max_length=30,default='HD'); director=models.CharField(max_length=160,blank=True)
    tags=models.JSONField(default=list,blank=True); genres=models.ManyToManyField(Genre,blank=True,related_name='contents'); cast=models.ManyToManyField(Person,blank=True,related_name='acted_contents')
    is_published=models.BooleanField(default=True); is_featured=models.BooleanField(default=False); views=models.PositiveBigIntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True); updated_at=models.DateTimeField(auto_now=True)
    class Meta: ordering=['-created_at']
    def __str__(self): return self.title

class Season(models.Model):
    content=models.ForeignKey(Content,on_delete=models.CASCADE,related_name='seasons'); number=models.PositiveIntegerField(); title=models.CharField(max_length=255,blank=True)
    class Meta: unique_together=[('content','number')]; ordering=['number']

class Episode(models.Model):
    season=models.ForeignKey(Season,on_delete=models.CASCADE,related_name='episodes'); number=models.PositiveIntegerField(); title=models.CharField(max_length=255)
    description=models.TextField(blank=True); thumbnail=models.URLField(blank=True); video_url=models.URLField(blank=True); duration=models.CharField(max_length=50,blank=True); air_date=models.DateField(null=True,blank=True); views=models.PositiveBigIntegerField(default=0)
    class Meta: unique_together=[('season','number')]; ordering=['number']

class LiveEvent(models.Model):
    content=models.OneToOneField(Content,on_delete=models.CASCADE,related_name='live_event'); category=models.CharField(max_length=80); viewers=models.PositiveIntegerField(default=0); start_time=models.DateTimeField(); is_live=models.BooleanField(default=False)
