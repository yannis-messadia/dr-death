# Dr Death - Analyse des meurtres de Harold Shipman avec Power BI

A/- Veille technologique : Power BI 

1.  Introduction à Power BI :

Power BI est une plateforme d’analyse et de visualisation de données développée par Microsoft. Elle permet de se connecter à de nombreuses sources de données, de les transformer, puis de créer des rapports interactifs et des tableaux de bord visuels. Il est très utilisée en entreprise, Power BI facilite la prise de décisions data-driven grâce à une interface intuitive et des outils puissants de modélisation.

3.  Notion clé : le Dashboard

Un dashboard (ou tableau de bord) est une interface graphique qui regroupe plusieurs visualisations de données en un seul écran. Son objectif est de synthétiser des informations clés de manière claire et interactive pour permettre une lecture rapide et une prise de décision éclairée. Les éléments clés dans le dashboard : Graphiques (barres, lignes, secteurs…), KPIs (indicateurs de performance), Filtres dynamiques, Cartes géographiques

5.  Avantages de Power BI :
  * Gratuit en local 
  * Large connectivité : Compatible avec Excel, CSV, SQL, Azure, API web, etc.
  * Fonctionnement par glisser-déposer, facile à prendre en main.
  * Actualisation automatique : Si la source est connectée, les données peuvent se mettre à jour automatiquement.
  * Possibilité de publier les rapports via Power BI Service (version cloud).
  * Personnalisation avce des visualisations et des filtres.


4. Limites et inconvénients : 
    * Apprentissage technique nécessaire pour les fonctionnalités avancées (langage DAX, Power Query M).
    * Fonctionnalités restreintes sur la version gratuite, notamment pour le partage dans Power BI Service.
    * L’outil peut ralentir avec de très gros volumes de données mal optimisés.

5. Fonctionnalités principales :
    * Connexion à plusieurs sources : fichiers locaux, bases de données, services cloud, API web…
    * Transformation des données via l’éditeur Power Query (nettoyage, filtrage, fusion…).
    * Modélisation : création de relations entre tables, calculs avancés avec DAX.
    * Création de rapports interactifs : graphiques dynamiques, filtres, indicateurs de performance, cartes…
    * Publication & collaboration : partage des rapports sur le cloud grâce à Power BI Service.

6. Types de sources de données compatibles :
    * Fichiers plats : Excel, CSV, JSON, XML
    * Bases de données : SQL Server, MySQL, PostgreSQL, Oracle…
    * Services cloud : Azure, Salesforce, Google Analytics, SharePoint…
    * API Web : extraction de données via une URL
    * Sources locales : import manuel depuis l’ordinateur

7. Visualisations:
    * Graphiques à barres / colonnes : comparaison entre catégories
    * Graphiques linéaires : analyse d’évolution dans le temps
    * Graphiques en secteurs / donuts : répartition des données
    * Cartes : visualisation géographique
    * Cartes thermiques : intensité de valeurs sur des zones
    * Tableaux de bord KPI : suivi de performance
    * Slicers : filtres interactifs pour explorer les données

B/- Contexte :
Ce projet vise à analyser les meurtres commis par Harold Shipman, l’un des tueurs en série les plus prolifiques de l’histoire du Royaume-Uni, à l’aide de Power BI. Deux fichiers de données sont utilisés :
* shipman-confirmed-victims.csv : Contient la liste des victimes confirmées de Shipman, avec leur nom, âge, sexe, date et lieu du décès. Utilisé pour analyser les profils des victimes et l’évolution temporelle des meurtres.
* shipman-times-comparison.csv : Compare les heures de décès des patients de Shipman à celles des patients d’autres médecins généralistes. Utilisé pour identifier un schéma horaire anormal dans les décès.

C/- Problématique étudiée :
Quels types de personnes Harold Shipman a-t-il assassinées, et quand sont-elles mortes ?

D/- Analyse de données :

a. Répartition par sexe :

Sur l’ensemble des victimes confirmées, environ 80 % étaient des femmes, contre seulement 20 % d’hommes. Cette surreprésentation féminine suggère une stratégie ciblée de la part de Shipman, qui exploitait probablement la vulnérabilité des patientes âgées vivant seules. Cette disparité, statistiquement significative, met en évidence un biais sexuel marqué dans ses meurtres.

b. Répartition des âges :

L’analyse de la variable "âge" montre que plus de 75 % des victimes avaient entre 70 et 90 ans, avec une moyenne d’âge d’environ 76 ans. Cette distribution fortement asymétrique vers la droite indique que Shipman visait essentiellement des personnes âgées, souvent considérées comme en fin de vie, ce qui rendait ses actes plus difficiles à détecter. Les personnes de moins de 60 ans représentaient moins de 5 % des victimes.

c. Évolution temporelle des meurtres :

La répartition annuelle des décès met en évidence une intensification progressive de ses meurtres : près de 60 % des décès sont concentrés sur les dix dernières années (1988–1998), avec un pic autour de 1995 à 1998. Cette montée en fréquence témoigne d’une escalade dans son comportement criminel, potentiellement liée à un sentiment d’impunité croissant.

d. Lieu des décès :

Plus de 90 % des décès sont survenus à domicile, lieu dans lesquel Shipman exerçait un contrôle total et bénéficiait de la confiance de ses patients. Cette donnée confirme qu’il agissait dans un environnement maîtrisé, limitant ainsi les risques de suspicion externe ou d’intervention d’autres professionnels de santé.
