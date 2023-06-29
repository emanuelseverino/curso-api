from datetime import datetime,timezone

from rest_framework.permissions import BasePermission


class VencimentoPermission(BasePermission):

    message = "Atualize seu plano."

    def has_permission(self, request, view):
        vencimento = request.user.vencimento
        data_atual = datetime.now(timezone.utc)
        if vencimento is None:

            return False
        if vencimento.date() < data_atual.date():
            return False
        return True