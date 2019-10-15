import graphene
from graphene_django.types import DjangoObjectType

from .models import Tutoria

#Traer toda la data
class LinkType(DjangoObjectType):
    class Meta:
        model = Tutoria

class General(graphene.InputObjectType):
    materia = graphene.String()
    descripcion = graphene.String()
    cupos=graphene.Int()
    idtutor=graphene.Int()
    idtoken=graphene.String()

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
 #Eliminar tutoria
class DeleteTutoria(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):
        obj = Tutoria.objects.get(id=id)
        obj.delete()
        return DeleteTutoria(ok=True)

class UpdateTutoria(graphene.Mutation):
    ok = graphene.Boolean()
    class Arguments:
        input = General(required=True)
        id = graphene.Int(required=True)

    def mutate(self, info, id,input=None):
        ok=False
        obj=Tutoria.objects.get(id=id)
        if obj:
            ok = True
            obj.materia = input.materia
            obj.descripcion = input.descripcion
            obj.cupos=input.cupos
            obj.idtutor=input.idtutor
            obj.idtoken=input.idtoken
            obj.save()
            return UpdateTutoria(ok=ok)
        return UpdateTutoria(ok=ok)


class Mutation(graphene.ObjectType):
    create_tutoria = CrearTutoria.Field()
    delete_tutoria = DeleteTutoria.Field()
    update_tutoria = UpdateTutoria.Field()
