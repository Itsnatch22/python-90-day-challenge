import datetime
import random
import time

# ============================================================
#   ARTEMIS II - INTERACTIVE MISSION SIMULATION
# ============================================================

astronauts = {
    "1": "Christina H. Koch",
    "2": "Victor J. Glover",
    "3": "Jeremy Hansen",
    "4": "Reid Wiseman",
    "5": "All crew",
}

crew_responses = {
    "Christina H. Koch": {
        "default": [
            "Copy that, Mission Control. Systems are stable and the crew is locked in.",
            "Understood. We are focused, on checklist, and enjoying the view when we can.",
            "Received. Orion is treating us well so far.",
        ],
        "status": [
            "Status report from Koch: crew steady, checklists clean, and the cabin feels good.",
            "Koch here. No major surprises on my panel. We are in solid shape.",
        ],
        "joke": [
            "I would tell you a space joke, but I need a little more launch window.",
            "Best joke up here is still the freeze-dried coffee.",
        ],
        "moon": [
            "The Moon looks quiet from here, but the moment feels enormous.",
            "Every pass reminds us why this mission matters.",
        ],
    },
    "Victor J. Glover": {
        "default": [
            "Copy that. We are synced up and ready for the next call.",
            "Understood, Mission Control. Glover here. Team is doing well.",
            "Received loud and clear. Standing by.",
        ],
        "status": [
            "Glover here. Crew rhythm is good, systems are responsive, and confidence is high.",
            "No drama on my board right now. We are where we want to be.",
        ],
        "joke": [
            "Current crew vote says gravity is overrated.",
            "We checked the cabin twice. Still no shortcut to the Moon.",
        ],
        "moon": [
            "This mission feels historic even in the quiet moments.",
            "Hard to overstate what it means to see the Moon getting closer.",
        ],
    },
    "Jeremy Hansen": {
        "default": [
            "Copy that, Mission Control. Hansen here. All systems look nominal.",
            "Understood. Spirits are strong and we are keeping the procedures tight.",
            "Received. Canada would approve of this view.",
        ],
        "status": [
            "Hansen here. Navigation is behaving, the cabin is calm, and the crew is sharp.",
            "We are in good shape and keeping the mission disciplined.",
        ],
        "joke": [
            "If anyone asks, I am billing this as the ultimate window seat.",
            "We have traveled all this way and still cannot find decent espresso.",
        ],
        "moon": [
            "The lunar horizon is incredible. Photographs will not do it justice.",
            "You can feel the weight of history out here.",
        ],
    },
    "Reid Wiseman": {
        "default": [
            "Copy that. Wiseman here. We are doing well up here.",
            "Understood, Mission Control. Orion still has fewer meetings than Houston.",
            "Received loud and clear. Ready for the next step.",
        ],
        "status": [
            "Wiseman here. Vehicle is solid, crew is steady, and nobody has floated away yet.",
            "We are stable. Also, I would like it noted that morale improves when snacks appear.",
        ],
        "joke": [
            "Please advise whether lunar orbit comes with complimentary Wi-Fi.",
            "I still have an unresolved Outlook issue, but otherwise things are great.",
        ],
        "moon": [
            "The Moon is the kind of sight that resets your brain a little.",
            "You spend a lifetime imagining this view, then suddenly it is outside the window.",
        ],
    },
}

STATE_LIMITS = {
    "fuel": (0, 100),
    "hull": (0, 100),
    "morale": (0, 100),
    "risk": (0, 100),
}

state = {}
DELAY_SCALE = 0.2


def reset_state():
    state.clear()
    state.update(
        {
            "fuel": 100,
            "hull": 100,
            "morale": 100,
            "science": 0,
            "risk": 10,
            "phase": "Briefing",
            "commander": None,
            "mission_result": "active",
            "landed": False,
        }
    )


def mission_log(event, delay=1.0, prefix="SYSTEM"):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] [{prefix}] {event}")
    if delay > 0:
        time.sleep(delay * DELAY_SCALE)


