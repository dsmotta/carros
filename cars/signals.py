from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory
from geminiAI_api.client import car_gemini_ai
 

def car_iventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(     # retorno um dicionario com chave e valor
        total_value=Sum('value')
    )['total_value'] # esta sintaxe obtemos somente o valor de retorno do dicionario
    CarInventory.objects.create(
        cars_count = cars_count,
        cars_value = cars_value
    )

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        ai_bio = car_gemini_ai(instance.model, instance.brand, instance.factory_year)
        instance.bio = ai_bio


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
   car_iventory_update()

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_iventory_update()