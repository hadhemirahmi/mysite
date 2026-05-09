from datetime import date

from django.db import models

class Produit(models.Model):
    libelle  = models.CharField(max_length=100)
    description = models.TextField( default="")
    prix = models.DecimalField(max_digits=10, decimal_places=3)
    type = models.CharField(max_length=2,choices=[('em','embllé'),('fr','frais'),('cs','conserve')], default='em')
    Img=models.ImageField(blank=True)
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE, null=True)
    fournisseur=models.ForeignKey('Fournisseur', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.libelle+","+self.description+","+str(self.prix)+", "+self.type
class  Categorie(models.Model):
    nom = models.CharField(max_length=50,default='Alimentaire')
    def __str__(self):
        return self.nom
class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    adresse=models.TextField()
    email=models.EmailField()
    telephone=models.CharField(max_length=8)
    def __str__(self):
        return self.nom+","+self.adresse+","+self.email+","+self.telephone
class ProduitC(Produit):
    def __str__(self):
        return self.libelle+","+self.description+","+str(self.prix)+", "+self.type
class ProduitNC(Produit):
    Duree_garantie =models.CharField(max_length=100)
    def __str__(self):
        return self.libelle+","+self.description+","+str(self.prix)+", "+self.type+","+self.Duree_garantie
class Commande(models.Model):
    dateCde = models.DateField( null=True,default=date.today)
    totalCde = models.DecimalField(max_digits=10, decimal_places=3, editable=True, default=0)
    produits = models.ManyToManyField('Produit')
    def save(self, *args, **kwargs):
        if self.pk:
            self.totalCde = sum(p.prix for p in self.produits.all())
        super().save(*args, **kwargs)


