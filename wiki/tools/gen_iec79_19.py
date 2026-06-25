#!/usr/bin/env python3
"""Generate the IEC 79-19 concept pages per the LLM-Wiki method (decompose to the
source's own definitions + per-component repair topics). Re-runnable: edit DATA
here, not the output pages.

The standard is a matrix: type of protection (clause 3="d", 4="i", 5="p", 6="e",
7="n") x component (enclosures, windings, ...). Each component = one concept page
synthesising the requirement across the protection types that address it.
"""
import os

WIKI = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CON = os.path.join(WIKI, "concepts")
STD = os.path.join(WIKI, "standards")

def sym(s):  # only link symbols that exist
    return s if os.path.isfile(os.path.join(WIKI, "symbols", s + ".md")) else None

# clause / label / page for each protection type, in clause order
TYPE = {
    "d": ("type-of-protection-d", '"d" — flameproof enclosure', "clause 3"),
    "i": ("type-of-protection-i", '"i" — intrinsic safety',     "clause 4"),
    "p": ("type-of-protection-p", '"p" — pressurization',        "clause 5"),
    "e": ("type-of-protection-e", '"e" — increased safety',      "clause 6"),
    "n": ("type-of-protection-n", '"n" — non-sparking',          "clause 7"),
}
ORDER = ["d", "i", "p", "e", "n"]

# ---------------------------------------------------------------- definitions (clause 2.2)
DEFS = [
    ("serviceable-condition", "Serviceable condition", "2.2.1",
     "Condition which permits a replacement or reclaimed component part to be used "
     "without prejudice to the performance or explosion-protection aspects of the "
     "apparatus, with due regard to the certification requirements as applicable.",
     ["repair", "reclamation", "component-part"]),
    ("component-part", "Component part", "2.2.5",
     "An indivisible item. The assembly of such items may form an apparatus.",
     ["reclamation", "serviceable-condition"]),
    ("manufacturer", "Manufacturer", "2.2.8",
     "Maker of the apparatus (who may also be the supplier, importer or agent), in whose "
     "name the certification of the apparatus was usually originally registered. Much of "
     "the standard turns on “reference to the manufacturer” for winding data, "
     "spare parts and any rating change.",
     ["repairer", "certification"]),
    ("user", "User", "2.2.9",
     "User of the apparatus. Carries statutory responsibilities (2.3.3) and issues the "
     "instructions to the repairer (2.5).",
     ["repairer", "repair"]),
    ("repairer", "Repairer", "2.2.10",
     "Repairer of the apparatus, who may be the manufacturer, the user or a third party "
     "(repair agency). Carries statutory responsibilities (2.3.4) and must hold the "
     "training, documentation and facilities required by clause 2.6.",
     ["user", "manufacturer", "repair"]),
    ("certification", "Certification", "2.2.11",
     "Certification leading to the issue of a certificate of conformity, referring "
     "primarily to assessments of apparatus carried out by a recognized testing "
     "authority. The standard may also apply to apparatus certified by other authorities "
     "or self-certified by manufacturers/users against recognized standards.",
     ["certificate-references", "manufacturer"]),
    ("certificate-references", "Certificate references", "2.2.12",
     "A certificate reference number may refer to a single design or a range of similar "
     "apparatus. The suffix “X” added to the certificate number indicates "
     "special conditions of use — the certification documents must be studied "
     "before such apparatus is installed, repaired, overhauled, reclaimed or modified.",
     ["certification", "modification"]),
]

# ---------------------------------------------------------------- protection types (clauses 3-7)
PROT = {
    "d": ("Type of protection \"d\" — flameproof enclosure", "2.2.14", "3",
          "Protection in which parts that can ignite an explosive gas atmosphere are placed "
          "in an **enclosure that withstands the pressure of an internal explosion** and "
          "prevents transmission of the explosion to the surrounding atmosphere. The flame "
          "paths/gaps are critical and must not be reclaimed beyond spec.",
          ["enclosures", "threaded-holes-for-fasteners", "windings", "rotors-and-stators", "insulation"],
          ["02-01-04", "06-08-01", "06-04-01"]),
    "i": ("Type of protection \"i\" — intrinsic safety", "2.2.15", "4",
          "A circuit in which **no spark or thermal effect** produced under the prescribed "
          "test conditions (normal operation plus specified faults) can cause ignition of "
          "the explosive atmosphere. Typically instrumentation and low-energy circuits; "
          "safety depends on encapsulated barriers and conductor separation, not the enclosure.",
          ["optocouplers", "internal-wiring", "transformers", "encapsulated-parts", "non-electrical-parts", "terminations"],
          ["03-02-02"]),
    "p": ("Type of protection \"p\" — pressurization", "2.2.16", "5",
          "Protection by which entry of the surrounding atmosphere into the enclosure is "
          "prevented by maintaining a **protective gas at a pressure above** the external "
          "atmosphere (with or without continuous flow). Repair must not increase gas "
          "leakage or create stagnant volumes.",
          ["enclosures", "cable-and-conduit-entries", "windings", "insulation"],
          ["02-01-04"]),
    "e": ("Type of protection \"e\" — increased safety", "2.2.17", "6",
          "Measures applied to give, with a higher degree of security, freedom from "
          "excessive temperatures and from arcs or sparks in the interior and on external "
          "parts of apparatus that does not produce them in normal service. Creepage/"
          "clearance distances and the temperature class are decisive.",
          ["windings", "rotors-and-stators", "terminations", "insulation", "lampholders", "lamps", "ballasts"],
          ["06-03-01", "06-02-07", "06-08-01"]),
    "n": ("Type of protection \"n\" — non-sparking", "2.2.18", "7",
          "Protection applied so that, in normal operation, the apparatus is not capable of "
          "igniting the surrounding explosive atmosphere and a fault capable of ignition is "
          "not likely to occur (includes non-sparking and restricted-breathing enclosures).",
          ["enclosures", "cable-and-conduit-entries", "windings", "insulation", "shafts-and-housings"],
          []),
}

