---
name: veo-camera-movement
description: Transform natural language camera movement descriptions into professional Veo 3.1 video prompts using industry-standard cinematography terminology. Use when users request video generation with camera movements, describe shots using vague language (e.g., "camera gets closer", "camera spins"), need guidance on which camera movement serves their creative intent, or want to learn film terminology. Handles all movement types from static shots to complex movements like dolly zoom, FPV drone, snorricam, and bullet time. Outputs complete paste-ready Veo prompts following the five-part formula: [Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance].
---

# Veo 3.1 Camera Movement Prompting Skill

## Overview

This skill transforms natural language camera movement descriptions into professional, technically precise Veo 3.1 video prompts. It bridges the gap between creative vision and cinematic execution by translating casual descriptions into industry-standard terminology while educating users on proper film language.

**Use this skill when:**
- Users request video generation with camera movement
- Users describe shots using vague or non-technical language
- Users need guidance on which camera movement best serves their creative intent
- Users want to learn professional cinematography terminology

## Core Methodology

### The Veo 3.1 Prompt Formula

Every output must follow this five-part structure:

```
[Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance]
```

**Component Breakdown:**

1. **Cinematography**: Camera movement, shot type, lens characteristics, framing
2. **Subject**: Detailed description of the primary focus (character, object, scene element)
3. **Action**: What the subject is doing in the frame
4. **Context**: Environment, setting, background elements, spatial relationships
5. **Style & Ambiance**: Mood, lighting, aesthetic references, temporal quality, film stock characteristics

### Audio Integration

Veo 3.1 generates synchronized audio. Include when relevant:
- **Dialogue**: Use quotation marks (e.g., Character says, "We need to leave now.")
- **SFX**: Describe specific sounds (e.g., SFX: thunder rumbles in the distance)
- **Ambient**: Define background soundscape (e.g., Ambient noise: bustling city traffic and distant sirens)

## Interaction Pattern

### Step 1: Intake
User describes their desired shot in natural language. Claude identifies:
- Core camera movement intent
- Subject matter
- Emotional/narrative goal
- Any ambiguities requiring clarification

### Step 2: Clarify (Maximum 1-2 Questions)
If the movement intent is ambiguous, ask ONE targeted question offering 2-3 specific options:

**Example:**
> "You want to move closer to the subject. Which approach serves your narrative better?
> - **Dolly in**: Smooth, deliberate push that builds intensity
> - **Crash zoom in**: Rapid, jarring zoom that creates sudden emphasis or shock
> - **Super dolly in**: Aggressive, fast push for dramatic impact"

### Step 3: Construct Full Veo Prompt
Deliver:
1. Complete Veo 3.1 prompt following the five-part formula
2. Brief technical explanation of the camera movement chosen (1-2 sentences)
3. Why this movement serves the creative intent

## Camera Movement Reference Library

### Category 1: Static & Minimal Movement

**Static**
- Definition: Camera locked on tripod, no movement
- Use for: Dialogue-heavy scenes, focused performances, deliberate composition
- Emotional effect: Stability, objectivity, allows subject to command frame

**Dutch Angle**
- Definition: Camera tilted on its roll axis, creating diagonal horizon
- Use for: Psychological unease, disorientation, instability, villainy
- Emotional effect: Tension, wrongness, imbalance

**Focus Change / Rack Focus**
- Definition: Shift focus from foreground to background (or vice versa) without camera movement
- Use for: Revealing new information, shifting attention, narrative transitions
- Emotional effect: Discovery, realization, redirected attention

### Category 2: Push/Pull Movements

**Dolly In**
- Definition: Camera moves forward toward subject on tracks or stabilizer
- Use for: Building intensity, intimacy, revealing emotion
- Emotional effect: Engagement, focus, intensification

**Dolly Out / Pull Out**
- Definition: Camera moves backward away from subject
- Use for: Revealing context, isolation, emotional distance
- Emotional effect: Detachment, revelation, loneliness

**Super Dolly In**
- Definition: Aggressive, rapid forward dolly movement
- Use for: Sudden dramatic emphasis, action sequences, heightened intensity
- Emotional effect: Impact, urgency, explosive energy

**Super Dolly Out**
- Definition: Fast backward dolly movement
- Use for: Rapid reveals, shocked reactions, dramatic scale shift
- Emotional effect: Surprise, scale, expanding scope

**Zoom In**
- Definition: Lens focal length change to magnify subject without camera movement
- Use for: Gradual emphasis, artificial intensification, retro aesthetic
- Emotional effect: Artificial focus (can feel unnatural or stylized)

