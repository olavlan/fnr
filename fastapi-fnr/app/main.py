from fastapi import FastAPI
from app.person import Person
from app.people_collection import PeopleCollection, DEFAULT_AGE_STEPS

app = FastAPI()

INVALID_NUMBER_ERROR = {"error": "Fødselsnummeret er ikke gyldig"} 
DEFAULT_DATASET_FILEPATH = "data/fnr.txt"

@app.get("/validate/{fnr}", summary="Validér fødselsnummer")
def validate(fnr):
    """
    Sjekk om den gitte parameteren er et gyldig fødselsnummer.
    """
    try:
        Person(fnr)
        valid = True
    except:
        valid = False
    return {"valid": valid}

@app.get("/gender/{fnr}", summary="Hent kjønn for fødselsnummer")
def gender(fnr):
    """
    Sjekk om det gitte fødselsnummeret betegner mann eller kvinne. 
    """
    try: 
        p = Person(fnr)
        return {"gender": p.get_gender()}
    except:
        return INVALID_NUMBER_ERROR

@app.get("/age/{fnr}", summary="Hent alder for fødselsnummer")
def age(fnr):
    """
    For gitt fødselsnummer, hent alder ved slutten av inneværende år. 
    """
    try: 
        p = Person(fnr)
        return {"age": p.get_age()}
    except:
        return INVALID_NUMBER_ERROR

@app.get("/dataset/exists/{fnr}", summary="Sjekk om fødselsnummer eksisterer")
def exists(fnr, dataset_filepath = DEFAULT_DATASET_FILEPATH):
    """
    Sjekk om det gitte fødselsnummeret finnes i datasettet.

    Valgfrie parametre: 
    * **dataset_filepath**: Stien til en datafil som inneholder fødselsnumre (ett per linje).
    """
    try: 
        p = Person(fnr)
        return {"exists": p.exists_in_dataset(dataset_filepath)}
    except:
        return INVALID_NUMBER_ERROR

@app.get("/dataset/counts/", summary="Tell gyldige fødselsnumre")
def counts(dataset_filepath = DEFAULT_DATASET_FILEPATH):
    """
    Tell antall gyldige fødselsnumre i datasettet, totalt og for menn og kvinner.
    
    Valgfrie parametre: 
    * **dataset_filepath**: Stien til en datafil som inneholder fødselsnumre (ett per linje).
    """
    pc = PeopleCollection(dataset_filepath)
    return pc.get_counts()

@app.get("/dataset/detailed_counts/", summary="Tell gyldige fødselsnumre etter kjønn og alder")
def detailed_counts(dataset_filepath = DEFAULT_DATASET_FILEPATH, age_steps = DEFAULT_AGE_STEPS):
    """
    Tell antall gyldige fødselsnumre i datasettet, etter kjønn og aldersgruppe. 
    
    Standard aldersinndeling er 0-17, 18-24, 25-34, 35-44, 45-54, 55-64, 65-

    Valgfrie parametre: 
    * **dataset_filepath**: Stien til en datafil som inneholder fødselsnumre (ett per linje).
    * **age_steps** (int): Angi egendefinert aldersinndeling som kommaseparert liste av heltallsverdier. \
        Eksempel: 20,40,60 gir aldersinndelingen 0-20, 21-40, 41-60, 61-.
    """
    pc = PeopleCollection(dataset_filepath)
    return pc.get_detailed_counts(age_steps)