# ---------------------------------------------------------------- component repair topics (the substance)
# meta: title, intro, related-concepts, symbols
COMP_META = {
    "enclosures": ("Enclosures — Ex repair",
        "The housing that provides or maintains explosion protection — flameproof "
        "containment for type \"d\", and a certified degree of protection (IP) for "
        "\"e\"/\"p\"/\"n\". Repair must never degrade that function.",
        ["cable-and-conduit-entries", "threaded-holes-for-fasteners", "light-transmitting-parts"], ["02-01-04"]),
    "cable-and-conduit-entries": ("Cable and conduit entries — Ex repair",
        "The glands/fittings where cables or conduit pass into the enclosure; they must "
        "preserve the flameproof joint (type \"d\") or the certified degree of protection "
        "(IP54 min for \"e\"/\"n\").",
        ["enclosures", "terminations"], ["03-02-02"]),
    "terminations": ("Terminations — Ex repair",
        "Terminals, bushings and connection points; repair must preserve creepage and "
        "clearance distances and the certified insulation materials (comparative tracking index).",
        ["insulation", "internal-wiring"], ["03-02-02"]),
    "insulation": ("Insulation — Ex repair",
        "The winding/conductor insulation system; replacement must be of equal or superior "
        "class (IEC 85) and a superior class never licenses a rating increase without "
        "reference to the [[manufacturer]].",
        ["windings", "terminations", "copy-winding"], []),
    "windings": ("Windings — Ex repair",
        "Motor/transformer windings. The electrical construction decisively influences "
        "explosion safety, so rewinding follows strict original-data and [[copy-winding]] "
        "rules and may, for type \"e\", have to be done by the original manufacturer.",
        ["copy-winding", "rotors-and-stators", "testing-after-repair", "insulation"], ["06-03-01", "06-02-07"]),
    "rotors-and-stators": ("Rotors and stators — Ex repair",
        "Rotor cages and stator cores. Skimming increases the air gap and can raise surface "
        "temperatures (temperature class) or pressure-piling, so air-gap checks and a stator "
        "core flux test apply.",
        ["windings", "shafts-and-housings"], ["06-08-01"]),
    "shafts-and-housings": ("Shafts and housings — Ex reclamation",
        "Shafts and bearing housings (including flameproof joints), reclaimed by metal "
        "spraying, sleeving or welding — any machining to the specified flamepath dimensions.",
        ["sleeve-bearings", "rotors-and-stators", "enclosures"], []),
    "sleeve-bearings": ("Sleeve bearings — Ex reclamation",
        "Plain bearing surfaces, reclaimed by electroplating or metal spraying.",
        ["shafts-and-housings"], []),
    "light-transmitting-parts": ("Light transmitting parts — Ex repair",
        "Viewing windows / luminaire lenses; not repairable or re-cemented — replace "
        "with complete manufacturer assemblies, and never clean plastics with solvent "
        "(household detergent only).",
        ["enclosures", "lamps"], []),
    "encapsulated-parts": ("Encapsulated parts — Ex repair",
        "Components embedded in compound (luminaire switching devices, shunt-diode safety "
        "barriers, encapsulated batteries/components) — generally not repairable; "
        "replace as a unit of the original design, preserving the safety description.",
        ["batteries", "transformers", "optocouplers"], []),
    "batteries": ("Batteries — Ex repair",
        "Batteries in Ex apparatus — replace only with manufacturer-specified types; "
        "where encapsulated, replace the whole assembly.",
        ["encapsulated-parts"], []),
    "lamps": ("Lamps — Ex repair",
        "Replacement lamps must be manufacturer-specified types and never exceed the "
        "specified wattage (in type \"e\" the single pin of a single-pin fluorescent tube "
        "forms a flameproof enclosure in the lampholder).",
        ["lampholders", "light-transmitting-parts"], ["08-10-01"]),
    "lampholders": ("Lampholders — Ex repair",
        "Lampholders are invariably specific types (single-pin for fluorescent, screw for "
        "others); use only manufacturer-specified replacements and do not rewire factory-"
        "made connections unless equipped to the same standard.",
        ["lamps", "ballasts"], []),
    "ballasts": ("Ballasts (chokes and capacitors) — Ex repair",
        "Chokes and capacitors for discharge lamps; replace only with manufacturer-listed "
        "parts (consult the manufacturer about proprietary alternatives).",
        ["lamps", "lampholders"], []),
    "optocouplers": ("Optocouplers — Ex repair",
        "Opto-isolators in intrinsically safe circuits; replace only with a component of "
        "the same or directly equivalent type and certification.",
        ["encapsulated-parts", "internal-wiring"], []),
    "internal-wiring": ("Internal wiring and connections — Ex repair",
        "Internal connections and their segregation. Renewed wiring must be no inferior "
        "electrically/thermally/mechanically and no smaller in cross-section; for type "
        "\"i\" critical inter-conductor distances must be kept in their original positions.",
        ["terminations", "optocouplers"], []),
    "transformers": ("Transformers — Ex repair",
        "Transformers in Ex apparatus; a faulty unit is replaced via the manufacturer and "
        "no embedded (encapsulated) thermal trip is ever repaired or replaced in the field.",
        ["windings", "encapsulated-parts", "testing-after-repair"], ["06-09-01"]),
    "non-electrical-parts": ("Non-electrical parts — Ex repair",
        "Parts (fittings, windows) that do not affect the electrical circuit or the "
        "creepage/clearance distances — and hence not intrinsic safety — may be "
        "replaced by new parts of equivalent type.",
        ["light-transmitting-parts"], []),
    "auxiliary-equipment": ("Auxiliary equipment — Ex repair",
        "Add-ons such as anti-condensation heaters and embedded temperature sensors; sensors "
        "are best embedded in the winding before varnishing/curing, and adding auxiliary "
        "equipment requires consulting the manufacturer on feasibility and procedure.",
        ["windings", "testing-after-repair"], []),
    "threaded-holes-for-fasteners": ("Threaded holes and flameproof joint faces — Ex reclamation",
        "Damaged fastener threads and flameproof joint faces in type \"d\" enclosures; "
        "reclaimed only after consulting the manufacturer and without altering the joint "
        "gap, flange dimensions or surface finish so as to contravene the standard.",
        ["enclosures", "shafts-and-housings"], []),
    "testing-after-repair": ("Testing after repair (of windings) — Ex apparatus",
        "The post-repair test regime after winding work: winding-resistance measurement "
        "(phase-balanced), an insulation-resistance test (≥500 V d.c., ≥20 MΩ "
        "at 20 °C for a complete rewind up to 660 V), a high-voltage test, and an "
        "energized check; rotating machines add a full-speed run and a locked-rotor "
        "reduced-voltage full-load test (see IEC 34).",
        ["windings", "transformers"], []),
}

