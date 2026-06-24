#!/usr/bin/env python3
"""Generate the IEC 60617-2 portion of the symbol KG from structured data.

Data extracted by vision-reading `../Standards-Reference/Publication No.617-2.pdf`
(1st edition, 1983). 154 symbols across 17 sections (3 chapters) + Appendix A.
Edit the DATA below, not the output files; re-run to regenerate.
"""
import os, json

WIKI = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
STD_ID = "60617-2"; ASSET_DIR = "60617-2"

PART = dict(id="60617-2",
  title_en="Symbol elements, qualifying symbols and other symbols having general application",
  title_fr="Éléments de symboles, symboles distinctifs et autres symboles d'application générale",
  standard="IEC 60617-2 (formerly IEC 617-2)", edition="1st edition, 1983",
  source="Publication No.617-2.pdf",
  tc="Prepared by IEC Sub-Committee 3A (Graphical Symbols) of Technical Committee No. 3.")

# section SS -> (slug, title_en, title_fr, chapter)
SECTIONS = {
 "01":("outlines-enclosures","Outlines and enclosures","Cadres et enveloppes","I — Symbol elements"),
 "02":("current-voltage","Kind of current and voltage","Nature du courant et de la tension","II — Qualifying symbols"),
 "03":("variability","Variability","Variabilité","II — Qualifying symbols"),
 "04":("force-motion","Direction of force or motion","Sens de l'effort ou du mouvement","II — Qualifying symbols"),
 "05":("flow","Direction of flow","Sens de propagation","II — Qualifying symbols"),
 "06":("characteristic-quantity","Operational dependence on a characteristic quantity","Fonctionnement dépendant d'une grandeur caractéristique","II — Qualifying symbols"),
 "07":("material","Types of material","Types de matière","II — Qualifying symbols"),
 "08":("effect-dependence","Effect or dependence","Effet ou dépendance","II — Qualifying symbols"),
 "09":("radiation","Radiation","Rayonnement","II — Qualifying symbols"),
 "10":("waveforms","Signal waveforms","Forme des signaux","II — Qualifying symbols"),
 "11":("printing","Printing, perforating and facsimile","Impression, perforation, télécopie","II — Qualifying symbols"),
 "12":("mechanical-controls","Mechanical controls","Commandes mécaniques","III — Other symbols having general application"),
 "13":("operating-devices","Operating devices and methods","Dispositifs et méthodes de commande","III — Other symbols having general application"),
 "14":("non-electrical-control","Control by non-electrical quantities","Commande par grandeurs non électriques","III — Other symbols having general application"),
 "15":("earth-frame","Earth and frame connections, equipotentiality","Mise à la terre et à la masse, équipotentialité","III — Other symbols having general application"),
 "16":("ideal-circuit-elements","Ideal circuit elements","Éléments idéaux de circuit","III — Other symbols having general application"),
 "17":("miscellaneous","Miscellaneous","Divers","III — Other symbols having general application"),
 "A1":("older-symbols","Older symbols (Appendix A)","Anciens symboles (Annexe A)","Appendix A"),
}

# asset page -> ordered IDs (mirror of crop_symbols.py); printed page = asset-2
PAGE_IDS={
 10:["02-01-01","02-01-02","02-01-03","02-01-04","02-01-05"],11:["02-01-06","02-01-07"],
 12:["02-02-01","02-02-02","02-02-03","02-02-04","02-02-05","02-02-06","02-02-07"],
 13:["02-02-08","02-02-09","02-02-10","02-02-11","02-02-12","02-02-13","02-02-14","02-02-15","02-02-16"],
 14:["02-03-01","02-03-02","02-03-03","02-03-04"],
 15:["02-03-05","02-03-06","02-03-07","02-03-08","02-03-09","02-03-10","02-03-11","02-03-12"],
 16:["02-04-01","02-04-02","02-04-03","02-04-04","02-04-05","02-04-06"],
 17:["02-05-01","02-05-02","02-05-03","02-05-04","02-05-05","02-05-06","02-05-07","02-05-08"],
 18:["02-06-01","02-06-02","02-06-03","02-06-04","02-06-05"],
 19:["02-07-01","02-07-02","02-07-03","02-07-04","02-07-05","02-07-06","02-07-07"],
 20:["02-08-01","02-08-02","02-08-03","02-08-04","02-08-05"],
 21:["02-09-01","02-09-02","02-09-03"],
 22:["02-10-01","02-10-02","02-10-03","02-10-04","02-10-05","02-10-06"],
 23:["02-11-01","02-11-02","02-11-03","02-11-04","02-11-05","02-11-06"],
 24:["02-12-01","02-12-02","02-12-03","02-12-04","02-12-05","02-12-06","02-12-07","02-12-08","02-12-09"],
 25:["02-12-10","02-12-11","02-12-12","02-12-13","02-12-14","02-12-15","02-12-16","02-12-17","02-12-18","02-12-19","02-12-20","02-12-21","02-12-22","02-12-23"],
 26:["02-13-01","02-13-02","02-13-03","02-13-04","02-13-05","02-13-06","02-13-07","02-13-08","02-13-09","02-13-10"],
 27:["02-13-11","02-13-12","02-13-13","02-13-14","02-13-15","02-13-16","02-13-17","02-13-18","02-13-19","02-13-20","02-13-21"],
 28:["02-13-22","02-13-23","02-13-24","02-13-25","02-13-26","02-13-27"],
 29:["02-14-01","02-14-02","02-14-03","02-14-04","02-14-05"],
 30:["02-15-01","02-15-02","02-15-03","02-15-04","02-15-05"],
 31:["02-16-01","02-16-02","02-16-03"],
 32:["02-17-01","02-17-02","02-17-03","02-17-04","02-17-05","02-17-06"],
 33:["02-17-07","02-17-08","02-17-09"],34:["02-A1-01"]}