def section_break(title):
    print("\n" + "=" * 60)
    print(f"   {title}")
    print("=" * 60 + "\n")
    if DELAY_SCALE > 0:
        time.sleep(0.4 * DELAY_SCALE)


def safe_input(prompt):
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print()
        mission_log("Input interrupted. Using a safe default.", delay=0.4, prefix="INPUT")
        return ""


def menu_choice(prompt, options, default=None):
    while True:
        print(prompt)
        for key, label in options.items():
            print(f"  {key}. {label}")
        raw = safe_input("> ")

        if not raw and default is not None:
            return default

        if raw in options:
            return raw

        print("Invalid selection. Try again.\n")


def clamp_stat(key, value):
    if key not in STATE_LIMITS:
        return value
    low, high = STATE_LIMITS[key]
    return max(low, min(high, value))


def update_stat(key, delta, reason):
    before = state[key]
    after = clamp_stat(key, before + delta)
    state[key] = after
    sign = "+" if after - before >= 0 else ""
    mission_log(
        f"{key.upper()} {before} -> {after} ({sign}{after - before}): {reason}",
        delay=0.3,
        prefix="STATE",
    )


def display_status():
    print(
        f"[STATUS] Fuel: {state['fuel']:>3} | Hull: {state['hull']:>3} | "
        f"Morale: {state['morale']:>3} | Science: {state['science']:>3} | "
        f"Risk: {state['risk']:>3}"
    )


def mission_alive():
    if state["fuel"] <= 0:
        state["mission_result"] = "lost"
        mission_log("Fuel reserves have been exhausted. Mission can no longer continue.", prefix="ALERT")
        return False

    if state["hull"] <= 0:
        state["mission_result"] = "lost"
        mission_log("Critical hull failure. Mission lost.", prefix="ALERT")
        return False

    if state["morale"] <= 0:
        state["mission_result"] = "abort"
        mission_log("Crew morale has collapsed. Mission is forced into an early return profile.", prefix="ALERT")
        return False

    if state["fuel"] < 20:
        mission_log("Fuel reserves are getting tight.", delay=0.4, prefix="CAUTION")
    if state["hull"] < 35:
        mission_log("Hull integrity is lower than mission rules would like.", delay=0.4, prefix="CAUTION")
    if state["morale"] < 35:
        mission_log("Crew morale is trending low. Keep the comms supportive.", delay=0.4, prefix="CAUTION")

    return True


def adjust_risk(delta, reason):
    update_stat("risk", delta, reason)


def phase_title(name):
    state["phase"] = name
    display_status()


def pick_reply_category(message):
    if not message:
        return "default"

    lowered = message.lower()
    if any(word in lowered for word in ("status", "report", "update", "how are you")):
        return "status"
    if any(word in lowered for word in ("joke", "funny", "laugh")):
        return "joke"
    if any(word in lowered for word in ("moon", "lunar", "view", "window")):
        return "moon"
    return "default"


def maybe_boost_morale(message):
    lowered = message.lower()
    if any(word in lowered for word in ("good job", "proud", "great work", "well done", "you got this")):
        update_stat("morale", 2, "Mission Control sent a morale boost")


def astronaut_reply(name, message=None):
    category = pick_reply_category(message or "")
    pool = crew_responses[name].get(category) or crew_responses[name]["default"]
    reply = random.choice(pool)

    if category == "status":
        reply += (
            f" Current numbers from up here look like fuel {state['fuel']}, "
            f"hull {state['hull']}, morale {state['morale']}."
        )

    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] [{name.upper()}] {reply}")
    if DELAY_SCALE > 0:
        time.sleep(0.5 * DELAY_SCALE)


def speak_to_crew(choice, message):
    maybe_boost_morale(message)

    if choice == "5":
        mission_log("Broadcasting to all crew...", delay=0.4, prefix="COMMS")
        for key, name in astronauts.items():
            if key != "5":
                astronaut_reply(name, message)
        return

    name = astronauts.get(choice)
    if name and name != "All crew":
        astronaut_reply(name, message)
    else:
        print("Invalid selection.\n")


