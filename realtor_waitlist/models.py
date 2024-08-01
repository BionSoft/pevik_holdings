from django.db import models


class RealtorWaitlist(models.Model):
    email = models.EmailField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email