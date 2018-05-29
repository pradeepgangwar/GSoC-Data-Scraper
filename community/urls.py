from django_distill import distill_url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from gsoc.views import index as gsoc_index
from gsoc.views import projects as gsoc_projects


def get_index():
    # The index URI regex, ^$, contains no parameters, named or otherwise.
    # You can simply just return nothing here.
    return None


urlpatterns = [
    distill_url(
        r'^$', TemplateView.as_view(template_name='index.html'),
        name='index',
        distill_func=get_index,
        distill_file='index.html',
    ),
    distill_url(
        r'^gsoc/$', gsoc_index,
        name='community-gsoc',
        distill_func=get_index,
        distill_file='gsoc/index.html',
    ),
    distill_url(
        r'^gsoc/projects/$', gsoc_projects,
        name='community-gsoc-projects',
        distill_func=get_index,
        distill_file='gsoc/projects.html',
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