**Zoom Out**
- Definition: Lens focal length change to de-magnify subject
- Use for: Context reveal, de-emphasis, pulling back perspective
- Emotional effect: Distance, context, diminishment

**Crash Zoom In**
- Definition: Extremely rapid zoom into subject
- Use for: Sudden realization, shock, comedic emphasis
- Emotional effect: Jarring attention, surprise, urgency

**Crash Zoom Out**
- Definition: Extremely rapid zoom out from subject
- Use for: Shock reveal, sudden context shift, comedic timing
- Emotional effect: Disorienting expansion, dramatic reveal

**Rapid Zoom In / Rapid Zoom Out**
- Definition: Fast but not crash-speed zoom movement
- Use for: Emphasis without extreme jarring effect, dynamic energy
- Emotional effect: Heightened attention, energy, stylization

**Dolly Zoom In / Dolly Zoom Out** (Vertigo Effect)
- Definition: Camera dollies one direction while zooming opposite direction
- Use for: Psychological unease, supernatural forces, internal conflict, realization
- Emotional effect: Disorientation, warped perception, surreal dread

**Double Dolly**
- Definition: Two simultaneous dolly movements (often subject and camera)
- Use for: Complex spatial relationships, parallel action, enhanced dynamism
- Emotional effect: Layered motion, complexity, visual sophistication

**YoYo Zoom**
- Definition: Rapid zoom in then out (or vice versa) in quick succession
- Use for: Disorientation, emphasis with retreat, comedic timing
- Emotional effect: Uncertainty, playfulness, visual stutter

**Eating Zoom**
- Definition: Slow zoom in during eating/consumption activity
- Use for: Character focus during dining scenes, intimate moments
- Emotional effect: Intimacy, focus, mundane elevation

### Category 3: Lateral Movements

**Pan Left / Pan Right**
- Definition: Camera rotates horizontally on fixed axis
- Use for: Following action, revealing environment, connecting spaces
- Emotional effect: Continuity, exploration, spatial relationship

**Whip Pan**
- Definition: Extremely fast pan creating motion blur
- Use for: Transitions, sudden attention shifts, energetic pacing
- Emotional effect: Urgency, disorientation, kinetic energy

**Arc Left / Arc Right**
- Definition: Camera moves in circular path around stationary subject
- Use for: Revealing subject from multiple angles, building tension, showcasing
- Emotional effect: Examination, menace, dynamic presentation

**360 Orbit**
- Definition: Complete circular movement around subject
- Use for: Full subject reveal, contemplation, hero moments, disorientation
- Emotional effect: Comprehensive view, isolation, showcase

**Dolly Left / Dolly Right** (Truck)
- Definition: Camera moves laterally parallel to subject
- Use for: Following lateral action, maintaining distance while moving
- Emotional effect: Parallel observation, tracking, containment

**Lazy Susan**
- Definition: Subject rotates on turntable while camera remains fixed
- Use for: Product showcase, character reveal, stylized presentation
- Emotional effect: Examination, display, artificiality

### Category 4: Vertical Movements

**Tilt Up**
- Definition: Camera pivots upward on fixed axis
- Use for: Revealing scale, awe, tall subjects, power dynamics
- Emotional effect: Grandeur, intimidation, ascension

**Tilt Down**
- Definition: Camera pivots downward on fixed axis
- Use for: Descending reveals, diminishment, grounding
- Emotional effect: Descent, vulnerability, discovery

**Crane Up**
- Definition: Camera physically rises vertically
- Use for: Establishing scale, god's-eye perspective, epic reveals
- Emotional effect: Elevation, grandeur, omniscience

**Crane Down**
- Definition: Camera physically descends vertically
- Use for: Intimate entry, descent into setting, focusing in
- Emotional effect: Grounding, intimacy, descent

**Jib Up / Jib Down**
- Definition: Smaller-scale vertical movement using jib arm
- Use for: Subtle vertical shifts, reveals, dynamic framing adjustments
- Emotional effect: Light elevation changes, subtle dynamics

**Crane Over The Head**
- Definition: Crane movement that arcs up and over subject
- Use for: Dynamic reveals, following action over obstacles, showmanship
- Emotional effect: Fluid spectacle, comprehensive view, athleticism

**Overhead / Bird's Eye**
- Definition: Camera positioned directly above subject looking down
- Use for: God's perspective, vulnerability, pattern reveal, isolation
- Emotional effect: Omniscience, smallness, exposure

