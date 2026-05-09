import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from blog.models import Post
from django.contrib.auth.models import User
from django.utils.text import slugify

def seed_blog():
    user = User.objects.first()
    if not user:
        user = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')

    posts_data = [
        {
            'title': 'Bienvenue sur notre nouveau Blog !',
            'content': 'Nous sommes ravis de lancer notre nouvel espace de partage. Vous y trouverez des actualités, des conseils et des tutoriels sur le commerce électronique.',
            'status': 1
        },
        {
            'title': 'Les tendances du E-commerce en 2024',
            'content': 'Le commerce électronique continue d\'évoluer. Cette année, l\'IA et la personnalisation sont au cœur de la stratégie des entreprises.',
            'status': 1
        },
        {
            'title': 'Comment choisir son fournisseur ?',
            'content': 'Le choix d\'un fournisseur est crucial pour la réussite de votre boutique en ligne. Voici quelques critères à prendre en compte : fiabilité, prix, et qualité de service.',
            'status': 1
        }
    ]

    for data in posts_data:
        if not Post.objects.filter(title=data['title']).exists():
            Post.objects.create(
                title=data['title'],
                slug=slugify(data['title']),
                author=user,
                content=data['content'],
                status=data['status']
            )
            print(f"Post '{data['title']}' créé.")
        else:
            print(f"Post '{data['title']}' existe déjà.")

if __name__ == '__main__':
    seed_blog()