def configure_simulation():
    global DELAY_SCALE

    section_break("MISSION SETUP")
    mission_log("Welcome to the Artemis II interactive mission simulator.", delay=0.6, prefix="NASA")
    mode = menu_choice(
        "Pick a pacing mode:",
        {
            "1": "Cinematic (slow and dramatic)",
            "2": "Fast (recommended)",
            "3": "Instant (almost no waiting)",
        },
        default="2",
    )

    DELAY_SCALE = {"1": 1.0, "2": 0.2, "3": 0.0}[mode]

    commander = menu_choice(
        "Choose your primary crew contact:",
        {
            "1": "Christina H. Koch",
            "2": "Victor J. Glover",
            "3": "Jeremy Hansen",
            "4": "Reid Wiseman",
        },
        default="1",
    )
    state["commander"] = astronauts[commander]
    mission_log(f"Primary crew contact set to {state['commander']}.", delay=0.4, prefix="COMMS")


def mission_brief():
    section_break("MISSION BRIEF")
    mission_log("Mission objectives: survive, manage risk, and bring home useful science.", prefix="NASA")
    mission_log("Your calls will change fuel, hull, morale, science, and mission risk.", prefix="NASA")
    mission_log("Clean flying is good. Bold flying can pay off. Reckless flying usually does not.", prefix="NASA")
    display_status()


def phase_prelaunch():
    section_break("PHASE 1 - PRE-LAUNCH CHECKS")
    phase_title("Pre-Launch")
    mission_log("Ground crews complete their final walkaround of the launch stack.", prefix="LAUNCH")
    mission_log("The crew is strapped into Orion and waiting on your call.", prefix="LAUNCH")

    choice = menu_choice(
        "Final go/no-go decision:",
        {
            "1": "Order one extra systems sweep before launch",
            "2": "Stay on schedule and launch on the planned window",
        },
        default="1",
    )

    if choice == "1":
        mission_log("Extra diagnostics reveal a minor sensor mismatch and correct it.", prefix="LAUNCH")
        update_stat("fuel", -2, "Additional ground conditioning before launch")
        adjust_risk(-8, "Extra systems sweep reduced launch uncertainty")
        update_stat("morale", -1, "Crew waited a bit longer on the pad")
    else:
        mission_log("You keep the timeline tight and the launch team likes the confidence.", prefix="LAUNCH")
        adjust_risk(8, "Skipped the extra sweep")
        update_stat("morale", 2, "Crew appreciates the decisive call")

    return mission_alive()