**Incline**
- Definition: Camera rises at an angle while moving forward
- Use for: Heroic reveals, ascending perspectives, upward journey
- Emotional effect: Elevation, triumph, ascension

### Category 5: Complex & Specialty Movements

**Snorricam**
- Definition: Camera rigidly mounted to subject, background moves while subject stays centered
- Use for: Subjective psychological states, intoxication, dissociation, intense POV
- Emotional effect: Disorientation, internal focus, altered states

**Robo Arm**
- Definition: Programmable robotic arm creates impossible, repeatable moves
- Use for: Impossible angles, precise choreography, superhuman movement
- Emotional effect: Otherworldly, precise, mechanical perfection

**Bullet Time**
- Definition: Time appears frozen while camera moves around subject (array camera simulation)
- Use for: Dramatic pause, action highlight, superhuman moments
- Emotional effect: Time suspension, emphasis, spectacular pause

**3D Rotation**
- Definition: Camera rotates around multiple axes simultaneously
- Use for: Disorientation, impossible perspectives, supernatural elements
- Emotional effect: Spatial confusion, unreality, complexity

**FPV Drone**
- Definition: Fast, agile first-person drone flight through spaces
- Use for: Immersive flight, chasing, impossible navigation through tight spaces
- Emotional effect: Speed, freedom, immersion, kinetic thrill

**Flying Cam Transition**
- Definition: Smooth flight-like movement transitioning between spaces
- Use for: Scene transitions, impossible moves, fluid connection
- Emotional effect: Seamlessness, magic, fluidity

**Through Object In / Through Object Out**
- Definition: Camera appears to pass through solid object (digital effect)
- Use for: Transitions, impossible movement, visual trickery
- Emotional effect: Magic, impossibility, fluid transition

**Hyperlapse**
- Definition: Time-lapse with camera movement through space
- Use for: Journey compression, time passage with spatial change
- Emotional effect: Temporal and spatial compression, journey

**Timelapse (Human / Landscape / Glam)**
- Definition: Accelerated time passage with static camera
- Use for: Time passage, transformation, process reveal
- Human: Crowds, activity flow
- Landscape: Weather, light changes, natural cycles
- Glam: Beauty reveals, preparation montages
- Emotional effect: Time's passage, transformation, rhythm

### Category 6: Organic & Handheld

**Handheld**
- Definition: Camera operator holds camera without stabilization
- Use for: Documentary feel, intimacy, urgency, realism
- Emotional effect: Immediacy, authenticity, instability

**Wiggle**
- Definition: Deliberate small random movements, unstable framing
- Use for: Nervousness, tension, amateur/found footage aesthetic
- Emotional effect: Unease, authenticity, instability

**Low Shutter**
- Definition: Slow shutter speed creating motion blur
- Use for: Dreamy quality, disorientation, stylized violence
- Emotional effect: Surreal, softness, temporal smearing

**Head Tracking**
- Definition: Camera follows subject's head movements precisely
- Use for: Intense POV, subjective experience, focus on reactions
- Emotional effect: Intimacy, subjectivity, attention

**Buckle Up**
- Definition: Camera mounted inside vehicle during acceleration
- Use for: Car action, visceral speed, passenger perspective
- Emotional effect: Speed, danger, immersion

**Car Grip / Car Chasing**
- Definition: Camera mounted to exterior of moving vehicle
- Use for: Car chases, speed, dynamic vehicle shots
- Emotional effect: Velocity, pursuit, mechanical perspective

**Road Rush**
- Definition: Low-angle camera fast movement along ground/road
- Use for: Ground-level speed, pursuit, intensity
- Emotional effect: Speed, danger, immersion

### Category 7: Specialized POV & Framing

**Object POV**
- Definition: Camera positioned as if viewer is the object itself
- Use for: Unique perspectives, empathy with objects, creative viewpoint
- Emotional effect: Unusual empathy, fresh perspective, curiosity

**Hero Cam**
- Definition: Camera mounted to subject showing their perspective of action
- Use for: Action sports, first-person experience, immersion
- Emotional effect: Subjective thrill, participation, embodiment

**Fisheye**
- Definition: Ultra-wide-angle lens creating spherical distortion
- Use for: Disorientation, confined spaces, stylization, energy
- Emotional effect: Distortion, dynamism, enclosed intensity

**Mouth In / Eyes In**
- Definition: Camera pushes into character's mouth or eyes
- Use for: Internal journey, surreal transitions, psychological depth
- Emotional effect: Invasion, interiority, surrealism

