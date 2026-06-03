---
title: Bike Purchase Howto's
jupytext:
    formats: md:myst
    text_representation:
        extension: .md
        format_name: myst
kernelspec:
    display_name: python3
    language: python
    name: python3
mystnb:
    render_markdown_format: myst
---


# Bike purchase Howto's

These are excerpts from AI chatbot, helping me choose my next bike. 

```{tip}
 🛠️ A Casual Conversation: Choosing My Next Bike (And What I Learned)

> *"A curious cyclist trying to level up — and all the good stuff that came from asking the right questions."*
```

---

## 🚲 The Situation

I wanted a fast, durable bike that could handle occasional loads and rough roads, and I was stuck between two models: the **Giant FastRoad 1** and the **FastRoad SL 1**. What started as a simple A vs B comparison quickly evolved into a deep dive — gearing, cadence, bike geometries, gravel vs road options, warranties, and even internal cable routing.

Here’s how the conversation unfolded. It’s not a polished buyer’s guide — it’s a record of a real Q&A. You might find it useful if you're in a similar spot.

---

## 🤔 Initial Comparison: FastRoad 1 vs FastRoad SL 1

```{div}
:class: user-bubble

**Q:** What are the key differences in specs and reliability?
```

```{div}
:class: ai-bubble

**A:**

- **FastRoad SL 1**:

  - 50/34T chainrings, 11-speed Shimano 105 drivetrain
  - Lighter ALUXX SL frame (\~10.2 kg)
  - Internal cable routing

- **FastRoad 1**:

  - 50/34T, 10-speed Shimano Tiagra
  - Standard ALUXX frame (\~10.5–10.8 kg)
  - External cable routing

**Verdict:** SL 1 is a bit lighter and has a higher-end drivetrain. Both are good in terms of durability.

```
---

## ⚙️ Speed vs Cadence: Where Do I Stand?

```{div}
:class: user-bubble

**Q:** I currently ride a 700c, 42T crankset, 7-speed Shimano Tourney setup. I can hit 39 km/h — what cadence does that imply?

```

```{div}
:class: ai-bubble

**A:** We modeled it:

- With a 42/13T gear at \~95–100 RPM, you hit 39 km/h
- Confirmed with speed-vs-cadence plots (see below!)

### 📊 Plot: Speed vs Cadence for Current Bike

(*Your current setup vs potential upgrade scenarios*)



### ⚖️ Formula Used to Estimate Cadence:

Cadence is calculated using:

Cadence (RPM) = (Speed * 1000) / (Wheel Circumference * Gear Ratio * 60)

Where:

- Speed in km/h
- Wheel circumference in meters (700x28c ≈ 2.096 m)
- Gear ratio = front\_chainring / rear\_cog

```
## ♻️ What Happens With a 50T Chainring?

```{div}
:class: user-bubble

**Q:** What if I switch to 50/11T like the FastRoad SL 1? How much faster can I go at the same cadence?

```

```{div}
:class: ai-bubble

**A:**

- At 96 RPM (your estimated peak), you’ll hit **\~55 km/h** with a 50/11T
- That’s \~16 km/h faster than current setup, **without spinning faster**

### 📊 Plot: Speed vs Cadence (Including FastRoad SL 1)

### 🔢 Formula Used to Estimate Speed:

Speed (km/h) = Cadence * Gear Ratio * Wheel Circumference * 60 / 1000

---

## 🤭 Exploring Drop-Bar Alternatives

I also wanted drop-bar options with:

- Crank size ≥ 50T
- 10+ speeds
- Rear rack option (even if occasional)
- Slightly wider tires for rough roads

### 📋 Models Considered

| Model                    | Gearing                | Weight    | Notes                                        |
| ------------------------ | ---------------------- | --------- | -------------------------------------------- |
| **Giant Contend AR 3**   | 50/34, 11-34 (2x8)     | \~10.4 kg | Endurance geometry, rack mounts, disc brakes |
| **Trek Domane AL 4**     | 50/34, 11-speed Tiagra | \~10.3 kg | Hidden routing, full rack/fender mounts      |
| **Cannondale Synapse 1** | 50/34, 11-speed        | \~10.2 kg | Alloy, endurance ride, rack-ready            |
| **Genesis CDA 20**       | 46/30, 9-speed Sora    | \~11.4 kg | External cables, steel frame, touring-ready  |

---

## 🏷️ Warranty Considerations

| Brand          | Frame Warranty | Notes                            |
| -------------- | -------------- | -------------------------------- |
| **Giant**      | Lifetime       | For alloy frames, original owner |
| **Trek**       | Lifetime       | Alloy & carbon included          |
| **Cannondale** | Lifetime       | Must register within 30 days     |
| **Genesis**    | Lifetime       | Steel and alloy frames covered   |

All offer solid lifetime warranties for original owners. ✅

---

## 🔧 Internal vs External Cabling

| Type         | Pros                             | Cons                                |
| ------------ | -------------------------------- | ----------------------------------- |
| **Internal** | Clean look, aero, protected      | Harder to service, costlier repairs |
| **External** | Easier maintenance, DIY-friendly | Exposed, messier appearance         |

If you value aesthetics and don't mind shop servicing: internal. If you're more hands-on or going long-distance: external.

---

## 📃 Racks & Load Handling

Even the performance models like FastRoad SL 1 support:

- Rear rack mounts on seatstays/dropouts
- Fender mounts

✅ All shortlisted bikes support rear rack use — suitable for occasional loads.


## 📊 Sizing: What Fits a 171 cm Rider?

| Model                       | Suggested Size |
| --------------------------- | -------------- |
| **Giant FastRoad (1/SL 1)** | Small          |
| **Giant Contend AR 3**      | Small          |
| **Trek Domane AL 4**        | 52 cm          |
| **Cannondale Synapse**      | 51 or 54 cm    |
| **Genesis CDA 20**          | Small / 52 cm  |

Try before buying if possible — some brands size large (like Giant).

---

## 🧠 Final Takeaways

- ✅ **FastRoad SL 1** offers better speed at same cadence, lighter frame, and mounts.
- 🛠️ **Genesis CDA 20** shines for self-maintainers, simplicity, and steel comfort.
- 📏 At 171 cm, you're comfortably in Small/52 territory across brands.
- 💡 All options allow some form of light touring or rack setup.

```

---

## 📂 Appendix: Cadence to Speed Code (Python)

```{code-cell}

import matplotlib.pyplot as plt
import numpy as np

# Cadence and gear setup
cadences = np.arange(40, 130, 5)
wheel_circumference_m = 2.096  # 700x28c approx

# Gearing options
gear_ratios = {
    "42/13": 42/13,
    "42/12": 42/12,
    "50/11": 50/11
}

# Plot speed vs cadence
for label, ratio in gear_ratios.items():
    speed_kmh = cadences * ratio * wheel_circumference_m * 60 / 1000
    plt.plot(cadences, speed_kmh, label=f"{label} (ratio {ratio:.2f})")

plt.title("Speed vs Cadence")
plt.xlabel("Cadence (RPM)")
plt.ylabel("Speed (km/h)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
```

---

## 📢 Share the Ride

I hope this conversation helps someone else starting their cycling journey — feel free to fork it or reuse it! 🚴‍♂️

*Got suggestions or corrections? Open a pull request on GitHub or reach out on the discussions tab!*

