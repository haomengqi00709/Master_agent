---
id: temperature-classes-t1-t6
type: concept
tags: [concept, iec-79-4, ex, ignition-temperature]
---

# Temperature classes T1–T6 (relationship to ignition temperature)

The bridge between the [[ignition-temperature]] measured by [[iec-79-4]] and the
**explosion-protection framework** for Ex apparatus. The IEC 79 family classifies
electrical apparatus by the **maximum surface temperature** it may attain (IEC
79-8, "Classification of maximum surface temperatures"), into six **temperature
classes**:

| Class | Max. surface temperature of apparatus |
|-------|----------------------------------------|
| **T1** | 450 °C |
| **T2** | 300 °C |
| **T3** | 200 °C |
| **T4** | 135 °C |
| **T5** | 100 °C |
| **T6** | 85 °C |

The safety rule is simple: **the apparatus's maximum surface temperature (its
T-class limit) must stay below the [[ignition-temperature|ignition temperature]]
of the gas/vapour it may meet.** IEC 79-4 supplies that gas-side number; IEC 79-8
sets the apparatus-side limit; together they let a designer pick apparatus of a
T-class low enough for the hazardous substances present. A gas with a low ignition
temperature (e.g. **carbon disulphide 102 °C** in [[ignition-temperature-data-list]])
demands a high class such as **T5/T6**, whereas a high-ignition gas (e.g. benzene
560 °C) tolerates **T1**.

This is why the type-of-protection pages of the sibling repair standard
[[iec-79-19]] repeatedly insist that repairs **must not infringe the temperature
class / temperature classification** on the certification label — see
[[type-of-protection-e]], [[type-of-protection-n]], [[type-of-protection-p]] and
[[enclosures]] (a rewind or a part substitution that raises surface temperature
could violate the class). The [[factors-affecting-ignition-temperature|impurity
caution]] folded from amendment [[iec-79-4a]] matters here too: trichlorosilane's
drop from 230 °C to 185 °C on ageing could move it to a more onerous class.

> Note: the T-class boundary values above are the IEC 79-8 classification limits
> referenced by this family; IEC 79-4 itself only measures the gas ignition
> temperature that the classification consumes.

**Related:** [[ignition-temperature]] · [[ignition-temperature-data-list]] · [[iec-79-19]] · [[type-of-protection-e]] · [[type-of-protection-n]] · [[type-of-protection-p]] · [[iec-79-4]]