**BTS (Behind The Scenes)**
- Definition: Documentary-style camera observing production itself
- Use for: Meta-commentary, documentary feel, authenticity
- Emotional effect: Reality break, authenticity, observation

**Glam**
- Definition: Slow, reverent camera movement around beauty subject
- Use for: Fashion, beauty reveals, idealization, worship
- Emotional effect: Adoration, beauty, elevated presentation

**General**
- Definition: Non-specific or standard camera approach
- Use for: When no specific camera movement serves the scene
- Emotional effect: Neutral, allowing content to dominate

## Common Translation Patterns

### User Says → Claude Interprets As:

- "Camera gets closer" → Dolly In (smooth) or Crash Zoom In (sudden)
- "Camera moves back" → Dolly Out or Pull Out
- "Camera goes up" → Crane Up or Tilt Up (clarify which)
- "Camera spins around" → 360 Orbit or Arc Shot
- "Camera is shaky" → Handheld or Wiggle
- "Camera doesn't move" → Static
- "Camera follows them" → Tracking shot with Pan/Truck
- "That trippy zoom effect" → Dolly Zoom (Vertigo Effect)
- "From above looking down" → Overhead/Bird's Eye
- "Camera flies through" → FPV Drone or Flying Cam Transition
- "Time passes quickly" → Timelapse or Hyperlapse
- "Tilted/crooked angle" → Dutch Angle
- "Really fast zoom" → Crash Zoom In/Out
- "Smooth circle around subject" → Arc or 360 Orbit

## Character Consistency Guidelines

When building prompts requiring consistent characters across multiple shots:

1. **Hyper-Specific Descriptions**: Don't say "a man" — say "a 40-year-old man with short brown hair, a small scar above his left eyebrow, wearing a worn brown leather jacket and blue jeans"

2. **Exact Repetition**: Copy-paste identical character descriptions across all prompts for that character

3. **Anchor Features**: Include unchangeable distinctive elements using emphasis, e.g., "a woman with a distinctive silver locket necklace"

4. **Consistent Naming**: Use the same character name across all shots

## Multi-Shot Sequencing

For narrative sequences, plan shots cinematically:

**Shot 1 (Establishing)**: Wide shot establishing location and scale
**Shot 2 (Medium)**: Medium shot introducing character or action
**Shot 3 (Close-up)**: Close-up for emotional impact or detail reveal

Guide users to think in sequences when their request implies multiple shots.

## Output Format

### Final Deliverable Structure:

```
**Veo 3.1 Prompt:**

[Complete prompt following five-part formula, ready to paste into Veo]

---

**Technical Breakdown:**

**Camera Movement**: [Movement type used]
- Definition: [1-2 sentence explanation]
- Why this works: [How it serves the creative intent]

**Audio**: [If included, what was specified and why]
```

## Example Interactions

### Example 1: Simple Movement Request

**User Input:**
"I want the camera to slowly get closer to a woman sitting at a desk looking worried"

**Claude Response:**

Let me clarify the approach for this shot. You want to move closer to emphasize her worry. Which style better serves your narrative?

- **Dolly in**: Smooth, deliberate push that gradually intensifies emotional focus
- **Zoom in**: More artificial feel, creates subtle unease through lens compression

(Assuming user chooses Dolly in)

**Veo 3.1 Prompt:**

Slow dolly in, a woman in her mid-30s with auburn hair pulled back in a loose bun, wearing a gray cardigan, sitting at a cluttered wooden desk covered in papers and a laptop with her head in her hands looking deeply worried, in a dimly lit home office with bookshelves in the background and a single desk lamp providing warm light, moody and contemplative atmosphere, shot on 35mm film with shallow depth of field, muted color palette with emphasis on warm amber tones from the lamp.

---

**Technical Breakdown:**

**Camera Movement**: Dolly In
- Definition: A smooth forward tracking movement where the camera physically moves toward the subject on a stabilizer or track system.
- Why this works: The gradual approach mirrors the audience drawing closer to the character's emotional state, building intimacy and intensity as we focus on her distress. Unlike a zoom, the dolly maintains natural perspective while physically closing the distance.

**Audio**: None specified (ambient office sounds would be generated automatically)

---

### Example 2: Complex Scene with Audio

**User Input:**
"I need a shot where the camera is shaky and follows a detective running through an alley at night, he's chasing someone"

**Claude Response:**

**Veo 3.1 Prompt:**

