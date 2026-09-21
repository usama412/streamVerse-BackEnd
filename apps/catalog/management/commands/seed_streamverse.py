from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from apps.catalog.models import Genre,Content,Season,Episode,Person,LiveEvent
from apps.billing.models import Plan
from apps.blog.models import BlogPost
class Command(BaseCommand):
 def handle(self,*args,**kwargs):
  User=get_user_model(); admin,_=User.objects.get_or_create(email='admin@streamverse.local',defaults={'username':'admin','is_staff':True,'is_superuser':True}); admin.set_password('Admin123!ChangeMe'); admin.save()
  for name in ['Action','Drama','Comedy','Sci-Fi','Thriller','Anime','Documentary','Romance']:
   Genre.objects.get_or_create(name=name,slug=slugify(name))
  for name,price,features in [('Free',0,['HD access','Limited library']),('Standard',9.99,['Full HD','No ads','Watch on 2 devices']),('Premium',14.99,['4K','No ads','4 devices','Downloads'])]: Plan.objects.get_or_create(name=name,defaults={'slug':slugify(name),'price':price,'features':features})
  sample=[('The Last Horizon','A cinematic sci-fi adventure across distant worlds.','movie'),('Neon City','Crime and ambition collide in a futuristic city.','movie'),('Shadow Protocol','A covert agent races against a global threat.','movie'),('Chronicles of Dawn','An epic fantasy series of kingdoms and secrets.','show'),('Cyber Samurai','A high-energy anime about honor and technology.','anime')]
  for title,desc,typ in sample:
   c,_=Content.objects.get_or_create(slug=slugify(title),defaults={'title':title,'description':desc,'content_type':typ,'year':2026,'language':'English','country':'USA','quality':'4K','rating':8.5,'video_url':'https://storage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4','poster':'https://images.unsplash.com/photo-1489599849927-2ee91cede3ba'})
   c.genres.add(Genre.objects.get(slug='action'))
   if typ=='show':
    s,_=Season.objects.get_or_create(content=c,number=1)
    for i in range(1,7): Episode.objects.get_or_create(season=s,number=i,defaults={'title':f'Episode {i}','video_url':'https://storage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4'})
  self.stdout.write(self.style.SUCCESS('StreamVerse seed data created.'))
