# tests/test_placeholder.py

def test_always_passes():
    """
    Un test semplicissimo per confermare che pytest è installato,
    rileva i file di test e può eseguire un'asserzione.
    """
    print("Pytest sta eseguendo questo test!")
    assert 1 + 1 == 2

def test_application_is_importable():
    """
    Un test leggermente più avanzato che controlla se il pacchetto 'application'
    (con il suo __init__.py) è correttamente trovato da pytest.
    """
    try:
        import application
    except ImportError:
        # Se fallisce l'import, forza il fallimento del test con un messaggio chiaro
        assert False, "Impossibile importare il pacchetto 'application'. Manca __init__.py?"
    
    # Se l'import ha successo, il test passa
    assert True
