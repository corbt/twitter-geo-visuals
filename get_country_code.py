import pycountry

name_map = {
    "Venezuela": "Venezuela, Bolivarian Republic of",
    "South Korea": "Korea, Republic of",
    "North Korea": "Korea, Democratic People's Republic of",
    "Russia": "Russian Federation",
    "The Bahamas": "Bahamas",
    "Ivory Coast": u"C\xf4te d'Ivoire",
    "Bolivia": "Bolivia, Plurinational State of",
    "US Virgin Islands": "United States Minor Outlying Islands",
    "Syria": "Syrian Arab Republic",
    "Iran": "Iran, Islamic Republic of",
    "Taiwan": "Taiwan, Province of China",
    "Tanzania": "Tanzania, United Republic of",
    "Hong Kong SAR": "Hong Kong",
    "Moldova": "",
    "FYRO Macedonia": "Macedonia, Republic of",
    "Vatican City": "Holy See (Vatican City State)",
    "Congo (DRC)": "Congo, The Democratic Republic of the",
    "French-Guadeloupe": "Guadeloupe",
    "Congo, Republic of the": "Congo",
    "Kosovo": "Serbia"
}

def get_cc(name):
    if name in name_map:
        name = name_map[name]
    try:
        return pycountry.countries.get(name=name).alpha3
    except:
        return None