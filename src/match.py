
####
### All changes listed:
###
### - [00:00] First half started
### - [05:10] Fault - T1 - yellow card
### - [07:33] Goal - T1
### - [20:14] Goal - T1
### - [25:10] Fault - T1 - red card
### - [29:02] Fault - T1 - red card
### - [43:44] Goal - T2
### - [45:00] Extra time +01
### - [45:00 + 01:00] First half ended
### - [45:00] Second half started
### - [46:25] Fault - T2 - yellow card
### - [51:54] Goal - T2
### - [59:41] Goal - T2
### - [62:12] Fault - T1 - yellow card
### - [67:37] Goal - T2
### - [77:55] Goal - T2
### - [82:04] Fault - T2 - red card
### - [88:59] Goal - T1
### - [90:00] Extra time +03
### - [90:00 + 02:01] Goal - T1
### - [90:00 + 03:00] Second half ended
### - [90:00 + 03:00] Result 4-5 - T2 Wins
####
CHANGES = {
    ### - First half
    "FIRST_HALF": [
        ### - [00:00] First half started
        {
            "time": "00:00",
            "ops": {
                "/matchData/scores": {
                    "type": "set",
                    "value": {
                        "ht": {
                            "home": 0,
                            "away": 0
                        },
                        "total": {
                            "home": 0,
                            "away": 0
                        }
                    }
                },
                "/matchData/status": {
                    "type": "set",
                    "value": "playing"
                },
                "/matchData/period": {
                    "type": "set", # TODO: this should be an append to array
                    "value": [
                        {
                            "id": 1,
                            "start": "2022-01-12T14:00:44Z"
                        }
                    ]
                }
            }
        },
        ### - [05:10] Fault - T1 - yellow card
        {
            "time": "05:10",
            "ops": {
                "/matchData/scores": {
                    "type": "set",
                    "value": {
                        "ht": {
                            "home": 0,
                            "away": 0
                        },
                        "total": {
                            "home": 0,
                            "away": 0
                        }
                    }
                },
                "/matchData/status": {
                    "type": "set",
                    "value": "playing"
                },
                "/matchData/period": {
                    "type": "set",
                    "value": [
                        {
                            "id": 1,
                            "start": "2022-01-12T14:00:44Z"
                        }
                    ]
                }
            }
        },
        ### - [45:00] Extra time +01
        # TODO: add sth
        {
            "time": "45:00",
            "ops": {}
        },
        ### - [45:00 + 01:00] First half ended
        {
            "time": "46:00",
            "ops": {
                "/matchData/status": {
                    "type": "set",
                    "value": "halftime"
                },
                "/matchData/period/0": {
                    "type": "set",
                    "value": {
                        "id": 1,
                        "start": "2023-01-12T14:00:00Z",
                        "end": "2023-01-12T14:46:22Z"
                    }
                }
            }
        },
    ],
    "SECOND_HALF": [
        ### - [45:00] Second half started
        {
            "time": "45:00",
            "ops": {
                "/matchData/scores": {
                    "type": "set", # TODO: this should be an addition of a property and not a replacement
                    "value": {
                        "ht": {
                            "home": 0,
                            "away": 0
                        },
                        "ft": {
                            "home": 0,
                            "away": 0
                        },
                        "total": {
                            "home": 0,
                            "away": 0
                        }
                    }
                },
                "/matchData/status": {
                    "type": "set",
                    "value": "playing"
                },
                "/matchData/period": {
                    "type": "set", # TODO: this should be an append to array
                    "value": [
                        {
                            "id": 1,
                            "start": "2023-01-12T14:00:00Z",
                            "end": "2023-01-12T14:46:22Z"
                        },
                        {
                            "id": 2,
                            "start": "2023-01-12T15:02:00Z",
                        }
                    ]
                }
            }
        },
        ### - [90:00 + 03:00] Second half ended
        {
            "time": "93:00",
            "ops": {
                "/matchData/status": {
                    "type": "set",
                    "value": "finished"
                },
                "/matchData/period/1": {
                    "type": "set",
                    "value": {
                        "id": 2,
                        "start": "2023-01-12T15:02:00Z",
                        "end": "2023-01-12T15:50:00Z"
                    }
                }
            }
        },
    ]
}

