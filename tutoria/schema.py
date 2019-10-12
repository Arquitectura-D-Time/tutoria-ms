import graphene
from graphene_django import DjangoObjectType

from .models import Tutoria

#Traer toda la data
class LinkType(DjangoObjectType):
    class Meta:
        model = Tutoria


class Query(graphene.ObjectType):
    tutorias = graphene.List(LinkType)

    def resolve_tutorias(self, info, **kwargs):
        return Tutoria.objects.all()
#Crear tutorias
class CrearTutoria(graphene.Mutation):
    id = graphene.Int()
    materia = graphene.String()
    descripcion = graphene.String()
    class Arguments:
        materia = graphene.String()
        descripcion = graphene.String()
        cupos=graphene.Int()
        idtutor=graphene.Int()
        idtoken=graphene.String()
    def mutate(self, info, materia,descripcion,cupos,idtutor,idtoken):
        tutoria= Tutoria(materia=materia, descripcion=descripcion,cupos=cupos,idtutor=idtutor,idtoken=idtoken)
        tutoria.save()

        return CrearTutoria(
            id=tutoria.id,
            materia=tutoria.materia,
            descripcion=tutoria.descripcion,
        )
class Mutation(graphene.ObjectType):
    create_tutoria = CrearTutoria.Field()
