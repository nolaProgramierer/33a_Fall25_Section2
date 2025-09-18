SESSION_KEY = "pianos"  # Key used to store piano data in the session


def get_piano(request, **kwargs):
    """
    Retrieve a single piano from the session that matches all given attributes.
    """
    pianos = request.session.get(SESSION_KEY, [])
    
    if not kwargs:
        # No criteria provided; cannot match anything
        return None
    
    # Iterate through pianos and return the first one that matches all key-value pairs
    return next((
        piano for piano in pianos
        # all() ensures every attribute in kwargs matches the piano
        if all(piano.get(key) == value for key, value in kwargs.items())
    ), None) # None returned if no match found


def get_all_pianos(request):
    """
    Return all pianos stored in the session.
    """
    # Default to empty list if session key does not exist
    return request.session.get(SESSION_KEY, [])


def save_to_session(request, piano_list):
    """
    Save a list of pianos to the session and mark session as modified.
    """
    request.session[SESSION_KEY] = piano_list
    # Ensures Django persists the change
    request.session.modified = True


def piano_exists(request, new_piano):
    """
    Check if a piano with the same attributes already exists in the session.
    """
    pianos = get_all_pianos(request)
    # any() returns True if at least one piano matches all attributes
    return any(
        piano["brand"] == new_piano["brand"] and
        piano["finish"] == new_piano["finish"] and
        piano["price"] == new_piano["price"] 
        for piano in pianos
    )


def piano_from_form(form):
    """
    Convert a valid Django form into a piano dictionary.
    """
    # Extract cleaned data from form and return as a dictionary
    return {
        "brand": form.cleaned_data["brand"],
        "finish": form.cleaned_data["finish"],
        "price": form.cleaned_data["price"]
    }


