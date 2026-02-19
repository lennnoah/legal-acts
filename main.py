from nicegui import ui

data = [
    {"id": {"de": "Rechtsakt", "en": "Legal act"}, "description" : {"de": "Rechtshandlung, die auf die Erzeugung einer Rechtsfolge abzielt", "en": "Legal act aimed at creating a legal consequence"} , 
     "children" : [{"id": {"de":"Verleihung", "en": "Grant"},"description": {"de": "Rechtsakt, vornehmlich im diplomatischen Sinne, in dem Recht oder Besitz an einen neuen Empfänger verliehen wird", "en": "Legal act, primarily in a diplomatic context, in which rights or possession are granted to a new recipient"}, 
                    "children": [{"id":{"de": "Besitzrechtliche Verfügungen", "en": "Property Transactions"}, "description": {"de": "Rechtsakt, welcher den besitzrechtlichen Status eines Objekts verändert", "en": "Legal act that changes the possessory status of an object"},
                                  "children": [{"id": {"de": "Dotation", "en": "Endowment"}, "description": {"de": "Ausstattung mit Einkünften und Gütern", "en": "Allocation of income and assets"}},
                                               {"id": {"de": "Zollbefreiung", "en": "Customs exemption"}, "description": {"de": "Personen einer Region sind von jeglichen Zöllen in einer bestimmten Region befreit", "en": "People from a region are exempt from all customs duties in a specific region."}},
                                               {"id": {"de": "Temporäre Verleihung (bspw. Verpfändung)", "en": "Temporary grants (e.g., pledging)"}, "description": {"de": "Rechtsakt der zeitlich begrenzten Übertragung eines Lehens gegen Zahlung einer Pfandsumme", "en": "Legal act of the temporary transfer of a fief in exchange for the payment of a pledge sum."}},
                                               {"id": {"de": "Erbrechtliche Verleihungen", "en": "Hereditary grants"}, "description": {"de": "Rechtsakt der Übertragung von erblichen Besitz", "en": "Legal act of transferring hereditary property"}},
                                               {"id": {"de": "Lehensverleihungen", "en": "enfeoffment"}, "description": {"de": "Rechtsakt der Übertragung eines „Lehens“(oft Land oder ein Amt), eine sogenannte Leihe, durch einen Lehnsherrn an einen Lehnsmann (Vasallen) im Austausch für dessen Treue und Dienst, wie Kriegsdienste oder politische Unterstützung", "en": "Legal act of transferring a “fief” (often land or an office), a so-called loan, from a feudal lord to a vassal in exchange for the latter's loyalty and service, such as military service or political support."}},
                                               {"id": {"de": "Schenkung", "en": "gift"}, "description": {"de": "Rechtsakt der freiwilligen Aufgabe von Gütern, Rechten oder Ansprüchen ohne verpflichtende Gegengabe", "en": "A legal act of voluntarily transferring assets, rights, or claims without a binding consideration in return"}},
                                               {"id": {"de": "Testamentarische Verfügung", "en": "Testamentary Disposition"}, "description": {"de": "Rechtsakt, welcher den künftigen Verbleib von Gütern, Rechten und Ansprüchen nach dem Tod des Testanten verfügt", "en": "Legal act specifying the future allocation of goods, rights, and claims after the death of the testator"}},
                                               {"id": {"de": "Kreditgewährung", "en": "Granting of a Credit"}, "description": {"de": "Rechtsakt, welcher einen gewissen monetären oder materiellen Wert, bei der Erwartung der Rückzahlung mit etwaigen zusätzlichen Gebühren, auf Zeit vergibt", "en": "Legal act by which a certain monetary or material value is provided for a period of time, with the expectation of repayment and possible additional fees"}},
                                               {"id": {"de": "Verkauf", "en": "Sale"}, "description": {"de": "Rechtsakt der Übertragung gewisser Güter, Rechte oder Ansprüche gegen eine bestimmte Zahlung", "en": "Legal act of transferring certain goods, rights, or claims in exchange for a specific payment"}},
                                               {"id": {"de": "Tausch", "en": "Exchange"}, "description": {"de": "Rechtsakt des Austauschs gewisser Güter, Rechte oder Ansprüche gegen andere Güter, Rechte oder Ansprüche", "en": "Legal act of exchanging certain goods, rights, or claims for other goods, rights, or claims"}},
                                               ]}, 
                                 {"id": {"de": "Privilegienerweiterung", "en": "Extension of privileges"}, "description": {"de": "Rechtsakt, der innegehabte Rechte um zusätzliche Rechte erweitert", "en": "Legal act that extends existing rights by granting additional rights"}},
                                 {"id": {"de": "Zinsfestlegung", "en": "Fixing of Interest Rates"}, "description": {"de": "Rechtsakt, welcher die jährliche Zahlungsbelastung eines Gutes, einer Person oder eines Rechts bestimmt", "en": "A legal act that determines the annual payment burden of an asset, a person, or a right"}},
                                 {"id": {"de": "Verleihung des Weiderechts", "en": "Granting of grazing rights"}, "description": {"de": "Verleihung des Rechts, Vieh auf einem bestimmten Bereich weiden zu lassen", "en": "Granting of the right to graze livestock in a certain area"}},
                                 {"id": {"de": "Rechtevergabe", "en": "Granting of rights"}, "description": {"de": "Rechtsakt der spezielle Rechte (etwa städtische, institutionelle oder wirtschaftliche Privilegien) vergibt", "en": "Legal act that grants specific rights (such as municipal, institutional, or economic privileges)"},
                                  "children": [{"id": {"de": "Institutionelle Privilegien", "en": "Institutional privileges"}, "description": {"de": "Akt der Vergabe von Rechten an nicht-städtische Institution", "en": "Act of granting rights to a non-municipal institution"},
                                                "children": [{"id": {"de": "Gründung", "en": "Founding"}, "description": {"de": "Ereignis der Schaffung einer Organisation oder einer anderen Einheit, die von Dauer sein soll", "en": "action of creating an organization or other entity intended to endure"}},
                                                             {"id": {"de": "Verlegung", "en": "Relocation"}, "description": {"de": "Rechtsakt, welcher festlegt, dass eine bestimmte Institution ihren bisherigen Sitz aufgeben und einen bestimmten anderen beziehen muss", "en": "Legal act which determines that a particular institution must vacate its previous location and move to a specified new one"}}
                                                             ]},
                                               {"id": {"de": "Wirtschaftliche Privilegien", "en": "Economic privileges"}, "description": {"de": "Akt der Vergabe von Rechten mit wirtschaftlich-ökonomischem Hintergrund", "en": "Act of granting rights with an economic background"},
                                                "children": [{"id": {"de": "Abgabenbefreiung", "en": "Tax Exemption"}, "description": {"de": "Rechtsakt, welcher den Inhaber von festgelegten normalerweise verpflichtenden Abgaben entbindet", "en": "Legal act that exempts the holder from specified, usually obligatory, charges"}},
                                                             {"id": {"de": "Vergabe von Handelsrechten", "en": "Granting Trading Rights"}, "description": {"de": "Rechtsakt, welcher den Inhaber die rechtliche Möglichkeit gibt, an einem bestimmten sonst zugangsbeschränkten Ort Handel zu treiben", "en": "Legal act granting the holder the legal possibility to trade at a specific, otherwise restricted, location"}},
                                                             {"id": {"de": "Vergabe von Nutzungsrechten", "en": "Granting of Usage Rights"}, "description": {"de": "Rechtsakte, welcher den Inhaber zur Ausübung einer bestimmten Nutzung in einem festgelegten Kontext erlaubt", "en": "Legal act permitting the holder to exercise a certain usage in a defined context"}},
                                                             {"id": {"de": "Vergabe von Zollrechten", "en": "Granting of Toll Rights"}, "description": {"de": "Rechtsakt, welcher den Inhaber zur Einnahme von Gebühren auf durchgehende Waren oder Zugtiere an bestimmten Orten berechtigt", "en": "Legal act entitling the holder to collect fees on passing goods or draft animals at specified locations"}},
                                                             {"id": {"de": "Gewährung einer Zollbefreiung", "en": "Granting Toll Exemption"}, "description": {"de": "Rechtsakt, welcher den Inhaber von der Zahlung von Gebühen auf durchgehende Waren und Zugtiere an bestimmten Orten befreit", "en": "Legal act exempting the holder from paying fees on passing goods and draft animals at certain locations"}},
                                                             {"id": {"de": "Vergabe von Münzrechten", "en": "Granting of Coinage Rights"}, "description": {"de": "Rechtsakt, welcher den Inhaber zum Prägen von Münzen berechtigt", "en": "Legal act entitling the holder to mint coins"}},
                                                             {"id": {"de": "Vergabe von Umtauschrecht", "en": "Granting the Right of Currency Regulation"}, "description": {"de": "Rechtsakt, welcher die Zusammensetzung oder Umrechnungsmodalitäten von barem Geld reguliert", "en": "Legal act regulating the composition or conversion modalities of cash money"}},
                                                             {"id": {"de": "Vergabe von Wasserrechten", "en": "Granting of Water Rights"}, "description": {"de": "Rechtsakt, welcher den Inhaber zur festgelegten Nutzung eines speziellen Abschnitts eines fließenden oder stehenden Gewässers berechtigt", "en": "Legal act entitling the holder to a defined usage of a specific section of a flowing or standing body of water"}},
                                                             {"id": {"de": "Vergabe von Schürfrechten", "en": "Granting of Mining Rights"}, "description": {"de": "Rechtsakt, welcher den Inhaber zum ober- oder untertägigen Abbau von Rohstoffen berechtigt, oft in Kombination mit weiteen rechtlichen Regelungen", "en": "Legal act entitling the holder to surface or underground extraction of raw materials, often in combination with other legal regulations"}},
                                                             ]},
                                               {"id": {"de": "Städtische Privilegien", "en": "Municipal privileges"}, "description": {"de": "Akt der Vergabe von Rechten an eine städtische Körperschaft", "en": "Act of granting rights to a municipal corporation"},
                                                "children": [{"id": {"de":"Vergabe eines Jahrmarkts", "en": "Granting of Annual Fair"}, "description": {"de": "Rechtsakt, der einer Stadt die Abhaltung eins annual stattfindenden Marktes mit gewöhnlich mehr als lokaler Bedeutung gestattet", "en": "Legal act that allows a city to hold a fair that takes place annually and is usually of more than local significance"}},
                                                             {"id": {"de":"Vergabe von Stapelrecht", "en": "Granting of Staple Right"}, "description": {"de": "Rechtsakt, der einer Stadt ermöglicht, alle Durchreisenden zu zwingen, ein gewisses Gut für eine bestimmte Zeit auf dem lokalen Markt zum Kauf anzubieten", "en": "Legal act that enables a city to require all passers-by to offer a certain good for sale on the local market for a specific period"}},
                                                             {"id": {"de":"Stadtrechtsprivileg", "en": "Town Law Privilege"}, "description": {"de": "Rechtsakt, mit dem ein bestimmtes Stadtrecht an eine städtische Gemeinschaft verliehen wird", "en": "Legal act by which a specific town right is granted to a municipal community"}},
                                                             {"id": {"de":"Vergabe von Marktrecht", "en": "Granting of Market Rights"}, "description": {"de": "Rechtsakt, der einer Stadt die regelmäßige Abhaltung eines gewöhnlichen Marktes gestattet", "en": "Legal act that allows a city to hold a regular ordinary market"}},
                                                             ]}
                                               ]}
                                 ]}, 
                   {"id": {"de": "Rechtsaktbestätigung", "en": "Confirmation of legal act"}, "description": {"de": "Textsorte die innegehabte Rechte bestätigt", "en": "Text type confirms the rights held"},
                    "children": [{"id": {"de": "Bestätigung alter Rechte (ohne konkrete Vorlage)", "en": "Confirmation of older rights (without specific reference)"}, "description": {"de":"Rechtsakt, in dem ein Anspruch auf alte Rechte oder Besitzungen bestätigt wird, ohne dass eine explizite, frühere Urkunde der Textgestalt nach aufgeführt wird", "en": "Legal act in which a claim to ancient rights or possessions is confirmed, without explicitly referencing a previous document in its textual form"}},
                                 {"id": {"de": "Zinsfestlegung", "en": "Fixing of Interest Rates"}, "description": {"de":"Rechtsakt, welcher die jährliche Zahlungsbelastung eines Gutes, einer Person oder eines Rechts bestimmt", "en": "A legal act that determines the annual payment burden of an asset, a person, or a right"}},
                                 {"id": {"de": "Bestätigung des Schürfrechts", "en": "Confirmation of the mining right"}, "description": {"de": "Bestätigung des Rechts, in einem bestimmten Bereich Bergbau betreiben zu dürfen", "en": "Confirmation of the right to mine in a specific area"}},
                                 {"id": {"de": "Rechtsaktbestätigung ohne Übernahme des Rechtsinhalts", "en": "Confirmation of legal act without assuming the legal content"}, "description": {"de": "Rechtsakt, durch den die Echtheit einer älteren Urkunde bestätigt wird, ohne Erneuerung des Rechtsinhalts durch den Aussteller.", "en": "Legal act by which the authenticity of an older document is confirmed, without renewal of its legal content by the issuer."}},
                                 {"id": {"de": "Rechtsaktbestätigung mit Übernahme des Rechtsinhalts", "en": "Confirmation of legal act with assumption of legal content"}, "description": {"de": "Rechtsakt, durch den Rechtsinhalt einer älteren Urkunde teilweise oder vollständig bestätigt und erneuert wird.", "en": "Legal act by which the legal content of an older document is partially or fully confirmed and renewed."}}
                                 ]},
                   {"id": {"de": "Rechteentzug", "en": "Deprivation of rights"}, "description": {"de": "Rechtsakt, in dem einer Person oder Institution der Anspruch auf ein Recht oder Besitzungen entzogen wird", "en": "Legal act by which a person or institution is deprived of a right or property"},
                    "children": [{"id": {"de": "Konfiskation", "en": "Confiscation"}, "description": {"de": "Rechtsakt, welcher Besitztümer, Rechte oder Ansprüche in einem sanktionierenden Akt entzieht", "en": "Legal act by which property, rights, or claims are withdrawn in a sanctioning action"}}
                                 ]},
                   {"id": {"de": "Verwaltungsakt", "en": "Administrative act"}, "description": {"de": "Sammelbegriff für Rechtsakte, die im weitesten Sinne ordnenden Charakter haben", "en": "Collective term for legal acts that, in the broadest sense, have an ordering character"},
                    "children": [{"id": {"de": "Erlaubnis", "en": "Permission"}, "description": {"de": "Rechtsakt, welcher gewisse Handlungen oder Vollzüge erlaubt", "en": "A legal act that allows certain actions or executions"}},
                                 {"id": {"de": "Verbot", "en": "prohibition"}, "description": {"de": "Rechtsakt, welcher gewisse Handlungen oder Vollzüge, meist bei Strafe, untersagt", "en": "A legal act that prohibits certain actions or executions, usually under penalty"}},
                                 {"id": {"de": "Amtsverleihung", "en": "Appointment"}, "description": {"de": "Rechtsakt, welcher dem Begünstigten ein bestimmtes Amt zuspricht und diesen einsetzt", "en": "A legal act that confers a specific office on the beneficiary and appoints them to it"}},
                                 {"id": {"de": "Grenzregelung", "en": "Border Regulations"}, "description": {"de": "Rechtsakt, welcher die terrestrischen Grenzen gewisser Güter, Rechte oder Ansprüche und die damit zusammenhängenden Klärungsbedarfe festlegt", "en": "A legal act which determines the terrestrial boundaries of certain properties, rights or claims and addresses the associated need for clarification"}},
                                 {"id": {"de": "Anweisung", "en": "Instruction"}, "description": {"de": "Rechtsakt, welcher zur Ausführung eines bestimmten Vollzug oder bestimmten Handlung auffordert", "en": "A legal act that requests the execution of a specific enforcement or a specific action"}},
                                 {"id": {"de": "Schlichtung", "en": "arbitration"}, "description": {"de": "Rechtsakt, welcher auf den gütlichen Ausgleich zwischen mehreren Konfliktparteien abzielt", "en": "A legal act aimed at achieving an amicable settlement between several conflicting parties"}},
                                 {"id": {"de": "Befreiungsbrief", "en": "Letter of Release"}, "description": {"de": "Rechtsakt, welcher von gewissen Konsequenzen losspricht (entweder von Schulden oder Verpflichtungen oder im Sinne der Verleihung von bestimmten Freiheiten)", "en": "Legal act that discharges from certain consequences (either debts or obligations or in the sense of granting certain freedoms)"}}
                                 ]},
                   {"id": {"de": "Entsagung (generell)", "en": "Renunciation (general)"}, "description": {"de": "Sammelbezeichnung für Rechtsakte, in denen die Aufgabe von Rechtsansprüchen dokumentiert wird", "en":"Generic term for legal acts in which the relinquishment of legal claims is documented (see subclasses)"},
                    "children": [{"id": {"de": "Quittung", "en": "Quitclaim"}, "description": {"de": "Rechtsakt, in welchem auf gewisse Ansprüche, Güter oder Rechte auf Grund einer erfolgten vollständigen Gegenleistung verzichtet wird", "en": "Legal act in which certain claims, goods, or rights are relinquished due to full consideration received"}},
                                 {"id": {"de": "Zahlung", "en": "Payment"}, "description": {"de": "Rechtsakt, welcher gewisse Ansprüche auf Güter, Rechte oder Ansprüche durch eine teilweise Gegenleistung ablöst", "en": "Legal act whereby certain claims for goods, rights, or demands are discharged through partial consideration"}},
                                 {"id": {"de": "Verzicht", "en": "Renunciation of Claim"}, "description": {"de": "Rechtsakt, in welchem auf gewisse Ansprüche, Güter oder Recht verzichtet wird", "en": "Legal act in which certain claims, goods, or rights are relinquished"}}
                                 ]},
                   {"id": {"de": "Strafe", "en": "Punishment"}, "description": {"de": "Rechtsakt, in dem eine Strafe gegen eine Person oder Institution ausgesprochen wird", "en": "A legal act in which a penalty or punishment is imposed on a person or institution"},
                    "children": [{"id": {"de": "Verbannung", "en": "Banishment"}, "description": {"de": "Verweisung einer Person aus ihrer gewohnten Umgebung oder angestammten Heimat. Anders als das Exil ist die Verbannung niemals freiwillig, sondern Folge eines andauernden autoritativen Zwangs, der den Betroffenen die Rückkehr verwehrt", "en": "expelling a person from a city, country or state; an enforced status of exile as punishment"}}
                                 ]},
                   {"id": {"de": "Spezielle Rechtsakte", "en": "Special legal acts"}, "description": {"de": "Sammelbegriff für Rechtsakte, die sich nicht in die übrigen Kategorien einordnen lassen", "en": "Collective term for legal acts that cannot be classified into the other categories"},
                    "children": [{"id": {"de": "Politische Akte", "en": "Political Acts"}, "description": {"de": "Sammelbegriff für Rechtsakte die im breit verstandenen Sinne politische Kontexte betreffen", "en": "Collective term for legal acts relating to political contexts in the broadest sense"},
                                  "children": [{"id": {"de": "Schutzbrief", "en": "letter of protection"}, "description": {"de": "Rechtsakt, welcher den Inhaber unter den Schutz des Ausstellenden stellt", "en": "Legal act that places the holder under the protection of the issuer"},
                                                "children": [{"id": {"de": "Geleitbrief", "en": "letter of safe conduct"}, "description": {"de": "Rechtsakt, welcher den Empfänger eine sichere Passage an einen vorbestimmten Ort zusichert", "en": "Legal act which assures the recipient safe passage to a predetermined location."}}
                                                             ]}
                                               ]},
                                 {"id": {"de": "Kirchliche Angelegenheiten", "en": "Ecclesiastical Acts"}, "description": {"de": "Sammelbegriff für Rechtsakte im breit verstandenen kirchlichen Kontext", "en": "Collective term for legal acts in the broadly understood ecclesiastical context"},
                                  "children": [{"id": {"de": "Stiftung (Rechtsakt)", "en": "Donation (legal act)"}, "description": {"de": "Rechtsakt, welcher einen bestimmten Besitz oder Anspruch an eine Institution mit deren Einverständnis überträgt und hierbei genaue Gegenleistungen festlegt", "en": "Legal act which transfers a specific property or claim to an institution with its consent, specifying precise obligations in return."}}
                                               ]}
                                 ]}
                   ]}
]

