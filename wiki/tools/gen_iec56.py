#!/usr/bin/env python3
"""Decompose IEC 56 (HV AC circuit-breakers) into the wiki per the LLM-Wiki
pattern: a standard hub page + one concept page per real entity (device & types,
parts, operation/releases, general terms & insulation, characteristic quantities,
rated characteristics, tests). Each page is concise, cites its IEC 56 clause and
(where applicable) the IEV reference it adopts, and cross-links to related
concepts and 60617 symbols. Re-run to regenerate; edit DATA here, not the pages.
"""
import os, re
WIKI = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CON = os.path.join(WIKI, "concepts"); STD = os.path.join(WIKI, "standards")

# (id, title, clause, iev, one-sentence definition, [related concept ids], [symbol ids])
E = [
 # --- device & types (3.102) ---
 ("circuit-breaker","Circuit-breaker","3.102.3","441-14-20",
  "A mechanical switching device capable of making, carrying and breaking currents under normal conditions and also making, carrying for a specified time and breaking currents under specified abnormal conditions such as short circuit.",
  ["making-and-breaking-capacity","rated-voltage","rated-short-circuit-breaking-current","rated-operating-sequence","operating-mechanism"],["07-13-05","07-01-02","07-A2-08"]),
 ("dead-tank-circuit-breaker","Dead-tank circuit-breaker","3.102.4","441-14-25",
  "A circuit-breaker with interrupters in an earthed metal tank.",["circuit-breaker","live-tank-circuit-breaker"],[]),
 ("live-tank-circuit-breaker","Live-tank circuit-breaker","3.102.5","441-14-26",
  "A circuit-breaker with interrupters in a housing insulated from and elevated above earth.",["circuit-breaker","dead-tank-circuit-breaker"],[]),
 ("air-circuit-breaker","Air circuit-breaker","3.102.6","441-14-27",
  "A circuit-breaker in which the contacts open and close in air at atmospheric pressure.",["circuit-breaker"],[]),
 ("oil-circuit-breaker","Oil circuit-breaker","3.102.7","441-14-28",
  "A circuit-breaker in which the contacts open and close in insulating oil.",["circuit-breaker"],[]),
 ("vacuum-circuit-breaker","Vacuum circuit-breaker","3.102.8","441-14-29",
  "A circuit-breaker in which the contacts open and close in a highly evacuated chamber.",["circuit-breaker"],[]),
 ("gas-blast-circuit-breaker","Gas-blast circuit-breaker","3.102.9","441-14-30",
  "A circuit-breaker in which the arc is extinguished by a blast of gas.",["circuit-breaker","sf6-circuit-breaker","air-blast-circuit-breaker"],[]),
 ("sf6-circuit-breaker","Sulphur hexafluoride (SF6) circuit-breaker","3.102.10","441-14-31",
  "A gas-blast circuit-breaker using sulphur hexafluoride (SF6) as the interrupting and insulating medium.",["gas-blast-circuit-breaker","circuit-breaker"],[]),
 ("air-blast-circuit-breaker","Air-blast circuit-breaker","3.102.11","441-14-32",
  "A gas-blast circuit-breaker using compressed air as the interrupting medium.",["gas-blast-circuit-breaker","circuit-breaker"],[]),
 ("restrike-free-circuit-breaker","Restrike-free circuit-breaker","3.102.12","",
  "A circuit-breaker that interrupts without restrike during the capacitive-current breaking-test duties specified in IEC 56.",["circuit-breaker","restrike","capacitive-current-switching-test"],[]),
 # --- parts (3.103) ---
 ("pole","Pole (of a circuit-breaker)","3.103.1","441-15-01",
  "The portion of a circuit-breaker associated exclusively with one electrically separated conducting path of its main circuit.",["circuit-breaker","main-circuit"],[]),
 ("main-circuit","Main circuit","3.103.2","441-15-02",
  "All the conductive parts of a circuit-breaker included in the circuit it is designed to close and open.",["pole","main-contact"],[]),
 ("main-contact","Main contact","3.103.7","441-15-07",
  "A contact in the main circuit intended to carry the rated normal current in the closed position.",["arcing-contact","main-circuit"],["03-02-02"]),
 ("arcing-contact","Arcing contact","3.103.8","441-15-08",
  "A contact on which the arc is intended to be established, protecting the main contact from damage.",["main-contact"],[]),
 ("module","Module (of a pole)","3.103.22","",
  "A part of a pole comprising one or more interrupting units, used where several are connected in series/parallel per pole.",["pole"],[]),
 # --- operation & releases (3.104) ---
 ("dependent-manual-operation","Dependent manual operation","3.104.9","441-16-13",
  "An operation solely by directly applied manual energy, so the speed and force depend on the operator.",["independent-manual-operation","stored-energy-operation","operating-mechanism"],[]),
 ("independent-manual-operation","Independent manual operation","3.104.12","441-16-16",
  "A stored-energy operation where the energy is stored and released by manual means in one continuous action, so speed/force are independent of the operator.",["dependent-manual-operation","stored-energy-operation"],[]),
 ("stored-energy-operation","Stored-energy operation","3.104.11","441-16-15",
  "An operation by energy stored in the mechanism beforehand and sufficient to complete the operation under predetermined conditions.",["operating-mechanism","independent-manual-operation"],[]),
 ("instantaneous-release","Instantaneous release","3.104.17","441-16-32",
  "A release that operates without any intentional time delay.",["over-current-release","operating-mechanism"],["02-13-24","07-15-01"]),
 ("over-current-release","Over-current release","3.104.19","441-16-33",
  "A release that causes a circuit-breaker to open with or without time delay when the current exceeds a predetermined value.",["instantaneous-release","definite-time-delay-over-current-release","making-current-release","reverse-current-release"],["02-13-24"]),
 ("definite-time-delay-over-current-release","Definite time-delay over-current release","3.104.20","",
  "An over-current release that operates after a definite time delay independent of the over-current magnitude.",["over-current-release"],[]),
 ("making-current-release","Making-current release","3.104.18","",
  "A release that operates during a closing operation if the current exceeds a predetermined value.",["over-current-release"],[]),
 ("reverse-current-release","Reverse-current release","3.104.26","",
  "A release that operates when the current reverses direction (d.c. applications).",["over-current-release"],[]),
 ("interlocking-device","Interlocking device","3.104.31","441-16-49",
  "A device that makes the operation of a circuit-breaker dependent on the position or operation of other equipment.",["operating-mechanism"],["02-12-11"]),
 # --- general terms & insulation (3.101) ---
 ("external-insulation","External insulation","3.101.20","",
  "The air insulation and exposed surfaces of solid insulation subject to dielectric stress and atmospheric/external influences.",["internal-insulation","self-restoring-insulation","rated-insulation-level"],[]),
 ("internal-insulation","Internal insulation","3.101.21","",
  "The internal solid, liquid or gaseous insulation not exposed to atmospheric influences.",["external-insulation","rated-insulation-level"],[]),
 ("self-restoring-insulation","Self-restoring insulation","3.101.22","",
  "Insulation that completely recovers its insulating properties after a disruptive discharge.",["non-self-restoring-insulation","external-insulation"],[]),
 ("non-self-restoring-insulation","Non-self-restoring insulation","3.101.23","",
  "Insulation that loses its insulating properties, or does not fully recover them, after a disruptive discharge.",["self-restoring-insulation","internal-insulation"],[]),
 ("isolated-neutral-system","Isolated neutral system","3.101.5","",
  "A system whose neutral has no intentional connection to earth.",["resonant-earthed-system","earthed-neutral-system","earth-fault-factor"],[]),
 ("resonant-earthed-system","Resonant earthed system","3.101.6","",
  "A system earthed through a reactance tuned to the system capacitance (arc-suppression coil).",["isolated-neutral-system","earthed-neutral-system"],[]),
 ("earthed-neutral-system","Earthed neutral system","3.101.7","",
  "A system whose neutral is connected to earth, directly or through a low impedance.",["isolated-neutral-system","earth-fault-factor"],["02-15-01"]),
 ("earth-fault-factor","Earth fault factor","3.101.8","",
  "The ratio of the highest phase-to-earth voltage on a healthy phase during an earth fault to the phase-to-earth voltage without the fault — sets the duty severity.",["earthed-neutral-system","rated-voltage"],[]),
 # --- characteristic quantities (3.105) ---
 ("rated-value","Rated value","3.105.1","441-17-01",
  "A quantity value assigned, generally by the manufacturer, for a specified operating condition of a circuit-breaker.",["circuit-breaker"],[]),
 ("prospective-current","Prospective current","3.105.2","441-17-02",
  "The current that would flow if each pole of the circuit-breaker were replaced by a conductor of negligible impedance.",["prospective-peak-current","rated-short-circuit-breaking-current"],[]),
 ("prospective-peak-current","Prospective peak current","3.105.3","441-17-03",
  "The peak value of the prospective current during the transient period following initiation.",["prospective-current","rated-short-circuit-making-current"],[]),
 ("recovery-voltage","Recovery voltage","3.105","441-17-25",
  "The voltage that appears across the terminals of a circuit-breaker after the breaking of the current — comprising the transient (TRV) and power-frequency components.",["transient-recovery-voltage","restrike","reignition"],[]),
 ("restrike","Restrike","3.105","441-17-45",
  "A resumption of current between the contacts during a breaking operation, 1/4 cycle or more after current zero (significant in capacitive switching).",["reignition","recovery-voltage","restrike-free-circuit-breaker","capacitive-current-switching-test"],[]),
 ("reignition","Reignition","3.105","441-17-46",
  "A resumption of current between the contacts during a breaking operation, less than 1/4 cycle after current zero.",["restrike","recovery-voltage"],[]),
 # --- rated characteristics (clause 4) not already covered ---
 ("rated-peak-withstand-current","Rated peak withstand current","4.6","",
  "The peak current a closed circuit-breaker can withstand, associated with the rated short-time withstand current.",["rated-short-time-withstand-current","rated-short-circuit-making-current"],[]),
 ("rated-single-capacitor-bank-breaking-current","Rated single capacitor bank breaking current","4.107","",
  "The maximum capacitive current a circuit-breaker can break when switching a single capacitor bank.",["rated-back-to-back-capacitor-bank-breaking-current","capacitive-current-switching-test","restrike"],[]),
 ("rated-back-to-back-capacitor-bank-breaking-current","Rated back-to-back capacitor bank breaking current","4.110","",
  "The maximum capacitive current when breaking one of several (parallel) capacitor banks — severe inrush conditions.",["rated-single-capacitor-bank-breaking-current","rated-capacitor-bank-inrush-making-current","capacitive-current-switching-test"],[]),
 ("rated-capacitor-bank-inrush-making-current","Rated capacitor bank inrush making current","4.111","",
  "The peak inrush current the circuit-breaker can make when energising a capacitor bank.",["rated-back-to-back-capacitor-bank-breaking-current"],[]),
 ("rated-line-charging-breaking-current","Rated line-charging breaking current","4.108","",
  "The maximum line-charging (capacitive) current a circuit-breaker can break for an unloaded overhead line.",["rated-cable-charging-breaking-current","capacitive-current-switching-test"],[]),
 ("rated-cable-charging-breaking-current","Rated cable-charging breaking current","4.109","",
  "The maximum cable-charging (capacitive) current a circuit-breaker can break for an unloaded cable.",["rated-line-charging-breaking-current","capacitive-current-switching-test"],[]),
 ("rated-small-inductive-breaking-current","Rated small inductive breaking current","4.106","",
  "The small inductive current (e.g. unloaded transformers, shunt reactors, motors) a circuit-breaker can break without excessive overvoltage.",["magnetizing-and-small-inductive-current-switching-test"],[]),
 ("rated-out-of-phase-breaking-current","Rated out-of-phase breaking current","4.106A","",
  "The current a circuit-breaker can break with the two sides out of phase (up to ~2x phase voltage across it).",["out-of-phase-test","making-and-breaking-capacity"],[]),
 # --- tests (clause 6) ---
 ("dielectric-test","Dielectric test","6.1","",
  "Type tests verifying the rated insulation level (power-frequency, impulse and where applicable switching-impulse withstand).",["type-test","rated-insulation-level","partial-discharge-test"],[]),
 ("radio-interference-voltage-test","Radio interference voltage (RIV) test","6.2","",
  "A dielectric type test measuring the radio-interference voltage produced by the circuit-breaker.",["dielectric-test"],[]),
 ("partial-discharge-test","Partial discharge test","6.1.9","",
  "A test detecting partial discharges in the insulation as an indicator of insulation quality.",["dielectric-test"],[]),
 ("temperature-rise-test","Temperature-rise test","6.3","",
  "A type test verifying that carrying the rated normal current does not exceed the specified temperature-rise limits.",["type-test","rated-normal-current"],[]),
 ("mechanical-and-environmental-test","Mechanical and environmental test","6.101","",
  "Type tests of mechanical endurance and operation under environmental conditions (e.g. temperature, humidity, ice).",["type-test","rated-operating-sequence"],[]),
 ("short-circuit-test","Short-circuit (making and breaking) test","6.102","",
  "Type tests demonstrating the making-and-breaking capacity under short circuit, per the basic test-duties.",["type-test","test-duty","making-and-breaking-capacity","short-circuit-test-procedure"],[]),
 ("short-circuit-test-procedure","Short-circuit test procedure","6.105","",
  "The procedure (quantities, circuits, sequence) for performing the short-circuit making and breaking tests.",["short-circuit-test","test-duty","short-circuit-test-quantities"],[]),
 ("short-circuit-test-quantities","Short-circuit test quantities","6.104","",
  "The applied/recovery voltages, currents and TRV that must be reproduced in short-circuit testing.",["short-circuit-test-procedure","transient-recovery-voltage"],[]),
 ("critical-current-test","Critical-current test","6.107","",
  "Tests at the current giving the longest arcing time (the 'critical' current), often more severe than full-rated current.",["short-circuit-test"],[]),
 ("single-phase-short-circuit-test","Single-phase short-circuit test","6.108","",
  "Short-circuit tests performed on a single pole/phase to represent single-phase fault conditions.",["short-circuit-test"],[]),
 ("short-line-fault-test","Short-line fault test","6.109","",
  "Tests of the breaking capacity under the severe line-side TRV of a short-line fault.",["short-line-fault","transient-recovery-voltage","short-circuit-test"],[]),
 ("capacitive-current-switching-test","Capacitive current switching test","6.111","",
  "Tests of line-/cable-charging and capacitor-bank switching, focused on restrike performance.",["restrike","rated-line-charging-breaking-current","rated-back-to-back-capacitor-bank-breaking-current","restrike-free-circuit-breaker"],[]),
 ("magnetizing-and-small-inductive-current-switching-test","Magnetizing and small inductive current switching test","6.112","",
  "Tests of switching unloaded transformers/reactors, checking overvoltages from current chopping.",["rated-small-inductive-breaking-current"],[]),
 ("out-of-phase-test","Out-of-phase making and breaking test","6.110","",
  "Tests of making/breaking with the two sides out of phase.",["rated-out-of-phase-breaking-current","making-and-breaking-capacity"],[]),
]

