import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

os.makedirs('Assets/CipherCourtPolish/Diagrams', exist_ok=True)

NAVY = '#102C57'
STEEL = '#35598E'
LIGHT_BLUE = '#EDF4FC'
BORDER_COLOR = '#1A365D'
TEXT_DARK = '#1A202C'
GOLD = '#D69E2E'
GREEN = '#2F855A'
RED = '#C53030'
BG_COLOR = '#FFFFFF'

# ═════════════════════════════════════════════════════════════════════════════
# 1. USE CASE DIAGRAM
# ═════════════════════════════════════════════════════════════════════════════
def create_use_case_diagram():
    fig, ax = plt.subplots(figsize=(11, 8.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # System boundary box
    rect = patches.FancyBboxPatch((24, 6), 52, 88, boxstyle="round,pad=1.5", 
                                  linewidth=2, edgecolor=NAVY, facecolor='#F7FAFC')
    ax.add_patch(rect)
    ax.text(50, 91, "CIPHER COURT SYSTEM BOUNDARY", ha='center', va='center', 
            fontsize=13, fontweight='bold', color=NAVY, family='sans-serif')

    # Left Actor: Player Investigator
    circle_p = patches.Circle((10, 56), 3, facecolor=LIGHT_BLUE, edgecolor=NAVY, linewidth=1.5)
    ax.add_patch(circle_p)
    ax.plot([10, 10], [53, 44], color=NAVY, linewidth=2)
    ax.plot([6, 14], [49, 49], color=NAVY, linewidth=2)
    ax.plot([6, 10, 14], [39, 44, 39], color=NAVY, linewidth=2)
    ax.text(10, 34, "Player\nInvestigator\n(Actor)", ha='center', va='center', 
            fontsize=9.5, fontweight='bold', color=TEXT_DARK)

    # Right Actor: Unity Engine / PhysX
    rect_sys = patches.Rectangle((86, 48), 8, 8, facecolor=LIGHT_BLUE, edgecolor=STEEL, linewidth=1.5)
    ax.add_patch(rect_sys)
    ax.text(90, 52, "SYS", ha='center', va='center', fontsize=9, fontweight='bold', color=STEEL)
    ax.text(90, 40, "Unity Engine &\nPhysics Subsystem\n(System Actor)", ha='center', va='center', 
            fontsize=9.5, fontweight='bold', color=TEXT_DARK)

    use_cases = [
        (50, 83, "UC-01: Navigate 3D Spatial Environment"),
        (50, 75, "UC-02: Center-Screen Raycast Clue Focus"),
        (50, 67, "UC-03: Inspect & Rotate Forensic Exhibit"),
        (50, 59, "UC-04: Solve Binary Keypad Puzzle (L1)"),
        (50, 51, "UC-05: Calibrate Ballistic Trajectory (L2)"),
        (50, 43, "UC-06: Rotate Caesar Rotor Cipher (L3)"),
        (50, 35, "UC-07: Crack Evidence Locker Tumblers (L4)"),
        (50, 27, "UC-08: Expose Witness Contradiction (L5)"),
        (50, 19, "UC-09: Deliver Final Courtroom Verdict (L6)"),
        (50, 11, "UC-10: Trigger Asynchronous Scene Load"),
    ]

    for x, y, label in use_cases:
        oval = patches.FancyBboxPatch((x - 22, y - 2.8), 44, 5.6, 
                                      boxstyle="round,pad=0.8", linewidth=1.2, 
                                      edgecolor=STEEL, facecolor=LIGHT_BLUE)
        ax.add_patch(oval)
        ax.text(x, y, label, ha='center', va='center', fontsize=8.5, fontweight='bold', color=NAVY)
        # Association lines
        ax.plot([15, x - 22], [48, y], color='#718096', linewidth=1, linestyle='-')
        if y <= 27 or y >= 75:
            ax.plot([x + 22, 85], [y, 48], color='#A0AEC0', linewidth=1, linestyle='--')

    plt.tight_layout()
    path = 'Assets/CipherCourtPolish/Diagrams/uml_use_case_diagram.png'
    plt.savefig(path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"Generated: {path}")

# ═════════════════════════════════════════════════════════════════════════════
# 2. CLASS DIAGRAM
# ═════════════════════════════════════════════════════════════════════════
def create_class_diagram():
    fig, ax = plt.subplots(figsize=(12, 9), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 97, "CIPHER COURT – HIGH-LEVEL CLASS DIAGRAM", ha='center', va='center', 
            fontsize=14, fontweight='bold', color=NAVY)

    def draw_class(x, y, w, h, name, attrs, methods, is_interface=False):
        header_color = '#2B6CB0' if is_interface else NAVY
        rect = patches.Rectangle((x, y - h), w, h, linewidth=1.5, edgecolor=BORDER_COLOR, facecolor='#FFFFFF')
        ax.add_patch(rect)
        # Header banner
        header_h = h * 0.28
        h_rect = patches.Rectangle((x, y - header_h), w, header_h, linewidth=1, edgecolor=BORDER_COLOR, facecolor=header_color)
        ax.add_patch(h_rect)
        prefix = "«interface»\n" if is_interface else ""
        ax.text(x + w/2, y - header_h/2, f"{prefix}{name}", ha='center', va='center', 
                fontsize=8, fontweight='bold', color='#FFFFFF')
        # Attributes
        attr_text = "\n".join(attrs)
        ax.text(x + 1, y - header_h - 1, attr_text, ha='left', va='top', fontsize=6.8, color=TEXT_DARK)
        # Divider line
        div_y = y - header_h - (h * 0.35)
        ax.plot([x, x + w], [div_y, div_y], color=BORDER_COLOR, linewidth=1)
        # Methods
        meth_text = "\n".join(methods)
        ax.text(x + 1, div_y - 1, meth_text, ha='left', va='top', fontsize=6.8, color=TEXT_DARK)

    # Classes
    draw_class(5, 92, 26, 20, "PlayerController", 
               ["- walkSpeed: float = 4.5f", "- gravity: float = -18f", "- lookXLimit: float = 85f", "- cc: CharacterController"],
               ["+ Awake(): void", "+ Update(): void", "+ HandleMovement(): void", "+ HandleLook(): void"])

    draw_class(37, 92, 26, 20, "PlayerInteraction", 
               ["- interactDistance: float = 2.5f", "- reticleImage: Image", "- currentTarget: GameObject"],
               ["+ Awake(): void", "+ Update(): void", "+ PerformRaycast(): void", "+ TriggerInteract(): void"])

    draw_class(69, 92, 26, 18, "IInteractable", 
               [], ["+ Interact(): void"], is_interface=True)

    draw_class(37, 65, 26, 18, "PuzzleBase", 
               ["# isSolved: bool = false", "# onSolved: UnityEvent"], 
               ["+ ValidateSolution(): bool", "+ OnPuzzleSolved(): void", "+ ResetPuzzle(): void"])

    draw_class(5, 42, 26, 19, "Level1KeypadPuzzle", 
               ["- targetCode: string = '1011'", "- currentInput: string", "- exitDoor: Transform"],
               ["+ OnDigitPressed(string): void", "+ ValidateKeypadCode(): void", "+ Update(): void"])

    draw_class(37, 42, 26, 19, "Level2BallisticsPuzzle", 
               ["- targetAngle: float = 38.5f", "- currentAngle: float", "- trajectoryDisplay: TMP"],
               ["+ AdjustAngle(float): void", "+ CheckAlignment(): void", "+ UpdateDisplay(): void"])

    draw_class(69, 42, 26, 19, "Level3CipherPuzzle", 
               ["- targetShift: int = 3", "- currentShift: int", "- encryptedMemo: string"],
               ["+ RotateRotorClockwise(): void", "+ EvaluateDecryption(): void"])

    draw_class(5, 19, 26, 16, "Level4LockerPuzzle", 
               ["- targetCombo: int[3]", "- currentDials: int[3]"],
               ["+ AdvanceDial(int): void", "+ CheckCombination(): void"])

    draw_class(37, 19, 26, 16, "Level5EvidencePresentation", 
               ["- contradictionIndex: int = 2", "- statementExposed: bool"],
               ["+ PresentEvidence(int): void"])

    draw_class(69, 19, 26, 16, "Level6VerdictPuzzle", 
               ["- verdictDelivered: bool", "- gavelSFX: AudioClip"],
               ["+ DeliverFinalVerdict(bool): void"])

    # Inheritance & Interface arrows
    ax.annotate('', xy=(50, 65), xytext=(50, 42), arrowprops=dict(arrowstyle="-|>", color=NAVY, lw=1.5))
    ax.annotate('', xy=(50, 65), xytext=(18, 42), arrowprops=dict(arrowstyle="-|>", color=NAVY, lw=1.5))
    ax.annotate('', xy=(50, 65), xytext=(82, 42), arrowprops=dict(arrowstyle="-|>", color=NAVY, lw=1.5))
    ax.annotate('', xy=(69, 83), xytext=(63, 83), arrowprops=dict(arrowstyle="->", color=STEEL, lw=1.5, ls='--'))

    plt.tight_layout()
    path = 'Assets/CipherCourtPolish/Diagrams/uml_class_diagram.png'
    plt.savefig(path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"Generated: {path}")

# ═════════════════════════════════════════════════════════════════════════════
# 3. SEQUENCE DIAGRAM: RAYCAST INTERACTION
# ═════════════════════════════════════════════════════════════════════════
def create_sequence_diagram_interaction():
    fig, ax = plt.subplots(figsize=(11, 7.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 96, "SEQUENCE DIAGRAM: PLAYER RAYCAST DETECTION & INTERACTION", 
            ha='center', va='center', fontsize=12, fontweight='bold', color=NAVY)

    lifelines = [
        (12, "Player"),
        (30, "PlayerCamera"),
        (48, "PlayerInteraction"),
        (66, "Physics (PhysX)"),
        (82, "HUD Reticle UI"),
        (94, "IInteractable")
    ]

    for x, name in lifelines:
        # Box
        rect = patches.FancyBboxPatch((x - 6, 88), 12, 5, boxstyle="round,pad=0.3", 
                                      facecolor=LIGHT_BLUE, edgecolor=NAVY, linewidth=1.2)
        ax.add_patch(rect)
        ax.text(x, 90.5, name, ha='center', va='center', fontsize=7.5, fontweight='bold', color=NAVY)
        # Dashed line
        ax.plot([x, x], [88, 8], color='#CBD5E0', linestyle='--', linewidth=1.2)

    # Messages
    calls = [
        (82, 12, 30, "MoveMouse(deltaX, deltaY)", '->'),
        (76, 30, 48, "UpdateCameraRay(origin, forward)", '->'),
        (70, 48, 66, "Raycast(ray, 2.5m, layerMask)", '->'),
        (64, 66, 48, "RaycastHit(hitCollider, dist=1.8m)", '-->'),
        (58, 48, 82, "SetReticleColor(Cyan), SetScale(1.35x)", '->'),
        (52, 48, 82, "ShowPrompt('[E] Inspect Evidence')", '->'),
        (44, 12, 48, "KeyPress(KeyCode.E)", '->'),
        (38, 48, 94, "GetComponent<IInteractable>().Interact()", '->'),
        (32, 94, 82, "OpenInspectionModal(clueData)", '->'),
        (24, 12, 48, "MoveAway (> 2.5m)", '->'),
        (18, 48, 82, "ResetReticle(White, 1.0x), HidePrompt()", '->')
    ]

    for y, x1, x2, msg, style in calls:
        color = NAVY if style == '->' else STEEL
        ls = '-' if style == '->' else '--'
        ax.annotate('', xy=(x2, y), xytext=(x1, y),
                    arrowprops=dict(arrowstyle="->", color=color, lw=1.2, ls=ls))
        mid_x = (x1 + x2) / 2
        ax.text(mid_x, y + 1.6, msg, ha='center', va='bottom', fontsize=7, color=TEXT_DARK)

    plt.tight_layout()
    path = 'Assets/CipherCourtPolish/Diagrams/uml_sequence_diagram_interaction.png'
    plt.savefig(path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"Generated: {path}")

# ═════════════════════════════════════════════════════════════════════════════
# 4. SEQUENCE DIAGRAM: PUZZLE VERIFICATION & UNLOCK
# ═════════════════════════════════════════════════════════════════════════
def create_sequence_diagram_puzzle():
    fig, ax = plt.subplots(figsize=(11, 7.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 96, "SEQUENCE DIAGRAM: PUZZLE VERIFICATION & EXIT DOOR UNLOCK LIFECYCLE", 
            ha='center', va='center', fontsize=12, fontweight='bold', color=NAVY)

    lifelines = [
        (12, "Player"),
        (32, "KeypadConsole UI"),
        (52, "Level1KeypadPuzzle"),
        (72, "AudioSource"),
        (88, "ExitDoorMotor")
    ]

    for x, name in lifelines:
        rect = patches.FancyBboxPatch((x - 7, 88), 14, 5, boxstyle="round,pad=0.3", 
                                      facecolor=LIGHT_BLUE, edgecolor=NAVY, linewidth=1.2)
        ax.add_patch(rect)
        ax.text(x, 90.5, name, ha='center', va='center', fontsize=7.5, fontweight='bold', color=NAVY)
        ax.plot([x, x], [88, 8], color='#CBD5E0', linestyle='--', linewidth=1.2)

    calls = [
        (82, 12, 32, "ClickDigitButton('1')", '->'),
        (76, 32, 52, "OnDigitPressed('1')", '->'),
        (70, 52, 72, "PlayOneShot(buttonClickSFX)", '->'),
        (64, 12, 52, "InputRemainingDigits('0', '1', '1')", '->'),
        (56, 52, 52, "ValidateKeypadCode(): Target '1011' MATCH", '->'),
        (50, 52, 32, "UpdateDisplay('<color=green>ACCESS GRANTED</color>')", '->'),
        (44, 52, 72, "PlayOneShot(correctChimeSFX)", '->'),
        (38, 52, 88, "SetOpeningDoor(true)", '->'),
        (30, 88, 88, "Quaternion.Slerp(rotY, 90 deg, Time.deltaTime)", '->'),
        (22, 12, 88, "CrossDoorwayTriggerBounds()", '->'),
        (14, 88, 52, "FinalLevelExit.LoadSceneAsync('Level2_Computer')", '->')
    ]

    for y, x1, x2, msg, style in calls:
        color = GREEN if "GRANTED" in msg or "MATCH" in msg else NAVY
        ax.annotate('', xy=(x2, y), xytext=(x1, y),
                    arrowprops=dict(arrowstyle="->", color=color, lw=1.2))
        mid_x = (x1 + x2) / 2 if x1 != x2 else x1 + 6
        ax.text(mid_x, y + 1.6, msg, ha='center', va='bottom', fontsize=7.2, color=TEXT_DARK)

    plt.tight_layout()
    path = 'Assets/CipherCourtPolish/Diagrams/uml_sequence_diagram_puzzle.png'
    plt.savefig(path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"Generated: {path}")

# ═════════════════════════════════════════════════════════════════════════════
# 5. ACTIVITY DIAGRAM
# ═════════════════════════════════════════════════════════════════════════
def create_activity_diagram():
    fig, ax = plt.subplots(figsize=(10, 8.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 97, "ACTIVITY DIAGRAM: INVESTIGATIVE GAMEPLAY & TRIAL WORKFLOW", 
            ha='center', va='center', fontsize=12, fontweight='bold', color=NAVY)

    # Start circle
    circle = patches.Circle((50, 92), 2, facecolor='#1A202C')
    ax.add_patch(circle)

    activities = [
        (50, 83, "Launch Application & Navigate Main Menu", "rect"),
        (50, 74, "Spawn in Investigation Room (Level 1..6)", "rect"),
        (50, 65, "First-Person Navigation (WASD + Mouse Look)", "rect"),
        (50, 56, "Center-Screen Raycast Hover Check", "diamond"),
        (50, 46, "Inspect Forensic Clue / Interact with Console", "rect"),
        (50, 36, "Formulate & Input Cryptographic Solution", "rect"),
        (50, 26, "Validate Mathematical Solution", "diamond"),
        (50, 16, "Door Slerp Rotation & Trigger Exit Volume", "rect"),
        (50, 7, "Courtroom Verdict Showdown -> Victory Complete", "rect")
    ]

    for x, y, label, shape in activities:
        if shape == "rect":
            box = patches.FancyBboxPatch((x - 22, y - 2.6), 44, 5.2, boxstyle="round,pad=0.5", 
                                         facecolor=LIGHT_BLUE, edgecolor=NAVY, linewidth=1.2)
            ax.add_patch(box)
            ax.text(x, y, label, ha='center', va='center', fontsize=8, fontweight='bold', color=NAVY)
        elif shape == "diamond":
            poly = patches.Polygon([[x, y + 3.2], [x + 18, y], [x, y - 3.2], [x - 18, y]], 
                                   closed=True, facecolor='#FEFCBF', edgecolor=GOLD, linewidth=1.2)
            ax.add_patch(poly)
            ax.text(x, y, label, ha='center', va='center', fontsize=7.5, fontweight='bold', color='#744210')

    # Flow arrows
    y_coords = [92, 83, 74, 65, 56, 46, 36, 26, 16, 7]
    for i in range(len(y_coords) - 1):
        ax.annotate('', xy=(50, y_coords[i+1] + 3), xytext=(50, y_coords[i] - 3),
                    arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.3))

    # Rejection loop from Validate Solution back to Input Solution
    ax.annotate('', xy=(28, 36), xytext=(32, 26),
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.2, connectionstyle="arc3,rad=-0.4"))
    ax.text(23, 31, "[Incorrect Code]\nTrigger Buzzer", fontsize=6.5, color=RED, ha='right')

    plt.tight_layout()
    path = 'Assets/CipherCourtPolish/Diagrams/uml_activity_diagram.png'
    plt.savefig(path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"Generated: {path}")

# ═════════════════════════════════════════════════════════════════════════════
# 6. STATE MACHINE DIAGRAM
# ═════════════════════════════════════════════════════════════════════════
def create_state_machine_diagram():
    fig, ax = plt.subplots(figsize=(11, 8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 96, "FINITE STATE MACHINE (FSM) DIAGRAM: GAME & LEVEL LIFECYCLE", 
            ha='center', va='center', fontsize=12, fontweight='bold', color=NAVY)

    states = [
        (20, 80, "STATE_MAIN_MENU\nCursor Free | UI Active"),
        (50, 80, "STATE_EXPLORING\nCursor Locked | WASD Move"),
        (80, 80, "STATE_RETICLE_FOCUSED\nRaycast Hit <= 2.5m | Cyan HUD"),
        (80, 50, "STATE_INSPECTING\nModal Display | Motion Restrained"),
        (50, 50, "STATE_VALIDATING\nEvaluate Logic Equation"),
        (20, 50, "STATE_DOOR_OPENING\nInterpolate Slerp Rot 90°"),
        (20, 20, "STATE_SCENE_TRANSITION\nAsync Load Next Level"),
        (50, 20, "STATE_COURTROOM_VERDICT\nJudge Gavel | Bench Deliberation"),
        (80, 20, "STATE_GAME_COMPLETE\nVictory Screen | Return Menu")
    ]

    for x, y, label in states:
        box = patches.FancyBboxPatch((x - 12, y - 6), 24, 12, boxstyle="round,pad=0.8", 
                                     facecolor=LIGHT_BLUE, edgecolor=NAVY, linewidth=1.2)
        ax.add_patch(box)
        ax.text(x, y, label, ha='center', va='center', fontsize=7.5, fontweight='bold', color=NAVY)

    # State transitions
    ax.annotate('Click Start', xy=(38, 80), xytext=(32, 80), arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.2))
    ax.annotate('Hover Clue', xy=(68, 80), xytext=(62, 80), arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.2))
    ax.annotate('Press [E]', xy=(80, 56), xytext=(80, 74), arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.2))
    ax.annotate('Submit', xy=(62, 50), xytext=(68, 50), arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.2))
    ax.annotate('Pass', xy=(32, 50), xytext=(38, 50), arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.2))
    ax.annotate('Walk Exit', xy=(20, 26), xytext=(20, 44), arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.2))
    ax.annotate('L6 Climax', xy=(38, 20), xytext=(32, 20), arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.2))
    ax.annotate('Verdict Guilty', xy=(68, 20), xytext=(62, 20), arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.2))

    plt.tight_layout()
    path = 'Assets/CipherCourtPolish/Diagrams/uml_state_machine_diagram.png'
    plt.savefig(path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"Generated: {path}")

