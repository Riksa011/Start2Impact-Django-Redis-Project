import time
from datetime import datetime
from django.db import models
from .utils import sendTransaction


# User model with nickname feature
class User(models.Model):
    nickname = models.CharField(max_length=20)

    def __str__(self):
        return self.nickname


# Item model with id code, name, upload date, description, owner, blockchain transaction ID hash features
class Item(models.Model):
    id_code = models.CharField(max_length=20)
    upload_date = models.DateTimeField(blank=True, null=True)
    item_name = models.CharField(max_length=50)
    item_description = models.TextField(max_length=200, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    txId = models.CharField(max_length=66, default=None, null=True)
    item_history = models.TextField(default="", null=True)
    item_actions_number = models.IntegerField(default=0)
    item_last_action = models.TextField(default="", null=True)

    # function to send the transaction to the blockchain with the item last action as message
    def writeOnChain(self):
        self.txId = sendTransaction(self.item_last_action)
        self.save()

    # function to set the upload date and the id code
    def set_date_and_id_code(self):
        current_ts = datetime.now()
        rounded_current_ts = current_ts.replace(microsecond=0)
        self.upload_date = rounded_current_ts
        self.id_code = int(time.time())
        self.save()

    def __str__(self):
        return self.item_name