ID2PAGE={i:p for p,ids in PAGE_IDS.items() for i in ids}

def S(id,en,fr,desc,aliases=None,notes=None,form=None,forms=None,see=None,
      concept=None,refs=None,example=False,superseded_by=None,supersedes=None):
    sec=id.split("-")[1]
    return dict(id=id,sec=sec,en=en,fr=fr,desc=desc,aliases=aliases or [],
                notes=notes or [],form=form,forms=forms or [],see=see or [],
                concept=concept or [],refs=refs or [],example=example,
                superseded_by=superseded_by,supersedes=supersedes)

SYMBOLS=[
 # Section 1 — Outlines and enclosures
 S("02-01-01","Item / equipment / functional unit (Form 1)","Dispositif / équipement / unité fonctionnelle (Forme 1)",
   "General outline for an item, equipment, unit or functional unit (square/rectangle). Form 1.",
   notes=["Suitable symbols or legends shall be inserted in or added to the symbol outline to indicate the item, equipment or function."],form="Form 1",forms=["02-01-02","02-01-03"]),
 S("02-01-02","Item / equipment / functional unit (Form 2)","Dispositif / équipement (Forme 2)","Outline for an item/equipment. Form 2.",form="Form 2",forms=["02-01-01","02-01-03"]),
 S("02-01-03","Item / equipment / functional unit (Form 3)","Dispositif / équipement (Forme 3)","Outline for an item/equipment (rounded/oval). Form 3.",form="Form 3",forms=["02-01-01","02-01-02"]),
 S("02-01-04","Envelope (tank) / enclosure (Form 1)","Enveloppe (impôt ou cuve) / Enceinte (Forme 1)","Envelope (tank) or enclosure. Form 1.",
   notes=["An outline of another shape may be used.","If the enclosure has special protective features may be drawn to these by a note."],form="Form 1",forms=["02-01-05"]),
 S("02-01-05","Envelope (tank) / enclosure (Form 2)","Enveloppe / Enceinte (Forme 2)","Envelope (tank) or enclosure. Form 2.",
   notes=["The use of the envelope symbol is optional. It may be omitted if no confusion will arise. If necessary the envelope may be split."],form="Form 2",forms=["02-01-04"]),
 S("02-01-06","Boundary line","Ligne de séparation","A boundary line.",
   notes=["Used to indicate items associated physically, mechanically or functionally.","Any combination of short and long strokes may be used."]),
 S("02-01-07","Screen (shield)","Écran","A screen (shield).",notes=["The screen may be drawn in any convenient shape."]),
 # Section 2 — Kind of current and voltage
 S("02-02-01","Direct current (Form 1)","Courant continu (Forme 1)","Direct current.",
   notes=["The voltage may be indicated at the right of the symbol and the type of system at the left."],form="Form 1",forms=["02-02-03"]),
 S("02-02-02","Direct current, three conductors incl. mid-wire — example","Courant continu, trois conducteurs dont un conducteur médian — exemple",
   "Worked example: direct current, three conductors including mid-wire, 220 V (110 V between each outer conductor and mid-wire), shown as “2M — 220/110 V”. 2M may be replaced by 2+M.",example=True),
 S("02-02-03","Direct current (Form 2)","Courant continu (Forme 2)","Direct current, alternative form.",
   notes=["To be used if symbol 02-02-01 causes confusion."],form="Form 2",forms=["02-02-01"]),
 S("02-02-04","Alternating current","Courant alternatif","Alternating current.",
   notes=["The numerical value of the frequency or the frequency range may be added at the right-hand side of the symbol."]),
 S("02-02-05","Alternating current, 50 Hz — example","Courant alternatif, 50 Hz — exemple","Worked example: alternating current of 50 Hz (“∿ 50 Hz”).",example=True,see=["02-02-04"]),
 S("02-02-06","Alternating current, frequency range 100–600 kHz — example","Courant alternatif, gamme de fréquences 100–600 kHz — exemple",
   "Worked example: alternating current frequency range 100 kHz to 600 kHz. The voltage may also be indicated to the right of the symbol.",example=True,see=["02-02-04"]),
 S("02-02-07","Three-phase with neutral, 50 Hz, 400/230 V — example","Triphasé avec neutre, 50 Hz, 400/230 V — exemple",
   "Worked example: alternating current, three-phase with neutral, 50 Hz, 400 V (230 V between phase and neutral), shown as “3N ∿ 50 Hz 400/230 V”. 3N may be replaced by 3+N.",example=True),
 S("02-02-08","Three-phase AC, TN-S system — example","Triphasé, système TN-S — exemple",
   "Worked example: alternating current, three-phase, 50 Hz, with neutral and protective conductor separate (TN-S).",
   notes=["If it is necessary to indicate a system in accordance with the designations established in IEC Publication 364-3 (Electrical installations of buildings, Part 3), the corresponding designation should be added to the right of the symbol."],
   refs=["364-3"],example=True),
 S("02-02-09","Relatively low frequencies","Fréquences relativement basses",
   "Relatively low frequencies (example: power frequencies or sub-audio frequencies). Used when it is necessary on a drawing to distinguish between frequency ranges.",see=["02-02-10","02-02-11"]),
 S("02-02-10","Medium frequencies","Fréquences moyennes","Medium frequencies (example: audio frequencies).",see=["02-02-09","02-02-11"]),
 S("02-02-11","Relatively high frequencies","Fréquences relativement hautes","Relatively high frequencies (example: super-audio, carrier and radio frequencies).",see=["02-02-09","02-02-10"]),
 S("02-02-12","Rectified current with alternating component","Courant redressé avec composante alternative",
   "Rectified current with alternating component (if it is necessary to distinguish it from a steady direct current)."),
 S("02-02-13","Positive polarity","Polarité positive","Positive polarity (+).",see=["02-02-14"]),
 S("02-02-14","Negative polarity","Polarité négative","Negative polarity (−).",see=["02-02-13"]),
 S("02-02-15","Neutral","Neutre","Neutral (N).",notes=["The symbol for the neutral conductor is given in IEC Publication 445."],refs=["445"]),
 S("02-02-16","Mid-wire","Médian","Mid-wire (M).",notes=["The symbol for mid-wire is given in IEC Publication 445."],refs=["445"]),
 # Section 3 — Variability
 S("02-03-01","Variability, non-inherent","Variabilité extrinsèque","Non-inherent (extrinsic) variability — the variable quantity is controlled by an external device. The sign is drawn across the main symbol at about 45° to its centre line.",see=["02-03-03"]),
 S("02-03-02","Variability, non-inherent, non-linear","Variabilité extrinsèque non linéaire","Non-inherent, non-linear variability.",see=["02-03-01"]),
 S("02-03-03","Variability, inherent","Variabilité intrinsèque","Inherent (intrinsic) variability — depends on qualities of the device itself (e.g. resistance changes with voltage or temperature).",
   notes=["Information on the controlling quantity, for example voltage or temperature, may be shown near the symbol."],see=["02-03-01"]),
 S("02-03-04","Variability, inherent, non-linear","Variabilité intrinsèque non linéaire","Inherent, non-linear variability.",notes=["The note with symbol 02-03-03 applies."],see=["02-03-03"]),
 S("02-03-05","Pre-set adjustment","Ajustement prédéterminé","Pre-set adjustment.",notes=["Information on the conditions under which adjustment is permitted may be shown near the symbol."]),
 S("02-03-06","Pre-set adjustment at zero current only — example","Ajustement prédéterminé autorisé à courant nul — exemple","Worked example: pre-set adjustment permitted only at zero current (“I = 0”).",example=True,see=["02-03-05"]),
 S("02-03-07","Variability in steps / stepping action","Variabilité par échelons / action pas à pas","Variability in steps; stepping action.",notes=["A figure indicating the number of steps may be added."]),
 S("02-03-08","Variability, non-inherent, in five steps — example","Variabilité extrinsèque à cinq échelons — exemple","Worked example: non-inherent variability in five steps (“5”).",example=True,see=["02-03-07"]),
 S("02-03-09","Continuous variability","Variabilité continue","Continuous variability."),
 S("02-03-10","Pre-set adjustment, continuously variable — example","Ajustement prédéterminé à action continue — exemple","Worked example: pre-set adjustment, continuously variable.",example=True,see=["02-03-05","02-03-09"]),
 S("02-03-11","Automatic (inherent) control","Régulation automatique","Automatic (inherent) control.",notes=["The controlled quantity may be indicated adjacent to the symbol."]),
 S("02-03-12","Amplifier with automatic gain control — example","Amplificateur avec contrôle automatique de gain — exemple","Worked example: amplifier with automatic gain control (AGC), shown “dB ▷”.",example=True,see=["02-03-11"]),
 # Section 4 — Direction of force or motion
 S("02-04-01","Rectilinear force or motion in direction of arrow","Effort ou mouvement de translation dans le sens de la flèche","Rectilinear force or motion in the direction of the arrow."),
 S("02-04-02","Bidirectional rectilinear force or motion","Effort ou mouvement dans les deux sens","Bidirectional rectilinear force or motion.",see=["02-04-01"]),
 S("02-04-03","Unidirectional rotation","Rotation unidirectionnelle","Unidirectional rotation in the direction of the arrow, for example clockwise."),
 S("02-04-04","Bidirectional rotation","Rotation dans les deux sens","Bidirectional rotation.",see=["02-04-03"]),
 S("02-04-05","Bidirectional rotation, limited","Rotation limitée dans les deux sens","Bidirectional rotation, limited in both directions.",see=["02-04-04"]),
 S("02-04-06","Reciprocating motion","Mouvement oscillant","Reciprocating motion."),
 # Section 5 — Direction of flow
 S("02-05-01","Propagation / energy flow / signal flow, one way","Propagation / transit d'énergie / signal, un seul sens","Propagation, energy flow or signal flow, one way."),
 S("02-05-02","Propagation both ways, simultaneously","Propagations simultanées dans les deux sens","Propagation both ways, simultaneously; simultaneous transmission and reception.",see=["02-05-03"]),
 S("02-05-03","Propagation both ways, not simultaneously","Propagations non simultanées dans les deux sens","Propagation both ways, not simultaneously; alternate transmission and reception.",see=["02-05-02"]),
 S("02-05-04","Transmission","Émission","Transmission.",notes=["The dot may be omitted if the sense is unambiguously given by the arrowhead in combination with the symbol to which it is applied (for example see symbol 10-06-04)."],see=["02-05-05","10-06-04"]),
 S("02-05-05","Reception","Réception","Reception.",notes=["The dot may be omitted if the sense is unambiguously given by the arrowhead (for example see symbol 10-06-03)."],see=["02-05-04","10-06-03"]),
 S("02-05-06","Energy flow from the busbars","Transit de l'énergie issue des barres","Energy flow from the busbars."),
 S("02-05-07","Energy flow towards the busbars","Transit de l'énergie vers les barres","Energy flow towards the busbars.",see=["02-05-06"]),
 S("02-05-08","Bidirectional energy flow","Transit de l'énergie dans les deux sens","Bidirectional energy flow.",see=["02-05-06","02-05-07"]),
 # Section 6 — Operational dependence on a characteristic quantity
 S("02-06-01","Operating above setting value (>)","Fonctionnement au-dessus de la valeur d'ajustement (>)","Operating when the characteristic quantity is higher than the setting value."),
 S("02-06-02","Operating below setting value (<)","Fonctionnement au-dessous de la valeur d'ajustement (<)","Operating when the characteristic quantity is lower than the setting value."),
 S("02-06-03","Operating outside a range (≷)","Fonctionnement hors d'une plage (≷)","Operating when the characteristic quantity is either higher than a given high setting or lower than a given low setting."),
 S("02-06-04","Operating at zero (=0)","Fonctionnement à valeur nulle (=0)","Operating when the value of the characteristic quantity becomes zero."),
 S("02-06-05","Operating near zero (≈0)","Fonctionnement proche de zéro (≈0)","Operating when the value of the characteristic quantity differs from zero by an amount which is very small compared with the normal value."),
 # Section 7 — Types of material
 S("02-07-01","Material, unspecified","Matière non spécifiée","Material, unspecified.",notes=["The type of material may be indicated either by its chemical symbol or by one of the qualifying symbols 02-07-02..07. The rectangle may be omitted when used with another symbol. See ISO 128."],refs=["ISO 128"]),
 S("02-07-02","Material, solid","Matière solide","Material, solid.",see=["02-07-01"]),
 S("02-07-03","Material, liquid","Matière liquide","Material, liquid.",see=["02-07-01"]),
 S("02-07-04","Material, gas","Matière gazeuse","Material, gas.",see=["02-07-01"]),
 S("02-07-05","Material, electret","Électret","Material, electret.",see=["02-07-01"]),
 S("02-07-06","Material, semiconducting","Semi-conducteur","Material, semiconducting.",see=["02-07-01"]),
 S("02-07-07","Material, insulating (dielectric)","Isolant ou diélectrique","Material, insulating (dielectric).",see=["02-07-01"]),
 # Section 8 — Effect or dependence
 S("02-08-01","Thermal effect","Effet thermique","Thermal effect."),
 S("02-08-02","Electromagnetic effect","Effet électromagnétique","Electromagnetic effect."),
 S("02-08-03","Magnetostrictive effect","Effet par magnétostriction","Magnetostrictive effect."),
 S("02-08-04","Magnetic field effect or dependence","Effet ou dépendance du champ magnétique","Magnetic field effect or dependence."),
 S("02-08-05","Delay","Temporisation","Delay."),
 # Section 9 — Radiation
 S("02-09-01","Radiation, non-ionizing, electromagnetic","Rayonnement électromagnétique non ionisant","Radiation, non-ionizing, electromagnetic (for example radio waves or visible light). Arrows pointing away from a symbol denote emission by the device."),
 S("02-09-02","Coherent radiation, non-ionizing","Rayonnement cohérent, non ionisant","Coherent radiation, non-ionizing (for example coherent light)."),
 S("02-09-03","Radiation, ionizing","Rayonnement ionisant","Radiation, ionizing.",notes=["If it is necessary to show the specific type of ionizing radiation, the symbol may be supplemented by letters: α alpha particle, β beta particle, γ gamma rays, D deuteron, p proton, η neutron, π pion, κ K meson, μ muon, X X-ray."]),
 # Section 10 — Signal waveforms
 S("02-10-01","Positive-going pulse","Impulsion positive","Positive-going pulse. Each symbol represents an idealized shape of the waveform."),
 S("02-10-02","Negative-going pulse","Impulsion négative","Negative-going pulse.",see=["02-10-01"]),
 S("02-10-03","Pulse of alternating current","Impulsion de courant alternatif","Pulse of alternating current."),
 S("02-10-04","Positive-going step function","Fonction échelon positive","Positive-going step function.",see=["02-10-05"]),
 S("02-10-05","Negative-going step function","Fonction échelon négative","Negative-going step function.",see=["02-10-04"]),
 S("02-10-06","Saw-tooth","Onde en dents de scie","Saw-tooth waveform."),
 # Section 11 — Printing, perforating and facsimile
 S("02-11-01","Tape printing","Impression sur bande","Tape printing."),
 S("02-11-02","Tape perforating or using perforated tape","Perforation de bande ou utilisation de bande perforée","Tape perforating, or using perforated tape."),
 S("02-11-03","Simultaneous printing and perforating of one tape","Impression et perforation simultanées sur la même bande","Simultaneous printing and perforating of one tape."),
 S("02-11-04","Page printing","Impression sur page","Page printing."),
 S("02-11-05","Keyboard","Clavier","Keyboard."),
 S("02-11-06","Facsimile","Télécopie","Facsimile."),
 # Section 12 — Mechanical controls
 S("02-12-01","Mechanical / pneumatic / hydraulic connection (link) (Form 1)","Liaison mécanique / pneumatique / hydraulique (Forme 1)","Mechanical connection (link); also pneumatic or hydraulic connection. Form 1.",form="Form 1",forms=["02-12-04"]),
 S("02-12-02","Mechanical connection with direction of force/motion","Liaison mécanique avec indication du sens de l'effort ou du mouvement","Mechanical connection with indication of direction of force or motion."),
 S("02-12-03","Mechanical connection with direction of rotation","Liaison mécanique avec indication du sens de rotation","Mechanical connection with indication of direction of rotation.",notes=["The arrow is supposed to be placed in front of the connection symbol."]),
 S("02-12-04","Mechanical connection (link) (Form 2)","Liaison mécanique (Forme 2)","Mechanical connection (link). Form 2.",notes=["To be used if the space is too restricted to permit the use of symbol 02-12-01."],form="Form 2",forms=["02-12-01"]),
 S("02-12-05","Delayed action (Form 1)","Mouvement retardé (Forme 1)","Delayed action.",notes=["Delayed action in the direction of movement from the arc towards the centre."],form="Form 1",forms=["02-12-06"]),
 S("02-12-06","Delayed action (Form 2)","Mouvement retardé (Forme 2)","Delayed action. Form 2.",form="Form 2",forms=["02-12-05"]),
 S("02-12-07","Automatic return","Retour automatique","Automatic return.",notes=["The triangle is pointed in the return direction."]),
 S("02-12-08","Non-automatic return / device maintaining a position","Retour non automatique / dispositif de maintien dans une position","Non-automatic return; device for maintaining a given position."),
 S("02-12-09","Detent, disengaged","Crantage, libéré","Detent, disengaged.",see=["02-12-10"]),
 S("02-12-10","Detent, engaged","Crantage, en prise","Detent, engaged.",see=["02-12-09"]),
 S("02-12-11","Mechanical interlock between two devices","Verrouillage mécanique entre deux appareils","Mechanical interlock between two devices."),
 S("02-12-12","Latching device, disengaged","Dispositif d'accrochage libéré","Latching device, disengaged.",see=["02-12-13"]),
 S("02-12-13","Latching device, engaged","Dispositif d'accrochage en prise","Latching device, engaged.",see=["02-12-12"]),
 S("02-12-14","Blocking device","Dispositif de blocage","Blocking device.",see=["02-12-15"]),
 S("02-12-15","Blocking device engaged (movement to left blocked)","Dispositif de blocage engagé","Blocking device engaged, movement to the left is blocked.",see=["02-12-14"]),
 S("02-12-16","Clutch / mechanical coupling","Embrayage / accouplement mécanique","Clutch; mechanical coupling.",see=["02-12-17","02-12-18"]),
 S("02-12-17","Mechanical coupling, disengaged","Accouplement mécanique débrayé","Mechanical coupling, disengaged.",see=["02-12-16","02-12-18"]),
 S("02-12-18","Mechanical coupling, engaged","Accouplement mécanique embrayé","Mechanical coupling, engaged.",see=["02-12-16","02-12-17"]),
 S("02-12-19","Unidirectional coupling (free wheel) — example","Accouplement à entraînement dans un seul sens, roue libre — exemple","Worked example: unidirectional coupling device for rotation; free wheel.",example=True,see=["02-12-16"]),
 S("02-12-20","Brake","Frein","Brake.",see=["02-12-21","02-12-22"]),
 S("02-12-21","Electric motor with brake applied — example","Moteur électrique avec frein serré — exemple","Worked example: electric motor with brake applied.",example=True,see=["02-12-20"]),
 S("02-12-22","Electric motor with brake released — example","Moteur électrique avec frein desserré — exemple","Worked example: electric motor with brake released.",example=True,see=["02-12-20"]),
 S("02-12-23","Gearing","Engrenage","Gearing."),
 # Section 13 — Operating devices and methods
 S("02-13-01","Manually operated control, general case","Commande mécanique manuelle, cas général","Manually operated control, general case.",see=["02-13-02"]),
 S("02-13-02","Manually operated control with restricted access","Commande manuelle à accès restreint","Manually operated control with restricted access.",see=["02-13-01"]),
 S("02-13-03","Operated by pulling","Commande par tirette","Operated by pulling."),
 S("02-13-04","Operated by turning","Commande rotative","Operated by turning."),
 S("02-13-05","Operated by pushing","Commande par poussoir","Operated by pushing."),
 S("02-13-06","Operated by proximity effect","Commande par effet de proximité","Operated by proximity effect."),
 S("02-13-07","Operated by touching","Commande par effleurement","Operated by touching."),
 S("02-13-08","Emergency switch (mushroom-head safety feature)","Bouton-poussoir de sécurité type « coup de poing »","Emergency switch with mushroom-head safety feature."),
 S("02-13-09","Operated by handwheel","Commande par volant","Operated by handwheel."),
 S("02-13-10","Operated by pedal","Commande par pédale","Operated by pedal."),
 S("02-13-11","Operated by lever","Commande par levier","Operated by lever."),
 S("02-13-12","Operated by removable handle","Commande manuelle amovible","Operated by removable handle."),
 S("02-13-13","Operated by key","Commande par clef","Operated by key."),
 S("02-13-14","Operated by crank","Commande par manivelle","Operated by crank."),
 S("02-13-15","Operated by roller","Commande par galet","Operated by roller."),
 S("02-13-16","Operated by cam","Commande par came","Operated by cam.",notes=["If desired, a more detailed drawing of the cam may be shown; this applies also to a profile plate."],see=["02-13-17","02-13-18","02-13-19"]),
 S("02-13-17","Cam profile — example","Profil de came — exemple","Worked example: cam profile.",example=True,see=["02-13-16"]),
 S("02-13-18","Profile plate / cam profile (stepped)","Profil d'un dispositif linéaire / profil de came","Profile plate; cam profile (stepped representation).",see=["02-13-16"]),
 S("02-13-19","Operated by cam and roller","Commande par came et galet","Operated by cam and roller.",see=["02-13-16","02-13-15"]),
 S("02-13-20","Operated by stored mechanical energy","Commande par accumulation d'énergie mécanique","Operated by stored mechanical energy.",notes=["Information showing the form of stored energy may be added in the square."]),
 S("02-13-21","Operated by pneumatic/hydraulic control, single acting","Commande hydraulique ou pneumatique à simple effet","Operated by pneumatic or hydraulic control, single acting.",see=["02-13-22"]),
 S("02-13-22","Operated by pneumatic/hydraulic control, double acting","Commande hydraulique ou pneumatique à double effet","Operated by pneumatic or hydraulic control, double acting.",see=["02-13-21"]),
 S("02-13-23","Operated by electromagnetic actuator","Commande électromagnétique","Operated by electromagnetic actuator.",supersedes="02-A1-01"),
 S("02-13-24","Operated by electromagnetic overcurrent protection","Commande par protection électromagnétique de surintensité","Operated by electromagnetic overcurrent protection."),
 S("02-13-25","Operated by thermal actuator","Commande par élément thermosensible","Operated by thermal actuator, for example thermal relay, thermal overcurrent protection."),
 S("02-13-26","Operated by electric motor","Commande par moteur électrique","Operated by electric motor."),
 S("02-13-27","Operated by electric clock","Commande par horloge électrique","Operated by electric clock."),
 # Section 14 — Control by non-electrical quantities
 S("02-14-01","Control by fluid level","Commande par le niveau d'un fluide","Control by fluid level.",notes=["Letter symbols from IEC Publication 27 may be used to denote operating quantities."],refs=["27"]),
 S("02-14-02","Control by number of events / by a counter","Commande par un nombre d'événements / par comptage","Control by number of events; control by a counter."),
 S("02-14-03","Control by flow","Commande par le débit d'un fluide","Control by flow.",see=["02-14-04"]),
 S("02-14-04","Control by gas flow — example","Commande par le débit d'un gaz — exemple","Worked example: control by gas flow.",example=True,see=["02-14-03"]),
 S("02-14-05","Control by relative humidity","Commande par humidité relative","Control by relative humidity."),
 # Section 15 — Earth and frame connections, equipotentiality
 S("02-15-01","Earth (ground), general symbol","Terre, symbole général","Earth (ground), general symbol.",
   notes=["Supplementary information may be given to define the status or purpose of the earth if this is not readily apparent."],see=["02-15-02","02-15-03"]),
 S("02-15-02","Noiseless earth (ground)","Terre sans bruit","Noiseless earth (ground).",see=["02-15-01"]),
 S("02-15-03","Protective earth (ground)","Terre de protection","Protective earth (ground).",
   notes=["May be used in place of symbol 02-15-01 to indicate an earth connection having a protective function, for example protection against electrical shock in case of a fault."],see=["02-15-01"]),
 S("02-15-04","Frame / chassis","Masse / châssis","Frame; chassis.",
   notes=["The hatching may be completely or partly omitted if there is no ambiguity; if omitted, the line representing the frame or chassis shall be thicker."]),
 S("02-15-05","Equipotentiality","Équipotentialité","Equipotentiality."),
 # Section 16 — Ideal circuit elements
 S("02-16-01","Ideal current source","Source idéale de courant","Ideal current source.",
   notes=["Additional indications may be added according to IEC Publication 375 (Conventions concerning electric and magnetic circuits)."],refs=["375"],see=["02-16-02"]),
 S("02-16-02","Ideal voltage source","Source idéale de tension","Ideal voltage source.",refs=["375"],see=["02-16-01"]),
 S("02-16-03","Ideal gyrator","Gyrateur idéal","Ideal gyrator.",refs=["375"]),
 # Section 17 — Miscellaneous
 S("02-17-01","Fault (assumed location)","Défaut (emplacement supposé)","Fault; indication of assumed fault location."),
 S("02-17-02","Flashover / break-through","Défaut d'isolement (contournement, perforation, claquage)","Flashover; break-through (insulation failure by flashover, puncture, etc.)."),
 S("02-17-03","Permanent magnet","Aimant permanent","Permanent magnet."),
 S("02-17-04","Moving (e.g. sliding) contact","Contact mobile (par exemple glissant)","Moving (for example sliding) contact."),
 S("02-17-05","Test point indicator","Indicateur de point de contrôle","Test point indicator."),
 S("02-17-06","Changer / converter, general symbol","Convertisseur, symbole général","Changer; converter, general symbol.",
   notes=["If the direction of change is not obvious, it may be indicated by an arrowhead on the outline of the symbol.",
          "A symbol/legend for input or output quantity may be inserted in each half; see IEC 617-6 and 617-10.",
          "The diagonal line is used as a solidus to show a converting function; see IEC 617-12 and 617-13."],
   refs=["617-6","617-10","617-12","617-13"]),
 S("02-17-07","Galvanic separator","Séparateur galvanique","Galvanic separator.",
   notes=["If necessary, indication of the way of separation may be given below the qualifying symbol, for example X≠Y (galvanic separation by opto-coupler)."]),
 S("02-17-08","Identifier of analogue signals","Symbole d'identification des signaux analogiques","Identifier of analogue signals.",
   notes=["Used only when it is necessary to distinguish between analogue and digital signals."],see=["02-17-09"]),
 S("02-17-09","Identifier of digital signals","Symbole d'identification des signaux numériques","Identifier of digital signals.",
   notes=["The note with symbol 02-17-08 applies. A number (n) of bits may be denoted as n·#."],see=["02-17-08"]),
 # Appendix A — older symbols
 S("02-A1-01","Operated by electromagnetic actuator (older symbol)","Commande électromagnétique (ancien symbole)",
   "Older symbol: operated by electromagnetic actuator. Required for a change-over period only.",
   notes=["Should be superseded as soon as practicable by symbol 02-13-23."],superseded_by="02-13-23"),
]

