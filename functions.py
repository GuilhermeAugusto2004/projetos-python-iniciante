from datetime import datetime


def today():
    today = datetime.now()
    return today


def verify_date(date):
    try:
        date_format = datetime.strptime(date, "%d-%m-%Y")
        return date_format
    except:
        raise Exception("ENTRADA INVALIDA")


def verify_due(date_ref):
    duo_date = verify_date(date=date_ref)
    if today() > duo_date:
        return True
    else:
        return False
