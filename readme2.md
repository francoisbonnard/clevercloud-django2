
```bash
git remote add clever git+ssh://git@push-n3-par-clevercloud-customers.services.clever-cloud.com/app_a3a23a35-ac68-4ee0-b8a5-24def9d14b99.git
git branch -M master
git push -u clever master
```


CC_PYTHON_MODULE photoshare.wsgi:application

``` bash
git branch -M main
git remote add origin2 https://github.com/francoisbonnard/clevercloud-django2.git
git push -u origin2 main
```

[python decouple](https://pypi.org/project/python-decouple/)

[mysqlclient vs pymysql](https://stackoverflow.com/questions/43102442/whats-the-difference-between-mysqldb-mysqlclient-and-mysql-connector-python)

[django doc on clever cloud](https://developers.clever-cloud.com/guides/python-django-sample/)


```python
CC_PYTHON_MANAGE_TASKS="migrate, assets:precompile"
CC_PYTHON_MANAGE_TASKS="makemigrations, migrate, createsuperuser"
```

createsuperuser

```bash
ssh -t ssh@sshgateway-clevercloud-customers.services.clever-cloud.com app_a3a23a35-ac68-4ee0-b8a5-24def9d
```
ssh -t ssh@sshgateway-clevercloud-customers.services.clever-cloud.com app_a3a23a35-ac68-4ee0-b8a5-24def9d14b99

[Reddit](https://www.reddit.com/r/django/comments/1c329xo/how_to_create_a_superuser_on_paas_without_using/)

database

```bash
mysql -h bht2f0la4j8cz8fiwfdm-mysql.services.clever-cloud.com -u uczgzdxr8ml1xeex -P3306 -p bht2f0la4j8cz8fiwfdm

USE bht2f0la4j8cz8fiwfdm

SELECT * FROM auth_user;

```

![superuser after ssh](image.png)

[doc static files](https://docs.djangoproject.com/en/5.0/howto/static-files/)
[doc static files](https://docs.djangoproject.com/en/5.0/howto/static-files/deployment/)

![chrome console failed to load resources](image-1.png)

[What's the difference between STATIC_URL and STATIC_ROOT in Django?](https://stackoverflow.com/questions/37716200/whats-the-difference-between-static-url-and-static-root-in-django)

[Check this Taiga](https://www.clever-cloud.com/blog/features/2017/10/10/1fdba-django-taiga/)

[Deployment](https://docs.djangoproject.com/en/4.2/howto/deployment/)

[statix files in production](https://docs.djangoproject.com/en/4.2/howto/static-files/deployment/)