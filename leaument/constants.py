from datetime import date

CALENDER_BEGINNING = date(1792, 9, 22)

EXTRA_DAYS = [
    "Jour de la Vertu",
    "Jour du Génie",
    "Jour du Travail",
    "Jour de l'Opinion",
    "Jour des Récompenses",
    "Jour de la Révolution",
]

MONTHS = [
    "Vendémiaire",
    "Brumaire",
    "Frimaire",
    "Nivôse",
    "Pluviôse",
    "Ventôse",
    "Germinal",
    "Floréal",
    "Prairial",
    "Messidor",
    "Thermidor",
    "Fructidor",
]

# Gotten from scripts/parse_day_values_from_wikipedia, and
# corrected for gender afterwards.
DAY_VALUES = [
  [
    {
      "name": "Raisin",
      "href": "/wiki/Raisin",
      "gender": "M"
    },
    {
      "name": "Safran",
      "href": "/wiki/Safran_(%C3%A9pice)",
      "gender": "M"
    },
    {
      "name": "Châtaigne",
      "href": "/wiki/Ch%C3%A2taigne",
      "gender": "F"
    },
    {
      "name": "Colchique",
      "href": "/wiki/Colchique",
      "gender": "F"
    },
    {
      "name": "Cheval",
      "href": "/wiki/Cheval",
      "gender": "M"
    },
    {
      "name": "Balsamine",
      "href": "/wiki/Balsaminaceae",
      "gender": "F"
    },
    {
      "name": "Carotte",
      "href": "/wiki/Carotte",
      "gender": "F"
    },
    {
      "name": "Amarante",
      "href": "/wiki/Amarante_(plante)",
      "gender": "F"
    },
    {
      "name": "Panais",
      "href": "/wiki/Panais",
      "gender": "M"
    },
    {
      "name": "Cuve",
      "href": "/wiki/Cuve",
      "gender": "F"
    },
    {
      "name": "Pomme de terre",
      "href": "/wiki/Pomme_de_terre",
      "gender": "F"
    },
    {
      "name": "Immortelle",
      "href": "/wiki/Immortelle_commune",
      "gender": "F"
    },
    {
      "name": "Potiron",
      "href": "/wiki/Potiron",
      "gender": "M"
    },
    {
      "name": "Réséda",
      "href": "/wiki/R%C3%A9s%C3%A9da",
      "gender": "M"
    },
    {
      "name": "Âne",
      "href": "/wiki/%C3%82ne",
      "gender": "M"
    },
    {
      "name": "Belle-de-nuit",
      "href": "/wiki/Mirabilis_jalapa",
      "gender": "F"
    },
    {
      "name": "Citrouille",
      "href": "/wiki/Citrouille",
      "gender": "F"
    },
    {
      "name": "Sarrasin",
      "href": "/wiki/Sarrasin_commun",
      "gender": "M"
    },
    {
      "name": "Tournesol",
      "href": "/wiki/Tournesol",
      "gender": "M"
    },
    {
      "name": "Pressoir",
      "href": "/wiki/Pressoir",
      "gender": "M"
    },
    {
      "name": "Chanvre",
      "href": "/wiki/Chanvre",
      "gender": "M"
    },
    {
      "name": "Pêche",
      "href": "/wiki/P%C3%AAche_(fruit)",
      "gender": "F"
    },
    {
      "name": "Navet",
      "href": "/wiki/Navet",
      "gender": "M"
    },
    {
      "name": "Amaryllis",
      "href": "/wiki/Amaryllis_(plante)",
      "gender": "F"
    },
    {
      "name": "Bœuf",
      "href": "/wiki/Bos_taurus",
      "gender": "M"
    },
    {
      "name": "Aubergine",
      "href": "/wiki/Aubergine",
      "gender": "F"
    },
    {
      "name": "Piment",
      "href": "/wiki/Piment",
      "gender": "M"
    },
    {
      "name": "Tomate",
      "href": "/wiki/Tomate",
      "gender": "F"
    },
    {
      "name": "Orge",
      "href": "/wiki/Orge_commune",
      "gender": "F"
    },
    {
      "name": "Tonneau",
      "href": "/wiki/Tonneau_(r%C3%A9cipient)",
      "gender": "M"
    }
  ],
  [
    {
      "name": "Pomme",
      "href": "/wiki/Pomme",
      "gender": "F"
    },
    {
      "name": "Céleri",
      "href": "/wiki/C%C3%A9leri",
      "gender": "M"
    },
    {
      "name": "Poire",
      "href": "/wiki/Poire",
      "gender": "F"
    },
    {
      "name": "Betterave",
      "href": "/wiki/Betterave",
      "gender": "F"
    },
    {
      "name": "Oie",
      "href": "/wiki/Oie",
      "gender": "F"
    },
    {
      "name": "Héliotrope",
      "href": "/wiki/H%C3%A9liotrope",
      "gender": "M"
    },
    {
      "name": "Figue",
      "href": "/wiki/Figue",
      "gender": "F"
    },
    {
      "name": "Scorsonère",
      "href": "/wiki/Scorson%C3%A8re",
      "gender": "F"
    },
    {
      "name": "Alisier",
      "href": "/wiki/Sorbus_torminalis",
      "gender": "M"
    },
    {
      "name": "Charrue",
      "href": "/wiki/Charrue",
      "gender": "F"
    },
    {
      "name": "Salsifis",
      "href": "/wiki/Salsifis",
      "gender": "M"
    },
    {
      "name": "Mâcre",
      "href": "/wiki/M%C3%A2cre_nageante",
      "gender": "F"
    },
    {
      "name": "Topinambour",
      "href": "/wiki/Topinambour",
      "gender": "M"
    },
    {
      "name": "Endive",
      "href": "/wiki/Endive",
      "gender": "F"
    },
    {
      "name": "Dindon",
      "href": "/wiki/Dinde",
      "gender": "M"
    },
    {
      "name": "Chervis",
      "href": "/wiki/Chervis",
      "gender": "M"
    },
    {
      "name": "Cresson",
      "href": "/wiki/Cresson_de_fontaine",
      "gender": "M"
    },
    {
      "name": "Dentelaire",
      "href": "/wiki/Plumbago",
      "gender": "F"
    },
    {
      "name": "Grenade",
      "href": "/wiki/Grenade_(fruit)",
      "gender": "F"
    },
    {
      "name": "Herse",
      "href": "/wiki/Herse_(agriculture)",
      "gender": "F"
    },
    {
      "name": "Bacchante",
      "href": "/wiki/Baccharis_halimifolia",
      "gender": "F"
    },
    {
      "name": "Azerole",
      "href": "/wiki/Crataegus_azarolus",
      "gender": "F"
    },
    {
      "name": "Garance",
      "href": "/wiki/Garance_des_teinturiers",
      "gender": "F"
    },
    {
      "name": "Orange",
      "href": "/wiki/Orange_(fruit)",
      "gender": "F"
    },
    {
      "name": "Faisan",
      "href": "/wiki/Faisan",
      "gender": "M"
    },
    {
      "name": "Pistache",
      "href": "/wiki/Pistache",
      "gender": "F"
    },
    {
      "name": "Macjonc",
      "href": "/wiki/Gesse_tub%C3%A9reuse",
      "gender": "M"
    },
    {
      "name": "Coing",
      "href": "/wiki/Coing",
      "gender": "M"
    },
    {
      "name": "Cormier",
      "href": "/wiki/Cormier",
      "gender": "M"
    },
    {
      "name": "Rouleau",
      "href": "/wiki/Rouleau_agricole",
      "gender": "M"
    }
  ],
  [
    {
      "name": "Raiponce",
      "href": "/wiki/Raiponce_(plante)",
      "gender": "F"
    },
    {
      "name": "Turneps",
      "href": "/wiki/Brassica_rapa",
      "gender": "M"
    },
    {
      "name": "Chicorée",
      "href": "/wiki/Chicor%C3%A9e",
      "gender": "F"
    },
    {
      "name": "Nèfle",
      "href": "/wiki/N%C3%A8fle",
      "gender": "F"
    },
    {
      "name": "Cochon",
      "href": "/wiki/Porc",
      "gender": "M"
    },
    {
      "name": "Mâche",
      "href": "/wiki/Valerianella_locusta",
      "gender": "F"
    },
    {
      "name": "Chou-fleur",
      "href": "/wiki/Chou-fleur",
      "gender": "M"
    },
    {
      "name": "Miel",
      "href": "/wiki/Miel",
      "gender": "M"
    },
    {
      "name": "Genièvre",
      "href": "/wiki/Juniperus_communis",
      "gender": "M"
    },
    {
      "name": "Pioche",
      "href": "/wiki/Pioche",
      "gender": "F"
    },
    {
      "name": "Cire",
      "href": "/wiki/Cire",
      "gender": "F"
    },
    {
      "name": "Raifort",
      "href": "/wiki/Raifort",
      "gender": "F"
    },
    {
      "name": "Cèdre",
      "href": "/wiki/C%C3%A8dre",
      "gender": "M"
    },
    {
      "name": "Sapin",
      "href": "/wiki/Sapin",
      "gender": "M"
    },
    {
      "name": "Chevreuil",
      "href": "/wiki/Chevreuil",
      "gender": "M"
    },
    {
      "name": "Ajonc",
      "href": "/wiki/Ulex",
      "gender": "M"
    },
    {
      "name": "Cyprès",
      "href": "/wiki/Cypr%C3%A8s",
      "gender": "M"
    },
    {
      "name": "Lierre",
      "href": "/wiki/Hedera",
      "gender": "M"
    },
    {
      "name": "Sabine",
      "href": "/wiki/Juniperus_sabina",
      "gender": "F"
    },
    {
      "name": "Hoyau",
      "href": "/wiki/Hoyau",
      "gender": "M"
    },
    {
      "name": "Érable sucré",
      "href": "/wiki/%C3%89rable_%C3%A0_sucre",
      "gender": "M"
    },
    {
      "name": "Bruyère",
      "href": "/wiki/Bruy%C3%A8re",
      "gender": "F"
    },
    {
      "name": "Roseau",
      "href": "/wiki/Roseau",
      "gender": "M"
    },
    {
      "name": "Oseille",
      "href": "/wiki/Rumex",
      "gender": "F"
    },
    {
      "name": "Grillon",
      "href": "/wiki/Gryllidae",
      "gender": "M"
    },
    {
      "name": "Pignon",
      "href": "/wiki/Pignon_(pin)",
      "gender": "M"
    },
    {
      "name": "Liège",
      "href": "/wiki/Li%C3%A8ge_(mat%C3%A9riau)",
      "gender": "M"
    },
    {
      "name": "Truffe",
      "href": "/wiki/Truffe_(champignon)",
      "gender": "F"
    },
    {
      "name": "Olive",
      "href": "/wiki/Olive",
      "gender": "F"
    },
    {
      "name": "Pelle",
      "href": "/wiki/Pelle_(outil)",
      "gender": "F"
    }
  ],
  [
    {
      "name": "Tourbe",
      "href": "/wiki/Tourbe",
      "gender": "F"
    },
    {
      "name": "Houille",
      "href": "/wiki/Houille",
      "gender": "F"
    },
    {
      "name": "Bitume",
      "href": "/wiki/Bitume",
      "gender": "M"
    },
    {
      "name": "Soufre",
      "href": "/wiki/Soufre",
      "gender": "M"
    },
    {
      "name": "Chien",
      "href": "/wiki/Chien",
      "gender": "M"
    },
    {
      "name": "Lave",
      "href": "/wiki/Lave",
      "gender": "F"
    },
    {
      "name": "Terre végétale",
      "href": "/wiki/Humus",
      "gender": "F"
    },
    {
      "name": "Fumier",
      "href": "/wiki/Fumier",
      "gender": "M"
    },
    {
      "name": "Salpêtre",
      "href": "/wiki/Nitrate_de_potassium",
      "gender": "M"
    },
    {
      "name": "Fléau",
      "href": "/wiki/Fl%C3%A9au_(agriculture)",
      "gender": "M"
    },
    {
      "name": "Granit",
      "href": "/wiki/Granit",
      "gender": "M"
    },
    {
      "name": "Argile",
      "href": "/wiki/Argile",
      "gender": "F"
    },
    {
      "name": "Ardoise",
      "href": "/wiki/Ardoise",
      "gender": "F"
    },
    {
      "name": "Grès",
      "href": "/wiki/Gr%C3%A8s_(g%C3%A9ologie)",
      "gender": "M"
    },
    {
      "name": "Lapin",
      "href": "/wiki/Oryctolagus_cuniculus",
      "gender": "M"
    },
    {
      "name": "Silex",
      "href": "/wiki/Silex",
      "gender": "M"
    },
    {
      "name": "Marne",
      "href": "/wiki/Marne_(g%C3%A9ologie)",
      "gender": "F"
    },
    {
      "name": "Pierre à chaux",
      "href": "/wiki/Calcaire",
      "gender": "F"
    },
    {
      "name": "Marbre",
      "href": "/wiki/Marbre",
      "gender": "M"
    },
    {
      "name": "Van",
      "href": "/wiki/Van_(agriculture)",
      "gender": "M"
    },
    {
      "name": "Pierre à plâtre",
      "href": "/wiki/Gypse",
      "gender": "F"
    },
    {
      "name": "Sel",
      "href": "/wiki/Chlorure_de_sodium",
      "gender": "M"
    },
    {
      "name": "Fer",
      "href": "/wiki/Fer",
      "gender": "M"
    },
    {
      "name": "Cuivre",
      "href": "/wiki/Cuivre",
      "gender": "M"
    },
    {
      "name": "Chat",
      "href": "/wiki/Chat",
      "gender": "M"
    },
    {
      "name": "Étain",
      "href": "/wiki/%C3%89tain",
      "gender": "M"
    },
    {
      "name": "Plomb",
      "href": "/wiki/Plomb",
      "gender": "M"
    },
    {
      "name": "Zinc",
      "href": "/wiki/Zinc",
      "gender": "M"
    },
    {
      "name": "Mercure",
      "href": "/wiki/Mercure_(chimie)",
      "gender": "M"
    },
    {
      "name": "Crible",
      "href": "/wiki/Tamis",
      "gender": "M"
    }
  ],
  [
    {
      "name": "Lauréole",
      "href": "/wiki/Daphne_laureola",
      "gender": "F"
    },
    {
      "name": "Mousse",
      "href": "/wiki/Bryophyta",
      "gender": "F"
    },
    {
      "name": "Fragon",
      "href": "/wiki/Ruscus_aculeatus",
      "gender": "M"
    },
    {
      "name": "Perce neige",
      "href": "/wiki/Perce-neige",
      "gender": "M"
    },
    {
      "name": "Taureau",
      "href": "/wiki/Taureau",
      "gender": "M"
    },
    {
      "name": "Laurier thym",
      "href": "/wiki/Viorne_tin",
      "gender": "M"
    },
    {
      "name": "Amadouvier",
      "href": "/wiki/Amadouvier",
      "gender": "M"
    },
    {
      "name": "Mézéréon",
      "href": "/wiki/Bois-joli",
      "gender": "M"
    },
    {
      "name": "Peuplier",
      "href": "/wiki/Peuplier",
      "gender": "M"
    },
    {
      "name": "Cognée",
      "href": "/wiki/Cogn%C3%A9e",
      "gender": "F"
    },
    {
      "name": "Ellébore",
      "href": "/wiki/Hell%C3%A9bore",
      "gender": "F"
    },
    {
      "name": "Brocoli",
      "href": "/wiki/Brocoli",
      "gender": "M"
    },
    {
      "name": "Laurier",
      "href": "/wiki/Laurus_nobilis",
      "gender": "M"
    },
    {
      "name": "Avelinier",
      "href": "/wiki/Noisetier",
      "gender": "M"
    },
    {
      "name": "Vache",
      "href": "/wiki/Vache",
      "gender": "F"
    },
    {
      "name": "Buis",
      "href": "/wiki/Buis",
      "gender": "M"
    },
    {
      "name": "Lichen",
      "href": "/wiki/Lichen",
      "gender": "M"
    },
    {
      "name": "If",
      "href": "/wiki/Taxus",
      "gender": "M"
    },
    {
      "name": "Pulmonaire",
      "href": "/wiki/Pulmonaria",
      "gender": "F"
    },
    {
      "name": "Serpette",
      "href": "/wiki/Serpette",
      "gender": "F"
    },
    {
      "name": "Thlaspi",
      "href": "/wiki/Thlaspi",
      "gender": "M"
    },
    {
      "name": "Thymèle",
      "href": "/wiki/Daphn%C3%A9_garou",
      "gender": "F"
    },
    {
      "name": "Chiendent",
      "href": "/wiki/Chiendent",
      "gender": "M"
    },
    {
      "name": "Trainasse",
      "href": "/wiki/Renou%C3%A9e_des_oiseaux",
      "gender": "F"
    },
    {
      "name": "Lièvre",
      "href": "/wiki/Li%C3%A8vre",
      "gender": "M"
    },
    {
      "name": "Guède",
      "href": "/wiki/Pastel_des_teinturiers",
      "gender": "F"
    },
    {
      "name": "Noisetier",
      "href": "/wiki/Noisetier",
      "gender": "M"
    },
    {
      "name": "Cyclamen",
      "href": "/wiki/Cyclamen",
      "gender": "M"
    },
    {
      "name": "Chélidoine",
      "href": "/wiki/Chelidonium_majus",
      "gender": "F"
    },
    {
      "name": "Traîneau",
      "href": "/wiki/Tra%C3%AEneau",
      "gender": "M"
    }
  ],
  [
    {
      "name": "Tussilage",
      "href": "/wiki/Tussilage",
      "gender": "M"
    },
    {
      "name": "Cornouiller",
      "href": "/wiki/Cornus_(plante)",
      "gender": "M"
    },
    {
      "name": "Violier",
      "href": "/wiki/V%C3%A9lar",
      "gender": "M"
    },
    {
      "name": "Troène",
      "href": "/wiki/Tro%C3%A8ne",
      "gender": "M"
    },
    {
      "name": "Bouc",
      "href": "/wiki/Bouc",
      "gender": "M"
    },
    {
      "name": "Asaret",
      "href": "/wiki/Asaret",
      "gender": "M"
    },
    {
      "name": "Alaterne",
      "href": "/wiki/Nerprun_alaterne",
      "gender": "M"
    },
    {
      "name": "Violette",
      "href": "/wiki/Viola_(genre_v%C3%A9g%C3%A9tal)",
      "gender": "F"
    },
    {
      "name": "Marceau",
      "href": "/wiki/Saule_marsault",
      "gender": "M"
    },
    {
      "name": "Bêche",
      "href": "/wiki/B%C3%AAche",
      "gender": "F"
    },
    {
      "name": "Narcisse",
      "href": "/wiki/Narcissus",
      "gender": "M"
    },
    {
      "name": "Orme",
      "href": "/wiki/Orme",
      "gender": "M"
    },
    {
      "name": "Fumeterre",
      "href": "/wiki/Fumeterre",
      "gender": "F"
    },
    {
      "name": "Vélar",
      "href": "/wiki/V%C3%A9lar",
      "gender": "M"
    },
    {
      "name": "Chèvre",
      "href": "/wiki/Ch%C3%A8vre",
      "gender": "F"
    },
    {
      "name": "Épinard",
      "href": "/wiki/%C3%89pinard",
      "gender": "M"
    },
    {
      "name": "Doronic",
      "href": "/wiki/Doronicum",
      "gender": "M"
    },
    {
      "name": "Mouron",
      "href": "/wiki/Mouron_(flore)",
      "gender": "M"
    },
    {
      "name": "Cerfeuil",
      "href": "/wiki/Cerfeuil_commun",
      "gender": "M"
    },
    {
      "name": "Cordeau",
      "href": "/wiki/Cordeau",
      "gender": "M"
    },
    {
      "name": "Mandragore",
      "href": "/wiki/Mandragore",
      "gender": "F"
    },
    {
      "name": "Persil",
      "href": "/wiki/Persil",
      "gender": "M"
    },
    {
      "name": "Cochléaria",
      "href": "/wiki/Cochlearia",
      "gender": "M"
    },
    {
      "name": "Pâquerette",
      "href": "/wiki/P%C3%A2querette",
      "gender": "F"
    },
    {
      "name": "Thon",
      "href": "/wiki/Thon",
      "gender": "M"
    },
    {
      "name": "Pissenlit",
      "href": "/wiki/Pissenlit",
      "gender": "M"
    },
    {
      "name": "Sylvie",
      "href": "/wiki/An%C3%A9mone_sylvie",
      "gender": "F"
    },
    {
      "name": "Capillaire",
      "href": "/wiki/Capillaire_de_Montpellier",
      "gender": "F"
    },
    {
      "name": "Frêne",
      "href": "/wiki/Fr%C3%AAne",
      "gender": "M"
    },
    {
      "name": "Plantoir",
      "href": "/wiki/Plantoir",
      "gender": "M"
    }
  ],
  [
    {
      "name": "Primevère",
      "href": "/wiki/Primev%C3%A8re",
      "gender": "F"
    },
    {
      "name": "Platane",
      "href": "/wiki/Platane",
      "gender": "M"
    },
    {
      "name": "Asperge",
      "href": "/wiki/Asperge",
      "gender": "F"
    },
    {
      "name": "Tulipe",
      "href": "/wiki/Tulipe",
      "gender": "F"
    },
    {
      "name": "Poule",
      "href": "/wiki/Poule",
      "gender": "F"
    },
    {
      "name": "Bette",
      "href": "/wiki/Bette_(plante)",
      "gender": "F"
    },
    {
      "name": "Bouleau",
      "href": "/wiki/Bouleau",
      "gender": "M"
    },
    {
      "name": "Jonquille",
      "href": "/wiki/Jonquille",
      "gender": "F"
    },
    {
      "name": "Aulne",
      "href": "/wiki/Aulne",
      "gender": "M"
    },
    {
      "name": "Couvoir",
      "href": "/wiki/Incubateur_(%C5%93uf)",
      "gender": "M"
    },
    {
      "name": "Pervenche",
      "href": "/wiki/Pervenche",
      "gender": "F"
    },
    {
      "name": "Charme",
      "href": "/wiki/Charme",
      "gender": "M"
    },
    {
      "name": "Morille",
      "href": "/wiki/Morchella",
      "gender": "F"
    },
    {
      "name": "Hêtre",
      "href": "/wiki/H%C3%AAtre_commun",
      "gender": "M"
    },
    {
      "name": "Abeille",
      "href": "/wiki/Abeille",
      "gender": "F"
    },
    {
      "name": "Laitue",
      "href": "/wiki/Laitue",
      "gender": "F"
    },
    {
      "name": "Mélèze",
      "href": "/wiki/M%C3%A9l%C3%A8ze",
      "gender": "M"
    },
    {
      "name": "Ciguë",
      "href": "/wiki/Apiaceae",
      "gender": "F"
    },
    {
      "name": "Radis",
      "href": "/wiki/Radis",
      "gender": "M"
    },
    {
      "name": "Ruche",
      "href": "/wiki/Ruche",
      "gender": "F"
    },
    {
      "name": "Gainier",
      "href": "/wiki/Arbre_de_Jud%C3%A9e",
      "gender": "M"
    },
    {
      "name": "Romaine",
      "href": "/wiki/Laitue_romaine",
      "gender": "F"
    },
    {
      "name": "Marronnier",
      "href": "/wiki/Aesculus_hippocastanum",
      "gender": "M"
    },
    {
      "name": "Roquette",
      "href": "/wiki/Roquette_(plante)",
      "gender": "F"
    },
    {
      "name": "Pigeon",
      "href": "/wiki/Columba_(oiseau)",
      "gender": "M"
    },
    {
      "name": "Lilas",
      "href": "/wiki/Syringa_vulgaris",
      "gender": "M"
    },
    {
      "name": "Anémone",
      "href": "/wiki/An%C3%A9mone",
      "gender": "F"
    },
    {
      "name": "Pensée",
      "href": "/wiki/Viola_(genre_v%C3%A9g%C3%A9tal)",
      "gender": "F"
    },
    {
      "name": "Myrtille",
      "href": "/wiki/Myrtille",
      "gender": "F"
    },
    {
      "name": "Greffoir",
      "href": "/wiki/Greffoir",
      "gender": "M"
    }
  ],
  [
    {
      "name": "Rose",
      "href": "/wiki/Rose_(fleur)",
      "gender": "F"
    },
    {
      "name": "Chêne",
      "href": "/wiki/Ch%C3%AAne",
      "gender": "M"
    },
    {
      "name": "Fougère",
      "href": "/wiki/Filicophyta",
      "gender": "F"
    },
    {
      "name": "Aubépine",
      "href": "/wiki/Aub%C3%A9pine",
      "gender": "F"
    },
    {
      "name": "Rossignol",
      "href": "/wiki/Rossignol",
      "gender": "M"
    },
    {
      "name": "Ancolie",
      "href": "/wiki/Ancolie",
      "gender": "F"
    },
    {
      "name": "Muguet",
      "href": "/wiki/Muguet_de_mai",
      "gender": "M"
    },
    {
      "name": "Champignon",
      "href": "/wiki/Champignon",
      "gender": "M"
    },
    {
      "name": "Hyacinthe",
      "href": "/wiki/Hyacinthus",
      "gender": "F"
    },
    {
      "name": "Râteau",
      "href": "/wiki/R%C3%A2teau_(outil)",
      "gender": "M"
    },
    {
      "name": "Rhubarbe",
      "href": "/wiki/Rhubarbe",
      "gender": "F"
    },
    {
      "name": "Sainfoin",
      "href": "/wiki/Onobrychis",
      "gender": "M"
    },
    {
      "name": "Bâton-d'or",
      "href": "/wiki/V%C3%A9lar",
      "gender": "M"
    },
    {
      "name": "Chamérisier",
      "href": "/wiki/Lonicera_xylosteum",
      "gender": "M"
    },
    {
      "name": "Ver à soie",
      "href": "/wiki/Bombyx_du_m%C3%BBrier",
      "gender": "M"
    },
    {
      "name": "Consoude",
      "href": "/wiki/Consoude",
      "gender": "F"
    },
    {
      "name": "Pimprenelle",
      "href": "/wiki/Pimprenelle",
      "gender": "F"
    },
    {
      "name": "Corbeille d'or",
      "href": "/wiki/Corbeille_d%27or",
      "gender": "F"
    },
    {
      "name": "Arroche",
      "href": "/wiki/Arroche_des_jardins",
      "gender": "F"
    },
    {
      "name": "Sarcloir",
      "href": "/wiki/Sarcloir",
      "gender": "M"
    },
    {
      "name": "Statice",
      "href": "/wiki/Arm%C3%A9rie_maritime",
      "gender": "F"
    },
    {
      "name": "Fritillaire",
      "href": "/wiki/Fritillaire",
      "gender": "F"
    },
    {
      "name": "Bourrache",
      "href": "/wiki/Bourrache",
      "gender": "F"
    },
    {
      "name": "Valériane",
      "href": "/wiki/Val%C3%A9riane",
      "gender": "F"
    },
    {
      "name": "Carpe",
      "href": "/wiki/Carpe_(poisson)",
      "gender": "F"
    },
    {
      "name": "Fusain",
      "href": "/wiki/Fusain_d%27Europe",
      "gender": "M"
    },
    {
      "name": "Civette",
      "href": "/wiki/Ciboulette_commune",
      "gender": "F"
    },
    {
      "name": "Buglosse",
      "href": "/wiki/Anchusa",
      "gender": "F"
    },
    {
      "name": "Sénevé",
      "href": "/wiki/Moutarde_blanche",
      "gender": "M"
    },
    {
      "name": "Houlette",
      "href": "/wiki/Houlette_(agriculture)",
      "gender": "F"
    }
  ],
  [
    {
      "name": "Luzerne",
      "href": "/wiki/Luzerne_cultiv%C3%A9e",
      "gender": "F"
    },
    {
      "name": "Hémérocalle",
      "href": "/wiki/H%C3%A9m%C3%A9rocalle",
      "gender": "F"
    },
    {
      "name": "Trèfle",
      "href": "/wiki/Tr%C3%A8fle",
      "gender": "M"
    },
    {
      "name": "Angélique",
      "href": "/wiki/Angelica",
      "gender": "F"
    },
    {
      "name": "Canard",
      "href": "/wiki/Canard",
      "gender": "M"
    },
    {
      "name": "Mélisse",
      "href": "/wiki/M%C3%A9lisse_officinale",
      "gender": "F"
    },
    {
      "name": "Fromental",
      "href": "/wiki/Arrhenatherum_elatius",
      "gender": "M"
    },
    {
      "name": "Martagon",
      "href": "/wiki/Lis_martagon",
      "gender": "M"
    },
    {
      "name": "Serpolet",
      "href": "/wiki/Serpolet",
      "gender": "M"
    },
    {
      "name": "Faux",
      "href": "/wiki/Faux_(outil)",
      "gender": "M"
    },
    {
      "name": "Fraise",
      "href": "/wiki/Fraise",
      "gender": "F"
    },
    {
      "name": "Bétoine",
      "href": "/wiki/%C3%89piaire_officinale",
      "gender": "F"
    },
    {
      "name": "Pois",
      "href": "/wiki/Pois_cultiv%C3%A9",
      "gender": "M"
    },
    {
      "name": "Acacia",
      "href": "/wiki/Robinia_pseudoacacia",
      "gender": "M"
    },
    {
      "name": "Caille",
      "href": "/wiki/Caille",
      "gender": "F"
    },
    {
      "name": "Œillet",
      "href": "/wiki/%C5%92illet",
      "gender": "M"
    },
    {
      "name": "Sureau",
      "href": "/wiki/Sureau",
      "gender": "M"
    },
    {
      "name": "Pavot",
      "href": "/wiki/Pavot",
      "gender": "M"
    },
    {
      "name": "Tilleul",
      "href": "/wiki/Tilia",
      "gender": "M"
    },
    {
      "name": "Fourche",
      "href": "/wiki/Fourche",
      "gender": "F"
    },
    {
      "name": "Barbeau",
      "href": "/wiki/Cyanus_segetum",
      "gender": "M"
    },
    {
      "name": "Camomille",
      "href": "/wiki/Camomille_romaine",
      "gender": "F"
    },
    {
      "name": "Chèvrefeuille",
      "href": "/wiki/Ch%C3%A8vrefeuille",
      "gender": "M"
    },
    {
      "name": "Caille-lait",
      "href": "/wiki/Gaillet",
      "gender": "M"
    },
    {
      "name": "Tanche",
      "href": "/wiki/Tanche",
      "gender": "F"
    },
    {
      "name": "Jasmin",
      "href": "/wiki/Jasmin",
      "gender": "M"
    },
    {
      "name": "Verveine",
      "href": "/wiki/Verbena",
      "gender": "F"
    },
    {
      "name": "Thym",
      "href": "/wiki/Thym",
      "gender": "M"
    },
    {
      "name": "Pivoine",
      "href": "/wiki/Pivoine",
      "gender": "F"
    },
    {
      "name": "Chariot",
      "href": "/wiki/Chariot",
      "gender": "M"
    }
  ],
  [
    {
      "name": "Seigle",
      "href": "/wiki/Seigle",
      "gender": "M"
    },
    {
      "name": "Avoine",
      "href": "/wiki/Avoine_cultiv%C3%A9e",
      "gender": "F"
    },
    {
      "name": "Oignon",
      "href": "/wiki/Oignon",
      "gender": "M"
    },
    {
      "name": "Véronique",
      "href": "/wiki/V%C3%A9ronique_(plante)",
      "gender": "F"
    },
    {
      "name": "Mulet",
      "href": "/wiki/Mulet",
      "gender": "M"
    },
    {
      "name": "Romarin",
      "href": "/wiki/Romarin",
      "gender": "M"
    },
    {
      "name": "Concombre",
      "href": "/wiki/Concombre",
      "gender": "M"
    },
    {
      "name": "Échalote",
      "href": "/wiki/%C3%89chalote",
      "gender": "F"
    },
    {
      "name": "Absinthe",
      "href": "/wiki/Absinthe_(plante)",
      "gender": "F"
    },
    {
      "name": "Faucille",
      "href": "/wiki/Faucille",
      "gender": "F"
    },
    {
      "name": "Coriandre",
      "href": "/wiki/Coriandre",
      "gender": "F"
    },
    {
      "name": "Artichaut",
      "href": "/wiki/Artichaut",
      "gender": "M"
    },
    {
      "name": "Giroflée",
      "href": "/wiki/Girofl%C3%A9e_des_murailles",
      "gender": "F"
    },
    {
      "name": "Lavande",
      "href": "/wiki/Lavande",
      "gender": "F"
    },
    {
      "name": "Chamois",
      "href": "/wiki/Chamois",
      "gender": "M"
    },
    {
      "name": "Tabac",
      "href": "/wiki/Tabac",
      "gender": "M"
    },
    {
      "name": "Groseille",
      "href": "/wiki/Groseille",
      "gender": "F"
    },
    {
      "name": "Gesse",
      "href": "/wiki/Lathyrus",
      "gender": "F"
    },
    {
      "name": "Cerise",
      "href": "/wiki/Cerise",
      "gender": "F"
    },
    {
      "name": "Parc",
      "href": "/wiki/Parc",
      "gender": "M"
    },
    {
      "name": "Menthe",
      "href": "/wiki/Menthe",
      "gender": "F"
    },
    {
      "name": "Cumin",
      "href": "/wiki/Cumin",
      "gender": "M"
    },
    {
      "name": "Haricot",
      "href": "/wiki/Haricot",
      "gender": "M"
    },
    {
      "name": "Orcanète",
      "href": "/wiki/Orcanette_des_teinturiers",
      "gender": "F"
    },
    {
      "name": "Pintade",
      "href": "/wiki/Pintade",
      "gender": "F"
    },
    {
      "name": "Sauge",
      "href": "/wiki/Sauge",
      "gender": "F"
    },
    {
      "name": "Ail",
      "href": "/wiki/Ail_cultiv%C3%A9",
      "gender": "M"
    },
    {
      "name": "Vesce",
      "href": "/wiki/Vicia",
      "gender": "F"
    },
    {
      "name": "Blé",
      "href": "/wiki/Bl%C3%A9",
      "gender": "M"
    },
    {
      "name": "Chalemie",
      "href": "/wiki/Chalemie",
      "gender": "F"
    }
  ],
  [
    {
      "name": "Épeautre",
      "href": "/wiki/%C3%89peautre",
      "gender": "M"
    },
    {
      "name": "Bouillon-blanc",
      "href": "/wiki/Bouillon-blanc",
      "gender": "M"
    },
    {
      "name": "Melon",
      "href": "/wiki/Melon_(plante)",
      "gender": "M"
    },
    {
      "name": "Ivraie",
      "href": "/wiki/Ivraie",
      "gender": "F"
    },
    {
      "name": "Bélier",
      "href": "/wiki/B%C3%A9lier",
      "gender": "M"
    },
    {
      "name": "Prêle",
      "href": "/wiki/Equisetidae",
      "gender": "F"
    },
    {
      "name": "Armoise",
      "href": "/wiki/Armoise",
      "gender": "F"
    },
    {
      "name": "Carthame",
      "href": "/wiki/Carthame",
      "gender": "M"
    },
    {
      "name": "Mûre",
      "href": "/wiki/M%C3%BBre_(fruit_de_la_ronce)",
      "gender": "F"
    },
    {
      "name": "Arrosoir",
      "href": "/wiki/Arrosoir",
      "gender": "M"
    },
    {
      "name": "Panic",
      "href": "/wiki/Panic_(plante)",
      "gender": "M"
    },
    {
      "name": "Salicorne",
      "href": "/wiki/Salicorne",
      "gender": "F"
    },
    {
      "name": "Abricot",
      "href": "/wiki/Abricot",
      "gender": "M"
    },
    {
      "name": "Basilic",
      "href": "/wiki/Basilic_(plante)",
      "gender": "M"
    },
    {
      "name": "Brebis",
      "href": "/wiki/Mouton",
      "gender": "F"
    },
    {
      "name": "Guimauve",
      "href": "/wiki/Guimauve_officinale",
      "gender": "F"
    },
    {
      "name": "Lin",
      "href": "/wiki/Lin_cultiv%C3%A9",
      "gender": "M"
    },
    {
      "name": "Amande",
      "href": "/wiki/Amande",
      "gender": "F"
    },
    {
      "name": "Gentiane",
      "href": "/wiki/Gentiane",
      "gender": "F"
    },
    {
      "name": "Écluse",
      "href": "/wiki/%C3%89cluse",
      "gender": "F"
    },
    {
      "name": "Carline",
      "href": "/wiki/Carline",
      "gender": "F"
    },
    {
      "name": "Câprier",
      "href": "/wiki/C%C3%A2prier",
      "gender": "M"
    },
    {
      "name": "Lentille",
      "href": "/wiki/Lentille_cultiv%C3%A9e",
      "gender": "F"
    },
    {
      "name": "Aunée",
      "href": "/wiki/Inula",
      "gender": "F"
    },
    {
      "name": "Loutre",
      "href": "/wiki/Loutre",
      "gender": "F"
    },
    {
      "name": "Myrte",
      "href": "/wiki/Myrte",
      "gender": "M"
    },
    {
      "name": "Colza",
      "href": "/wiki/Colza",
      "gender": "M"
    },
    {
      "name": "Lupin",
      "href": "/wiki/Lupin",
      "gender": "M"
    },
    {
      "name": "Coton",
      "href": "/wiki/Coton",
      "gender": "M"
    },
    {
      "name": "Moulin",
      "href": "/wiki/Moulin",
      "gender": "M"
    }
  ],
  [
    {
      "name": "Prune",
      "href": "/wiki/Prune",
      "gender": "F"
    },
    {
      "name": "Millet",
      "href": "/wiki/Millet_(gramin%C3%A9e)",
      "gender": "M"
    },
    {
      "name": "Lycoperdon",
      "href": "/wiki/Vesse-de-loup",
      "gender": "M"
    },
    {
      "name": "Escourgeon",
      "href": "/wiki/Escourgeon",
      "gender": "M"
    },
    {
      "name": "Saumon",
      "href": "/wiki/Saumon",
      "gender": "M"
    },
    {
      "name": "Tubéreuse",
      "href": "/wiki/Tub%C3%A9reuse",
      "gender": "F"
    },
    {
      "name": "Sucrion",
      "href": "/wiki/Escourgeon",
      "gender": "M"
    },
    {
      "name": "Apocyn",
      "href": "/wiki/Asclepias_syriaca",
      "gender": "M"
    },
    {
      "name": "Réglisse",
      "href": "/wiki/R%C3%A9glisse",
      "gender": "F"
    },
    {
      "name": "Échelle",
      "href": "/wiki/%C3%89chelle_(outil)",
      "gender": "F"
    },
    {
      "name": "Pastèque",
      "href": "/wiki/Past%C3%A8que",
      "gender": "F"
    },
    {
      "name": "Fenouil",
      "href": "/wiki/Fenouil",
      "gender": "M"
    },
    {
      "name": "Épine-vinette",
      "href": "/wiki/%C3%89pine-vinette",
      "gender": "F"
    },
    {
      "name": "Noix",
      "href": "/wiki/Noix",
      "gender": "F"
    },
    {
      "name": "Truite",
      "href": "/wiki/Truite",
      "gender": "F"
    },
    {
      "name": "Citron",
      "href": "/wiki/Citron",
      "gender": "M"
    },
    {
      "name": "Cardère",
      "href": "/wiki/Card%C3%A8re_sauvage",
      "gender": "F"
    },
    {
      "name": "Nerprun",
      "href": "/wiki/Nerprun",
      "gender": "M"
    },
    {
      "name": "Tagette",
      "href": "/wiki/Tagetes",
      "gender": "M"
    },
    {
      "name": "Hotte",
      "href": "/wiki/Panier",
      "gender": "F"
    },
    {
      "name": "Églantier",
      "href": "/wiki/Rosa_canina",
      "gender": "M"
    },
    {
      "name": "Noisette",
      "href": "/wiki/Noisette",
      "gender": "F"
    },
    {
      "name": "Houblon",
      "href": "/wiki/Houblon",
      "gender": "M"
    },
    {
      "name": "Sorgho",
      "href": "/wiki/Sorgo_commun",
      "gender": "M"
    },
    {
      "name": "Écrevisse",
      "href": "/wiki/%C3%89crevisse",
      "gender": "F"
    },
    {
      "name": "Bigarade",
      "href": "/wiki/Bigaradier",
      "gender": "F"
    },
    {
      "name": "Verge d'or",
      "href": "/wiki/Solidago",
      "gender": "F"
    },
    {
      "name": "Maïs",
      "href": "/wiki/Ma%C3%AFs",
      "gender": "M"
    },
    {
      "name": "Marron",
      "href": "/wiki/Marron_(fruit)",
      "gender": "M"
    },
    {
      "name": "Panier",
      "href": "/wiki/Panier",
      "gender": "M"
    }
  ]
]

