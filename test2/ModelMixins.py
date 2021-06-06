from django.db import models
from django.contrib.auth.models import User

class RightsModelRelation(models.Model):

    user_link = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False, default=None,
                                    related_name="%(class)s_rights_user_test2")
    right_to_view = models.BooleanField(default=True)
    right_to_change = models.BooleanField(default=False)
    right_to_delete = models.BooleanField(default=False)


class RightsModelMixin(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=None,
                              related_name="%(class)s_owner_test2", )
    rights_link = models.ManyToManyField(RightsModelRelation, default=None,
                                         related_name="%(class)s_rights_link_test2")