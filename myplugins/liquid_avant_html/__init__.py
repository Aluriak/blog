"""Fait passer les balises liquid ({% img %}, {% video %}) avant les blocs HTML.

pelican-liquid-tags traite ses balises après que Markdown a mis de côté les blocs
HTML : une balise placée dans <center>…</center> restait brute. L'ancien plugin
liquid_tags (dépôt pelican-plugins) la traitait avant, comme ici.
À placer après 'pelican.plugins.liquid_tags' dans PLUGINS.

Corrige aussi {% video %} : sans hauteur ni affiche, pelican-liquid-tags écrivait
height="None" et poster="None" (le navigateur demandait alors l'adresse « None »).
"""

import re

from pelican import signals
from pelican.plugins.liquid_tags import video as _video
from pelican.plugins.liquid_tags.mdx_liquid_tags import LiquidTags, _LiquidTagsPreprocessor


@LiquidTags.register('video')
def video_sans_none(preprocessor, tag, markup):
    return re.sub(r'\s(?:width|height|poster)="None"', '', _video.video(preprocessor, tag, markup))


class LiquidTagsAvantHtml(LiquidTags):
    def extendMarkdown(self, md):
        md.registerExtension(self)
        html_block = md.preprocessors._priority[md.preprocessors.get_index_for_name('html_block')]
        md.preprocessors.register(_LiquidTagsPreprocessor(self), 'mdincludes', html_block.priority + 5)


def remplacer(pelican):
    extensions = pelican.settings['MARKDOWN'].get('extensions', [])
    for i, extension in enumerate(extensions):
        if type(extension) is LiquidTags:
            extensions[i] = LiquidTagsAvantHtml(extension.getConfigs())


def register():
    signals.initialized.connect(remplacer)