# per-component requirement text by protection type (from the source, clause-cited)
COMP = {
  "enclosures": {
    "d": "Prefer new manufacturer parts; damaged parts may be repaired only if the certified type of protection is preserved, with particular attention to re-assembly so flameproof joints comply with the standard/certification (3.2.1). Non-gasketed flameproof joints may be protected externally by grease, non-setting compound or non-hardening tape — but non-hardening tape only with group IIA gases (expert guidance for IIB) and never where group IIC apparatus is used with IIC gases. Reclaimed enclosure parts may be used only if they pass the applicable over-pressure test; non-integral parts (e.g. fixing lugs) may be welded/metal-stitched provided cracks do not extend to the flameproof enclosure (3.3.1).",
    "i": "Enclosures are required only where intrinsic safety depends on them, but are often present for other reasons; repair and overhaul shall not reduce the degree of protection (IP rating) offered by the enclosure (4.2.1).",
    "p": "Damaged parts may be repaired or replaced provided they are of at least equivalent strength and do not increase protective-gas leakage, restrict gas flow, let the explosive atmosphere enter, create stagnant volumes, or reduce heat dissipation so as to infringe the temperature class; gaskets/seals are replaced with the same (or a compatible) material (5.2.1). Reclamation by welding/metal stitching must keep the enclosure able to withstand the impact test and the appropriate over-pressure (5.3.1.1).",
    "e": "Damaged parts may be repaired or replaced provided the degree of protection and temperature classification on the certification label are preserved (including any more stringent environmental protection); impact-test requirements and the protection of air inlet/outlet openings are observed, adequate clearance kept between stationary and rotating parts, and only manufacturer-specified finishes applied; fan and fan-cover clearances and ventilation holes are checked before returning a rewound machine to service, damaged fans/covers replaced by manufacturer parts (or equal dimensions/quality avoiding frictional sparking and electrostatic charging) (6.2.1). Reclamation by welding/metal stitching must keep the impact-test withstand and degree of protection (6.3.1.1).",
    "n": "Damaged parts may be repaired or replaced provided the degree of protection and temperature classification on the certification label are preserved (including any more stringent environmental protection); impact-test requirements are met, adequate clearance kept between stationary and rotating parts, and for restricted-breathing enclosures particular attention is paid to gaskets/seals; only manufacturer-specified finishes applied, and fan-cover ventilation holes and fan clearances checked before a rewound machine returns to service (7.2.1). Reclamation by welding/metal stitching must not impair integrity so the enclosure still withstands the impact test and maintains the degree of protection (7.3.1).",
  },
  "cable-and-conduit-entries": {
    "d": "Entries into flameproof enclosures shall, after repair or overhaul, conform to the appropriate apparatus standard and/or certification documents (3.2.2). Additional entries shall not be made without reference to the manufacturer, and indirect entry shall not be changed to direct entry (3.4.2). Damaged male threaded parts should not be reclaimed (use new components); damaged female threads may be repaired after consultation with the manufacturer (3.3.1.2c).",
    "i": "Special entries maintain the enclosure's degree of protection; any repairs shall not reduce that degree of protection (4.2.2).",
    "p": "Entries shall preserve the degree of protection originally provided and shall not allow increased leakage of pressurizing gas (5.2.2); any modification shall maintain the specified type and degree of protection (5.4.2).",
    "e": "Entries shall preserve a minimum IP54 degree of protection per IEC 529 (6.2.2); modifications shall maintain the specified type and degree of protection (6.4.2).",
    "n": "Entries shall preserve a minimum IP54 degree of protection per IEC 529 (7.2.2); modifications shall maintain the specified type and degree of protection (7.4.2).",
  },
  "terminations": {
    "d": "Maintain clearance and creepage distances when refurbishing terminations; replacement terminals, bushings or parts must come from the manufacturer or conform to the relevant apparatus standard/certification (3.2.3). Termination assemblies containing a flameproof joint shall not be modified; those without may be replaced by alternatives of adequate design in number, current-carrying capacity, creepage/clearance and quality (3.4.3).",
    "i": "Replaced terminals should normally be of the same type; where unavailable, any alternative shall satisfy the creepage (per CTI) and clearance requirements for the maximum voltage and the separation needed to avoid inadvertent cross-connection (4.2.3).",
    "p": "The creepage and clearance distances as originally provided shall be preserved (5.2.3); any modification should use good engineering practice (5.4.3).",
    "e": "Materials, creepage/clearance distances and comparative tracking indices of termination insulation are normally specified in the certification documents, so replacement parts should come from the manufacturer or be used on his advice; loose-lead terminations shall comply with the certification documents (6.2.3). No modification without reference to the manufacturer (6.4.3).",
    "n": "Take care when refurbishing terminal compartments to maintain clearances/creepages per the apparatus standard; where non-metallic fixing screws are used, only replacement screws of similar material shall be used; loose-lead terminations shall comply with the certification documents (7.2.3). Terminations shall be modified only if compliance with the apparatus standard is maintained (7.4.3).",
  },
  "insulation": {
    "d": "A class of insulation the same as or superior to the original may be used (e.g. class E repaired with class F per IEC 85), but a superior class does not permit any increase in apparatus rating without reference to the manufacturer (3.2.4).",
    "p": "Any replacement insulation used in repair or overhaul should be at least of the quality and class originally employed (see IEC 85) (5.2.4).",
    "e": "Comprehensive details of the winding insulation system, including the impregnation varnish, are normally in the certification documents; where they are not, full information shall be sought from the manufacturer (6.2.4).",
    "n": "A class of insulation the same as or superior to the original may be used (e.g. class E repaired with class F per IEC 85), but a superior class does not permit a rating increase without reference to the manufacturer (7.2.4).",
  },
  "windings": {
    "d": "Original winding data should preferably be obtained from the manufacturer; otherwise copy-winding techniques may be used with an appropriate insulation system, and if superior insulation is used the rating shall not be increased without manufacturer reference (3.2.6). Faulty die-cast aluminium rotor cages are replaced with new manufacturer rotors; bar-wound cage rotors may be rewound with identical-specification materials kept tight in the slots (3.2.6.2). Rewinding for a different voltage or speed requires manufacturer reference, ensuring magnetic loading, current densities and losses are not increased, new creepage/clearance distances and the temperature class respected, and the rating plate updated (3.4.4).",
    "p": "Original winding data should preferably come from the manufacturer, otherwise copy-winding with an appropriate insulation system; superior insulation must not raise the rating without manufacturer reference, as the temperature class could be affected (5.2.6.1). Rewinding for another voltage requires manufacturer reference (magnetic loading, current densities and losses not increased; new creepage/clearance observed; new voltage within certification limits; rating plate changed); rewinding for a different speed needs manufacturer reference (5.4.4).",
    "e": "Because the electrical construction decisively influences explosion safety, the repairer must fully possess the necessary information and equipment, and unless all apparatus-standard requirements can be met the rewinding shall be done by the original manufacturer; the full original winding data must first be obtained (winding type/diagram, conductors per slot, parallel paths, interphase connections, conductor size, insulation/varnish system, resistance per phase), and the winding restored to original condition (partial replacement only on larger apparatus and only after manufacturer/certifier reference) (6.2.6.1). Rewinding for another voltage only after manufacturer reference with the same constraints, the IA/IN ratio within certification limits, rating plate changed; different speed needs manufacturer reference (6.4.4).",
    "n": "The original winding data shall be determined (preferably from the manufacturer, otherwise by copy-winding) and the new winding shall conform to the original; superior insulation should not raise the rating without manufacturer reference, and partial replacement is not recommended except on larger apparatus and only after manufacturer/certifier reference (7.2.6.1). Rewinding for another voltage is permissible after manufacturer reference under the same constraints with the rating plate changed; a different speed is not permissible without manufacturer reference (7.4.4).",
  },
  "rotors-and-stators": {
    "d": "If rotors and stators are lightly skimmed to remove eccentricities/surface damage, the increased air gap must not change pressure-piling characteristics or raise external surface temperatures so as to infringe the temperature class — seek advice (preferably the manufacturer) if uncertain. Skimmed or damaged stator cores shall be flux-tested to ensure no hot spots remain that could infringe the temperature classification or damage the windings (3.3.4).",
    "e": "Faulty die-cast aluminium cage rotors shall be replaced with completely new manufacturer rotors; bar-wound cage rotors rewound with identical-specification materials kept tight in undamaged slots (6.2.6.2). Light skimming (after consulting the manufacturer) must not let the increased air gap raise internal/external surface temperatures above the temperature class nor prevent protective devices giving the required tripping characteristics; skimmed/damaged stator cores should be flux-tested (6.3.3).",
    "n": "A faulty die-cast aluminium rotor shall be replaced with a complete new manufacturer rotor; bar-wound cage rotors rewound with equivalent-specification materials kept tight in the slots (7.2.6.2). Light skimming must not let the increased air gap raise internal/external surface temperatures above the temperature class, and skimmed/damaged stator cores should be flux-tested (7.3.3.3).",
  },
  "shafts-and-housings": {
    "d": "Shafts and bearing housings, including flameproof joints, may be reclaimed e.g. by metal spraying or sleeving, but any subsequent machining shall be to the flamepath dimensions specified in the apparatus standard/certification; welding may be appropriate with due regard to its limitations (3.3.2).",
    "p": "Reclaim shafts and bearing housings by metal spraying or sleeving; welding may be appropriate with due regard to its limitations (5.3.2).",
    "e": "Reclaim shafts and bearing housings by metal spraying or sleeving; welding may be appropriate with due regard to its limitations (6.3.1.3).",
    "n": "Reclaim shafts and bearing housings, preferably by metal spraying or sleeving; welding may be appropriate with due regard to its limitations (7.3.3.1).",
  },
  "sleeve-bearings": {
    "d": "Sleeve-bearing surfaces may be reclaimed by electroplating or metal spraying (3.3.3).",
    "p": "Sleeve-bearing surfaces may be built up by electroplating or metal spraying (5.3.3).",
    "e": "Sleeve-bearing surfaces may be reclaimed by electroplating or metal spraying (6.3.2).",
    "n": "Sleeve-bearing surfaces may be built up by electroplating or metal spraying (7.3.3.2).",
  },
  "light-transmitting-parts": {
    "d": "No attempt shall be made to re-cement or repair light transmitting parts; only complete replacement assemblies specified by the manufacturer shall be used, and plastics parts shall not be cleaned with solvents (household detergents recommended) (3.2.7).",
    "p": "Plastics light transmitting parts shall not be cleaned with solvent; household detergents are recommended (5.2.7).",
    "e": "No attempt shall be made to repair light transmitting parts and only manufacturer replacement components used; plastics parts shall not be cleaned with solvents (household detergents may be used) (6.2.7).",
    "n": "Plastics light transmitting or other parts should not be cleaned with solvents; household detergents may be used (7.2.7).",
  },
  "encapsulated-parts": {
    "d": "Encapsulated parts (e.g. switching devices in luminaires) are generally not considered suitable for repair (3.2.8).",
    "i": "Encapsulated components (e.g. batteries with internal current-limiting resistors, or fuse/zener-diode assemblies) are non-repairable and replaced only with original-design assemblies from the equipment manufacturer; shunt-diode safety barriers are totally encapsulated and no repair should be attempted (a replacement must keep the same safety description, U value and the 50 mm IS/non-IS separation) (4.2.7, 4.2.14).",
    "p": "In general, encapsulated parts (e.g. switching devices in luminaires) are not considered suitable for repair (5.2.8).",
    "e": "In general, encapsulated parts (e.g. switching devices in luminaires) are not considered suitable for repair or reclamation (6.2.8).",
    "n": "In general, encapsulated parts (e.g. switching devices in luminaires) are not considered suitable for repair (7.2.8).",
  },
  "batteries": {
    "d": "Where batteries are used, the manufacturer's advice should be followed (3.2.9).",
    "i": "Only types specified in the equipment manufacturer's instructions should be used as replacements, and where batteries are encapsulated the whole assembly should be replaced (4.2.11).",
    "p": "Where batteries are used, the manufacturer's advice should be followed (5.2.9).",
    "e": "Where batteries are used, reference shall be made to the manufacturer's instructions before any repair or replacement (6.2.9).",
    "n": "Where batteries are used, reference shall be made to the manufacturer's instructions before any repair or replacement (7.2.9).",
  },
  "lamps": {
    "d": "Lamp types specified by the manufacturer shall be used as replacements and the maximum specified wattage shall not be exceeded (3.2.10).",
    "p": "Lamp types specified by the manufacturer should be used and the maximum specified wattage should not be exceeded (5.2.10).",
    "e": "Lamp types specified by the manufacturer shall be used and the maximum wattage shall not be exceeded; special care with single-pin tubular fluorescent tubes because the single pin in the lampholder forms a flameproof enclosure and distortion/misalignment may affect the explosion protection (6.2.10).",
    "n": "Lamp types specified by the manufacturer shall be used and the maximum specified wattage shall not be exceeded (7.2.10).",
  },
  "lampholders": {
    "d": "Replacement lampholders listed by the manufacturer should be used (3.2.11).",
    "p": "Replacements listed by the manufacturer should be used (5.2.11).",
    "e": "Only manufacturer-specified replacements shall be used; where wiring to the lampholder is factory-made (crimps, etc.) rewiring shall not be undertaken unless the repairer can make it to the same standard (lampholders are invariably specific types — single-pin for fluorescent, screw for others) (6.2.11).",
    "n": "Replacements listed by the manufacturer shall be used (7.2.11).",
  },
  "ballasts": {
    "d": "Chokes or capacitors should be replaced only with the manufacturer's listed parts unless the manufacturer is consulted about alternatives (3.2.12).",
    "p": "Chokes or capacitors should be replaced only with manufacturer's listed parts, unless reference is made to the manufacturer about alternatives (5.2.12).",
    "e": "Defective chokes and capacitors shall only be replaced with the manufacturer's listed parts (6.2.12).",
    "n": "Chokes or capacitors should only be replaced with manufacturer's listed parts; if of proprietary manufacture, reference should be made to the original manufacturer about alternatives (7.2.12).",
  },
  "optocouplers": {
    "i": "Only components of the same or directly equivalent type and certification shall be used as replacements (4.2.9).",
  },
  "internal-wiring": {
    "d": "There are no particular requirements for this type of protection, but repairs to internal connections should be of a standard at least equivalent to the original design (3.2.5).",
    "i": "Certain inter-conductor distances and their segregation are critical, so disturbed internal wiring shall be re-located in its original position; damaged insulation, screens, outer sheaths and/or double insulation or fixing methods shall be replaced by equivalent material and re-fixed in the same configuration (4.2.12).",
    "p": "Internal connections should not be electrically, thermally or mechanically inferior to those originally fitted and should be of a standard at least equivalent to the original design (5.2.5).",
    "e": "If internal connections are renewed, the insulation shall not be electrically, thermally or mechanically inferior to that originally supplied, and the cross-sectional area shall not be less than originally fitted (6.2.5).",
    "n": "If internal connections are renewed, the insulation shall not be electrically, thermally or mechanically inferior to that originally supplied, and the cross-sectional area shall not be less than originally fitted (7.2.5).",
  },
  "transformers": {
    "i": "If a transformer is found faulty, the replacement shall be obtained from the equipment manufacturer, and no attempt shall be made to repair or replace any embedded (encapsulated) thermal trip device (4.2.13).",
    "p": "After winding repair, the transformer should preferably be energized at rated supply voltage, the supply current and secondary voltage/current measured and compared with the manufacturer's data, and balanced across all phases in three-phase systems (5.2.6.3.1 d).",
    "e": "After winding repair, the transformer should preferably be energized at rated supply voltage, measurements compared with the manufacturer's data, and balanced across all phases (6.2.6.3.1 d).",
    "n": "After winding repair, the transformer should preferably be energized at rated supply voltage, measurements compared with the manufacturer's data, and balanced across all phases (7.2.6.3.1 d).",
  },
  "non-electrical-parts": {
    "i": "Non-electrical parts (e.g. fittings or windows) that do not affect the electrical circuit or creepage/clearance distances, and hence not intrinsic safety, may be replaced by new parts of equivalent type (4.2.15).",
  },
  "auxiliary-equipment": {
    "d": "Temperature sensors monitoring winding temperatures should be embedded in the winding before varnishing/curing; certified flameproof brake units should be returned to the manufacturer with the machine; auxiliary devices using other types of protection require consulting the corresponding clauses (3.2.6.4). Adding auxiliary equipment such as anti-condensation heaters or temperature sensors requires consulting the manufacturer on feasibility and procedure (3.4.5).",
    "p": "Where additional auxiliary equipment is requested (e.g. anti-condensation heaters or temperature sensors), the manufacturer should be consulted on feasibility and procedure (5.4.5).",
    "e": "Temperature sensors monitoring winding temperatures are best embedded in the winding before varnishing/curing (6.2.6.3.3); adding auxiliary equipment requires consulting the manufacturer on feasibility and procedure (6.4.5).",
    "n": "Temperature sensors monitoring winding temperatures are best embedded in the winding before varnishing/curing (7.2.6.4); adding auxiliary equipment requires consulting the manufacturer on feasibility and procedure (7.4.5).",
  },
  "threaded-holes-for-fasteners": {
    "d": "Reclamation of damaged threaded holes may use the clause-2 techniques only with due consultation with the manufacturer and without contravening the apparatus standard (3.3.1.3); damaged or corroded flameproof joint faces may be machined (after consulting the manufacturer) only if the resulting joint gap and flange dimensions are not affected so as to contravene the standard/certification and surface finish is not reduced below the allowed level (3.3.1.2).",
  },
  "testing-after-repair": {
    "d": "After complete or partial winding repair (preferably with the apparatus assembled): winding-resistance measurement (balanced across three-phase windings), an insulation-resistance test (≥500 V d.c.; not less than ~20 MΩ at 20 °C for a complete rewind up to 660 V), a high-voltage test, and an energized rated-voltage check; rotating machines additionally require a full-speed run (investigating noise/vibration) and a locked-rotor reduced-voltage full-load current/phase-balance test, with high-voltage or non-cage machines possibly needing further tests (3.2.6.3).",
    "i": "Before equipment with intrinsically safe circuits only is re-installed in the hazardous area, the insulation between the IS circuit and the enclosure shall be checked by applying 500 V a.c. (50–60 Hz) between the terminals and the enclosure for 1 minute; this may be omitted if the enclosure is of insulating material and one side of the circuit is galvanically connected to it for safety reasons (4.2.16).",
    "p": "After complete or partial winding repair, with the apparatus assembled: measure/verify each winding's resistance (balanced for three-phase); insulation-resistance test (≥500 V d.c. recommended; ≥20 MΩ at 20 °C for a complete rewind up to 660 V) between windings and earth, between windings, between windings and auxiliaries, and between auxiliaries and earth; high-voltage test per the apparatus standard; transformers energized at rated voltage. Rotating machines additionally run at full speed (noise/vibration) and cage stators energized at reduced voltage with rotor locked to obtain full-load rated current and confirm phase balance/joint integrity (see IEC 34) (5.2.6.3).",
    "e": "Same post-winding-repair regime as for \"p\": winding resistance (phase-balanced), insulation resistance (≥500 V d.c.; ≥20 MΩ at 20 °C for a complete rewind up to 660 V) across all combinations, high-voltage test, transformers energized at rated voltage; rotating machines run at full speed and cage stators given a locked-rotor reduced-voltage full-load test (see IEC 34) (6.2.6.3).",
    "n": "Same post-winding-repair regime as for \"p\"/\"e\": winding resistance (phase-balanced), insulation resistance (≥500 V d.c.; ≥20 MΩ at 20 °C for a complete rewind up to 660 V) across all combinations, high-voltage test, transformers energized at rated voltage; rotating machines run at full speed and cage stators given a locked-rotor reduced-voltage full-load test (see IEC 34) (7.2.6.3).",
  },
}


