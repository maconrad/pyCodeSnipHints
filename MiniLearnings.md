# Mini Learnings

* [Django](#mini-learnings-django)  

## Mini Learnings Django

* Key Learnings and Examples for them

| Learning                                      | Description                                      |
|-----------------------------------------------|--------------------------------------------------|
| from django.db.models.signals import pre_save | Signals such as post_save, post_delete           |
| from django.dispatch import receiver          | Decorator to on receiving function               |
|      Example receiver                         | [Example Signal Receiver](#example-signal)       |
| update_fields on receiver function            | Must be explicitly appended in admin.py          |
|      Example update fields                    | [Example Update Fields](#example-update-fields)  |
| update() vs save() metod on objects           | Save triggers signal, updates does not           |
|      Example update fields                    | [Example Update Method](#example-update-method)  |
| Relation naming                               | Must be explicitly appended in admin.py          |
|      Example update fields                    | [Example Update Fields](#example-update-fields)  |
| Testing Limit Scope                           | [Example Testing](#example-testing)              |
| Serializer depth, relations, dynamic fields   | [Example Serializer](#example-serializer)        |  
| Channels workflow                             | [Example Channels](#example-channels)            |  

### Example Signal

* any()
* receives update_fields

```python
@receiver(post_save, sender=Phase)
def phase_post_save(sender, instance, created, raw, using, update_fields, **kwargs):
    '''
    This handler updates the decommissinable status of the related Service depending on whether the phase
    is decomissionalbe or not.
    '''
    decom_matches = ["uriIsReverseCapable", "decomUri"]
    if created or (update_fields and any(x in update_fields for x in decom_matches)):
        # if created or (update_fields and 'uriIsReverseCapable' in update_fields) or \
        #  (update_fields and 'decomUri' in update_fields):
        decom_current_state = instance.service.isDecommissionable
        instance.service.isDecommissionable = DECOM_TRIGGER_RECALC
        update_fields = ['isDecommissionable']
        instance.service.save(update_fields=update_fields)

    return True
```

### Example Update Fields

* Specify all update fields
* If a field has changed and is not included in update fields and save() method contains update fields, its content will be lost=not updated

```python
class PhaseAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        update_fields = []
        if change:
            for k, val in form.initial.items():
                if form.initial[k] != form.cleaned_data[k]:
                    update_fields.append(k)
            obj.save(update_fields=update_fields)
        else:
            obj.save()

admin.site.register(Phase, PhaseAdmin)
```

### Example Update Method

* save() method triggers signals (use inside signal to not start signal-loop)
* update() method does NOT trigger signals

```python
@receiver(post_save, sender=Service)
def service_post_save(sender, instance, created, raw, using, update_fields, **kwargs):
    if update_fields and 'isDecommissionable' in update_fields:

        phase_count = instance.phase_set.all().count()
        cnt_decomUri = instance.phase_set.filter(decomUri__isnull=False).count()
        cnt_reverseCap = instance.phase_set.filter(uriIsReverseCapable=True).count()

        if (cnt_decomUri + cnt_reverseCap) == 0:
            # save cannot be called-> loop
            # update only works on queryset
            Service.objects.filter(id=instance.id).update(isDecommissionable=DECOM_NO)
    ...
```

### Example Related Query

* If related_query_name not defined related_query_name=related_name
* Can be overriden

```python
class Tag(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="tags",
        related_query_name="tag",
    )
    name = models.CharField(max_length=255)

# That's now the name of the reverse filter
# If related_query_name not defined -> Article.objects.filter(tags__name="important")
Article.objects.filter(tag__name="important")
```

### Example Testing

* Limit Scope of Test Runner
* Automation/Tests/Tests.py Class ServiceInstanceHandlerTests method test_service_instance_decom_partly
* pytest.mark.xy would be an alternative if using pytest to limit scope


```bash
python manage.py test automation.tests.tests.ServiceInstanceHandlerTests.test_service_instance_decom_partly
```

### Example Serializer

* Write_only for relations
* SerializerMethodField to dynamically generate a field, if method name not specified, implicit method name of get_fieldname
* Overriding create method to extract data and add relationship
* If depth=2 or more, relations will be serialized, BUT those use the default serializer, not the one specified for that model
* If the serial for a specific model should be used, define it!
* See [Dynamic field Options](https://django.cowhite.com/blog/dynamic-fields-in-django-rest-framwork-serializers/)
* See [Dynamic filed Options Stackoverflow](https://stackoverflow.com/questions/18396547/django-rest-framework-adding-additional-field-to-modelserializer)

```python
class PhaseSerializer(serializers.ModelSerializer):
    service_id = serializers.IntegerField(write_only=True)
    ext_api_service_id = serializers.IntegerField(write_only=True)
    undeployable = serializers.SerializerMethodField()

    class Meta:
        model = Phase
        fields = (
            'id',
            'order',
            'name',
            'text',
            'auto_deploy',
            'idempotency',
            'uri',
            'service_id',
            'ext_api_service_id',
            'send_credentials',
            'undeployable'
        )
        depth = 2

    def get_undeployable(self, instance):
        return instance.uriIsReverseCapable or instance.decomUri is not None

    def create(self, validated_data):
        service_id = validated_data.pop('service_id')
        service = Service.objects.get(id=service_id)
        phase = Phase.objects.create(
            service=service,
            **validated_data
        )
        return phase

class PhaseInstanceSerializer(serializers.ModelSerializer):

    phase = PhaseSerializer()
    # devices = ServiceDeviceSerializer(many=True, required=False)

    class Meta:
        model = PhaseInstance
        fields = '__all__'
        depth = 2
```

### Example Channels

* type refers to method that is being called (in example below type=send_message)
* todo

```python
import json
import logging
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer

logger = logging.getLogger(__name__)


class AutomationPublisher(AsyncWebsocketConsumer):
    group_name = 'AutomationPublisherV1'

    async def connect(self):
        logger.debug(f'''Connect Websocket Called:
            {self.group_name}, {self.channel_name}''')
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    # pylint: disable=W0221
    async def disconnect(self, close_code):
        logger.debug(f'''Disconnect Websocket Called: {self.group_name},
            {self.channel_name}''')
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    # Send Message to Group
    async def send_message(self, data):
        logger.debug(f'Received data to publish: {data}')
        # We only wan't to send the payload not `type: send_message`
        data_to_send = data.get('data')

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'data': data_to_send
        }))

    @staticmethod
    def publish_message(object_to_publish):
        channel_layer = get_channel_layer()
        logger.info(f'Publish Message to Websockets DATA: {object_to_publish}')
        async_to_sync(channel_layer.group_send)(
            AutomationPublisher.group_name,
            {
                'type': 'send_message',
                'data': object_to_publish
            }
        )

# Somewhere where we want to notify
@receiver(pre_save, sender=PhaseInstance)
def phase_instance_post_save(sender, instance, **kwargs):
...
        AutomationPublisher.publish_message(
            {
                'info': 'phase_instance_updated',
                'phase_instance_id': instance.id,
                'service_instance_id': instance.service_instance.id,
            })
...

```
