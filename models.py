# The project's structure is justified by the fact that in the future,
# the application can scale and receive data not only from this API.
# The models will simplify the validation of data that our application receives
# from the API. Such validation is necessary for the ORM of this application
BORED_ACTIVITY_MODEL = {
        "activity": str,
        "type": str,
        "participants": int,
        "price": (float, int),
        "link": str,
        "key": str,
        "accessibility": (float, int)
    }

