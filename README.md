```python
$ python manage.py shell_plus
# Shell Plus Model Imports
from articles.models import Article, Comment
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from jobs.models import Job
# Shell Plus Django Imports
from django.core.cache import cache
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When, Exists, OuterRef, Subquery
from django.utils import timezone
from django.urls import reverse
Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> article = Article()
>>> article.title = '새로운 데이터'
>>> article.content = '새로운 내용'
>>> article.save()
>>> article
<Article: Article object (1)>
>>> comment = Comment()
>>> comment.content = 'First comment'
>>> comment.article = article
>>> comment.save()
```

```
>>> comment.article.pk
1
>>> comment.article.content
'새로운 내용'
>>> comment.article.title
'새로운 데이터'
>>>
```

