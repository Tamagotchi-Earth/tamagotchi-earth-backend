from django.conf import settings
from drf_spectacular.openapi import AutoSchema
from drf_spectacular.utils import OpenApiParameter


class CustomAutoSchema(AutoSchema):
    """Custom OpenAPI schema that adds accept-language parameter to all views"""
    global_params = [
        OpenApiParameter(
            name="Accept-Language",
            type=str,
            location=OpenApiParameter.HEADER,
            description=f"Controls selected language ({settings.LANGUAGES[0][1]} by default)",
            required=False,
            enum=[elem[0] for elem in settings.LANGUAGES]
        )
    ]

    def get_override_parameters(self):
        params = super().get_override_parameters()
        return params + self.global_params