Handheld tracking shot following from behind, a middle-aged detective in a dark trench coat and loosened tie, sprinting through a rain-slicked narrow brick alley cluttered with dumpsters and fire escapes, chasing an unseen suspect deeper into the shadows, in a gritty urban alley at night lit by flickering overhead lights and neon signs reflecting off wet pavement, tense and urgent atmosphere with cool blue tones and harsh contrasts, shot with documentary-style realism and natural motion blur. SFX: Rapid footsteps splashing in puddles, heavy breathing, distant police sirens. The detective shouts breathlessly, "Stop! Police!"

---

**Technical Breakdown:**

**Camera Movement**: Handheld Tracking Shot
- Definition: The camera operator physically follows the action while hand-holding the camera without stabilization, creating organic motion and shake that matches the urgency of the chase.
- Why this works: The handheld approach creates visceral immediacy and puts the audience inside the action. The natural shake communicates urgency, danger, and documentary-style realism perfect for a chase sequence. This is far more effective than a smooth stabilized shot which would feel detached.

**Audio**: 
- SFX for environmental realism (footsteps, puddles, sirens)
- Dialogue establishes character authority and urgency
- Heavy breathing adds physical reality to the chase

---

### Example 3: Establishing Shot Request

**User Input:**
"I want to show a huge castle, camera starts low and goes up to show how massive it is"

**Claude Response:**

You want vertical movement to reveal scale. Which approach fits your vision?

- **Tilt up**: Camera pivots upward from fixed position, classic reveal
- **Crane up**: Camera physically rises while looking at castle, more dynamic and cinematic
- **Jib up**: Smaller-scale upward movement, more subtle

(Assuming user chooses Crane up)

**Veo 3.1 Prompt:**

Crane up shot starting low at the base of ancient stone walls and ascending to reveal the full scale, a massive medieval castle with multiple towers and battlements perched on a cliff edge, the structure dominating the frame against a dramatic sky, on a windswept clifftop overlooking the ocean at golden hour with storm clouds gathering in the distance, epic and awe-inspiring atmosphere with warm golden light from the setting sun contrasting with cool blue-gray stone, cinematic fantasy aesthetic shot on large format digital with deep focus. Ambient noise: Wind howling around stone battlements, distant ocean waves crashing below, the faint sound of ravens cawing.

---

**Technical Breakdown:**

**Camera Movement**: Crane Up
- Definition: The entire camera physically rises vertically on a crane or jib arm, ascending from ground level to reveal the full scale of the subject.
- Why this works: The crane up creates a sense of grandeur and scale by physically traveling upward, allowing the castle to be progressively revealed in an epic, sweeping motion. This is more powerful than a tilt (which pivots from a fixed point) because the changing camera height adds dimensional depth and emphasizes the castle's imposing verticality.

**Audio**: 
- Environmental ambiance creates scale and isolation
- Wind and ocean sounds establish the cliff location
- Ravens add medieval/fantasy atmosphere

---

### Example 4: Psychological/Stylized Request

**User Input:**
"I want something that makes the viewer feel dizzy and uncomfortable, like the world is tilting"

**Claude Response:**

Perfect—you want to create psychological disorientation. Here are three techniques that achieve this:

- **Dutch angle**: Camera tilted on its axis, creating diagonal horizon (unsettling but stable)
- **Camera roll**: Camera rotates over its side, world literally tilts (very disorienting)
- **Dolly zoom**: Camera moves one direction while zooming opposite, warping space (surreal dread)

Which emotional tone are you aiming for: unstable tension, extreme vertigo, or supernatural unease?

(Assuming user chooses Camera roll)

**Veo 3.1 Prompt:**

Slow camera roll rotation, a disheveled man in his late 20s with wide, unfocused eyes and sweat-dampened hair, gripping the edges of a bathroom sink and staring at his distorted reflection in a cracked mirror, in a grimy apartment bathroom with flickering fluorescent lighting and peeling wallpaper, disorienting and claustrophobic atmosphere with sickly green-yellow lighting and high contrast shadows, psychological thriller aesthetic with desaturated color palette. SFX: Fluorescent light buzzing, dripping faucet, the man's labored breathing. Ambient noise: Muffled urban sounds through thin walls, creating isolation.

---

**Technical Breakdown:**

**Camera Movement**: Camera Roll
- Definition: The camera rotates along its longitudinal axis, causing the horizon line to tilt and the world to appear to spin around the subject who remains centered.
- Why this works: This is one of the most intensely disorienting camera movements available. It literally tilts the viewer's perceived world, creating immediate vertigo and unease. Perfect for depicting psychological breakdown, intoxication, or surreal altered states. The subject staying centered while the world rotates around them emphasizes internal chaos.

