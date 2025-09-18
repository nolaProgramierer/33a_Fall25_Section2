from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.http import JsonResponse
from . import utils
from .forms import AddPianoForm


def index(request):
    # Retrieve all pianos from the session and render the index page
    pianos = utils.get_all_pianos(request)
    return render(request, "pianos/index.html", {"pianos": pianos})


def add_piano_html(request):
    # Handle adding a piano using a plain HTML form
    if request.method == "POST":
        # Extract form data from POST request
        brand = request.POST["brand"]
        finish = request.POST["finish"]
        price = int(request.POST["price"])

        # Create a new piano dictionary
        new_piano = {"brand": brand, "finish": finish, "price": price}

        # Retrieve current pianos, append the new one, and save back to session
        pianos = utils.get_all_pianos(request)
        pianos.append(new_piano)
        utils.save_to_session(request, pianos)

        # Redirect to index after successful addition
        return HttpResponseRedirect(reverse("index"))

    # Render the add piano form page
    return render(request, "pianos/add_piano_html.html")


def add_piano(request):
    # Handle adding a piano using a Django form
    form = AddPianoForm(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
        # Convert form data into piano dictionary
        new_piano = utils.piano_from_form(form)

        # Prevent duplicate pianos
        if utils.piano_exists(request, new_piano):
            form.add_error(None, "A piano with these attributes already exists.")
            return render(request, "pianos/add_piano.html", {"form": form})
        
        # Append new piano to session and redirect to index
        pianos = utils.get_all_pianos(request)
        pianos.append(new_piano)
        utils.save_to_session(request, pianos)

        return HttpResponseRedirect(reverse("index"))
    
    # Render form page for GET request or invalid POST
    return render(request, "pianos/add_piano.html", {"form": form})


def piano_detail(request, brand, finish, price):
    # Retrieve a single piano by its attributes
    piano = utils.get_piano(request, brand=brand, finish=finish, price=price)
    if not piano:
        # Render "not found" page if piano doesn't exist
        return render(request, "pianos/piano_not_found.html")
    
    # Render detail page with piano data
    return render(request, "pianos/piano_detail.html", {"piano": piano})


def edit_piano(request, brand, finish, price):
    # Retrieve the piano to be edited
    piano_to_edit = utils.get_piano(request, brand=brand, finish=finish, price=price)
    
    if not piano_to_edit:
        # Piano not found, render "not found" page
        return render(request, "pianos/piano_not_found.html")
    
    # Initialize form with existing piano data
    form = AddPianoForm(request.POST or None, initial=piano_to_edit)
    
    if request.method == "POST" and form.is_valid():
        # Update the piano based on form data
        updated_piano = utils.piano_from_form(form)

        # Replace old piano with updated one in session
        pianos = utils.get_all_pianos(request)
        pianos = [updated_piano if piano == piano_to_edit else piano for piano in pianos]
        utils.save_to_session(request, pianos)

        # Redirect to index after successful edit
        return HttpResponseRedirect(reverse("index"))
    
    # Render edit page with form and current piano info
    return render(request, "pianos/edit_piano.html", {"form": form, "piano": piano_to_edit})


def confirm_remove_piano(request, brand, finish, price):
    # Prompt user to confirm removal of a piano
    pianos = utils.get_all_pianos(request)

    # Find piano that matches the given attributes
    piano_to_remove = next((
        piano for piano in pianos
        if piano['brand'] == brand and 
            piano['finish'] == finish and 
            piano['price'] == price 
        ), 
        None
        )
    
    if piano_to_remove:
        # Render confirmation page with piano info
        return render(request, 'pianos/confirm_remove_piano.html', {'piano': piano_to_remove})

    # Redirect to index if piano not found
    return HttpResponseRedirect(reverse('index'))

   
def remove_piano(request, brand, finish, price):
    # Remove a piano from the session based on its attributes
    pianos = utils.get_all_pianos(request)
    # Reformulate piano list without the piano passed to view
    new_pianos = [piano for piano in pianos 
                if not (piano['brand'] == brand 
                and piano['finish'] == finish 
                and piano['price'] == price)]
    utils.save_to_session(request, new_pianos)

    # Redirect to index after removal
    return HttpResponseRedirect(reverse('index'))


# -----------------------------------------------
# Debug views
def debug_session(request):
    # Return current session data as JSON (for debugging purposes)
    return JsonResponse(dict(request.session))


def reset_session(request):
    # Clear the session completely
    request.session.flush()
    return HttpResponse("Session cleared")

