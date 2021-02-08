Django
========

## Important Files

| FILE                                          | Description                                      | 
|-----------------------------------------------|--------------------------------------------------|
| app/settings.py                               | project config (e.g. DB, INSTALLED_APPS)         |
| app/urls.py                                   | URL declarations for this Django project         |
| app/asgi.py                                   | entry-point for ASGI-compatible web servers      |
| app/wsgi.py                                   | entry-point for WSGI-compatible web servers      |
| user-app/admin.py                             | Make the user app editable in Admin Page         |

## Important URLS

| URL                                           | Description                                      | 
|-----------------------------------------------|--------------------------------------------------|
| http://127.0.0.1:8000/admin/                  | Admin Page                                       |

## Important Packages

| Package                                       | Description                                      | 
|-----------------------------------------------|--------------------------------------------------|
| django.http                                   | E.g Http404, HttpResponse, HttpResponseRedirect  |
| django.shortcuts                              | E.g render, get_object_or_404                    |
| django.template                               | E.g loader                                       |
| django.urls                                   | E.g. path, reverse                               |
| django.contrib                                | E.g. admin, auth, contenttypes, sessions, messages, staticfiles |
| django.utils                                  | E.g. timezone                                    |
| django.db                                     | E.g. models                                      |
| django.views                                  | E.g. generic                                     |
| django.test                                   | E.g. TestCase (includes Client), Client          |
| django.test.utils                             | E.g. setup_test_environment (Template renderer)  |

## manage.py
* Before use, create a project with `django-admin startproject config .`

| python manage.py ...                          | Description                                      | 
|-----------------------------------------------|--------------------------------------------------|
| runserver [0.0.0.0:8000]                      | Run Development server                           |
| showmigrations <app-name>                     | Show migrations and if applied                   |
| makemigrations <app-name>                     | Compare model to migrations and crate diff       |
| sqlmigrate <app-name> 00xx                    | See what SQL the migration creates               |
| migrate                                       | Run open migrations                              |
| migrate <app-name> 00xx_auto_xx_xx            | Migrate to a specific version, e.g. back to that |
| check                                         | Check django project for problems                |
| shell                                         | Run Shell and interact wiht model, see below*    |
| loaddate path/to/file.json                    | E.g. loaddata app_data/automation.Auth.json      |
| dumpdata <app.Model>                          | E.g. dumpdata automation.Auth (needs env vars)   |
| createsuperuser                               | Prompts for all Info                             |
| drf_create_token                              | Create a Django Rest Framework Token for Auth    |
| changepassword                                | Change PW for a user                             |
| startapp <name>                               | Create a new APP                                 |
| test [app.tests.test_file.testClass.tmethod]  | Run all or specific tests                        |
| collectstatic                                 | Collect static files and save to STATIC_ROOT     |

See Reference: https://docs.djangoproject.com/en/3.1/ref/django-admin

```python
python manage.py shell

from automation.models import Auth
Auth.objects.create(name='token', type='Bearer', auth_username='admin', auth_value='3zz')
token_auth_object = Auth.objects.filter(name='token').first()
str(token_auth_object)
```

## VARIABLES
* xy

| Variable                                      | Description                                      | 
|-----------------------------------------------|--------------------------------------------------|
| STATIC_ROOT                                   | Folder where collectstatic dumps content         |
| DJANGO_SETTINGS_MODULE                        | Can helpt to adjust environment based on env var |
| DJANGO_SETTINGS_MODULE="app.settings.prod"    | Example                                          |
| DJANGO_SECRET_KEY                             | Secret key                                       |
| DEBUG                                         | Prod/Test (Static files no longer served)        |
| xy                                            | <todo>                                           |
| ALLOWED_HOSTS                                 | Should be configured for prod                    |

## Models

| Fields                          | Description                 | Special                       |
|---------------------------------|-----------------------------|-------------------------------|
| UUIDField                       | UUID, e.g. for PK           |                               |
| IntegerField                    | Integerfield, e.g. for PK   |                               |
| CharField                       | Lots of stuff               | choices                       |
| BooleanField                    | True/False                  |                               |
| DateTimeField                   | Interpreted                 |                               |
| ForeignKey                      | 1-to-n relation             | on_delete                     |
| OneToOneField                   | 1-to-1 relation             | on_delete                     |
| JSONField                       | JSON Data                   | 3.1 default, before extension |
| EncryptedTextField              | Encrypted in DB             | With SECRET_KEY by default    |

* max_length=100, blank=True, null=True, default=xy, primary_key=True, editable=False
* on_delete=models.CASCADE

See Reference: https://docs.djangoproject.com/en/3.1/ref/models/fields/

### Reverse Reference
<todo>

See examples: https://docs.djangoproject.com/en/3.1/topics/db/examples/
See: https://stackoverflow.com/questions/38388423/what-does-on-delete-do-on-django-models

### Model Methods
<todo>
* order_by()
* first()
* filter()

#### Filter Methods
* return Question.objects.filter(pub_date__lte=timezone.now())

See: https://docs.djangoproject.com/en/3.1/topics/db/queries/

## Signals
<todo>

## Websockets
<todo>

## Testing
assertEqual
assertQuerysetEqual
assertContains
assertRaisesRegexp