def phase_launch():
    section_break("PHASE 2 - LAUNCH SEQUENCE")
    phase_title("Launch")
    mission_log("Initiating terminal countdown sequence.", prefix="LAUNCH")

    for i in range(10, 0, -1):
        print(f"         T-minus {i}...")
        if DELAY_SCALE > 0:
            time.sleep(0.3 * DELAY_SCALE)

    mission_log("LIFTOFF! Artemis II clears the tower.", delay=1.2, prefix="LAUNCH")
    mission_log("The stack rides a column of fire into a clear morning sky.", prefix="LAUNCH")

    event = random.choice(["vibration", "debris", "comms"])

    if event == "vibration":
        mission_log("Unexpected engine vibration appears during ascent.", prefix="ALERT")
        choice = menu_choice(
            "How do you respond?",
            {
                "1": "Throttle back briefly and smooth the ride",
                "2": "Hold full power and punch through it",
            },
            default="1",
        )
        if choice == "1":
            update_stat("fuel", -4, "Temporary throttle adjustment during ascent")
            adjust_risk(-6, "Vibration damped early")
        else:
            update_stat("hull", -6, "Vehicle took a rougher ride through ascent")
            adjust_risk(10, "You accepted a more aggressive climb profile")
            update_stat("morale", 2, "The crew enjoyed the bold move more than they should admit")

    elif event == "debris":
        mission_log("Tracking flags a debris fragment crossing near the ascent corridor.", prefix="ALERT")
        choice = menu_choice(
            "How do you respond?",
            {
                "1": "Roll the vehicle to reduce exposure",
                "2": "Keep attitude stable and trust the corridor",
            },
            default="1",
        )
        if choice == "1":
            update_stat("fuel", -3, "Ascent roll maneuver")
            adjust_risk(-5, "Reduced potential strike exposure")
        else:
            update_stat("hull", -4, "A tiny fragment clips external material")
            adjust_risk(8, "You accepted the cleaner but riskier line")

    else:
        mission_log("Voice comms flicker during max Q.", prefix="ALERT")
        choice = menu_choice(
            "What is the call?",
            {
                "1": "Patch through backup comms immediately",
                "2": "Stay focused on ascent and fix comms after staging",
            },
            default="1",
        )
        if choice == "1":
            update_stat("morale", -1, "The crew worked the backup procedure under pressure")
            adjust_risk(-4, "Communications restored early")
        else:
            adjust_risk(6, "Temporary comms uncertainty accepted")
            update_stat("morale", 1, "Crew kept the priority on flying the vehicle")

    mission_log("Core stage separation confirmed.", prefix="LAUNCH")
    mission_log("Orion is free and stable in low Earth orbit.", prefix="LAUNCH")
    return mission_alive()


def phase_earth_orbits():
    section_break("PHASE 3 - EARTH ORBIT CHECKS")
    phase_title("Earth Orbit")
    mission_log("Two Earth orbits begin for system verification and crew adjustment.", prefix="ORBIT")

    choice = menu_choice(
        "Pick the orbit priority:",
        {
            "1": "Run a deep systems scan",
            "2": "Capture Earth imagery and outreach footage",
            "3": "Protect crew rest and adapt to microgravity",
        },
        default="1",
    )

    if choice == "1":
        update_stat("science", 4, "Collected detailed vehicle performance data")
        adjust_risk(-6, "Deep systems scan tightened mission confidence")
        update_stat("morale", -1, "Crew stayed busy instead of enjoying the view")
    elif choice == "2":
        update_stat("science", 8, "Captured outreach imagery and observation footage")
        update_stat("morale", 4, "Crew took a breath and enjoyed the mission")
    else:
        update_stat("morale", 8, "Crew adapted well to orbit")
        update_stat("science", 2, "Collected routine adaptation notes")
        adjust_risk(2, "Deferred some lower-priority scans")

    mission_log("Navigation lock for translunar injection is ready.", prefix="ORBIT")
    return mission_alive()


