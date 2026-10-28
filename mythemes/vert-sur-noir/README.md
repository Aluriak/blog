# vert-sur-noir

Thème du blog : fond noir, liens verts, barre latérale aux titres en chemins (`blog/`, `links/`…).
Thème clair (vert assombri, fond blanc cassé) quand l'appareil le demande.

Issu de [bootstrap2-dark](https://github.com/getpelican/pelican-themes/tree/master/bootstrap2),
dont il garde les couleurs, mais sans Bootstrap : une feuille de style (`static/css/blog.css`),
Font Awesome 6 free, embarqué (icônes de la barre latérale et du plugin checkbox), et pygments (code).

Réglages lus dans `pelicanconf.py` :
- `BLOG_LINKS`, `LINKS`, `OUTER_WEB` : groupes de liens de la barre latérale (icônes FA6 :
  « house », solid par défaut, ou « brands github ») ;
- `LANDING_URL` : lien « menu » de l'en-tête (la landing) ;
- `LICENCE`, `LICENCE_URL` : licence du pied de page ;
- `MAIL` : adresse mail, affichée en image (plugin mail_image) ;
- `tag_cloud` (plugin tag_cloud), `TAG_CLOUD_BADGE`.