def wl(slug):
    return "[[%s]]" % slug


def write(path, text):
    with open(path, "w") as f:
        f.write(text)


def gen_definitions():
    for slug, title, clause, text, related in DEFS:
        rel = " · ".join(wl(r) for r in related)
        body = (
            "---\nid: %s\ntype: concept\ntags: [concept, iec-79-19, ex-repair, definition]\n---\n\n"
            "# %s\n\n%s\n\nDefined in [[iec-79-19]] %s.\n\nRelated: %s\n"
            % (slug, title, text, clause, rel)
        )
        write(os.path.join(CON, slug + ".md"), body)
    return len(DEFS)


def gen_protection():
    for t, (title, iev, clause, desc, comps, syms) in PROT.items():
        comp_links = " · ".join(wl(c) for c in comps)
        sym_links = " · ".join(wl(s) for s in syms if sym(s))
        others = " · ".join(wl(TYPE[o][0]) for o in ORDER if o != t)
        body = "---\nid: %s\ntype: concept\ntags: [concept, iec-79-19, ex, protection-type]\n---\n\n# %s\n\n%s\n\nDefined in [[iec-79-19]] %s. Repair, overhaul, reclamation and modification requirements are in **[[iec-79-19]] clause %s**.\n\n**Component repair topics under this type:** %s\n" % (
            TYPE[t][0], title, desc, iev, clause, comp_links)
        if sym_links:
            body += "\n**Related symbols:** %s\n" % sym_links
        body += "\n**Other types of protection:** %s\n" % others
        write(os.path.join(CON, TYPE[t][0] + ".md"), body)
    return len(PROT)