INITIAL = {
    "matchInfo": {
        "date":           "2023-01-01Z",  
        "time":           "00:00:00Z",
        "overtimeLength": 0,
        "contenstant": [
            {
                "id":         "3oj3koph7uf63y1f9zr8r7ylo",
                "name":         "Newell's Old Boys",
                "shortName":    "NOB",
                "officialName": "Newell's Old Boys",
                "code":         "NOB",
                "position":     "home",
                "country": {
                    "id": "2vovxa97k7v7ofa85dah2xktb",
                    "name": "Argentina"
                }
            },
            {
                "id":         "1tsjuhn8qeikaj837w2ybx77n",
                "name":         "Sarmiento",
                "shortName":    "Sarmiento",
                "officialName": "CA Sarmiento",
                "code":         "SAR",
                "position":     "away",
                "country": {
                    "id": "2vovxa97k7v7ofa85dah2xktb",
                    "name": "Argentina"
                }
            }
        ],
        "venue": {
            "id":      "cozbni460l1y5l86n00qvvujn",
            "neutral":   "no",
            "longName":  "Estadio Marcelo Alberto Bielsa",
            "shortName": "Estadio Marcelo Alberto Bielsa"
        }
    },
    "matchData": {
        "status":    "scheduled",
        "lengthMin": 0,
        "lengthSec": 0,
        "period": [],
        "scores": {
            "ht": {
                "home": 0,
                "away": 0
            },
            "ft": {
                "home": 0,
                "away": 0
            },
            "total": {
                "home": 0,
                "away": 0
            }
        },
        "goals": [],
        "cards": [],
        "lineUp": [
            {
                "contestantId":  "3oj3koph7uf63y1f9zr8r7ylo",
                "formationUsed": "343",
                "players": [
                    {
                        "playerId": "bb4tpva9i4cdir6fiz6tbh8lx",
                        "firstName": "Alan Joaquín",
                        "lastName": "Aguerre",
                        "matchName": "A. Aguerre",
                        "shirtNumber": 1,
                        "position": "Goalkeeper",
                        "positionSide": "Centre",
                        "formationPlace": "1",
                        "stat": {}
                    },
                    {
                        "playerId": "3y90m5t5lg2o8kzcmvdu8slx",
                        "firstName": "Yonathan Emanuel",
                        "lastName": "Cabral",
                        "matchName": "Y. Cabral",
                        "shirtNumber": 16,
                        "position": "Defender",
                        "positionSide": "Left/Centre",
                        "formationPlace": "4",
                        "stat": {}
                    },
                    {
                        "playerId": "4ehikbxwqbhjb8a1afn2gbqvp",
                        "firstName": "Cristian Franco",
                        "lastName": "Lema",
                        "matchName": "C. Lema",
                        "shirtNumber": 2,
                        "position": "Defender",
                        "positionSide": "Centre",
                        "formationPlace": "5",
                        "stat": {}
                    },
                    {
                        "playerId": "f5dphmscqy4rpja7uke1v3vo4",
                        "firstName": "Milton Ramón",
                        "lastName": "Leyendeker",
                        "matchName": "M. Leyendeker",
                        "shirtNumber": 48,
                        "position": "Defender",
                        "positionSide": "Centre/Right",
                        "formationPlace": "6",
                        "stat": {}
                    },
                    {
                        "playerId": "1klp54n4s0e62fcqrnw1io4wl",
                        "firstName": "Matías Exequiel",
                        "lastName": "Orihuela Bonino",
                        "matchName": "M. Orihuela",
                        "shirtNumber": 33,
                        "position": "Midfielder",
                        "positionSide": "Left",
                        "formationPlace": "3",
                        "stat": {}
                    },
                    {
                        "playerId": "e6sqoj9d5bnxthkew2y247oph",
                        "firstName": "Julián Rodrigo",
                        "lastName": "Fernández",
                        "matchName": "J. Fernández",
                        "shirtNumber": 20,
                        "position": "Midfielder",
                        "positionSide": "Left/Centre",
                        "formationPlace": "8",
                        "stat": {}
                    },
                    {
                        "playerId": "7rq4qs8wab5jbofn3esgjju5m",
                        "firstName": "Juan Sebastián",
                        "lastName": "Sforza",
                        "matchName": "J. Sforza",
                        "shirtNumber": 13,
                        "position": "Midfielder",
                        "positionSide": "Centre/Right",
                        "formationPlace": "7",
                        "stat": {}
                    },
                    {
                        "playerId": "c9tb40pi96r8hy25vbo8b4lt6",
                        "firstName": "Manuel Tadeo",
                        "lastName": "Llano Massa",
                        "matchName": "M. Llano",
                        "shirtNumber": 41,
                        "position": "Midfielder",
                        "positionSide": "Right",
                        "formationPlace": "2",
                        "stat": {}
                    },
                    {
                        "playerId": "a6tltrhci8psih8emtburwx2i",
                        "firstName": "Justo",
                        "lastName": "Giani",
                        "matchName": "J. Giani",
                        "shirtNumber": 17,
                        "position": "Striker",
                        "positionSide": "Left/Centre",
                        "formationPlace": "11",
                        "stat": {}
                    },
                    {
                        "playerId": "c6dhth4ic6g4f1bm0onthtrdh",
                        "firstName": "Maximiliano Rubén",
                        "lastName": "Rodríguez",
                        "matchName": "M. Rodríguez",
                        "shirtNumber": 11,
                        "position": "Striker",
                        "positionSide": "Centre",
                        "formationPlace": "9",
                        "captain": "yes",
                        "stat": {}
                    },
                    {
                        "playerId": "1e1ydn9lturoduaiygks4v02c",
                        "firstName": "Luciano César",
                        "lastName": "Cingolani",
                        "matchName": "L. Cingolani",
                        "shirtNumber": 7,
                        "position": "Striker",
                        "positionSide": "Centre/Right",
                        "formationPlace": "10",
                        "stat": {}
                    },
                    {
                        "playerId": "d9rmi522gt6rl3zosxpqlp4yy",
                        "firstName": "Patricio Andrés",
                        "lastName": "Acevedo",
                        "matchName": "P. Acevedo",
                        "shirtNumber": 50,
                        "position": "Substitute",
                        "subPosition": "Defender",
                        "stat": {}
                    },
                    {
                        "playerId": "80irhkndhxke9rzq9o21qx89g",
                        "firstName": "Brian Nicolás",
                        "lastName": "Aguirre",
                        "matchName": "B. Aguirre",
                        "shirtNumber": 18,
                        "position": "Substitute",
                        "subPosition": "Attacker",
                        "stat": {}
                    },
                    {
                        "playerId": "1op5o2bmgxucl26sfxtg99jx0",
                        "firstName": "Williams",
                        "lastName": "Barlasina",
                        "matchName": "W. Barlasina",
                        "shirtNumber": 23,
                        "position": "Substitute",
                        "subPosition": "Goalkeeper",
                        "stat": {}
                    },
                    {
                        "playerId": "d9jwkejw11dyhslun5z54t4np",
                        "firstName": "Fernando Daniel",
                        "lastName": "Belluschi",
                        "matchName": "F. Belluschi",
                        "shirtNumber": 5,
                        "position": "Substitute",
                        "subPosition": "Midfielder",
                        "stat": {}
                    },
                    {
                        "playerId": "aa71oij1etjvgip30sckhr4ve",
                        "firstName": "Enzo Daniel",
                        "lastName": "Cabrera",
                        "matchName": "E. Cabrera",
                        "shirtNumber": 25,
                        "position": "Substitute",
                        "subPosition": "Attacker",
                        "stat": {}
                    },
                    {
                        "playerId": "59oc9127az1qzzcegyyka02dw",
                        "firstName": "Diego Ezequiel",
                        "lastName": "Calcaterra",
                        "matchName": "D. Calcaterra",
                        "shirtNumber": 15,
                        "position": "Substitute",
                        "subPosition": "Midfielder",
                        "stat": {}
                    },
                    {
                        "playerId": "11ixp4u1zzd34nqjg7dx6ldd5",
                        "firstName": "Manuel Vicente",
                        "lastName": "Capasso",
                        "matchName": "M. Capasso",
                        "shirtNumber": 22,
                        "position": "Substitute",
                        "subPosition": "Defender",
                        "stat": {}
                    },
                    {
                        "playerId": "9iru2vx2pwgkhpyqdzoeo69lg",
                        "firstName": "Martín Abel",
                        "lastName": "Luciano",
                        "matchName": "M. Luciano",
                        "shirtNumber": 49,
                        "position": "Substitute",
                        "subPosition": "Defender",
                        "stat": {}
                    },
                    {
                        "playerId": "6nb05gcrwxszd7hu7lohcubkk",
                        "firstName": "Zahir Facundo",
                        "lastName": "Mansilla",
                        "matchName": "Z. Mansilla",
                        "shirtNumber": 19,
                        "position": "Substitute",
                        "subPosition": "Defender",
                        "stat": {}
                    },
                    {
                        "playerId": "7tf01pzsvb8ia6lu7dbji8mlm",
                        "firstName": "Julián",
                        "lastName": "Marcioni",
                        "matchName": "J. Marcioni",
                        "shirtNumber": 39,
                        "position": "Substitute",
                        "subPosition": "Midfielder",
                        "stat": {}
                    },
                    {
                        "playerId": "105twqa3d2gwhb4y8xqu4xtrd",
                        "firstName": "Alexis Agustín",
                        "lastName": "Rodríguez",
                        "matchName": "A. Rodríguez",
                        "shirtNumber": 14,
                        "position": "Substitute",
                        "subPosition": "Attacker",
                        "stat": {}
                    },
                    {
                        "playerId": "1kysphf9bcl79c3i6qcmofx90",
                        "firstName": "Ramiro Gabriel",
                        "lastName": "Sordo",
                        "matchName": "R. Sordo",
                        "shirtNumber": 26,
                        "position": "Substitute",
                        "subPosition": "Attacker",
                        "stat": {}
                    }
                ],
                "teamOfficial": {
                    "id": "3897s5cs5iyk8g0g10fzywiqd",
                    "firstName": "Germán Adrián",
                    "lastName": "Burgos Maestromey",
                    "type": "manager"
                },
                "stat": {}
            },
            {
                "contestantId":  "1tsjuhn8qeikaj837w2ybx77n",
                "formationUsed": "4231",
                "players": [
                    {
                        "playerId": "c1frydda467yrnfhxf8e4a21h",
                        "firstName": "Manuel Matías",
                        "lastName": "Vicentini",
                        "matchName": "M. Vicentini",
                        "shirtNumber": 1,
                        "position": "Goalkeeper",
                        "positionSide": "Centre",
                        "formationPlace": "1",
                        "captain": "yes",
                        "stat": {}
                    },
                    {
                        "playerId": "9zzhpyu7m8jueozq7mlhra3t",
                        "firstName": "Lautaro",
                        "lastName": "Montoya",
                        "matchName": "L. Montoya",
                        "shirtNumber": 24,
                        "position": "Defender",
                        "positionSide": "Left",
                        "formationPlace": "3",
                        "stat": {}
                    },
                    {
                        "playerId": "di3cbejzhfxireipw056skyqx",
                        "firstName": "Braian Javier",
                        "lastName": "Salvareschi",
                        "matchName": "B. Salvareschi",
                        "shirtNumber": 18,
                        "position": "Defender",
                        "positionSide": "Left/Centre",
                        "formationPlace": "6",
                        "stat": {}
                    },
                    {
                        "playerId": "809o6c0dkj66zafvd9iimmei1",
                        "firstName": "Nicolás",
                        "lastName": "Bazzana",
                        "matchName": "N. Bazzana",
                        "shirtNumber": 23,
                        "position": "Defender",
                        "positionSide": "Centre/Right",
                        "formationPlace": "5",
                        "stat": {}
                    },
                    {
                        "playerId": "6pxu49x1nr5pexa76i873zecq",
                        "firstName": "Martín",
                        "lastName": "García",
                        "matchName": "Martín García",
                        "shirtNumber": 15,
                        "position": "Defender",
                        "positionSide": "Right",
                        "formationPlace": "2",
                        "stat": {}
                    },
                    {
                        "playerId": "6xju0r8dhqii5axuh7ej2cez9",
                        "firstName": "Federico",
                        "lastName": "Vismara",
                        "matchName": "F. Vismara",
                        "shirtNumber": 6,
                        "position": "Defensive Midfielder",
                        "positionSide": "Left/Centre",
                        "formationPlace": "4",
                        "stat": {}
                    },
                    {
                        "playerId": "bkw576csrec0yswaps72iduc5",
                        "firstName": "Federico",
                        "lastName": "Bravo",
                        "matchName": "F. Bravo",
                        "shirtNumber": 22,
                        "position": "Defensive Midfielder",
                        "positionSide": "Centre/Right",
                        "formationPlace": "8",
                        "stat": {}
                    },
                    {
                        "playerId": "9zemavr8h4ho4ivl7a270dai2",
                        "firstName": "Benjamín",
                        "lastName": "Borasi",
                        "matchName": "B. Borasi",
                        "shirtNumber": 31,
                        "position": "Attacking Midfielder",
                        "positionSide": "Left",
                        "formationPlace": "11",
                        "stat": {}
                    },
                    {
                        "playerId": "12cgmwvyv78fv1cnos5dvox5",
                        "firstName": "Sergio Alejandro",
                        "lastName": "Quiroga Gabutti",
                        "matchName": "S. Quiroga",
                        "shirtNumber": 10,
                        "position": "Attacking Midfielder",
                        "positionSide": "Centre",
                        "formationPlace": "10",
                        "stat": {}
                    },
                    {
                        "playerId": "2gdg292za7k73dk80fud4g1qt",
                        "firstName": "Gabriel Gustavo",
                        "lastName": "Alanís",
                        "matchName": "G. Alanís",
                        "shirtNumber": 17,
                        "position": "Attacking Midfielder",
                        "positionSide": "Right",
                        "formationPlace": "7",
                        "stat": {}
                    },
                    {
                        "playerId": "7jkf5dztu8l7n2mccezhd9qsp",
                        "firstName": "Jonathan",
                        "lastName": "Torres",
                        "matchName": "J. Torres",
                        "shirtNumber": 9,
                        "position": "Striker",
                        "positionSide": "Centre",
                        "formationPlace": "9",
                        "stat": {}
                    },
                    {
                        "playerId": "7swhfptvb003jhmsnbamj07sa",
                        "firstName": "Juan",
                        "lastName": "Antonini",
                        "matchName": "J. Antonini",
                        "shirtNumber": 20,
                        "position": "Substitute",
                        "subPosition": "Midfielder",
                        "stat": {}
                    },
                    {
                        "playerId": "52rg84ffamzw279qi7zy22ep5",
                        "firstName": "Yair Ezequiel",
                        "lastName": "Arismendi",
                        "matchName": "Y. Arismendi",
                        "shirtNumber": 26,
                        "position": "Substitute",
                        "subPosition": "Midfielder",
                        "stat": {}
                    },
                    {
                        "playerId": "5pxbdolaky90924vazle1pm1h",
                        "firstName": "Facundo",
                        "lastName": "Ferrero",
                        "matchName": "F. Ferrero",
                        "shirtNumber": 12,
                        "position": "Substitute",
                        "subPosition": "Goalkeeper",
                        "stat": {}
                    },
                    {
                        "playerId": "7tfhn8r50f5313ci7g1ntxihh",
                        "firstName": "Luis Yamil",
                        "lastName": "Garnier",
                        "matchName": "Y. Garnier",
                        "shirtNumber": 4,
                        "position": "Substitute",
                        "subPosition": "Midfielder",
                        "stat": {}
                    },
                    {
                        "playerId": "10o1hoqqgn4qhq37gr4wk56vo",
                        "firstName": "Joaquín",
                        "lastName": "Gho",
                        "matchName": "J. Gho",
                        "shirtNumber": 28,
                        "position": "Substitute",
                        "subPosition": "Midfielder",
                        "stat": {}
                    },
                    {
                        "playerId": "5csw8o2v8b6vohlnpdje5e2qy",
                        "firstName": "Luciano Emilio",
                        "lastName": "Gondou Zanelli",
                        "matchName": "L. Gondou",
                        "shirtNumber": 19,
                        "position": "Substitute",
                        "subPosition": "Attacker",
                        "stat": {}
                    },
                    {
                        "playerId": "8qo9ojvvwnkpkxeffozmafwlx",
                        "firstName": "Gabriel Maximiliano",
                        "lastName": "Graciani",
                        "matchName": "G. Graciani",
                        "shirtNumber": 7,
                        "position": "Substitute",
                        "subPosition": "Midfielder",
                        "stat": {}
                    },
                    {
                        "playerId": "8kwncbi9jjwuoeakt7rlv6bx1",
                        "firstName": "Pablo Matías Daniel",
                        "lastName": "Molina",
                        "matchName": "M. Molina",
                        "shirtNumber": 38,
                        "position": "Substitute",
                        "subPosition": "Defender",
                        "stat": {}
                    },
                    {
                        "playerId": "17ywocf7jo9yc8mxiup3waxn9",
                        "firstName": "Fausto Emanuel",
                        "lastName": "Montero",
                        "matchName": "F. Montero",
                        "shirtNumber": 30,
                        "position": "Substitute",
                        "subPosition": "Midfielder",
                        "stat": {}
                    },
                    {
                        "playerId": "3vldzwyy5quu7t4usmknhki6s",
                        "firstName": "Federico",
                        "lastName": "Paradela",
                        "matchName": "F. Paradela",
                        "shirtNumber": 39,
                        "position": "Substitute",
                        "subPosition": "Midfielder",
                        "stat": {}
                    },
                    {
                        "playerId": "53rkwe5vwde1j4i3p8j98rys5",
                        "firstName": "Claudio Martín",
                        "lastName": "Pombo",
                        "matchName": "C. Pombo",
                        "shirtNumber": 8,
                        "position": "Substitute",
                        "subPosition": "Midfielder",
                        "stat": {}
                    },
                    {
                        "playerId": "d7ryts5ubne8dr7j7cs5nlql1",
                        "firstName": "Guido Nahuel",
                        "lastName": "Vadalá",
                        "matchName": "G. Vadalá",
                        "shirtNumber": 11,
                        "position": "Substitute",
                        "subPosition": "Attacker",
                        "stat": {}
                    },
                    {
                        "playerId": "1uka1klxqlkztoxt5m5lo25lh",
                        "firstName": "Fabio Francisco",
                        "lastName": "Vázquez",
                        "matchName": "F. Vázquez",
                        "shirtNumber": 5,
                        "position": "Substitute",
                        "subPosition": "Midfielder",
                        "stat": {}
                    }
                ],
                "teamOfficial": {
                    "id": "5nw384sjy9vvr0uifh3z9smad",
                    "firstName": "Mario",
                    "lastName": "Sciacqua",
                    "type": "manager"
                },
                "stat": {}
            }
        ]
    }
}