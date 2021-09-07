# Json-Localizer-Generator-for-Microsoft-IStringLocalizer
json Localization file  Generator Script
### Summary

This script generates a json file respecting to Microsoft IStringLocalizer 

###Sample input file
`
There is no assets to be added.
There is no assets to be added.
Invalid asset can't be added.
User Id can't be null.
User Id can't be empty.
User Id not found.
User must be older than 18 years of age.
Email is not valid.
FirstName is not valid.
LastName is not valid.
Street must be valid.
Postal Code must be valid.
Line1 of the address must be valid.
House number must be valid.
something went wrong
`

###Sample output

`
[

  {
    "Key": "There is no assets to be added.",
    "LocalizedValue": {
      "en-US": "There is no assets to be added.",
      "de-DE": "Es gibt keine Assets, die hinzugefügt werden sollen."
    }
  },
  {
    "Key": "There is no assets to be added.",
    "LocalizedValue": {
      "en-US": "There is no assets to be added.",
      "de-DE": "Es gibt keine Assets, die hinzugefügt werden sollen."
    }
  },
  {
    "Key": "Invalid asset can't be added.",
    "LocalizedValue": {
      "en-US": "Invalid asset can't be added.",
      "de-DE": "Ungültiger Asset kann nicht hinzugefügt werden."
    }
  },
  {
    "Key": "User Id can't be null.",
    "LocalizedValue": {
      "en-US": "User Id can't be null.",
      "de-DE": "Benutzer-ID kann nicht null sein."
    }
  },
  {
    "Key": "User Id can't be empty.",
    "LocalizedValue": {
      "en-US": "User Id can't be empty.",
      "de-DE": "Benutzer-ID kann nicht leer sein."
    }
  },
  {
    "Key": "User Id not found.",
    "LocalizedValue": {
      "en-US": "User Id not found.",
      "de-DE": "Benutzer ID nicht gefunden."
    }
  },
  {
    "Key": "User must be older than 18 years of age.",
    "LocalizedValue": {
      "en-US": "User must be older than 18 years of age.",
      "de-DE": "Der Benutzer muss älter als 18 Jahre sein."
    }
  },
  {
    "Key": "Email is not valid.",
    "LocalizedValue": {
      "en-US": "Email is not valid.",
      "de-DE": "Email ist ungültig."
    }
  },
  {
    "Key": "FirstName is not valid.",
    "LocalizedValue": {
      "en-US": "FirstName is not valid.",
      "de-DE": "Vorname ist nicht gültig."
    }
  },
  {
    "Key": "LastName is not valid.",
    "LocalizedValue": {
      "en-US": "LastName is not valid.",
      "de-DE": "LastName ist nicht gültig."
    }
  },
  {
    "Key": "Street must be valid.",
    "LocalizedValue": {
      "en-US": "Street must be valid.",
      "de-DE": "Straße muss gültig sein."
    }
  },
  {
    "Key": "Postal Code must be valid.",
    "LocalizedValue": {
      "en-US": "Postal Code must be valid.",
      "de-DE": "Postleitzahl muss gültig sein."
    }
  },
  {
    "Key": "Line1 of the address must be valid.",
    "LocalizedValue": {
      "en-US": "Line1 of the address must be valid.",
      "de-DE": "Line1 der Adresse muss gültig sein."
    }
  },
  {
    "Key": "House number must be valid.",
    "LocalizedValue": {
      "en-US": "House number must be valid.",
      "de-DE": "Hausnummer muss gültig sein."
    }
  },
  {
    "Key": "something went wrong",
    "LocalizedValue": {
      "en-US": "something went wrong",
      "de-DE": "etwas ist schief gelaufen"
    }
  }

]
`
