"""Dessine l'adresse mail (réglage MAIL = (utilisateur, domaine)) dans mail.png.

Le thème affiche cette image à la place d'un lien mailto : les robots qui
cherchent des adresses dans le HTML ne la trouvent pas. Les couleurs et la
taille se règlent par MAIL_IMAGE : texte (thème sombre), texte_clair (thème
clair, dans mail-clair.png), fond, taille (hauteur de police en pixels).
Les images sont dessinées en double résolution, pour rester nettes sur les
écrans fins.
"""

import os

from PIL import Image, ImageDraw, ImageFont
from pelican import signals

DEFAUT = {'texte': '#7db904', 'texte_clair': '#4b7a00', 'fond': None, 'taille': 15}


def dessiner(pelican):
    mail = pelican.settings.get('MAIL')
    if not mail:
        return
    reglages = DEFAUT | pelican.settings.get('MAIL_IMAGE', {})
    adresse = '@'.join(mail)
    police = ImageFont.load_default(size=2 * reglages['taille'])
    gauche, haut, droite, bas = police.getbbox(adresse)
    marge = reglages['taille'] // 6
    for nom, couleur in (('mail.png', reglages['texte']), ('mail-clair.png', reglages['texte_clair'])):
        image = Image.new('RGBA', (droite + 2 * marge, bas + 2 * marge), reglages['fond'] or (0, 0, 0, 0))
        ImageDraw.Draw(image).text((marge, marge), adresse, font=police, fill=couleur)
        image.save(os.path.join(pelican.output_path, nom), optimize=True)


def register():
    signals.finalized.connect(dessiner)