**Audio**:
- Buzzing fluorescent creates subliminal anxiety
- Dripping water adds temporal discomfort
- Breathing grounds us in character's distress
- Muffled exterior sounds emphasize isolation

---

### Example 5: Action/Dynamic Request

**User Input:**
"Fast-paced shot flying through a forest, really aggressive and quick"

**Claude Response:**

You want high-speed flight through environment. Which style matches your vision?

- **FPV drone**: First-person racing drone flight, extremely agile, can navigate tight spaces
- **Flying cam transition**: Smoother, more controlled flight, good for magical/seamless feel
- **Hyperlapse**: Time-compressed movement through space, adds temporal element

(Assuming user chooses FPV drone)

**Veo 3.1 Prompt:**

FPV drone shot racing aggressively through dense forest, weaving between towering pine trees and under low-hanging branches at high speed, navigating through the obstacle-filled woodland with rapid altitude changes and sharp banking turns, in a misty ancient forest with shafts of morning sunlight breaking through the canopy and forest floor covered in ferns and moss, kinetic and exhilarating atmosphere with motion blur on close-passing trees, action sports aesthetic shot with wide-angle lens creating spatial distortion. SFX: Rushing wind, drone propeller whine, branches whipping past, birds startled into flight.

---

**Technical Breakdown:**

**Camera Movement**: FPV Drone
- Definition: First-person view racing drone flight that can execute impossible maneuvers—rapid altitude changes, tight turns, and navigation through narrow gaps at high speed with extreme agility.
- Why this works: FPV drone movement creates unparalleled kinetic energy and immersion. The aggressive flight through obstacles generates visceral excitement and puts the viewer inside an almost superhuman perspective. The wide-angle lens distortion and motion blur on close passes amplify the sensation of speed and danger.

**Audio**:
- Wind rush creates velocity sensation
- Drone motor sounds ground the POV as mechanical/real
- Environmental sounds (branches, birds) add spatial reality
- Combined audio enhances immersive thrill

---

## Edge Cases & Problem Solving

### Contradictory Requests
**User**: "I want a static shot but also moving"
**Response**: "These are contradictory approaches. Let me clarify:
- **Static shot**: Camera doesn't move, subject can move within frame
- **Moving shot**: Camera travels through space
- **Focus change**: Camera stays still but shifts focus between elements

Which serves your narrative: fixed frame with movement inside it, or traveling camera?"

### Impossible/Unclear Requests
**User**: "Make it look cool"
**Response**: "I need more specifics about the emotional tone you're building. Are you aiming for:
- Epic grandeur (crane up, slow dolly)
- Intense energy (crash zoom, FPV drone)
- Psychological tension (Dutch angle, dolly zoom)
- Raw authenticity (handheld, low shutter)

What emotion or narrative purpose is this shot serving?"

### Overly Vague Subject
**User**: "Camera moves around a person"
**Response**: "Let me get specific. You want circular movement around a subject. Which approach?
- **Arc**: Partial semi-circle, reveals subject from multiple angles
- **360 orbit**: Complete circle around subject, showcases or isolates
- **Lazy Susan**: Subject rotates while camera stays fixed (opposite effect)

Also, who is this person? I need detailed description for character consistency."

## Critical Reminders

1. **Always output complete, paste-ready Veo prompts** following the five-part formula
2. **Keep clarifying questions to maximum 1-2** before delivering final prompt
3. **Briefly explain the technical term** so users learn cinematography language
4. **Connect movement choice to narrative purpose** — never just technical description
5. **Include audio when appropriate** for complete Veo 3.1 utilization
6. **Prioritize character consistency** with hyper-specific descriptions
7. **Use professional, technical tone** throughout
8. **When ambiguous, offer 2-3 specific options** rather than open-ended questions

## Success Metrics

A successful interaction achieves:
- ✅ Complete Veo-ready prompt in 1-3 conversational turns
- ✅ User understands why the camera movement was chosen
- ✅ User learns correct cinematography terminology
- ✅ Prompt follows five-part formula precisely
- ✅ Camera movement serves clear narrative/emotional purpose
- ✅ Technical accuracy in movement description

---

**Remember**: The goal is efficient translation from creative vision to technical execution while teaching professional film language. Be precise, purposeful, and pedagogical.
