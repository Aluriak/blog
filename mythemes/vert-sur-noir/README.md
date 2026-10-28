# vert-sur-noir

Thème du blog : fond noir, liens verts, barre latérale aux titres en chemins (`blog/`, `links/`…).

Issu de [bootstrap2-dark](https://github.com/getpelican/pelican-themes/tree/master/bootstrap2),
dont il garde les couleurs, mais sans Bootstrap : une feuille de style (`static/css/blog.css`),
Font Awesome 6 free, embarqué (icônes de la barre latérale et du plugin checkbox), et pygments (code).

Réglages lus dans `pelicanconf.py` :
- `BLOG_LINKS`, `LINKS`, `OUTER_WEB` : groupes de liens de la barre latérale (icônes FA6 :
  « house », solid par défaut, ou « brands github ») ;
- `LANDING_URL` : lien « autres outils » de l'en-tête ;
- `LICENCE` : affichée dans le pied de page ;
- `tag_cloud` (plugin tag_cloud), `TAG_CLOUD_BADGE`.