def phase_trans_lunar():
    section_break("PHASE 4 - TRANS-LUNAR INJECTION")
    phase_title("Trans-Lunar Injection")
    mission_log("The service module is ready for the burn that sends Orion toward the Moon.", prefix="TLI")

    choice = menu_choice(
        "Choose the burn profile:",
        {
            "1": "Fuel-efficient burn with tighter margins",
            "2": "Nominal balanced burn",
            "3": "Conservative burn with extra correction room",
        },
        default="2",
    )

    if choice == "1":
        update_stat("fuel", 5, "Fuel-efficient translunar profile")
        adjust_risk(7, "Margins got tighter")
    elif choice == "2":
        mission_log("Nominal burn profile selected. Clean and balanced.", prefix="TLI")
    else:
        update_stat("fuel", -6, "Extra propellant used to widen correction room")
        adjust_risk(-8, "Conservative burn profile improved trajectory confidence")

    mission_log("Trans-lunar injection burn is underway.", prefix="TLI")
    for i in range(6, 0, -1):
        print(f"         Burn minute {i}...")
        if DELAY_SCALE > 0:
            time.sleep(0.2 * DELAY_SCALE)

    mission_log("Burn complete. Artemis II is outbound.", prefix="TLI")

    event = random.choice(["micrometeoroid", "solar_flare"])
    if event == "micrometeoroid":
        mission_log("A micrometeoroid field warning appears on the route model.", prefix="ALERT")
        choice = menu_choice(
            "How do you handle it?",
            {
                "1": "Make a small avoidance burn",
                "2": "Rotate the vehicle and ride it out",
            },
            default="1",
        )
        if choice == "1":
            update_stat("fuel", -5, "Avoidance burn around debris field")
            adjust_risk(-7, "Reduced strike probability")
        else:
            update_stat("hull", -5, "A few tiny impacts pepper the outer shell")
            update_stat("science", 3, "Crew logged useful observations on the event")
            adjust_risk(5, "Accepted a rougher transit")
    else:
        mission_log("Solar activity spikes. Radiation procedures are on the table.", prefix="ALERT")
        choice = menu_choice(
            "Your call:",
            {
                "1": "Put the crew into the best-shielded configuration",
                "2": "Stay on nominal operations and monitor closely",
            },
            default="1",
        )
        if choice == "1":
            update_stat("morale", -2, "Crew endured a cramped shelter period")
            adjust_risk(-6, "You played the radiation weather carefully")
        else:
            update_stat("morale", 2, "Crew appreciated the calm response")
            adjust_risk(8, "You accepted more uncertainty during solar activity")

    return mission_alive()


def phase_comms():
    section_break("PHASE 5 - MISSION CONTROL COMMUNICATIONS")
    phase_title("Crew Comms")
    mission_log("Open channel to Artemis II. The crew is live.", prefix="COMMS")
    mission_log("Tip: ask for a status report, a joke, or what the Moon looks like.", prefix="COMMS")

    while True:
        print("\nWho do you want to speak with?")
        for key, name in astronauts.items():
            print(f"  {key}. {name}")
        print("  0. Close comms channel\n")

        choice = safe_input("Mission Control - Select crew member: ")
        if choice == "0":
            mission_log("Closing comms channel.", prefix="COMMS")
            break

        if choice not in astronauts:
            print("Invalid selection.\n")
            continue

        message = safe_input("Mission Control: ")
        if not message:
            print("No message entered.\n")
            continue

        speak_to_crew(choice, message)

    return mission_alive()


def phase_lunar_orbit():
    section_break("PHASE 6 - LUNAR ORBIT OPERATIONS")
    phase_title("Lunar Operations")
    mission_log("The Moon fills the forward windows as Orion approaches the lunar encounter.", prefix="MOON")

    choice = menu_choice(
        "Choose the lunar objective:",
        {
            "1": "Attempt a lower, riskier pass for bonus science",
            "2": "Keep a safer mapping profile",
            "3": "Prioritize crew photography and morale",
        },
        default="2",
    )

    if choice == "1":
        update_stat("science", 12, "Low pass produced strong observation data")
        update_stat("hull", -4, "Low-altitude operations stressed the vehicle a little")
        adjust_risk(9, "Close lunar operations leave less margin")
    elif choice == "2":
        update_stat("science", 7, "Mapping profile delivered clean survey data")
        adjust_risk(-3, "Safer orbital operations around the Moon")
    else:
        update_stat("morale", 10, "Crew got a once-in-a-lifetime window session")
        update_stat("science", 4, "Crew still captured useful imagery")
        adjust_risk(2, "You traded some discipline for wonder")

    mission_log("Lunar flyby complete. Artemis II begins setting up for the ride home.", prefix="MOON")
    return mission_alive()


