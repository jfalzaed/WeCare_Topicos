from django.shortcuts import get_object_or_404
from Forum.models import Comentario, Like, Favorito, Respuesta
from abc import ABC, abstractmethod
from .base import Command

class CreateComentarioCommand(Command):
    def __init__(self, user, texto):
        self.user = user
        self.texto = texto

    def execute(self):
        return Comentario.objects.create(texto=self.texto, autor=self.user)


class EditComentarioCommand(Command):
    def __init__(self, comentario, nuevo_texto):
        self.comentario = comentario
        self.nuevo_texto = nuevo_texto

    def execute(self):
        self.comentario.texto = self.nuevo_texto
        self.comentario.save()
        return self.comentario


class DeleteComentarioCommand(Command):
    def __init__(self, comentario):
        self.comentario = comentario

    def execute(self):
        self.comentario.delete()


class ToggleLikeCommand(Command):
    def __init__(self, user, comentario):
        self.user = user
        self.comentario = comentario

    def execute(self):
        like, created = Like.objects.get_or_create(usuario=self.user, comentario=self.comentario)
        if not created:
            like.delete()
        return created


class ToggleFavoritoCommand(Command):
    def __init__(self, user, comentario):
        self.user = user
        self.comentario = comentario

    def execute(self):
        favorito, created = Favorito.objects.get_or_create(usuario=self.user, comentario=self.comentario)
        if not created:
            favorito.delete()
        return created


class CreateRespuestaCommand(Command):
    def __init__(self, user, texto, comentario_id):
        self.user = user
        self.texto = texto
        self.comentario_id = comentario_id

    def execute(self):
        return Respuesta.objects.create(
            texto=self.texto,
            autor=self.user,
            comentario_id=self.comentario_id
        )


class DeleteRespuestaCommand(Command):
    def __init__(self, respuesta):
        self.respuesta = respuesta

    def execute(self):
        self.respuesta.delete()
