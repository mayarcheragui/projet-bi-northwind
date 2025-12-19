\# 📊 Projet BI – Northwind



\## 🎯 Objectif du projet

Ce projet a pour objectif de mettre en place un mini système de Business Intelligence (BI) à partir de la base de données \*\*Northwind\*\*.



L’objectif est de :

\- Extraire les données (ETL)

\- Construire des tables de dimensions et une table de faits

\- Analyser les commandes

\- Visualiser les résultats à l’aide de graphiques (Python \& Notebook)



---



\## 🗂 Structure du projet

\# 📊 Projet BI – Northwind



\## 🎯 Objectif du projet

Ce projet a pour objectif de mettre en place un mini système de Business Intelligence (BI) à partir de la base de données \*\*Northwind\*\*.



L’objectif est de :

\- Extraire les données (ETL)

\- Construire des tables de dimensions et une table de faits

\- Analyser les commandes

\- Visualiser les résultats à l’aide de graphiques (Python \& Notebook)



---



\## 🗂 Structure du projet



projet\_bi\_northwind/

│

├── data/

│ ├── raw/ 

│ └── processed/

│

├── outputs/

│ └── figures/ 

│

├── scripts/

│ ├── etl.py 

│ └── dashboard.py 

│

├── analysis.ipynb 

├── reports/

│ └── Rapport projet.pdf 

│

├── video/ 

└── README.md



---



\## 🔄 ETL (Extract – Transform – Load)



Le script `etl.py` réalise les étapes suivantes :



\### 1️⃣ Extraction

\- Lecture des fichiers CSV :

&nbsp; - Employees

&nbsp; - Customers

&nbsp; - Orders



\### 2️⃣ Transformation

\- Création des dimensions :

&nbsp; - `dim\_employee`

&nbsp; - `dim\_customer`

\- Création de la table de faits `fact\_orders`

\- Calcul des indicateurs :

&nbsp; - `nb\_commandes\_livrees`

&nbsp; - `nb\_commandes\_non\_livrees`



\### 3️⃣ Chargement

\- Sauvegarde des tables transformées dans le dossier `data/processed`



---



\## 📊 Analyses \& Visualisations



Les graphiques générés permettent d’analyser :



\- Répartition globale des commandes livrées / non livrées

\- Commandes livrées / non livrées par client

\- Commandes livrées / non livrées par employé

\- Évolution mensuelle des commandes

\- Graphe 3D : employé / client / date / commandes livrées et non livrées



Les graphiques sont enregistrés dans :

outputs/figures



---



\## 📒 Jupyter Notebook



Le fichier `analysis.ipynb` permet :

\- D’explorer les données étape par étape

\- De générer les graphiques

\- D’expliquer l’analyse de manière pédagogique



---



\## 🛠 Technologies utilisées



\- Python

\- Pandas

\- Matplotlib

\- Plotly

\- Jupyter Notebook

\- SQL Server (source des données)



---



\## ✅ Résultat final



Le projet fournit :

\- Un ETL fonctionnel

\- Des données propres et structurées

\- Des visualisations claires

\- Un notebook explicatif

\- Une vidéo de présentation



---



\## 👩‍🎓 Projet académique

Projet réalisé dans le cadre d’un cours de Business Intelligence.