#Funktion, um den Tree in die jeweilige Sprache (de, en) zu setzen
def to_language_tree(nodes, lang="de"):
    result = []
    for node in nodes:
        new_node = {
            "id": node["id"][lang],
            "description": node["description"][lang],
        }
        if "children" in node:
            new_node["children"] = to_language_tree(node["children"], lang)
        result.append(new_node)
    return result

current_language = "de"

#hierdurch wird die Funktion zu einem neu renderbaren Ui-Block, der durch .refresh in der Funktion change_language neu erzeugt wird
@ui.refreshable
def render_ui():
    #erstellt den Header
    if current_language == "de":
        header = "Rechtsakttypologie der Projekte VAMOD und DigiHistDB"
    elif current_language == "en":
        header = "Typology of legal acts by the projects VAMOD and DigiHistDB"
    
    ui.label(header).classes("text-lg font-bold")

    #erstellt den Baum
    tree = ui.tree(to_language_tree(data, current_language), label_key="id") 

    #Darstellung des Baums mit Header und Description
    tree.add_slot('default-header', '''
        <span :props="props"><strong>{{ props.node.id }}</strong></span>
    ''')

    tree.add_slot('default-body', '''
        <span :props="props">{{ props.node.description }}</span>
    ''')

    #Filterfunktion
    ui.input('Filter').bind_value_to(tree, 'filter')

#Funktion, die die current_language ändert
def change_language(lang):
    global current_language
    current_language = lang
    render_ui.refresh()

render_ui()

#Toggle, um zwischen den Sprachen zu wechseln
ui.toggle(
    options={"de": "Deutsch", "en": "English"},
    value="de",
    on_change=lambda e: change_language(e.value),
).props("inline")

#Links auf FactGrid
with ui.row().classes("items-center gap-4"):
    ui.label("Find us on FactGrid!")
    ui.link("VAMOD","https://database.factgrid.de/wiki/FactGrid:VAMOD", new_tab=True)
    ui.link("DigiHistDB", "https://database.factgrid.de/wiki/Item:Q1091401", new_tab=True)

ui.run()