See: https://docs.djangoproject.com/en/3.1/topics/testing/
See Reference: https://docs.djangoproject.com/en/3.1/topics/testing/overview/
See Fixtures: https://docs.djangoproject.com/en/3.1/topics/testing/tools/
See Fixtures: https://docs.djangoproject.com/en/3.1/topics/testing/tools/#fixture-loading
See WhatHappens: https://adamj.eu/tech/2020/09/05/what-happens-when-you-run-manage.py-test/ (e.g. DB Creation)
See TestingFramework: https://docs.djangoproject.com/en/3.1/topics/testing/advanced/

### Mocking
* Response Lib
* Patch
* Patch.object()

See RealPythonTutorial: https://realpython.com/python-mock-library/#patching-an-objects-attributes
See MockTutorial: https://www.integralist.co.uk/posts/mocking-in-python/

### Examples 
* V1: "Standard Mocking"
* V2: Injection might be easier
* T3: Dynamic Return content via Response Lib
* T4: Assert JSON
* T5: setUp() Method - Runs before every test
* T6: fixtures 
* T7: setUpTestData() - Runs once for the class

V1

```python
# --> test calls create_service(auth=xy)
def create_service(template=SERVICE_TEMPLATE, auth=DEFAULT_AUTH):
# --> passes auth to create_phases
def create_phases(service, auth):
# --> passes auth to ext service
def create_ext_service(auth_name=DEFAULT_AUTH):

class ServiceInstanceHandlerTests(TestCase):
    @responses.activate
    @patch('automation.publisher.AutomationPublisher.publish_message',
      new=mocked_publish_message)
    def test_service_instance_check_ext_call_bearer_auth(self):
        responses.add(responses.POST, 'http://0.0.0.0:8822/1', json={}, status=200)
        service = create_service(auth='token')
        cmdb_entry = create_cmdb_entry(SERVICE_INSTANCE_DATA)
        service_instance = ServiceInstance(name='Test',
                                               service=service,
                                               cmdb_entry=cmdb_entry)
        service_instance.save()
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.headers['Authorization'], 'Bearer yzz')
```

V2: inject/patch auth service directly, either via Patch Object or via Patch Namespace

```python
# --> test calls create_service(auth=xy)
def create_service(template=SERVICE_TEMPLATE):
# --> passes auth to create_phases
def create_phases(service):
# --> passes auth to ext service
def create_ext_service(auth_name=DEFAULT_AUTH):

def mocked_token_authentication():
    if Auth.objects.all().count() == 0:
        create_auths()
    return Auth.objects.filter(name='token').first()

class ServiceInstanceHandlerTests(TestCase):
    @responses.activate
    @patch('automation.publisher.AutomationPublisher.publish_message',
      new=mocked_publish_message)
    @patch('automation.models.ExtApiService.auth', new_callable=mocked_token_authentication)
    # @patch.object(ExtApiService, 'auth', new_callable=mocked_token_authentication)
    def test_service_instance_check_ext_call_bearer_auth2(self, mock_dummy):
        responses.add(responses.POST, 'http://0.0.0.0:8822/1', json={}, status=200)
        service = create_service()
        cmdb_entry = create_cmdb_entry(SERVICE_INSTANCE_DATA)
        service_instance = ServiceInstance(name='Test',
                                               service=service,
                                               cmdb_entry=cmdb_entry)
        service_instance.save()
        # print(responses.calls[0].request.__dict__)
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.headers['Authorization'], 'Bearer xyz')

```

T3: Use Response Library to dynamically generate content
```python

```

T4: Compare JSON in assert

```python
self.assertEqual(json.loads(responses.calls[0].request.body),
          {"extra_vars":
            {"data":
              {
                "vlan_id": "1301"
              }
          }
        )
```

T5: setUp() method

```python
from django.test import TestCase
from automation.models import Auth

class AuthTestCase(TestCase):
    def setUp(self):
        Auth.objects.create(name="basic", type=Auth.BASIC, auth_username="admin", auth_value="password")
        Auth.objects.create(name="token", type=Auth.BEARER, auth_username="admin", auth_value="Z6PlWGq0DFa8cyjKFalYINovGayDlf")

    def test_auth_api_call_basic(self):
        """Test if api gets called with correct auth method of basic"""
        
		auth_basic = Auth.objects.get(name="basic")
        self.assertEqual(auth_basic.name, 'basic')

    def test_auth_api_call_token(self):
        """Test if api gets called with correct auth method of token"""
        
		auth_token = Auth.objects.get(name="token")
        self.assertEqual(auth_token.name, 'token')
```

T6: Django Fixtures


## Deploying
* High Level Steps
  * Split up settings.py (base.py + prod.py + dev.py)
  * Setup Gunicorn (WSGI HTTP Server) + Nginx (Reverse Proxy + Static Content) Whitenoise (Static Content)
    * Whitenoise runs as middleware
  * Create vEnv
  * Set ENV Vars (DJANGO_SETTINGS_MODULE / DJANGO_SECRET_KEY)
  * Run migrations
  * Collect Static
  * Create superuser
  * run in background with supervisord (gunicorn is a child process)
  * Logging

- [Deployment Guide](https://mattsegal.dev/simple-django-deployment.html)