# ---------- generation ----------
def yl(items): return "[]" if not items else "["+", ".join(json.dumps(x,ensure_ascii=False) for x in items)+"]"
def link(i): return f"[[{i}]]"
def secfile(ss): return f"{STD_ID}-{ss}-{SECTIONS[ss][0]}"
def printed(i): return ID2PAGE[i]-2
def write(p,c):
    os.makedirs(os.path.dirname(p),exist_ok=True); open(p,"w").write(c)

for s in SYMBOLS:
    ss=s["sec"]; slug,ten,tfr,chap=SECTIONS[ss]
    fm ="---\n"+f'id: {s["id"]}\ntype: symbol\nstandard: IEC 60617-2\npart: 2\n'
    fm+=f'chapter: {json.dumps(chap,ensure_ascii=False)}\nsection: "{ss}"\nedition: "1st edition, 1983"\n'
    fm+=f'name_en: {json.dumps(s["en"],ensure_ascii=False)}\nname_fr: {json.dumps(s["fr"],ensure_ascii=False)}\n'
    fm+=f'aliases: {yl(s["aliases"])}\nforms: {yl(s["forms"])}\nsee_also: {yl(s["see"])}\n'
    fm+=f'uses_concept: {yl(s["concept"])}\nreferences: {yl(["IEC "+r if not r.startswith("ISO") else r for r in s["refs"]])}\n'
    fm+=f'is_example: {"true" if s["example"] else "false"}\n'
    if s["superseded_by"]: fm+=f'superseded_by: "{s["superseded_by"]}"\n'
    if s["supersedes"]: fm+=f'supersedes: "{s["supersedes"]}"\n'
    fm+=f'source: "{PART["source"]}, printed p.{printed(s["id"])}"\ntags: [60617-2, section-{ss}]\n---\n\n'
    b =f'# {s["id"]} — {s["en"]}\n\n'
    b+=f'![{s["id"]}](../assets/{ASSET_DIR}/sym-{s["id"]}.png)\n'
    b+=f'<sub>Per-symbol crop from {PART["source"]}, printed p.{printed(s["id"])} '
    b+=f'([full page](../assets/{ASSET_DIR}/p{ID2PAGE[s["id"]]:02d}.png)).</sub>\n\n'
    b+=f'**Standard:** {link(PART["id"])} · **Chapter {chap}** · **Section:** {link(secfile(ss))}'
    if s["form"]: b+=f' · **{s["form"]}**'
    b+="\n\n## Description\n"+s["desc"]+"\n\n## Names\n"
    en=s["en"]+((" / "+" / ".join(s["aliases"])) if s["aliases"] else "")
    b+=f'- **EN:** {en}\n- **FR:** {s["fr"]}\n\n'
    if s["notes"]:
        b+="## Notes\n"+"".join(f'- {n}\n' for n in s["notes"])+"\n"
    rel=[]
    for f in s["forms"]: rel.append(f'{link(f)} — alternative form')
    if s["superseded_by"]: rel.append(f'superseded by {link(s["superseded_by"])}')
    if s["supersedes"]: rel.append(f'supersedes {link(s["supersedes"])}')
    for o in s["see"]: rel.append(link(o))
    for c in s["concept"]: rel.append(f'uses {link(c)}')
    for r in s["refs"]: rel.append(f'references **{r if r.startswith("ISO") else "IEC "+r}**')
    if rel: b+="## Related\n"+"".join(f'- {x}\n' for x in rel)
    write(os.path.join(WIKI,"symbols",s["id"]+".md"), fm+b)