def page(e):
    cid,title,clause,iev,desc,see,syms = e
    ref = f"[[iec-56]] {clause}" + (f" (adopts IEV {iev})" if iev else "")
    fm = f"---\nid: {cid}\ntype: concept\ntags: [concept, iec-56, circuit-breaker]\n---\n\n"
    b = f"# {title}\n\n{desc}\n\nDefined/specified in {ref}.\n"
    rel = [f"[[{s}]]" for s in see] + [f"symbol [[{s}]]" for s in syms]
    if rel: b += "\nRelated: " + " · ".join(rel) + "\n"
    return fm+b

for e in E:
    open(os.path.join(CON, e[0]+".md"),"w").write(page(e))

# rebuild the hub's concept index (categorised)
cats = [("Device & types", [e[0] for e in E[0:10]]),
        ("Parts", [e[0] for e in E[10:15]]),
        ("Operation & releases", [e[0] for e in E[15:24]]),
        ("General terms & insulation", [e[0] for e in E[24:32]]),
        ("Characteristic quantities", [e[0] for e in E[32:38]]),
        ("Rated characteristics", ["rated-voltage","rated-insulation-level","rated-frequency","rated-normal-current","rated-short-time-withstand-current","rated-peak-withstand-current","rated-duration-of-short-circuit","rated-short-circuit-breaking-current","rated-short-circuit-making-current","transient-recovery-voltage","rated-operating-sequence","short-line-fault","rated-single-capacitor-bank-breaking-current","rated-back-to-back-capacitor-bank-breaking-current","rated-capacitor-bank-inrush-making-current","rated-line-charging-breaking-current","rated-cable-charging-breaking-current","rated-small-inductive-breaking-current","rated-out-of-phase-breaking-current"]),
        ("Tests & duties", ["type-test","test-duty","making-and-breaking-capacity","dielectric-test","radio-interference-voltage-test","partial-discharge-test","temperature-rise-test","mechanical-and-environmental-test","short-circuit-test","short-circuit-test-procedure","short-circuit-test-quantities","critical-current-test","single-phase-short-circuit-test","short-line-fault-test","capacitive-current-switching-test","magnetizing-and-small-inductive-current-switching-test","out-of-phase-test"]),
        ("Operation", ["operating-mechanism"])]
hub = open(os.path.join(STD,"iec-56.md")).read()
idx = "## Concepts (decomposed per the LLM-Wiki method)\n"
for name, ids in cats:
    idx += f"\n**{name}** — " + " · ".join(f"[[{i}]]" for i in ids) + "\n"
# replace everything from the first "## The device" to "## Related standards"
hub = re.sub(r"## The device.*?(?=## Related standards)", idx + "\n", hub, flags=re.S)
open(os.path.join(STD,"iec-56.md"),"w").write(hub)

print(f"IEC 56: generated {len(E)} concept pages + rebuilt hub index "
      f"({sum(len(ids) for _,ids in cats)} links across {len(cats)} categories).")