# ═════════════════════════════════════════════════════════════════════════════
# 7. ENTITY-RELATIONSHIP (ER) DIAGRAM
# ═════════════════════════════════════════════════════════════════════════
def create_er_diagram():
    fig, ax = plt.subplots(figsize=(11, 8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 96, "ENTITY-RELATIONSHIP (ER) DIAGRAM: DATA PERSISTENCE ARCHITECTURE", 
            ha='center', va='center', fontsize=12, fontweight='bold', color=NAVY)

    def draw_entity(x, y, w, h, name, attrs):
        rect = patches.Rectangle((x, y - h), w, h, linewidth=1.5, edgecolor=BORDER_COLOR, facecolor='#FFFFFF')
        ax.add_patch(rect)
        header_h = h * 0.28
        h_rect = patches.Rectangle((x, y - header_h), w, header_h, linewidth=1, edgecolor=BORDER_COLOR, facecolor=NAVY)
        ax.add_patch(h_rect)
        ax.text(x + w/2, y - header_h/2, name, ha='center', va='center', fontsize=8.5, fontweight='bold', color='#FFFFFF')
        attr_text = "\n".join(attrs)
        ax.text(x + 1, y - header_h - 1, attr_text, ha='left', va='top', fontsize=6.8, color=TEXT_DARK)

    draw_entity(8, 88, 26, 22, "PLAYER_SESSION", 
                ["PK session_id: UUID", "candidate_id: VARCHAR", "start_time: DATETIME", "total_duration: FLOAT", "overall_status: VARCHAR", "final_score: INT"])

    draw_entity(45, 88, 26, 22, "LEVEL_PROGRESS", 
                ["PK level_id: INT", "FK session_id: UUID", "scene_name: VARCHAR", "is_cleared: BOOL", "clear_duration: FLOAT", "attempts_count: INT"])

    draw_entity(78, 88, 20, 20, "GAME_CONFIG", 
                ["PK config_id: INT", "master_volume: FLOAT", "mouse_sensitivity: FLOAT", "screen_resolution: VARCHAR"])

    draw_entity(8, 50, 26, 22, "EVIDENCE_ITEM", 
                ["PK evidence_id: VARCHAR", "FK level_id: INT", "evidence_title: VARCHAR", "discovery_time: FLOAT", "is_used_verdict: BOOL"])

    draw_entity(45, 50, 26, 22, "WITNESS_STATEMENT", 
                ["PK statement_id: INT", "FK level_id: INT", "witness_name: VARCHAR", "claim_text: TEXT", "is_contradicted: BOOL"])

    draw_entity(78, 50, 20, 22, "COURT_VERDICT", 
                ["PK verdict_id: INT", "FK session_id: UUID", "accused_name: VARCHAR", "bayesian_weight: FLOAT", "verdict_outcome: VARCHAR"])

    # Relationships
    ax.annotate('1:N initiates', xy=(45, 77), xytext=(34, 77), arrowprops=dict(arrowstyle="->", color=STEEL, lw=1.3))
    ax.annotate('1:N collects', xy=(21, 50), xytext=(21, 66), arrowprops=dict(arrowstyle="->", color=STEEL, lw=1.3))
    ax.annotate('1:N reviews', xy=(58, 50), xytext=(58, 66), arrowprops=dict(arrowstyle="->", color=STEEL, lw=1.3))
    ax.annotate('Evaluates Against', xy=(45, 39), xytext=(34, 39), arrowprops=dict(arrowstyle="<->", color=GOLD, lw=1.3, ls='--'))

    plt.tight_layout()
    path = 'Assets/CipherCourtPolish/Diagrams/uml_er_diagram.png'
    plt.savefig(path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"Generated: {path}")

# ═════════════════════════════════════════════════════════════════════════════
# 8. COMPONENT & DEPLOYMENT TOPOLOGY DIAGRAM
# ═════════════════════════════════════════════════════════════════════════
def create_deployment_diagram():
    fig, ax = plt.subplots(figsize=(11, 8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 96, "COMPONENT & DEPLOYMENT TOPOLOGY DIAGRAM", 
            ha='center', va='center', fontsize=12, fontweight='bold', color=NAVY)

    # Hardware Node 3D Box
    rect_hw = patches.FancyBboxPatch((8, 8), 84, 82, boxstyle="round,pad=1.2", 
                                     facecolor='#F7FAFC', edgecolor=NAVY, linewidth=2)
    ax.add_patch(rect_hw)
    ax.text(12, 87, "«device» Client PC Workstation (Intel x86-64 / NVIDIA RTX)", 
            ha='left', va='center', fontsize=9.5, fontweight='bold', color=NAVY)

    # OS Sub-node
    rect_os = patches.FancyBboxPatch((12, 12), 76, 70, boxstyle="round,pad=1.0", 
                                     facecolor='#EDF2F7', edgecolor=STEEL, linewidth=1.5)
    ax.add_patch(rect_os)
    ax.text(15, 78, "«execution environment» Windows 11 64-Bit OS (DirectX 12 / Vulkan)", 
            ha='left', va='center', fontsize=8.5, fontweight='bold', color=STEEL)

    # Components
    components = [
        (16, 52, 22, 18, "Unity Engine 6\nRuntime (Mono / IL2CPP)\n• PhysX Kinematics\n• SceneManager"),
        (42, 52, 22, 18, "Universal Render Pipeline\n(URP 17.0)\n• SRP Batcher\n• Forward+ Shaders"),
        (68, 52, 18, 18, "Input & EventSystem\n• GraphicRaycaster\n• CursorLockFixer"),
        (16, 20, 22, 22, "C# Gameplay Logic\n• PlayerController\n• PlayerInteraction\n• Level 1–6 Puzzles"),
        (42, 20, 22, 22, "Data Persistence\n• JsonUtility\n• SaveData.json\n• Telemetry Logger"),
        (68, 20, 18, 22, "Audio-Visual Assets\n• TextMeshPro Atlases\n• PBR Lit Materials\n• Spatial Sound SFX")
    ]

    for x, y, w, h, label in components:
        comp_box = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.5", 
                                          facecolor='#FFFFFF', edgecolor=BORDER_COLOR, linewidth=1.2)
        ax.add_patch(comp_box)
        # Small component icon tabs
        tab1 = patches.Rectangle((x - 1.5, y + h - 5), 3, 2.5, facecolor='#FFFFFF', edgecolor=BORDER_COLOR)
        tab2 = patches.Rectangle((x - 1.5, y + h - 10), 3, 2.5, facecolor='#FFFFFF', edgecolor=BORDER_COLOR)
        ax.add_patch(tab1)
        ax.add_patch(tab2)
        ax.text(x + w/2, y + h/2, label, ha='center', va='center', fontsize=7.2, color=TEXT_DARK)

    plt.tight_layout()
    path = 'Assets/CipherCourtPolish/Diagrams/uml_component_deployment_diagram.png'
    plt.savefig(path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"Generated: {path}")

if __name__ == "__main__":
    create_use_case_diagram()
    create_class_diagram()
    create_sequence_diagram_interaction()
    create_sequence_diagram_puzzle()
    create_activity_diagram()
    create_state_machine_diagram()
    create_er_diagram()
    create_deployment_diagram()
    print("All 8 UML diagrams generated successfully!")
