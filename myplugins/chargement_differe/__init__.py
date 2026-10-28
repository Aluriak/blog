"""Ajoute loading="lazy" aux images et iframes des articles et des pages.

Le navigateur ne les télécharge qu'à l'approche de l'écran, au lieu de tout
charger à l'ouverture de l'article. Celles qui ont déjà un attribut loading
sont laissées telles quelles.
"""

import re

from pelican import signals

SANS_LOADING = re.compile(r'<(img|iframe)\b(?![^>]*\bloading=)', re.IGNORECASE)


def differer(contenu):
    if contenu._content:
        contenu._content = SANS_LOADING.sub(r'<\1 loading="lazy"', contenu._content)


def register():
    signals.content_object_init.connect(differer)