def gen_components():
    n = 0
    for slug, types in COMP.items():
        title, intro, related, syms = COMP_META[slug]
        lines = [
            "---", "id: %s" % slug, "type: concept",
            "tags: [concept, iec-79-19, ex-repair, component]", "---", "",
            "# %s" % title, "", intro, "",
            "In [[iec-79-19]], repair/overhaul/reclamation of this component is "
            "specified per type of protection:", "",
        ]
        for t in ORDER:
            if t in types:
                page, label, clause = TYPE[t]
                lines.append("- **[[%s|%s]]** (%s): %s" % (page, label, clause, types[t]))
        lines.append("")
        rel = " · ".join(wl(r) for r in related)
        if rel:
            lines.append("**Related topics:** %s" % rel)
        sym_links = " · ".join(wl(s) for s in syms if sym(s))
        if sym_links:
            lines.append("")
            lines.append("**Related symbols:** %s" % sym_links)
        lines.append("")
        write(os.path.join(CON, slug + ".md"), "\n".join(lines))
        n += 1
    return n


HUB = """---
id: iec-79-19
type: standard
family: IEC 79 (explosive atmospheres)
standard: IEC 79-19
edition: "1st edition, 1993"
title_en: "Electrical apparatus for explosive gas atmospheres — Part 19: Repair and overhaul"
title_fr: "Matériel électrique pour atmosphères explosives gazeuses — Partie 19: Réparation et révision"
source: "Publication No. 79-19.pdf (scanned, 46 pp; OCR in kg-app/backend/corpus/iec-79-19.txt)"
tags: [standard, ex, explosive-atmospheres, repair, overhaul]
---

# IEC 79-19 — Repair and overhaul of Ex electrical apparatus

*Electrical apparatus for explosive gas atmospheres, Part 19: Repair and overhaul
for apparatus used in explosive gas atmospheres (other than mines or for the
manufacture of explosives).* 1st edition, 1993.

Unlike the [[index#standards|60617 parts]] (a symbol dictionary), this is a
**procedure / requirements standard**: it specifies how Ex-protected electrical
apparatus may be repaired, overhauled, reclaimed and modified without
invalidating its explosion-protection certification. Decomposed here per the
LLM-Wiki method — each definition, each type of protection, and **each
component repair topic** is its own concept page.

## Scope (clause 1)
Requirements for the **repair, overhaul, reclamation and modification** of
explosion-protected electrical apparatus for explosive gas atmospheres. Covers
the responsibilities of [[user]] and [[repairer]], documentation, and
type-of-protection-specific requirements.

## How the standard is organised (the decomposition map)
A **matrix**: type of protection (one clause each) × component. Clause 3 =
[[type-of-protection-d|"d"]], 4 = [[type-of-protection-i|"i"]], 5 =
[[type-of-protection-p|"p"]], 6 = [[type-of-protection-e|"e"]], 7 =
[[type-of-protection-n|"n"]]; within each, **.2** repair & overhaul, **.3**
reclamation, **.4** modification, sub-divided by component. The component pages
below synthesise each row across all protection types.

## Process & responsibilities (definitions, clause 2.2)
[[repair]] · [[overhaul]] · [[maintenance]] · [[reclamation]] · [[modification]] · [[copy-winding]] · [[serviceable-condition]] · [[component-part]] · [[manufacturer]] · [[user]] · [[repairer]] · [[certification]] · [[certificate-references]]

## Types of protection (clauses 3–7)
[[type-of-protection-d]] (flameproof, cl.3) · [[type-of-protection-i]] (intrinsic safety, cl.4) · [[type-of-protection-p]] (pressurization, cl.5) · [[type-of-protection-e]] (increased safety, cl.6) · [[type-of-protection-n]] (non-sparking, cl.7)

## Component repair topics (the substance — each synthesised across protection types)
**Enclosure & entries** — [[enclosures]] · [[cable-and-conduit-entries]] · [[threaded-holes-for-fasteners]] · [[light-transmitting-parts]]
**Windings & rotating parts** — [[windings]] · [[rotors-and-stators]] · [[shafts-and-housings]] · [[sleeve-bearings]] · [[insulation]] · [[testing-after-repair]]
**Connections** — [[terminations]] · [[internal-wiring]]
**Lighting** — [[lamps]] · [[lampholders]] · [[ballasts]]
**Electronic / encapsulated** — [[optocouplers]] · [[transformers]] · [[encapsulated-parts]] · [[batteries]]
**Other** — [[auxiliary-equipment]] · [[non-electrical-parts]]

## Related symbols (cross-links into the 60617 graph)
A SOW that touches Ex motors / enclosures / windings connects to:
- Machines & motors — [[06-04-01]] (machine, general), [[06-08-01]] (induction motor, squirrel cage), [[06-06-01]] (a.c. commutator motor)
- Windings — [[06-03-01]] (commutating/compensating winding), [[06-02-07]] (three-phase star winding)
- Motor control — [[07-14-01]] (motor starter, general)
- Enclosure & terminals — [[02-01-04]] (envelope / enclosure), [[03-02-02]] (terminal)
- Gas material — [[02-07-04]] (material, gas)

## Related standards
- References **IEC 364** (electrical installations), **IEC 85** (insulation thermal
  classes), **IEC 529** (degrees of protection / IP), **IEC 34** (rotating machines),
  and the parent **IEC 79-0** and type standards (**IEC 79-1** "d", **IEC 79-2** "p", etc.).
- Part of the **IEC 79** explosive-atmospheres family (sibling parts not in this collection).
"""


def main():
    nd = gen_definitions()
    npt = gen_protection()
    nc = gen_components()
    write(os.path.join(STD, "iec-79-19.md"), HUB)
    print("IEC 79-19: %d definition pages + %d protection-type pages (clauses fixed) "
          "+ %d component pages + rebuilt hub." % (nd, npt, nc))


if __name__ == "__main__":
    main()