# section hubs
for ss,(slug,ten,tfr,chap) in SECTIONS.items():
    syms=[s for s in SYMBOLS if s["sec"]==ss]
    if not syms: continue
    fm="---\n"+f'id: {secfile(ss)}\ntype: section\nstandard: IEC 60617-2\npart: 2\nsection: "{ss}"\n'
    fm+=f'chapter: {json.dumps(chap,ensure_ascii=False)}\ntitle_en: {json.dumps(ten,ensure_ascii=False)}\n'
    fm+=f'title_fr: {json.dumps(tfr,ensure_ascii=False)}\nsymbol_count: {len(syms)}\ntags: [60617-2, section]\n---\n\n'
    b=f'# 60617-2 Section {ss} — {ten}\n\n*{tfr}* · **Chapter {chap}** · **Part:** {link(PART["id"])} · {len(syms)} symbols\n\n'
    b+="| No. | Symbol | Name (EN) | Notes |\n|-----|--------|-----------|-------|\n"
    for s in syms:
        note=s["form"] or ("example" if s["example"] else "")
        b+=f'| {link(s["id"])} | ![](../assets/{ASSET_DIR}/sym-{s["id"]}.png) | {s["en"]} | {note} |\n'
    write(os.path.join(WIKI,"sections",secfile(ss)+".md"), fm+b)