def phase_return():
    section_break("PHASE 7 - RETURN TO EARTH")
    phase_title("Return")
    mission_log("Trans-Earth injection is ready. Time to come home.", prefix="RETURN")

    choice = menu_choice(
        "Choose the return strategy:",
        {
            "1": "Fastest return corridor with tighter margins",
            "2": "Nominal return profile",
            "3": "Spend extra fuel to widen the re-entry corridor",
        },
        default="2",
    )

    if choice == "1":
        update_stat("fuel", 4, "Saved fuel on the aggressive return profile")
        adjust_risk(8, "Fast corridor increased re-entry sensitivity")
    elif choice == "2":
        mission_log("Nominal return profile selected.", prefix="RETURN")
    else:
        update_stat("fuel", -6, "Extra correction burn on the ride home")
        adjust_risk(-7, "Wider corridor lowered re-entry risk")

    mission_log("Orion is inbound. The Pacific recovery zone is waiting.", prefix="RETURN")

    reentry_pressure = 0.12 + (state["risk"] / 120.0) + ((100 - state["hull"]) / 250.0)
    if random.random() < reentry_pressure:
        mission_log("Re-entry corridor starts drifting hotter than planned.", prefix="ALERT")
        choice = menu_choice(
            "Last-minute re-entry call:",
            {
                "1": "Command a small correction burn",
                "2": "Hold attitude and trust the current corridor",
            },
            default="1",
        )
        if choice == "1":
            update_stat("fuel", -4, "Late re-entry correction burn")
            adjust_risk(-5, "You pulled the corridor back toward nominal")
        else:
            update_stat("hull", -10, "Heat load rises on the way down")
            adjust_risk(10, "You rode a hotter corridor through entry")

    mission_log("Service module separation confirmed.", prefix="RETURN")
    mission_log("Plasma blackout begins as Orion hits the upper atmosphere.", prefix="RETURN")
    mission_log("Signal reacquired. Drogues deployed, then mains.", prefix="RETURN")

    if state["risk"] >= 85 or state["hull"] <= 10:
        state["mission_result"] = "hard_landing"
        update_stat("hull", -8, "Rough splashdown under damaged conditions")
        mission_log("Splashdown is rough, but the capsule remains intact.", prefix="RETURN")
    else:
        state["mission_result"] = "success"
        mission_log("Splashdown confirmed. Recovery teams report a clean return.", prefix="RETURN")

    state["landed"] = True
    return mission_alive()


def mission_grade(score):
    if score >= 330:
        return "Legendary"
    if score >= 280:
        return "Excellent"
    if score >= 220:
        return "Solid"
    if score >= 170:
        return "Scrappy"
    return "Barely Made It"


def mission_complete():
    section_break("MISSION COMPLETE")
    display_status()

    base_score = (
        state["fuel"]
        + state["hull"]
        + state["morale"]
        + (state["science"] * 4)
        + (100 - state["risk"])
    )

    if state["mission_result"] == "lost":
        base_score -= 140
    elif state["mission_result"] == "abort":
        base_score -= 70
    elif state["mission_result"] == "hard_landing":
        base_score -= 25

    score = max(0, int(base_score))
    grade = mission_grade(score)

    if state["mission_result"] == "lost":
        mission_log("The mission ended before a safe return could be achieved.", prefix="NASA")
    elif state["mission_result"] == "abort":
        mission_log("The crew survived, but the mission had to be cut short.", prefix="NASA")
    elif state["mission_result"] == "hard_landing":
        mission_log("The crew is home after a rough but survivable return.", prefix="NASA")
    else:
        mission_log("Artemis II returns home with crew and data intact.", prefix="NASA")

    mission_log(f"Primary crew contact this run: {state['commander']}.", prefix="NASA")
    mission_log(f"Mission score: {score}", prefix="NASA")
    mission_log(f"Mission rating: {grade}", prefix="NASA")

    print("\n" + "=" * 60)
    print("   Thanks for flying Artemis II.")
    print("   Try another run and make different calls to chase a better ending.")
    print("=" * 60 + "\n")


def main():
    reset_state()
    configure_simulation()
    mission_brief()

    phases = [
        phase_prelaunch,
        phase_launch,
        phase_earth_orbits,
        phase_trans_lunar,
        phase_comms,
        phase_lunar_orbit,
        phase_return,
    ]

    for phase in phases:
        if not phase():
            break

    mission_complete()


if __name__ == "__main__":
    main()
