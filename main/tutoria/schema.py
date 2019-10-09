import graphene
from graphene_django import DjangoObjectType

from .models import Tutoria


class LinkType(DjangoObjectType):
    class Meta:
        model = Tutoria


class Query(graphene.ObjectType):
    tutorias = graphene.List(LinkType)

    def resolve_tutorias(self, info, **kwargs):
        return Tutoria.objects.all()