# part page
fm="---\n"+f'id: {PART["id"]}\ntype: standard\nstandard: {json.dumps(PART["standard"],ensure_ascii=False)}\n'
fm+=f'edition: "{PART["edition"]}"\npart: 2\ntitle_en: {json.dumps(PART["title_en"],ensure_ascii=False)}\n'
fm+=f'title_fr: {json.dumps(PART["title_fr"],ensure_ascii=False)}\nsymbol_count: {len(SYMBOLS)}\n'
fm+=f'source: "{PART["source"]}"\nsupersedes: []\nsuperseded_by: []\ntags: [60617, standard, part]\n---\n\n'
b=f'# IEC 60617-2 — {PART["title_en"]}\n\n*{PART["title_fr"]}*\n\n'
b+=f'- **Standard:** {PART["standard"]}\n- **Edition:** {PART["edition"]}\n- **Source:** `{PART["source"]}` (scanned, 35 pp)\n'
b+=f'- **Origin:** {PART["tc"]}\n- **Symbols:** {len(SYMBOLS)} across {len([k for k in SECTIONS if any(s["sec"]==k for s in SYMBOLS)])} sections (3 chapters + Appendix A)\n\n'
b+="These are the **building-block** symbols (symbol elements and qualifying symbols) combined with the device symbols in the other 60617 parts. Foundational to the whole family.\n\n"
b+="## Chapters & sections\n"
lastchap=None
for ss,(slug,ten,tfr,chap) in SECTIONS.items():
    cnt=len([s for s in SYMBOLS if s["sec"]==ss])
    if chap!=lastchap: b+=f'\n**Chapter {chap}**\n'; lastchap=chap
    b+=f'- {link(secfile(ss))} — {ten} ({cnt})\n'
b+="\n## Related parts & standards\n- Part of the IEC 60617 family — see [[index#standards]].\n"
b+="- References **IEC 445**, **IEC 27**, **IEC 375**, **IEC 364-3**, **ISO 128**; cross-links to [[60617-3]] and (forward) Parts 6/10/12/13.\n"
write(os.path.join(WIKI,"standards",PART["id"]+".md"), fm+b)

print(f"Generated {len(SYMBOLS)} symbols, {len([k for k in SECTIONS if any(s['sec']==k for s in SYMBOLS)])} sections, 1 part.")
