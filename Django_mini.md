# Mini Learnings

## Chapter 1
* Models / ModelAdmin / ModelManagers / Fields (SlugField etc.)
* Functional & Class based Views
* Urls (context, parameters, Namespaces, path, re_path, get_absolute_url)
* Request & Reponse
* Pagination

| Topic                   | Description                                      | Page   |
|-------------------------|--------------------------------------------------|--------|
| runserver --settings... | Choosing between different settings files        | 7      |
| Uvicorn, Daphne         | ASGI App Servers (WSGI: Apache, Guniron or uWSGI)| 7      |
| Default installed apps  | admin, auth, contenttypes, sessions, messages, staticfiles | 8      |
| USE_TZ                  | Django timezone aware                            | 8      |
| SlugField               | Django Slugfield model, + unique_for_date        | 11     |
| utils.timezone          | Django TZ aware (similar to python: datetime.now)| 11     |
| Datetimefield           | auto_now_add (create), auto_now (update)         | 11     |
| ForeignKei related_name | Name of the Reverse direction Relationship       | 11     |
| Meta ordering           | Auto ordering via meta class (- for reverse)     | 11     |
| app_model for SQL Table | E.g. blog_post is the created Table in SQL       | 14     |
| manage.py sqlmigrate    | View SQL that gets pushed to DB                  | 14     |
| manage.py createsuperuser| Create a superuser                              | 14     |
| admin.site.register     | Alternatively with decorator @admin.register     | 17,19  |
| ModelAdmin list_display | Change admin site appearance                     | 19     |
| ModelAdmin extensions   | list_filter, search_fields, prepopulated_fields  | 20     |
| ModelAdmin extensions   | raw_id_fields, date_hierarchy, ordering          | 20     |
| ORM based on QuerySets  | = collection of queries, can apply filters, lazy | 21     |
| manage.py shell         | Interative shell with models available           | 21     |
| get(), save(), all()    | Single object, save to DB (before in memory), all| 22     |
| filter() lookup methods | publish__year, author__username (lookup relation)| 24     |
| order_by()              | - for reverse order ('title=asc', '-title'=dsc)  | 24     |
| models.Manager (def mgr)| Post.objects.all() -> objects default manager    | 25     |
| models.Manager (own mgr)| Inherit from Manager and override get_queryset   | 25     |
| models.Manager          | Post.objects.all() -> objects default manager    | 25     |
| default_manager_name    | If more than 1 mgr, add default explicitly       | 25     |
| render()                | Request, template path, context variables as dict| 27     |
| get_object_or_404       | HTTP404 if object not found                      | 27     |
| url namespaces          | app_name in app urls + namespace in global urls  | 28     |
| url namespaces          | unique in project, colon used, eg. blog:post_list | 28     |
| path converters         | E.g. <int:year>, capture values from URL         | 28     |
| re_path()               | Path converters using regex                      | 29     |
| get_absolute_url()      | Convention for Canonical URL, uses reverse()     | 29     |
| get_absolute_url()      | Used in templates to link                        | 32     |
| tags, vars, filters     | J2 {% tag %} e.g. block, {{var}}, \|filter       | 31     |
| {% load static %}       | Loads template tags from django.contrib.static   | 31     |
| truncatewords, linebreaks | J2 filter examples                             | 32     |
| django.core.paginator   | Built-in Paginator                               | 34-37  |
| Class-based Views       | Non-Functional, generic.ListView, context_object_name | 36-38  |
| Class-based Views       | template_name, querset, page_obj, paginate_by    | 36-38  |


## Chapter 2
* Email
* Forms & ModelForms

| Topic                   | Description                                      | Page   |
|-------------------------|--------------------------------------------------|--------|
| django forms Framework  | Form, ModelForm, widget, EmailField              | 41     |
| forms.py                | Django convention for forms, ValidationError     | 41     |
| forms in views          | Via request.method==POST check & form.is_valid   | 42     |
| form cleaned_data dict  | if is_valid() can be accessed                    | 42     |
| form.errors             | on is_valid() False                              | 42,43  |
| EMAIL_BACKEND           | backends.console or EMAIL_HOST, EMAIL_PORT etc.  | 43     |
| django.core.mail        | send_mail(subject,message,from,array_of_to_addr) | 44,45  |
| build_absolute_uri()    | Build full URL                                   | 45     |
| {{ form.as_p }}         | Render form in templates (.as_ul, .as_table)     | 46     |
| {% for field in form %} | Render each field separately                     | 46     |
| csrf_token              | Include CSRF token on POST requests              | 46     |
