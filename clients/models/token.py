from datetime import timedelta
from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions
from rest_framework.authtoken.models import Token


TOKEN_EXPIRED_AFTER_SECONDS = 60 * 10


class TokenExpiresAuthentication(TokenAuthentication):

    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

        _, token = self.token_expire_handler(key)

        return (token.user, token)

    def expires_token_in(self, token):
        time_elapsed = timezone.now() - token.created
        return timedelta(seconds=TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed

    def is_token_expired(self, token):
        return self.expires_token_in(token) < timedelta(seconds=0)

    def token_expire_handler(self, token):
        is_expired = self.is_token_expired(token)
        if is_expired:
            token.delete()
            token = Token.objects.create(user=token.user)
        return is_expired, token
