#if UNITY_EDITOR
using UnityEngine;
using UnityEngine.UI;
using UnityEditor;
using UnityEditor.SceneManagement;
using UnityEditor.Events;
using UnityEngine.SceneManagement;
using TMPro;
using System.IO;
using System.Linq;
using System.Collections.Generic;

[InitializeOnLoad]
public static class CipherCourtVisualPolisher
{
    const string RootName    = "_VISUAL_POLISH_V17_";
    const string FlagPath    = "Assets/CipherCourtPolish/POLISH_V17_APPLIED.txt";
    const string MatFolder   = "Assets/CipherCourtPolish/Materials";
    const string UIFolder    = "Assets/CipherCourtPolish/UI";

    // ── Refined Forensic & Judicial Palette ───────────────────────────────────
    static readonly Color WarmWhite   = new Color(0.92f, 0.90f, 0.86f, 1f);
    static readonly Color Gold        = new Color(0.95f, 0.82f, 0.42f, 1f);
    static readonly Color Cyan        = new Color(0.12f, 0.72f, 0.92f, 1f);
    static readonly Color CrimsonRed  = new Color(0.72f, 0.12f, 0.14f, 1f);
    static readonly Color PanelDark   = new Color(0.04f, 0.06f, 0.10f, 0.96f);
    static readonly Color BtnDark     = new Color(0.10f, 0.14f, 0.20f, 0.96f);

    static CipherCourtVisualPolisher()
    {
        EditorApplication.delayCall += AutoPolish;
    }

    [MenuItem("Cipher Court/Apply Professional V16 Overhaul")]
    public static void ApplyFromMenu() => ApplyAll(true);

    static void AutoPolish()
    {
        if (EditorApplication.isPlayingOrWillChangePlaymode || EditorApplication.isCompiling) return;
        if (File.Exists(FlagPath)) return;
        ApplyAll(false);
    }

    public static void ApplyAll(bool force)
    {
        if (!force && File.Exists(FlagPath)) return;

        EnsureFolder("Assets/CipherCourtPolish");
        EnsureFolder(MatFolder);
        EnsureFolder(UIFolder);

        GenerateUISprites();
        BuildMaterials();

        string[] scenes = {
            "Assets/Scenes/MainMenu.unity",
            "Assets/Scenes/Level1_Investigation.unity",
            "Assets/Scenes/Level2_Computer.unity",
            "Assets/Scenes/Level3_Evidence.unity",
            "Assets/Scenes/Level4_Archive.unity",
            "Assets/Scenes/Level5_CaseFiles.unity",
            "Assets/Scenes/Level6_FinalVerdict.unity",
            "Assets/Scenes/GameComplete.unity"
        };

        string previous = SceneManager.GetActiveScene().path;
        foreach (string path in scenes)
        {
            if (!File.Exists(path)) continue;
            Scene scene = EditorSceneManager.OpenScene(path, OpenSceneMode.Single);
            PolishScene(scene);
            EditorSceneManager.MarkSceneDirty(scene);
            EditorSceneManager.SaveScene(scene);
        }

        File.WriteAllText(FlagPath, "Cipher Court V16 Professional AAA-Tier Redesign applied.\n");
        AssetDatabase.ImportAsset(FlagPath);
        AssetDatabase.SaveAssets();
        AssetDatabase.Refresh();

        if (!string.IsNullOrEmpty(previous) && File.Exists(previous))
            EditorSceneManager.OpenScene(previous, OpenSceneMode.Single);
        else if (File.Exists("Assets/Scenes/MainMenu.unity"))
            EditorSceneManager.OpenScene("Assets/Scenes/MainMenu.unity", OpenSceneMode.Single);

        Debug.Log("Cipher Court V16: Clean architectural overhaul, real prefabs, and professional UI complete!");
    }

    // ═══════════════════════════════════════════════════════════════════════
    //  SCENE POLISH & PURGE
    // ═══════════════════════════════════════════════════════════════════════
    static void PolishScene(Scene scene)
    {
        PurgeLegacyObjects(scene);

        GameObject root = new GameObject(RootName);
        SceneManager.MoveGameObjectToScene(root, scene);

        // Set clean, atmospheric directional light
        foreach (Light l in Object.FindObjectsByType<Light>(FindObjectsSortMode.None))
        {
            if (l.type == LightType.Directional)
            {
                l.intensity = scene.name == "Level6_FinalVerdict" ? 0.65f : 0.45f;
                l.color = new Color(1.0f, 0.96f, 0.90f);
            }
            else if (l.name.Contains("RoomLight"))
            {
                Object.DestroyImmediate(l.gameObject);
            }
        }

        // Ensure cameras never cull geometry via occlusion culling bugs
        foreach (Camera cam in Object.FindObjectsByType<Camera>(FindObjectsSortMode.None))
        {
            cam.useOcclusionCulling = false;
        }

        switch (scene.name)
        {
            case "MainMenu":            BuildMainMenuRoom(root);      break;
            case "Level1_Investigation": BuildInvestigationRoom(root); break;
            case "Level2_Computer":     BuildCyberRoom(root);         break;
            case "Level3_Evidence":     BuildEvidenceRoom(root);      break;
            case "Level4_Archive":      BuildArchiveRoom(root);       break;
            case "Level5_CaseFiles":    BuildStatementsRoom(root);    break;
            case "Level6_FinalVerdict":  BuildCourtroom(root);         break;
            case "GameComplete":        BuildGameCompleteRoom(root);  break;
        }

        if (scene.name != "MainMenu" && scene.name != "GameComplete")
        {
            PositionInteractiveObjects(scene, root);
        }

        PolishUI(scene);
    }

    static void PurgeLegacyObjects(Scene scene)
    {
        string[] badPrefixes = {
            "_visual_polish", "finishedspacebehinddoor", "referencescenebackdrop",
            "keypadconsolevisual", "doorjamb", "passage", "exitheader", "sign",
            "cork", "evidsign", "archivsign", "cybersign", "truthsign",
            "promptlabel", "cluebeacon", "giantwall", "blockingwall", "partition",
            "desktop", "deskleg", "computerdesk", "monitorscreen", "evidencetable",
            "deftable", "prostable", "witnessbox", "judgebench", "juryplatform",
            "backwallleft", "backwallright", "backwalltop", "sr_l_", "sr_r_",
            "wall_back", "wall_front", "wall_left", "wall_right", "menutitle",
            "scalesofjustice", "judgegavel", "menuspot", "winlight"
        };

        // Also clean old duplicate Floor, Ceiling, LeftWall, RightWall, FrontWall, BackWall
        string[] badExact = {
            "floor", "ceiling", "leftwall", "rightwall", "frontwall", "backwall"
        };

        List<GameObject> toDelete = new List<GameObject>();
        foreach (var go in scene.GetRootGameObjects())
        {
            string n = go.name.ToLowerInvariant();
            if (scene.name == "MainMenu" || scene.name == "GameComplete")
            {
                // Keep only Main Camera, Canvas, EventSystem, Managers in Menu/Complete
                if (n.Contains("camera") || n.Contains("canvas") || n.Contains("event") || n.Contains("manager"))
                    continue;
                toDelete.Add(go);
                continue;
            }

            if (badExact.Contains(n) || badPrefixes.Any(p => n.StartsWith(p)))
            {
                toDelete.Add(go);
            }
        }

        foreach (var go in toDelete)
        {
            if (go) Object.DestroyImmediate(go);
        }
    }

    // ═══════════════════════════════════════════════════════════════════════
    //  SEAMLESS HUMAN-SCALE ROOM ARCHITECTURE (15m x 15m, 4.2m height)
    // ═══════════════════════════════════════════════════════════════════════
    static void BuildSeamlessRoomShell(GameObject root, Material floorMat, Material wallMat, Material ceilingMat, float doorX = 0f)
    {
        // Solid Floor (15m x 15m) & Ceiling (4.2m high)
        AddPhysicalCube(root, "Room_Floor",   new Vector3(0, -0.10f, 0),    new Vector3(15f, 0.20f, 15f), floorMat);
        AddPhysicalCube(root, "Room_Ceiling", new Vector3(0,  4.20f, 0),    new Vector3(15f, 0.20f, 15f), ceilingMat);

        // Front, Left, Right Walls
        AddPhysicalCube(root, "Room_Wall_Front", new Vector3(0, 2.10f, -7.5f), new Vector3(15f, 4.20f, 0.30f), wallMat);
        AddPhysicalCube(root, "Room_Wall_Left",  new Vector3(-7.5f, 2.10f, 0), new Vector3(0.30f, 4.20f, 15f), wallMat);
        AddPhysicalCube(root, "Room_Wall_Right", new Vector3( 7.5f, 2.10f, 0), new Vector3(0.30f, 4.20f, 15f), wallMat);

        // Back Wall with intentional Doorway Opening (2.4m wide, 3.2m high) at doorX
        float totalW = 15f;
        float doorW  = 2.4f;
        float doorH  = 3.2f;
        float wallH  = 4.2f;

        float leftW  = (totalW * 0.5f + doorX) - doorW * 0.5f;
        float rightW = (totalW * 0.5f - doorX) - doorW * 0.5f;

        float leftCenter  = -totalW * 0.5f + leftW * 0.5f;
        float rightCenter =  totalW * 0.5f - rightW * 0.5f;

        if (leftW > 0.1f)
            AddPhysicalCube(root, "Room_Wall_Back_L", new Vector3(leftCenter, wallH * 0.5f, 7.5f), new Vector3(leftW, wallH, 0.30f), wallMat);
        if (rightW > 0.1f)
            AddPhysicalCube(root, "Room_Wall_Back_R", new Vector3(rightCenter, wallH * 0.5f, 7.5f), new Vector3(rightW, wallH, 0.30f), wallMat);

        float lintelH = wallH - doorH;
        AddPhysicalCube(root, "Room_Wall_Back_Top", new Vector3(doorX, doorH + lintelH * 0.5f, 7.5f), new Vector3(doorW, lintelH, 0.30f), wallMat);

        // Baseboard Skirting Trim
        Material trim = LoadMat("Trim_Black");
        AddCube(root, "Baseboard_Front", new Vector3(0, 0.12f, -7.32f), new Vector3(14.6f, 0.24f, 0.06f), trim);
        AddCube(root, "Baseboard_Left",  new Vector3(-7.32f, 0.12f, 0), new Vector3(0.06f, 0.24f, 14.6f), trim);
        AddCube(root, "Baseboard_Right", new Vector3( 7.32f, 0.12f, 0), new Vector3(0.06f, 0.24f, 14.6f), trim);
    }

    // ═══════════════════════════════════════════════════════════════════════
    //  LEVEL 1: INVESTIGATION OFFICE
    // ═══════════════════════════════════════════════════════════════════════
    static void BuildInvestigationRoom(GameObject root)
    {
        SetAmbient(new Color(0.14f, 0.12f, 0.10f));
        Material floor    = LoadMat("Floor_DarkWood");
        Material wallChar = LoadMat("Wall_Charcoal");
        Material wallWood = LoadMat("Wood_Walnut");
        Material ceiling  = LoadMat("Ceiling_Dark");
        Material gold     = LoadMat("Accent_Gold");
        Material frameMat = LoadMat("Frame_Dark");
        Material paperMat = LoadMat("Paper_Warm");
        Material corkMat  = LoadMat("Cork_Board");

        BuildSeamlessRoomShell(root, floor, wallChar, ceiling, 0f);

        // Architectural Wainscoting up to 1.4m
        AddCube(root, "Wainscot_L", new Vector3(-7.32f, 0.70f, 0), new Vector3(0.06f, 1.40f, 14.6f), wallWood);
        AddCube(root, "Wainscot_R", new Vector3( 7.32f, 0.70f, 0), new Vector3(0.06f, 1.40f, 14.6f), wallWood);
        AddCube(root, "ChairRail_L", new Vector3(-7.30f, 1.42f, 0), new Vector3(0.08f, 0.06f, 14.6f), gold);
        AddCube(root, "ChairRail_R", new Vector3( 7.30f, 1.42f, 0), new Vector3(0.08f, 0.06f, 14.6f), gold);

        // ── Primary Focal Point: Executive Investigator Workstation ──
        SpawnOfficePrefab(root, "Office/full_desk_1.prefab", new Vector3(0f, 0f, 3.2f), Quaternion.Euler(0, 180, 0), Vector3.one * 1.05f);
        SpawnOfficePrefab(root, "Office/office_chair.prefab", new Vector3(0f, 0f, 4.3f), Quaternion.Euler(0, 0, 0), Vector3.one * 1.05f);
        SpawnOfficePrefab(root, "Office/table_lamp.prefab", new Vector3(1.1f, 0.85f, 3.2f), Quaternion.identity, Vector3.one);
        AddPointLight(root, "DeskWarmLamp", new Vector3(1.1f, 1.4f, 3.2f), new Color(1f, 0.85f, 0.60f), 2.2f, 4.5f);

        // Visitor Lounge Area in front of desk
        SpawnOfficePrefab(root, "Furniture/coffee_table.prefab", new Vector3(0f, 0f, 0.8f), Quaternion.identity, Vector3.one * 0.95f);
        SpawnOfficePrefab(root, "Furniture/chair_1.prefab", new Vector3(-1.3f, 0f, 0.8f), Quaternion.Euler(0, 90, 0), Vector3.one);
        SpawnOfficePrefab(root, "Furniture/chair_1.prefab", new Vector3( 1.3f, 0f, 0.8f), Quaternion.Euler(0, -90, 0), Vector3.one);

        // Flush Bookshelves along Left Wall
        SpawnOfficePrefab(root, "Furniture/modern_shelves.prefab", new Vector3(-7.0f, 0f, 2.2f), Quaternion.Euler(0, 90, 0), Vector3.one * 1.15f);
        SpawnOfficePrefab(root, "Furniture/modern_shelves_2.prefab", new Vector3(-7.0f, 0f, -1.0f), Quaternion.Euler(0, 90, 0), Vector3.one * 1.15f);

        // Filing Cabinets along Right Wall
        SpawnOfficePrefab(root, "Furniture/drawer_simple.prefab", new Vector3(7.0f, 0f, 2.0f), Quaternion.Euler(0, -90, 0), Vector3.one * 1.1f);
        SpawnOfficePrefab(root, "Furniture/drawer_simple.prefab", new Vector3(7.0f, 0f, -1.0f), Quaternion.Euler(0, -90, 0), Vector3.one * 1.1f);

        // Framed Wall Art
        SpawnOfficePrefab(root, "Decoration/painting.prefab", new Vector3(-7.32f, 2.8f, 0.6f), Quaternion.Euler(0, 90, 0), Vector3.one * 1.3f);
        SpawnOfficePrefab(root, "Decoration/photo_frame_wall.prefab", new Vector3(7.32f, 2.8f, 0.6f), Quaternion.Euler(0, -90, 0), Vector3.one * 1.3f);

        // Investigation Evidence Board on Back Wall
        AddCube(root, "EvidenceBoard_Frame", new Vector3(-4.2f, 2.6f, 7.32f), new Vector3(3.8f, 2.0f, 0.08f), frameMat);
        AddCube(root, "EvidenceBoard_Cork",  new Vector3(-4.2f, 2.6f, 7.28f), new Vector3(3.5f, 1.7f, 0.06f), corkMat);
        AddCube(root, "Doc_Suspect",         new Vector3(-5.0f, 2.8f, 7.24f), new Vector3(0.55f, 0.7f, 0.02f), paperMat);
        AddCube(root, "Doc_CrimeScene",      new Vector3(-4.2f, 2.9f, 7.24f), new Vector3(0.65f, 0.5f, 0.02f), LoadMat("Evidence_Red"));
        AddCube(root, "Doc_Report",          new Vector3(-3.4f, 2.6f, 7.24f), new Vector3(0.55f, 0.7f, 0.02f), paperMat);
        AddWallText(root, "BoardHeader", "CASE #101: EVIDENCE BOARD", new Vector3(-4.2f, 3.4f, 7.20f), Gold, 2.0f);

        // Soft ambient room lighting
        AddPointLight(root, "CeilAmbient_1", new Vector3(0f, 3.8f, -1.5f), new Color(1f, 0.92f, 0.82f), 2.5f, 9f);
        AddPointLight(root, "CeilAmbient_2", new Vector3(0f, 3.8f,  3.0f), new Color(1f, 0.92f, 0.82f), 2.5f, 9f);
    }

    // ═══════════════════════════════════════════════════════════════════════
    //  LEVEL 2: CYBER INVESTIGATION ROOM
    // ═══════════════════════════════════════════════════════════════════════
    static void BuildCyberRoom(GameObject root)
    {
        SetAmbient(new Color(0.08f, 0.09f, 0.12f));
        Material floor   = LoadMat("Floor_CyberTile");
        Material wall    = LoadMat("Wall_CyberDark");
        Material ceiling = LoadMat("Ceiling_Dark");
        Material server  = LoadMat("Server_Dark");
        Material blueLED = LoadMat("Light_Emissive_Blue");

        BuildSeamlessRoomShell(root, floor, wall, ceiling, 0f);

        // ── Primary Focal Point: Central Dual-Monitor Cyber Workstation ──
        SpawnOfficePrefab(root, "Office/full_desk_2.prefab", new Vector3(0f, 0f, 3.0f), Quaternion.Euler(0, 180, 0), Vector3.one * 1.15f);
        SpawnOfficePrefab(root, "Office/office_chair.prefab", new Vector3(0f, 0f, 1.8f), Quaternion.identity, Vector3.one * 1.1f);
        AddPointLight(root, "TerminalScreenGlow", new Vector3(0f, 1.3f, 2.8f), Cyan, 2.5f, 4.5f);

        // Secondary Workstation along Right Wall
        SpawnOfficePrefab(root, "Office/full_desk_3.prefab", new Vector3(5.2f, 0f, 0.5f), Quaternion.Euler(0, -90, 0), Vector3.one * 1.05f);
        SpawnOfficePrefab(root, "Office/office_chair.prefab", new Vector3(4.0f, 0f, 0.5f), Quaternion.Euler(0, 90, 0), Vector3.one);

        // Realistic Server Racks along Left Wall (Matte Dark, Subtle LEDs - NO giant glowing billboards!)
        for (int z = -2; z <= 2; z += 2)
        {
            AddPhysicalCube(root, "Server_" + z, new Vector3(-6.8f, 1.8f, z), new Vector3(0.85f, 3.6f, 1.4f), server);
            AddCube(root, "ServerLED_" + z, new Vector3(-6.35f, 1.8f, z), new Vector3(0.02f, 3.2f, 1.2f), blueLED);
            AddPointLight(root, "ServerLight_" + z, new Vector3(-5.8f, 1.8f, z), Cyan, 1.2f, 3.0f);
        }

        // Modern Tech Equipment Shelves
        SpawnOfficePrefab(root, "Furniture/modern_shelves.prefab", new Vector3(6.8f, 0f, 3.0f), Quaternion.Euler(0, -90, 0), Vector3.one * 1.15f);

        // Wall Banner on Back Wall
        AddWallText(root, "CyberHeader", "CYBER FORENSIC LABORATORY", new Vector3(0f, 3.7f, 7.32f), Cyan, 3.2f);
        AddWallText(root, "CyberSub", "NETWORK ENCRYPTION & DATA ANALYSIS", new Vector3(0f, 3.2f, 7.32f), WarmWhite, 2.0f);

        // Soft moody cyber lighting
        AddPointLight(root, "CyberCeil_1", new Vector3(0f, 3.8f, -1.0f), new Color(0.2f, 0.5f, 0.85f), 2.5f, 8f);
        AddPointLight(root, "CyberCeil_2", new Vector3(0f, 3.8f,  3.0f), new Color(0.2f, 0.5f, 0.85f), 2.5f, 8f);
    }

    // ═══════════════════════════════════════════════════════════════════════
    //  LEVEL 3: FORENSIC EVIDENCE EXAMINATION ROOM
    // ═══════════════════════════════════════════════════════════════════════
    static void BuildEvidenceRoom(GameObject root)
    {
        SetAmbient(new Color(0.12f, 0.13f, 0.14f));
        Material floor   = LoadMat("Floor_Marble");
        Material wall    = LoadMat("Wall_LightGrey");
        Material ceiling = LoadMat("Ceiling_Mid");
        Material wood    = LoadMat("Wood_Walnut");
        Material frameMat= LoadMat("Frame_Dark");
        Material paperMat= LoadMat("Paper_Warm");

        BuildSeamlessRoomShell(root, floor, wall, ceiling, 0f);

        // ── Primary Focal Point: Central Evidence Examination Table ──
        AddPhysicalCube(root, "EvidenceTable_Top", new Vector3(0, 0.85f, 1.8f), new Vector3(5.8f, 0.12f, 2.2f), wood);
        AddPhysicalCube(root, "EvidenceTable_LegL", new Vector3(-2.6f, 0.40f, 1.8f), new Vector3(0.15f, 0.80f, 1.8f), wood);
        AddPhysicalCube(root, "EvidenceTable_LegR", new Vector3( 2.6f, 0.40f, 1.8f), new Vector3(0.15f, 0.80f, 1.8f), wood);

        // Table Lamps on each end
        SpawnOfficePrefab(root, "Office/table_lamp.prefab", new Vector3(-2.5f, 0.92f, 1.8f), Quaternion.identity, Vector3.one);
        SpawnOfficePrefab(root, "Office/table_lamp.prefab", new Vector3( 2.5f, 0.92f, 1.8f), Quaternion.identity, Vector3.one);
        AddPointLight(root, "ExamLight_L", new Vector3(-2.5f, 1.5f, 1.8f), new Color(1f, 0.95f, 0.85f), 2.0f, 4.0f);
        AddPointLight(root, "ExamLight_R", new Vector3( 2.5f, 1.5f, 1.8f), new Color(1f, 0.95f, 0.85f), 2.0f, 4.0f);

        // Yellow Evidence Markers 1, 2, 3
        AddEvidenceMarker(root, "Zone1_Tag", new Vector3(-1.8f, 0.98f, 1.5f), "1");
        AddEvidenceMarker(root, "Zone2_Tag", new Vector3( 0.0f, 0.98f, 1.5f), "2");
        AddEvidenceMarker(root, "Zone3_Tag", new Vector3( 1.8f, 0.98f, 1.5f), "3");

        // Shelves and Storage along Perimeter
        SpawnOfficePrefab(root, "Furniture/modern_shelves.prefab", new Vector3(-7.0f, 0f, 2.0f), Quaternion.Euler(0, 90, 0), Vector3.one * 1.15f);
        SpawnOfficePrefab(root, "Furniture/modern_shelves_2.prefab", new Vector3(7.0f, 0f, 2.0f), Quaternion.Euler(0, -90, 0), Vector3.one * 1.15f);

        // Protocol Wall Board
        AddCube(root, "EvidSignBack", new Vector3(0, 3.3f, 7.32f), new Vector3(5.5f, 1.4f, 0.06f), frameMat);
        AddCube(root, "EvidSignPaper", new Vector3(0, 3.3f, 7.28f), new Vector3(5.2f, 1.1f, 0.04f), paperMat);
        AddWallText(root, "EvidSignTitle", "FORENSIC EVIDENCE VAULT", new Vector3(0, 3.55f, 7.24f), CrimsonRed, 2.8f);
        AddWallText(root, "EvidSignSub", "CHAIN OF CUSTODY // VERIFICATION ZONE", new Vector3(0, 3.10f, 7.24f), new Color(0.15f, 0.15f, 0.15f), 1.8f);

        // Neutral, clear lab lighting
        AddPointLight(root, "LabLight_1", new Vector3(0f, 3.8f, -1.0f), new Color(0.95f, 0.98f, 1f), 3.0f, 9f);
        AddPointLight(root, "LabLight_2", new Vector3(0f, 3.8f,  2.5f), new Color(0.95f, 0.98f, 1f), 3.0f, 9f);
    }

    // ═══════════════════════════════════════════════════════════════════════
    //  LEVEL 4: RESTRICTED ARCHIVE
    // ═══════════════════════════════════════════════════════════════════════
    static void BuildArchiveRoom(GameObject root)
    {
        SetAmbient(new Color(0.10f, 0.08f, 0.06f));
        Material floor   = LoadMat("Floor_Concrete");
        Material wall    = LoadMat("Wall_Archive");
        Material ceiling = LoadMat("Ceiling_Dark");
        Material frameMat= LoadMat("Frame_Dark");

        BuildSeamlessRoomShell(root, floor, wall, ceiling, 0f);

        // ── Two Rows of Tall Shelves Creating a Natural Library Aisle ──
        float[] aisleZ = { -2.5f, 0.8f, 4.0f };
        foreach (float z in aisleZ)
        {
            SpawnOfficePrefab(root, "Furniture/modern_shelves_3.prefab", new Vector3(-4.5f, 0f, z), Quaternion.identity, Vector3.one * 1.25f);
            SpawnOfficePrefab(root, "Furniture/modern_shelves_3.prefab", new Vector3( 4.5f, 0f, z), Quaternion.identity, Vector3.one * 1.25f);
        }

        // Archive Book Piles
        SpawnOfficePrefab(root, "Decoration/book_pile_1.prefab", new Vector3(-3.8f, 1.2f, 0.8f), Quaternion.identity, Vector3.one * 1.3f);
        SpawnOfficePrefab(root, "Decoration/book_pile_2.prefab", new Vector3( 3.8f, 1.2f, -2.5f), Quaternion.identity, Vector3.one * 1.3f);

        // Signage
        AddCube(root, "ArchivSignBack", new Vector3(0, 3.5f, 7.32f), new Vector3(5.0f, 1.2f, 0.06f), frameMat);
        AddWallText(root, "ArchivSignTitle", "RESTRICTED ARCHIVES", new Vector3(0, 3.75f, 7.26f), Gold, 3.2f);
        AddWallText(root, "ArchivSignSub", "AUTHORIZED CLEARANCE LEVEL 4 ONLY", new Vector3(0, 3.30f, 7.26f), WarmWhite, 1.8f);

        // Warm archive sconces
        for (int z = -2; z <= 3; z += 3)
        {
            AddPointLight(root, "Lantern_L_" + z, new Vector3(-2.2f, 2.8f, z), new Color(1f, 0.78f, 0.45f), 2.2f, 5.5f);
            AddPointLight(root, "Lantern_R_" + z, new Vector3( 2.2f, 2.8f, z), new Color(1f, 0.78f, 0.45f), 2.2f, 5.5f);
        }
    }

    // ═══════════════════════════════════════════════════════════════════════
    //  LEVEL 5: CASE ANALYSIS & WITNESS STATEMENTS (NO GIANT BLOCKING WALL!)
    // ═══════════════════════════════════════════════════════════════════════
    static void BuildStatementsRoom(GameObject root)
    {
        SetAmbient(new Color(0.12f, 0.10f, 0.08f));
        Material floor   = LoadMat("Floor_DarkWood");
        Material wall    = LoadMat("Wall_CourtWood");
        Material ceiling = LoadMat("Ceiling_Dark");
        Material wood    = LoadMat("Wood_Walnut");
        Material frameMat= LoadMat("Frame_Dark");
        Material paperMat= LoadMat("Paper_Warm");

        BuildSeamlessRoomShell(root, floor, wall, ceiling, 0f);

        // ── Primary Focal Point: Executive Conference Table & Chairs ──
        AddPhysicalCube(root, "ConfTable", new Vector3(0, 0.85f, 1.5f), new Vector3(5.8f, 0.14f, 2.4f), wood);
        AddPhysicalCube(root, "ConfLegL",  new Vector3(-2.6f, 0.40f, 1.5f), new Vector3(0.15f, 0.80f, 2.0f), wood);
        AddPhysicalCube(root, "ConfLegR",  new Vector3( 2.6f, 0.40f, 1.5f), new Vector3(0.15f, 0.80f, 2.0f), wood);

        // Executive Chairs around table
        SpawnOfficePrefab(root, "Office/office_chair.prefab", new Vector3(-1.6f, 0f, 0.1f), Quaternion.Euler(0, 0, 0), Vector3.one * 1.05f);
        SpawnOfficePrefab(root, "Office/office_chair.prefab", new Vector3( 1.6f, 0f, 0.1f), Quaternion.Euler(0, 0, 0), Vector3.one * 1.05f);
        SpawnOfficePrefab(root, "Office/office_chair.prefab", new Vector3(-1.6f, 0f, 2.9f), Quaternion.Euler(0, 180, 0), Vector3.one * 1.05f);
        SpawnOfficePrefab(root, "Office/office_chair.prefab", new Vector3( 1.6f, 0f, 2.9f), Quaternion.Euler(0, 180, 0), Vector3.one * 1.05f);

        // Table Props
        SpawnOfficePrefab(root, "Decoration/notepad.prefab", new Vector3(-0.8f, 0.93f, 1.4f), Quaternion.identity, Vector3.one);
        SpawnOfficePrefab(root, "Decoration/notepad.prefab", new Vector3( 0.8f, 0.93f, 1.6f), Quaternion.identity, Vector3.one);
        SpawnOfficePrefab(root, "Office/table_lamp.prefab", new Vector3(0f, 0.93f, 1.5f), Quaternion.identity, Vector3.one);
        AddPointLight(root, "ConfLampGlow", new Vector3(0f, 1.5f, 1.5f), new Color(1f, 0.88f, 0.65f), 2.2f, 5.0f);

        // Side Credenzas
        SpawnOfficePrefab(root, "Furniture/counter_1.prefab", new Vector3(-6.5f, 0f, 1.5f), Quaternion.Euler(0, 90, 0), Vector3.one * 1.1f);
        SpawnOfficePrefab(root, "Furniture/counter_1.prefab", new Vector3( 6.5f, 0f, 1.5f), Quaternion.Euler(0, -90, 0), Vector3.one * 1.1f);

        // Witness Testimonies Board on Back Wall (Flush against wall, ZERO obstruction!)
        AddCube(root, "CaseDisplay_Frame", new Vector3(0, 3.0f, 7.32f), new Vector3(6.5f, 1.8f, 0.06f), frameMat);
        AddCube(root, "CaseDisplay_Bg",    new Vector3(0, 3.0f, 7.28f), new Vector3(6.2f, 1.5f, 0.04f), paperMat);
        AddWallText(root, "CaseTitle", "WITNESS TESTIMONIES & STATEMENTS", new Vector3(0, 3.45f, 7.24f), CrimsonRed, 2.8f);
        AddWallText(root, "CaseSub", "CROSS-EXAMINE AFFIDAVITS // DETECT PERJURY", new Vector3(0, 2.95f, 7.24f), new Color(0.15f, 0.15f, 0.15f), 1.8f);

        // Warm Chandelier Lighting
        AddPointLight(root, "ConfChandelier", new Vector3(0, 3.8f, 1.5f), new Color(1f, 0.88f, 0.68f), 3.5f, 9f);
    }

    // ═══════════════════════════════════════════════════════════════════════
    //  LEVEL 6: GRAND COURTROOM / FINAL VERDICT
    // ═══════════════════════════════════════════════════════════════════════
    static void BuildCourtroom(GameObject root)
    {
        SetAmbient(new Color(0.24f, 0.21f, 0.18f));
        Material floor    = LoadMat("Floor_DarkWood");
        Material wall     = LoadMat("Wall_CourtWood");
        Material ceiling  = LoadMat("Ceiling_Court");
        Material richWood = LoadMat("Wood_Dark");
        Material gold     = LoadMat("Accent_Gold");
        Material carpet   = LoadMat("Rug_Dark");

        BuildSeamlessRoomShell(root, floor, wall, ceiling, 5.5f);

        // Central Red Carpet Runner
        AddCube(root, "CourtCarpet", new Vector3(0, 0.01f, 0), new Vector3(3.2f, 0.02f, 14.5f), carpet);

        // ── Primary Focal Point: Elevated Judge Bench ──
        AddPhysicalCube(root, "JudgePlatform",    new Vector3(0, 0.35f, 5.2f), new Vector3(8.5f, 0.70f, 2.8f), richWood);
        AddPhysicalCube(root, "JudgeBench_Front", new Vector3(0, 1.35f, 4.2f), new Vector3(7.5f, 1.80f, 0.20f), richWood);
        AddPhysicalCube(root, "JudgeBench_Top",   new Vector3(0, 2.25f, 4.8f), new Vector3(7.8f, 0.15f, 2.2f), richWood);

        // High-Backed Judge Chair
        SpawnOfficePrefab(root, "Office/office_chair.prefab", new Vector3(0, 0.70f, 5.6f), Quaternion.identity, Vector3.one * 1.3f);

        // Law Books & Gavel on Bench
        SpawnOfficePrefab(root, "Decoration/book_pile_1.prefab", new Vector3(-2.2f, 2.35f, 4.5f), Quaternion.identity, Vector3.one * 1.2f);
        BuildGavel(root, new Vector3(2.2f, 2.35f, 4.5f));

        // National Scales of Justice & Emblem
        BuildScalesOfJustice(root, new Vector3(0, 2.35f, 4.6f), 1.1f);
        AddCylinder(root, "JusticeEmblem_Ring", new Vector3(0, 3.8f, 7.32f), new Vector3(1.6f, 0.04f, 1.6f), gold);
        AddWallText(root, "EmblemText", "SATYAMEVA JAYATE", new Vector3(0, 3.8f, 7.28f), Gold, 2.2f);
        AddWallText(root, "TruthSign", "TRUTH ALWAYS PREVAILS", new Vector3(0, 3.3f, 7.28f), WarmWhite, 2.4f);

        // Indian Flags flanking Judge Bench
        BuildIndianFlag(root, "Flag_Left",  new Vector3(-3.5f, 3.2f, 7.32f));
        BuildIndianFlag(root, "Flag_Right", new Vector3( 3.5f, 3.2f, 7.32f));

        // Witness Stand on Left
        AddPhysicalCube(root, "WitnessBox_Base",  new Vector3(-5.2f, 0.25f, 3.6f), new Vector3(2.0f, 0.50f, 2.0f), richWood);
        AddPhysicalCube(root, "WitnessBox_Front", new Vector3(-5.2f, 0.85f, 2.7f), new Vector3(2.0f, 1.00f, 0.10f), richWood);
        AddPhysicalCube(root, "WitnessBox_Side",  new Vector3(-4.3f, 0.85f, 3.6f), new Vector3(0.10f, 1.00f, 2.0f), richWood);
        SpawnOfficePrefab(root, "Office/office_chair.prefab", new Vector3(-5.2f, 0.50f, 3.8f), Quaternion.identity, Vector3.one);

        // Prosecution Desk (Right) & Defense Desk (Left)
        SpawnOfficePrefab(root, "Office/full_desk_1.prefab", new Vector3( 3.2f, 0f, 1.4f), Quaternion.Euler(0, -90, 0), Vector3.one);
        SpawnOfficePrefab(root, "Office/office_chair.prefab", new Vector3( 3.2f, 0f, 0.4f), Quaternion.identity, Vector3.one);

        SpawnOfficePrefab(root, "Office/full_desk_1.prefab", new Vector3(-3.2f, 0f, 1.4f), Quaternion.Euler(0, 90, 0), Vector3.one);
        SpawnOfficePrefab(root, "Office/office_chair.prefab", new Vector3(-3.2f, 0f, 0.4f), Quaternion.identity, Vector3.one);

        // Spectator Gallery Railing & Benches in rear
        AddPhysicalCube(root, "GalleryRailing_L", new Vector3(-3.8f, 0.55f, -1.8f), new Vector3(5.5f, 1.10f, 0.12f), richWood);
        AddPhysicalCube(root, "GalleryRailing_R", new Vector3( 3.8f, 0.55f, -1.8f), new Vector3(5.5f, 1.10f, 0.12f), richWood);

        for (int z = -4; z <= -2; z += 2)
        {
            AddPhysicalCube(root, "Bench_L_" + z, new Vector3(-4.0f, 0.40f, z), new Vector3(4.5f, 0.40f, 0.6f), richWood);
            AddPhysicalCube(root, "Bench_R_" + z, new Vector3( 4.0f, 0.40f, z), new Vector3(4.5f, 0.40f, 0.6f), richWood);
        }

        // Courtroom Lighting
        AddPointLight(root, "JudgeChandelier", new Vector3(0, 3.8f, 4.0f), new Color(1f, 0.92f, 0.78f), 4.5f, 12f);
        AddPointLight(root, "GalleryChandelier", new Vector3(0, 3.8f, -2.0f), new Color(1f, 0.92f, 0.78f), 4.0f, 10f);
        AddPointLight(root, "CenterChandelier", new Vector3(0, 3.8f, 1.0f), new Color(1f, 0.92f, 0.78f), 4.0f, 10f);
    }

    // ═══════════════════════════════════════════════════════════════════════
    //  MAIN MENU (CLEAN 2D CINEMATIC - ZERO 3D OVERLAPS)
    // ═══════════════════════════════════════════════════════════════════════
    static void BuildMainMenuRoom(GameObject root)
    {
        // Absolutely NO 3D cubes, text, gavels, or scales in MainMenu!
        // Camera clears to solid black behind 2D Canvas
        var cam = Object.FindFirstObjectByType<Camera>();
        if (cam)
        {
            cam.clearFlags = CameraClearFlags.SolidColor;
            cam.backgroundColor = new Color(0.04f, 0.05f, 0.08f, 1f);
        }

        ApplyCinematicBackground("Assets/CipherCourtPolish/Backgrounds/Menu_Legal_Cinematic.png");
        StyleMainMenuUI();
    }

    // ═══════════════════════════════════════════════════════════════════════
    //  GAME COMPLETE (CLEAN 2D CINEMATIC)
    // ═══════════════════════════════════════════════════════════════════════
    static void BuildGameCompleteRoom(GameObject root)
    {
        var cam = Object.FindFirstObjectByType<Camera>();
        if (cam)
        {
            cam.clearFlags = CameraClearFlags.SolidColor;
            cam.backgroundColor = new Color(0.04f, 0.05f, 0.08f, 1f);
        }

        ApplyCinematicBackground("Assets/CipherCourtPolish/Backgrounds/Complete_Legal_Cinematic.png");
        StyleGameCompleteUI();
    }

    // ═══════════════════════════════════════════════════════════════════════
    //  DOOR REVEAL & EXTENDED LIT CORRIDOR
    // ═══════════════════════════════════════════════════════════════════════
    static void AddDoorReveal(GameObject root, GameObject door)
    {
        Vector3 c = door.transform.position;
        Material frameMat = LoadMat("Trim_Black");

        float doorW = 2.4f;
        float doorH = 3.0f;

        // Side Jambs and Top Header
        AddCube(root, "DoorJamb_L", c + new Vector3(-doorW * 0.5f - 0.10f, 0, 0), new Vector3(0.15f, doorH, 0.20f), frameMat);
        AddCube(root, "DoorJamb_R", c + new Vector3( doorW * 0.5f + 0.10f, 0, 0), new Vector3(0.15f, doorH, 0.20f), frameMat);
        AddCube(root, "DoorJamb_T", c + new Vector3(0, doorH * 0.5f + 0.10f, 0),  new Vector3(doorW + 0.35f, 0.15f, 0.20f), frameMat);
        AddWallText(root, "ExitHeader", "SECURE EXIT", c + new Vector3(0, doorH * 0.5f + 0.32f, -0.06f), Gold, 2.0f);

        // Fully enclosed 3D lit corridor behind door
        AddDoorPassageBacking(root, c);
    }

    static void AddDoorPassageBacking(GameObject root, Vector3 doorPos)
    {
        Material wallDark  = LoadMat("Wall_Charcoal");
        Material floorWood = LoadMat("Floor_DarkWood");
        Material carpet    = LoadMat("Rug_Dark");

        float pw = 2.8f;
        float ph = 3.4f;
        float pd = 3.5f;
        Vector3 pc = doorPos + new Vector3(0, 0, pd * 0.5f + 0.05f);

        // Physical solid floor, walls, and ceiling - player CANNOT fall into void!
        AddPhysicalCube(root, "Passage_Floor",  pc + new Vector3(0, -0.05f, 0), new Vector3(pw, 0.10f, pd), floorWood);
        AddCube(root, "Passage_Carpet", pc + new Vector3(0,  0.01f, 0), new Vector3(1.4f, 0.02f, pd), carpet);
        AddPhysicalCube(root, "Passage_WallL",  pc + new Vector3(-pw * 0.5f, ph * 0.5f, 0), new Vector3(0.10f, ph, pd), wallDark);
        AddPhysicalCube(root, "Passage_WallR",  pc + new Vector3( pw * 0.5f, ph * 0.5f, 0), new Vector3(0.10f, ph, pd), wallDark);
        AddPhysicalCube(root, "Passage_Ceil",   pc + new Vector3(0, ph, 0), new Vector3(pw, 0.10f, pd), wallDark);
        AddPhysicalCube(root, "Passage_Back",   pc + new Vector3(0, ph * 0.5f, pd * 0.5f), new Vector3(pw, ph, 0.10f), wallDark);

        AddPointLight(root, "PassageGlow", pc + new Vector3(0, ph * 0.70f, 0), new Color(0.2f, 0.95f, 0.5f), 3.5f, 6.0f);
        AddWallText(root, "PassageText", "SECURE EXIT // PROCEED", pc + new Vector3(0, ph * 0.60f, pd * 0.46f), Gold, 2.2f);
    }

    // ═══════════════════════════════════════════════════════════════════════
    //  INTERACTIVE CLUE PROPS & POSITIONS
    // ═══════════════════════════════════════════════════════════════════════
    static void PositionInteractiveObjects(Scene scene, GameObject root)
    {
        Vector3 doorPos = scene.name == "Level6_FinalVerdict" ? new Vector3(5.5f, 1.5f, 7.4f) : new Vector3(0f, 1.5f, 7.4f);

        // Align Exit Door Mesh
        var door = scene.GetRootGameObjects()
            .FirstOrDefault(g => g != null && (g.name == "Door" || g.name.ToLowerInvariant().Contains("exitdoor")));
        if (door)
        {
            door.transform.position = doorPos;
            AddDoorReveal(root, door);
        }

        // Align LevelExit Trigger so walking through the doorway reliably finishes the level
        var exitObj = scene.GetRootGameObjects()
            .FirstOrDefault(g => g != null && (g.name == "LevelExit" || g.GetComponent<LevelExit>() != null || g.GetComponent<FinalLevelExit>() != null));
        if (exitObj)
        {
            exitObj.transform.position = doorPos + new Vector3(0, 0, 0.8f);
            var col = exitObj.GetComponent<BoxCollider>();
            if (!col) col = exitObj.AddComponent<BoxCollider>();
            col.isTrigger = true;
            col.center = Vector3.zero;
            col.size = new Vector3(2.5f, 3.2f, 2.5f);
        }

        switch (scene.name)
        {
            case "Level1_Investigation":
                var collectables = Object.FindObjectsByType<CollectibleItem>(FindObjectsSortMode.None)
                    .Where(c => c != null && c.gameObject != null).ToList();
                GameObject clue1 = collectables.FirstOrDefault(c => c.name.ToLowerInvariant().Contains("clue") || c.name.ToLowerInvariant().Contains("evidence"))?.gameObject;
                GameObject key1  = collectables.FirstOrDefault(c => c.name.ToLowerInvariant().Contains("key") || (clue1 != null && c.gameObject != clue1))?.gameObject;

                if (!clue1)
                {
                    clue1 = new GameObject("InvestigationClue_Item");
                    clue1.AddComponent<CollectibleItem>();
                }
                clue1.transform.position = new Vector3(-0.5f, 0.95f, 3.2f);
                CreateRealisticDossierProp(clue1, "CONFIDENTIAL CASE FILE", LoadMat("Folder_Red"));
                HighlightClue(root, clue1, "Inspect Confidential Dossier", Gold);

                if (!key1)
                {
                    key1 = new GameObject("SecurityKey_Item");
                    var keyComp = key1.AddComponent<CollectibleItem>();
                    var typeField = typeof(CollectibleItem).GetField("itemType", System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Instance);
                    if (typeField != null) typeField.SetValue(keyComp, CollectibleItem.ItemType.Key);
                }
                key1.transform.position = new Vector3(0.5f, 0.95f, 3.2f);
                CreateRealisticKeyProp(key1);
                HighlightClue(root, key1, "Collect Security Key", Gold);
                break;

            case "Level2_Computer":
                var passClueComp = Object.FindFirstObjectByType<PasswordClue>();
                GameObject clue2 = passClueComp ? passClueComp.gameObject : null;
                if (!clue2)
                {
                    clue2 = new GameObject("PasswordClue_Item");
                    clue2.AddComponent<PasswordClue>();
                }
                clue2.transform.position = new Vector3(5.0f, 0.92f, 0.5f);
                CreateRealisticUsbProp(clue2);
                HighlightClue(root, clue2, "Inspect Encrypted USB Drive", Cyan);

                var term2 = Object.FindObjectsByType<GameObject>(FindObjectsSortMode.None)
                    .FirstOrDefault(g => g != null && g.transform != null && (g.transform.parent == null || g.transform.parent.name != RootName) && (g.name.ToLowerInvariant().Contains("computerterminal") || g.name.ToLowerInvariant().Contains("terminal")));
                if (term2)
                {
                    term2.transform.position = new Vector3(0f, 0.95f, 2.5f);
                    HighlightClue(root, term2, "Access Cyber Terminal", Cyan);
                }
                break;

            case "Level3_Evidence":
                var evItems = Object.FindObjectsByType<EvidenceItem>(FindObjectsSortMode.None)
                    .Where(e => e != null && e.gameObject != null)
                    .Select(e => e.gameObject)
                    .ToList();
                if (evItems.Count == 0)
                {
                    evItems = Object.FindObjectsByType<GameObject>(FindObjectsSortMode.None)
                        .Where(g => g != null && g.transform != null && (g.transform.parent == null || g.transform.parent.name != RootName) &&
                               (g.name.ToLowerInvariant().Contains("evidence_a") || g.name.ToLowerInvariant().Contains("evidence_b") || g.name.ToLowerInvariant().Contains("evidence_c") ||
                               (g.name.ToLowerInvariant().Contains("evidence") && !g.name.ToLowerInvariant().Contains("terminal") && !g.name.ToLowerInvariant().Contains("puzzle") && !g.name.ToLowerInvariant().Contains("light") && !g.name.ToLowerInvariant().Contains("door") && !g.name.ToLowerInvariant().Contains("canvas") && !g.name.ToLowerInvariant().Contains("camera") && !g.name.ToLowerInvariant().Contains("room"))))
                        .ToList();
                }
                Vector3[] slots3 = { new Vector3(-1.8f, 0.95f, 1.8f), new Vector3(0.0f, 0.95f, 1.8f), new Vector3(1.8f, 0.95f, 1.8f) };
                string[] labels3 = { "Evidence A: Forensic USB", "Evidence B: Suspect ID Report", "Evidence C: Autopsy Dossier" };
                int idx3 = 0;
                foreach (var f in evItems)
                {
                    if (!f || f.transform == null) continue;
                    if (f.transform.parent != null && f.transform.parent.name == RootName) continue;
                    if (idx3 < slots3.Length)
                    {
                        f.transform.position = slots3[idx3];
                        if (idx3 == 0) CreateRealisticUsbProp(f);
                        else if (idx3 == 1) CreateRealisticPhotoProp(f);
                        else CreateRealisticDossierProp(f, "AUTOPSY REPORT", LoadMat("Paper_Warm"));

                        HighlightClue(root, f, labels3[idx3], Gold);
                        idx3++;
                    }
                }

                var evTerm = Object.FindFirstObjectByType<EvidencePuzzleInteraction>();
                GameObject term3 = evTerm ? evTerm.gameObject :
                    Object.FindObjectsByType<GameObject>(FindObjectsSortMode.None)
                        .FirstOrDefault(g => g != null && g.transform != null && (g.transform.parent == null || g.transform.parent.name != RootName) && (g.name.ToLowerInvariant().Contains("evidenceterminal") || (g.name.ToLowerInvariant().Contains("terminal") && !g.name.ToLowerInvariant().Contains("computer"))));
                if (term3)
                {
                    term3.transform.position = new Vector3(0f, 0.95f, 3.8f);
                    HighlightClue(root, term3, "Submit Evidence Code", Gold);
                }
                break;

            case "Level4_Archive":
                var clues4 = Object.FindObjectsByType<Level4Clue>(FindObjectsSortMode.None)
                    .Where(c => c != null && c.gameObject != null)
                    .Select(c => c.gameObject)
                    .ToList();
                if (clues4.Count == 0)
                {
                    clues4 = Object.FindObjectsByType<GameObject>(FindObjectsSortMode.None)
                        .Where(g => g != null && g.transform != null && (g.transform.parent == null || g.transform.parent.name != RootName) && g.name.ToLowerInvariant().Contains("clue"))
                        .ToList();
                }
                Vector3[] slots4 = { new Vector3(-4.0f, 1.35f, 3.2f), new Vector3(4.0f, 1.35f, 0.8f), new Vector3(-4.0f, 1.35f, -2.5f) };
                string[] labels4 = { "Inspect Case Ledger", "Inspect Tagged Archive Box", "Inspect Restricted Keycard" };
                for (int i = 0; i < clues4.Count && i < slots4.Length; i++)
                {
                    if (!clues4[i] || clues4[i].transform == null) continue;
                    clues4[i].transform.position = slots4[i];
                    if (i == 0) CreateRealisticLedgerProp(clues4[i]);
                    else if (i == 1) CreateRealisticBoxProp(clues4[i]);
                    else CreateRealisticKeycardProp(clues4[i]);

                    HighlightClue(root, clues4[i], labels4[i], Gold);
                }

                var archiveKeypadComp = Object.FindFirstObjectByType<ArchiveKeypad>();
                GameObject keypad4 = archiveKeypadComp ? archiveKeypadComp.gameObject :
                    Object.FindObjectsByType<GameObject>(FindObjectsSortMode.None)
                        .FirstOrDefault(g => g != null && g.transform != null && (g.transform.parent == null || g.transform.parent.name != RootName) && g.name.ToLowerInvariant().Contains("keypad"));

                if (!keypad4)
                {
                    keypad4 = new GameObject("ArchiveKeypad_Terminal");
                    keypad4.AddComponent<ArchiveKeypad>();
                }
                keypad4.transform.position = new Vector3(1.8f, 1.30f, 7.3f);
                BuildWallMountedKeypadConsole(root, keypad4);
                HighlightClue(root, keypad4, "Use Electronic Keypad", Gold);

                var l4Puzzle = Object.FindFirstObjectByType<Level4ArchivePuzzle>();
                var akScript = keypad4.GetComponent<ArchiveKeypad>();
                if (akScript && l4Puzzle) akScript.puzzle = l4Puzzle;
                break;

            case "Level5_CaseFiles":
                var files5 = Object.FindObjectsByType<Level5File>(FindObjectsSortMode.None)
                    .Where(f => f != null && f.gameObject != null)
                    .Select(f => f.gameObject)
                    .ToList();
                if (files5.Count == 0)
                {
                    files5 = Object.FindObjectsByType<GameObject>(FindObjectsSortMode.None)
                        .Where(g => g != null && g.transform != null && (g.transform.parent == null || g.transform.parent.name != RootName) && (g.name.ToLowerInvariant().Contains("file") || g.name.ToLowerInvariant().Contains("statement")))
                        .ToList();
                }
                Vector3[] slots5 = { new Vector3(-1.6f, 0.95f, 1.5f), new Vector3(0.0f, 0.95f, 1.5f), new Vector3(1.6f, 0.95f, 1.5f) };
                Material[] mats5 = { LoadMat("Folder_Red"), LoadMat("Flag_Green"), LoadMat("Flag_Blue") };
                string[] names5 = { "Statement A: Key Witness", "Statement B: Primary Suspect", "Statement C: Expert Forensic" };

                for (int i = 0; i < files5.Count && i < slots5.Length; i++)
                {
                    if (!files5[i] || files5[i].transform == null) continue;
                    if (files5[i].transform.parent != null && files5[i].transform.parent.name == RootName) continue;
                    files5[i].transform.position = slots5[i];
                    CreateRealisticDossierProp(files5[i], names5[i], mats5[i]);
                    HighlightClue(root, files5[i], "Inspect " + names5[i], Gold);
                }

                var term5Comp = Object.FindFirstObjectByType<Level5Terminal>();
                GameObject term5 = term5Comp ? term5Comp.gameObject :
                    Object.FindObjectsByType<GameObject>(FindObjectsSortMode.None)
                        .FirstOrDefault(g => g != null && g.transform != null && (g.transform.parent == null || g.transform.parent.name != RootName) && g.name.ToLowerInvariant().Contains("terminal"));
                if (term5)
                {
                    term5.transform.position = new Vector3(0f, 0.95f, 3.8f);
                    HighlightClue(root, term5, "Access Case File Terminal", Gold);
                }
                break;

            case "Level6_FinalVerdict":
                var statements6 = Object.FindObjectsByType<Level6Statement>(FindObjectsSortMode.None)
                    .Where(s => s != null && s.gameObject != null)
                    .Select(s => s.gameObject)
                    .ToList();
                if (statements6.Count == 0)
                {
                    statements6 = Object.FindObjectsByType<GameObject>(FindObjectsSortMode.None)
                        .Where(g => g != null && g.transform != null && (g.transform.parent == null || g.transform.parent.name != RootName) && (g.name.ToLowerInvariant().Contains("statement") || g.name.ToLowerInvariant().Contains("clue")))
                        .ToList();
                }
                Vector3[] slots6 = { new Vector3(-3.2f, 0.95f, 1.4f), new Vector3(3.2f, 0.95f, 1.4f), new Vector3(-5.2f, 0.95f, 3.6f) };
                for (int i = 0; i < statements6.Count && i < slots6.Length; i++)
                {
                    if (!statements6[i] || statements6[i].transform == null) continue;
                    if (statements6[i].transform.parent != null && statements6[i].transform.parent.name == RootName) continue;
                    statements6[i].transform.position = slots6[i];
                    CreateRealisticDossierProp(statements6[i], "EVIDENCE EXHIBIT #" + (i + 1), LoadMat("Folder_Red"));
                    HighlightClue(root, statements6[i], "Inspect Court Exhibit #" + (i + 1), Gold);
                }
                var term6Comp = Object.FindFirstObjectByType<Level6Terminal>();
                GameObject term6 = term6Comp ? term6Comp.gameObject :
                    Object.FindObjectsByType<GameObject>(FindObjectsSortMode.None)
                        .FirstOrDefault(g => g != null && g.transform != null && (g.transform.parent == null || g.transform.parent.name != RootName) && (g.name.ToLowerInvariant().Contains("terminal") || g.name.ToLowerInvariant().Contains("verdict")));
                if (term6)
                {
                    term6.transform.position = new Vector3(0.0f, 0.95f, 3.2f);
                    HighlightClue(root, term6, "Deliver Final Verdict", CrimsonRed);
                }
                break;
        }
    }

    // ═══════════════════════════════════════════════════════════════════════
    //  REALISTIC 3D CLUE MESH BUILDERS
    // ═══════════════════════════════════════════════════════════════════════
    static void CleanOldClueVisuals(GameObject target)
    {
        if (!target || target.transform == null) return;
        for (int i = target.transform.childCount - 1; i >= 0; i--)
        {
            var child = target.transform.GetChild(i);
            if (!child) continue;
            if (child.name.StartsWith("ClueVisual") || child.name.StartsWith("ClueBeacon"))
                Object.DestroyImmediate(child.gameObject);
        }
        var r = target.GetComponent<MeshRenderer>();
        if (r) r.enabled = false;
    }

    static void CreateRealisticDossierProp(GameObject target, string label, Material folderMat)
    {
        CleanOldClueVisuals(target);
        GameObject visual = new GameObject("ClueVisual_Dossier");
        visual.transform.SetParent(target.transform, false);
        visual.transform.localPosition = Vector3.zero;

        AddCube(visual, "Cover", new Vector3(0, 0.02f, 0), new Vector3(0.50f, 0.03f, 0.70f), folderMat);
        AddCube(visual, "Pages", new Vector3(0.02f, 0.025f, 0), new Vector3(0.48f, 0.025f, 0.68f), LoadMat("Paper_Warm"));
        AddCube(visual, "Seal", new Vector3(0, 0.038f, 0.18f), new Vector3(0.15f, 0.01f, 0.15f), LoadMat("Evidence_Red"));
    }

    static void CreateRealisticKeyProp(GameObject target)
    {
        CleanOldClueVisuals(target);
        GameObject visual = new GameObject("ClueVisual_Key");
        visual.transform.SetParent(target.transform, false);
        visual.transform.localPosition = Vector3.zero;

        Material gold = LoadMat("Metal_Gold");
        AddCylinder(visual, "Ring", new Vector3(0, 0.02f, -0.12f), new Vector3(0.12f, 0.02f, 0.12f), gold);
        AddCube(visual, "Shaft", new Vector3(0, 0.02f, 0.04f), new Vector3(0.035f, 0.02f, 0.30f), gold);
        AddCube(visual, "Tooth", new Vector3(0.035f, 0.02f, 0.14f), new Vector3(0.04f, 0.02f, 0.04f), gold);
    }

    static void CreateRealisticUsbProp(GameObject target)
    {
        CleanOldClueVisuals(target);
        GameObject visual = new GameObject("ClueVisual_USB");
        visual.transform.SetParent(target.transform, false);
        visual.transform.localPosition = Vector3.zero;

        AddCube(visual, "Body", new Vector3(0, 0.02f, 0), new Vector3(0.14f, 0.035f, 0.32f), LoadMat("Trim_Black"));
        AddCube(visual, "Tip", new Vector3(0, 0.02f, 0.20f), new Vector3(0.10f, 0.025f, 0.10f), LoadMat("Metal_Dark"));
        AddCube(visual, "LED", new Vector3(0, 0.04f, -0.07f), new Vector3(0.03f, 0.01f, 0.03f), LoadMat("Light_Emissive_Blue"));
    }

    static void CreateRealisticPhotoProp(GameObject target)
    {
        CleanOldClueVisuals(target);
        GameObject visual = new GameObject("ClueVisual_Photo");
        visual.transform.SetParent(target.transform, false);
        visual.transform.localPosition = Vector3.zero;

        AddCube(visual, "Paper", new Vector3(0, 0.01f, 0), new Vector3(0.42f, 0.015f, 0.32f), LoadMat("Paper_Warm"));
        AddCube(visual, "Inner", new Vector3(0, 0.018f, 0), new Vector3(0.36f, 0.01f, 0.26f), LoadMat("Frame_Dark"));
    }

    static void CreateRealisticLedgerProp(GameObject target)
    {
        CleanOldClueVisuals(target);
        GameObject visual = new GameObject("ClueVisual_Ledger");
        visual.transform.SetParent(target.transform, false);
        visual.transform.localPosition = Vector3.zero;

        AddCube(visual, "Cover", new Vector3(0, 0.04f, 0), new Vector3(0.55f, 0.08f, 0.75f), LoadMat("Leather_Dark"));
        AddCube(visual, "Pages", new Vector3(0.02f, 0.04f, 0), new Vector3(0.52f, 0.07f, 0.72f), LoadMat("Paper_Warm"));
    }

    static void CreateRealisticBoxProp(GameObject target)
    {
        CleanOldClueVisuals(target);
        GameObject visual = new GameObject("ClueVisual_Box");
        visual.transform.SetParent(target.transform, false);
        visual.transform.localPosition = Vector3.zero;

        AddCube(visual, "Crate", new Vector3(0, 0.22f, 0), new Vector3(0.55f, 0.44f, 0.55f), LoadMat("Archive_Box"));
        AddCube(visual, "Tag", new Vector3(0, 0.22f, 0.28f), new Vector3(0.22f, 0.15f, 0.02f), LoadMat("Paper_Warm"));
    }

    static void CreateRealisticKeycardProp(GameObject target)
    {
        CleanOldClueVisuals(target);
        GameObject visual = new GameObject("ClueVisual_Keycard");
        visual.transform.SetParent(target.transform, false);
        visual.transform.localPosition = Vector3.zero;

        AddCube(visual, "Card", new Vector3(0, 0.01f, 0), new Vector3(0.22f, 0.012f, 0.35f), LoadMat("White_Mat"));
        AddCube(visual, "Chip", new Vector3(0, 0.016f, 0.06f), new Vector3(0.08f, 0.01f, 0.06f), LoadMat("Metal_Gold"));
    }

    static void BuildWallMountedKeypadConsole(GameObject root, GameObject keypadObj)
    {
        if (!keypadObj) return;
        for (int i = keypadObj.transform.childCount - 1; i >= 0; i--)
            Object.DestroyImmediate(keypadObj.transform.GetChild(i).gameObject);

        Material metal = LoadMat("Metal_Dark");
        Material screen = LoadMat("Screen_Cyan");
        Material gold = LoadMat("Accent_Gold");

        GameObject visual = new GameObject("KeypadConsoleVisual");
        visual.transform.SetParent(keypadObj.transform, false);
        visual.transform.localPosition = Vector3.zero;

        AddCube(visual, "Plate", new Vector3(0, 0, 0), new Vector3(0.45f, 0.65f, 0.08f), metal);
        AddCube(visual, "LCD",   new Vector3(0, 0.18f, -0.05f), new Vector3(0.35f, 0.18f, 0.03f), screen);
        AddCube(visual, "Keys",  new Vector3(0, -0.12f, -0.05f), new Vector3(0.35f, 0.28f, 0.03f), gold);

        AddPointLight(visual, "ConsoleLight", new Vector3(0, 0.18f, -0.2f), Cyan, 1.5f, 2.5f);
    }

    static void HighlightClue(GameObject root, GameObject target, string promptText, Color beaconColor)
    {
        if (!target) return;

        var old = target.transform.Find("ClueBeacon");
        if (old) Object.DestroyImmediate(old.gameObject);

        GameObject beacon = new GameObject("ClueBeacon");
        beacon.transform.SetParent(target.transform, false);
        beacon.transform.localPosition = Vector3.up * 0.65f;

        Light l = beacon.AddComponent<Light>();
        l.type = LightType.Point;
        l.color = beaconColor;
        l.intensity = 1.8f;
        l.range = 3.0f;
        l.shadows = LightShadows.None;

        GameObject pin = GameObject.CreatePrimitive(PrimitiveType.Sphere);
        pin.name = "Pin";
        pin.transform.SetParent(beacon.transform, false);
        pin.transform.localPosition = Vector3.zero;
        pin.transform.localScale = Vector3.one * 0.12f;
        var col = pin.GetComponent<Collider>();
        if (col) Object.DestroyImmediate(col);
        var r = pin.GetComponent<Renderer>();
        if (r) r.sharedMaterial = LoadMat("Light_Emissive_Warm");

        AddWallText(beacon, "Prompt", "[ E ] " + promptText, Vector3.up * 0.30f, Gold, 1.8f);
    }

    // ═══════════════════════════════════════════════════════════════════════
    //  UI REDESIGN (CLEAN DIALOGS, COMPACT CARDS, SLEEK HUD)
    // ═══════════════════════════════════════════════════════════════════════
    static void PolishUI(Scene scene)
    {
        Sprite cardSprite   = LoadUISprite("panel_glass_card.png");
        Sprite crimsonNorm  = LoadUISprite("btn_crimson_normal.png");
        Sprite darkNorm     = LoadUISprite("btn_charcoal_normal.png");
        Sprite hudSprite    = LoadUISprite("hud_badge.png");

        // 1. Re-style all Puzzle Panels to Compact, Centered Investigation Cards (NOT screen-stretching bars!)
        string[] panelKeywords = { "puzzlepanel", "evidencepanel", "keypadpanel", "passwordpanel", "casepanel", "verdictpanel" };
        foreach (var img in Object.FindObjectsByType<Image>(FindObjectsSortMode.None))
        {
            if (!img) continue;
            string n = img.name.ToLowerInvariant();
            if (panelKeywords.Any(k => n.Contains(k)))
            {
                RectTransform rt = img.rectTransform;
                rt.anchorMin = new Vector2(0.5f, 0.5f);
                rt.anchorMax = new Vector2(0.5f, 0.5f);
                rt.pivot     = new Vector2(0.5f, 0.5f);
                rt.sizeDelta = new Vector2(480f, 340f);

                if (cardSprite)
                {
                    img.sprite = cardSprite;
                    img.type = Image.Type.Sliced;
                    img.color = Color.white;
                }
            }
        }

        // 2. Style Input Fields with Dark Background & Subtle Border
        foreach (TMP_InputField inp in Object.FindObjectsByType<TMP_InputField>(FindObjectsSortMode.None))
        {
            RectTransform ir = inp.GetComponent<RectTransform>();
            ir.sizeDelta = new Vector2(280f, 44f);
            var bg = inp.GetComponent<Image>();
            if (bg)
            {
                bg.color = new Color(0.06f, 0.08f, 0.12f, 0.98f);
            }
            if (inp.textComponent != null)
            {
                inp.textComponent.fontSize = 20f;
                inp.textComponent.alignment = TextAlignmentOptions.Center;
                inp.textComponent.color = Color.white;
            }
        }

        // 3. HUD Badges (Top-Left and Top-Right)
        foreach (TMP_Text t in Object.FindObjectsByType<TMP_Text>(FindObjectsSortMode.None))
        {
            if (!t) continue;
            string tn = t.name.ToLowerInvariant();
            t.extraPadding = true;

            if (tn.Contains("timer"))
            {
                t.color = new Color(0.92f, 0.96f, 1.0f);
                t.fontSize = 20f;
                t.fontStyle = FontStyles.Bold;
                if (!t.text.StartsWith("TIME", System.StringComparison.OrdinalIgnoreCase))
                    t.text = "TIME " + t.text.Replace("Time:", "").Replace("Time ", "").Trim();
            }
            else if (tn.Contains("attempt"))
            {
                t.color = new Color(1f, 0.78f, 0.40f);
                t.fontSize = 20f;
                t.fontStyle = FontStyles.Bold;
                if (!t.text.StartsWith("ATTEMPTS", System.StringComparison.OrdinalIgnoreCase))
                {
                    bool noTrack = scene.name == "Level1_Investigation" || scene.name == "Level5_CaseFiles";
                    t.text = "ATTEMPTS: " + (noTrack ? "—" : "3");
                }
            }
        }

        // 4. Buttons with 9-Slice Sprites & Hover Transitions
        foreach (Button b in Object.FindObjectsByType<Button>(FindObjectsSortMode.None))
        {
            string bn = b.name.ToLowerInvariant();
            Image img = b.GetComponent<Image>();
            TMP_Text txt = b.GetComponentInChildren<TMP_Text>();

            bool isPrimary = bn.Contains("start") || bn.Contains("play") || bn.Contains("submit") ||
                             bn.Contains("login") || bn.Contains("verdict") ||
                             ((bn.Contains("quit") || bn.Contains("exit")) && scene.name == "GameComplete");

            if (img)
            {
                img.sprite = isPrimary ? (crimsonNorm ?? img.sprite) : (darkNorm ?? img.sprite);
                img.type = Image.Type.Sliced;
                img.color = Color.white;
            }

            ColorBlock cb = b.colors;
            cb.normalColor = Color.white;
            cb.highlightedColor = new Color(1f, 0.95f, 0.85f);
            cb.pressedColor = new Color(0.7f, 0.7f, 0.7f);
            cb.selectedColor = cb.highlightedColor;
            cb.fadeDuration = 0.10f;
            b.colors = cb;

            if (txt)
            {
                txt.color = Color.white;
                txt.fontStyle = FontStyles.Bold;
                if (txt.fontSize > 22f || txt.fontSize < 16f) txt.fontSize = 18f;
            }
        }

        WireSceneButtons(scene);
    }

    static void StyleMainMenuUI()
    {
        // Set up clean single title & subtitle in Canvas (NO overlapping duplicate titles!)
        var texts = Object.FindObjectsByType<TMP_Text>(FindObjectsSortMode.None).ToList();
        var title = texts.FirstOrDefault(t => t.name.ToLowerInvariant().Contains("title"));
        if (title)
        {
            title.text = "<color=#E2E8F0>CIPHER</color> <color=#B71C1C>COURT</color>";
            title.fontSize = 58f;
            title.fontStyle = FontStyles.Bold;
            title.raycastTarget = false;
            RectTransform tr = title.rectTransform;
            tr.anchorMin = new Vector2(0.5f, 0.5f);
            tr.anchorMax = new Vector2(0.5f, 0.5f);
            tr.pivot     = new Vector2(0.5f, 0.5f);
            tr.anchoredPosition = new Vector2(0f, 170f);
        }

        var sub = texts.FirstOrDefault(t => (t.name.ToLowerInvariant().Contains("subtitle") || t.name.ToLowerInvariant().Contains("tagline")) && t != title);
        if (sub)
        {
            sub.text = "<color=#ECC94B>ESCAPE TO JUSTICE</color>\n<size=16><color=#CBD5E0><i>“Find the Truth. Reach Justice.”</i></color></size>";
            sub.fontSize = 22f;
            sub.fontStyle = FontStyles.Normal;
            sub.raycastTarget = false;
            RectTransform sr = sub.rectTransform;
            sr.anchorMin = new Vector2(0.5f, 0.5f);
            sr.anchorMax = new Vector2(0.5f, 0.5f);
            sr.pivot     = new Vector2(0.5f, 0.5f);
            sr.anchoredPosition = new Vector2(0f, 105f);
        }

        // Layout Buttons neatly
        var buttons = Object.FindObjectsByType<Button>(FindObjectsSortMode.None).ToList();
        var startBtn = buttons.FirstOrDefault(b => b.name.ToLowerInvariant().Contains("start") || b.name.ToLowerInvariant().Contains("play"));
        var instBtn  = buttons.FirstOrDefault(b => b.name.ToLowerInvariant().Contains("instruction"));
        var quitBtn  = buttons.FirstOrDefault(b => b.name.ToLowerInvariant().Contains("quit") || b.name.ToLowerInvariant().Contains("exit"));

        if (startBtn)
        {
            RectTransform br = startBtn.GetComponent<RectTransform>();
            br.anchorMin = new Vector2(0.5f, 0.5f);
            br.anchorMax = new Vector2(0.5f, 0.5f);
            br.pivot     = new Vector2(0.5f, 0.5f);
            br.anchoredPosition = new Vector2(0f, -25f);
            br.sizeDelta = new Vector2(280f, 50f);
        }

        if (instBtn)
        {
            RectTransform br = instBtn.GetComponent<RectTransform>();
            br.anchorMin = new Vector2(0.5f, 0.5f);
            br.anchorMax = new Vector2(0.5f, 0.5f);
            br.pivot     = new Vector2(0.5f, 0.5f);
            br.anchoredPosition = new Vector2(0f, -85f);
            br.sizeDelta = new Vector2(280f, 50f);
        }

        if (quitBtn)
        {
            RectTransform br = quitBtn.GetComponent<RectTransform>();
            br.anchorMin = new Vector2(0.5f, 0.5f);
            br.anchorMax = new Vector2(0.5f, 0.5f);
            br.pivot     = new Vector2(0.5f, 0.5f);
            br.anchoredPosition = new Vector2(0f, -145f);
            br.sizeDelta = new Vector2(280f, 50f);
        }

        // Instructions Panel
        var instPanel = Object.FindObjectsByType<GameObject>(FindObjectsSortMode.None)
            .FirstOrDefault(g => g.name.ToLowerInvariant().Contains("instruction") && g.name.ToLowerInvariant().Contains("panel"));
        if (instPanel)
        {
            RectTransform pr = instPanel.GetComponent<RectTransform>();
            if (pr)
            {
                pr.anchorMin = new Vector2(0.5f, 0.5f);
                pr.anchorMax = new Vector2(0.5f, 0.5f);
                pr.pivot     = new Vector2(0.5f, 0.5f);
                pr.anchoredPosition = Vector2.zero;
                pr.sizeDelta = new Vector2(620f, 440f);
            }
            var pImg = instPanel.GetComponent<Image>();
            Sprite cardSprite = LoadUISprite("panel_glass_card.png");
            if (pImg && cardSprite)
            {
                pImg.sprite = cardSprite;
                pImg.type = Image.Type.Sliced;
                pImg.color = Color.white;
            }

            var txt = instPanel.GetComponentsInChildren<TMP_Text>().FirstOrDefault(t => t.name.ToLowerInvariant().Contains("content") || t.name.ToLowerInvariant().Contains("body") || t.name.ToLowerInvariant().Contains("text"));
            if (txt)
            {
                txt.text = "<b><color=#ECC94B>INVESTIGATION PROTOCOLS</color></b>\n\n" +
                           "<b>MOVEMENT:</b>  W, A, S, D  –  Walk\n" +
                           "<b>LOOK:</b>  Mouse  –  Look Around\n" +
                           "<b>INTERACT:</b>  [ E ]  –  Inspect & Collect Evidence\n\n" +
                           "<b>CASE OBJECTIVE:</b>\n" +
                           "Search each crime scene, analyze digital evidence,\n" +
                           "crack the encrypted archives, cross-examine witness\n" +
                           "statements, and present your case in court.\n\n" +
                           "<i>Truth always prevails under the law.</i>";
                txt.fontSize = 18f;
                txt.alignment = TextAlignmentOptions.TopLeft;
                txt.color = WarmWhite;
            }
        }
    }

    static void StyleGameCompleteUI()
    {
        var title = Object.FindObjectsByType<TMP_Text>(FindObjectsSortMode.None)
            .FirstOrDefault(t => t.name.ToLowerInvariant().Contains("title"));
        if (title)
        {
            title.text = "<b><color=#D4AF37><size=56>CASE SOLVED</size></color>\n<color=#B71C1C><size=40>JUSTICE SERVED</size></color></b>";
            title.fontSize = 56f;
            title.fontStyle = FontStyles.Bold;
            title.alignment = TextAlignmentOptions.Center;
            title.raycastTarget = false;
            RectTransform tr = title.rectTransform;
            tr.anchorMin = new Vector2(0.5f, 0.5f);
            tr.anchorMax = new Vector2(0.5f, 0.5f);
            tr.pivot     = new Vector2(0.5f, 0.5f);
            tr.anchoredPosition = new Vector2(0f, 160f);
            tr.sizeDelta = new Vector2(800f, 130f);
        }

        var sub = Object.FindObjectsByType<TMP_Text>(FindObjectsSortMode.None)
            .FirstOrDefault(t => t.name.ToLowerInvariant().Contains("sub") || t.name.ToLowerInvariant().Contains("desc") || t.name.ToLowerInvariant().Contains("congrat"));
        if (sub)
        {
            sub.text = "“You have uncovered the truth, presented the evidence, and solved the case.”\n\n<size=18><color=#CBD5E0><i>“Justice is not a place, it is a process.”</i></color></size>";
            sub.fontSize = 22f;
            sub.color = WarmWhite;
            sub.alignment = TextAlignmentOptions.Center;
            sub.raycastTarget = false;
            RectTransform sr = sub.rectTransform;
            sr.anchorMin = new Vector2(0.5f, 0.5f);
            sr.anchorMax = new Vector2(0.5f, 0.5f);
            sr.pivot     = new Vector2(0.5f, 0.5f);
            sr.anchoredPosition = new Vector2(0f, 40f);
            sr.sizeDelta = new Vector2(750f, 100f);
        }

        var buttons = Object.FindObjectsByType<Button>(FindObjectsSortMode.None).ToList();
        var menuBtn = buttons.FirstOrDefault(b => b.name.ToLowerInvariant().Contains("menu") || b.name.ToLowerInvariant().Contains("main"));
        var quitBtn = buttons.FirstOrDefault(b => b.name.ToLowerInvariant().Contains("quit") || b.name.ToLowerInvariant().Contains("exit"));

        if (menuBtn)
        {
            RectTransform br = menuBtn.GetComponent<RectTransform>();
            br.anchorMin = new Vector2(0.5f, 0.5f);
            br.anchorMax = new Vector2(0.5f, 0.5f);
            br.pivot     = new Vector2(0.5f, 0.5f);
            br.anchoredPosition = new Vector2(0f, -40f);
            br.sizeDelta = new Vector2(280f, 50f);
        }

        if (quitBtn)
        {
            RectTransform br = quitBtn.GetComponent<RectTransform>();
            br.anchorMin = new Vector2(0.5f, 0.5f);
            br.anchorMax = new Vector2(0.5f, 0.5f);
            br.pivot     = new Vector2(0.5f, 0.5f);
            br.anchoredPosition = new Vector2(0f, -105f);
            br.sizeDelta = new Vector2(280f, 50f);
        }
    }

    static void WireSceneButtons(Scene scene)
    {
        if (scene.name == "MainMenu")
        {
            var menuMgr = Object.FindFirstObjectByType<MainMenuManager>();
            if (menuMgr != null)
            {
                foreach (Button b in Object.FindObjectsByType<Button>(FindObjectsSortMode.None))
                {
                    string bn = b.name.ToLowerInvariant();
                    while (b.onClick.GetPersistentEventCount() > 0)
                    {
                        UnityEventTools.RemovePersistentListener(b.onClick, 0);
                    }

                    if (bn.Contains("start") || bn.Contains("play"))
                    {
                        UnityEventTools.AddPersistentListener(b.onClick, menuMgr.StartGame);
                    }
                    else if (bn.Contains("instruction"))
                    {
                        UnityEventTools.AddPersistentListener(b.onClick, menuMgr.OpenInstructions);
                    }
                    else if (bn.Contains("close") || bn.Contains("back"))
                    {
                        UnityEventTools.AddPersistentListener(b.onClick, menuMgr.CloseInstructions);
                    }
                    else if (bn.Contains("quit") || bn.Contains("exit"))
                    {
                        UnityEventTools.AddPersistentListener(b.onClick, menuMgr.QuitGame);
                    }
                    EditorUtility.SetDirty(b);
                }
            }
        }
        else if (scene.name == "GameComplete")
        {
            var compMgr = Object.FindFirstObjectByType<GameCompleteManager>();
            if (compMgr != null)
            {
                foreach (Button b in Object.FindObjectsByType<Button>(FindObjectsSortMode.None))
                {
                    string bn = b.name.ToLowerInvariant();
                    while (b.onClick.GetPersistentEventCount() > 0)
                    {
                        UnityEventTools.RemovePersistentListener(b.onClick, 0);
                    }

                    if (bn.Contains("menu") || bn.Contains("main"))
                    {
                        UnityEventTools.AddPersistentListener(b.onClick, compMgr.MainMenu);
                    }
                    else if (bn.Contains("quit") || bn.Contains("exit"))
                    {
                        UnityEventTools.AddPersistentListener(b.onClick, compMgr.QuitGame);
                    }
                    EditorUtility.SetDirty(b);
                }
            }
        }
    }

    // ═══════════════════════════════════════════════════════════════════════
    //  PROCEDURAL 9-SLICE UI SPRITE GENERATOR
    // ═══════════════════════════════════════════════════════════════════════
    static void GenerateUISprites()
    {
        CreateRoundedCardTexture("panel_glass_card.png", 128, 128, 16, 2,
            new Color(0.04f, 0.06f, 0.10f, 0.95f), new Color(0.08f, 0.12f, 0.18f, 0.97f),
            new Color(0.95f, 0.82f, 0.42f, 0.90f));

        CreateRoundedCardTexture("btn_crimson_normal.png", 128, 48, 12, 2,
            new Color(0.68f, 0.10f, 0.14f, 0.98f), new Color(0.48f, 0.06f, 0.08f, 0.98f),
            new Color(0.95f, 0.82f, 0.42f, 0.70f));

        CreateRoundedCardTexture("btn_crimson_hover.png", 128, 48, 12, 2,
            new Color(0.85f, 0.14f, 0.18f, 1f), new Color(0.62f, 0.08f, 0.10f, 1f),
            new Color(1.0f, 0.92f, 0.60f, 1f));

        CreateRoundedCardTexture("btn_charcoal_normal.png", 128, 48, 12, 2,
            new Color(0.12f, 0.16f, 0.22f, 0.95f), new Color(0.06f, 0.08f, 0.12f, 0.98f),
            new Color(0.35f, 0.45f, 0.58f, 0.60f));

        CreateRoundedCardTexture("btn_charcoal_hover.png", 128, 48, 12, 2,
            new Color(0.18f, 0.24f, 0.32f, 1f), new Color(0.10f, 0.14f, 0.18f, 1f),
            new Color(0.95f, 0.82f, 0.42f, 0.85f));

        CreateRoundedCardTexture("hud_badge.png", 128, 48, 14, 2,
            new Color(0.04f, 0.06f, 0.10f, 0.88f), new Color(0.08f, 0.10f, 0.16f, 0.92f),
            new Color(0.95f, 0.82f, 0.42f, 0.65f));

        AssetDatabase.Refresh();
    }

    static void CreateRoundedCardTexture(string filename, int w, int h, int radius, int border,
                                         Color topColor, Color botColor, Color borderColor)
    {
        string path = $"{UIFolder}/{filename}";
        if (File.Exists(path)) return;

        Texture2D tex = new Texture2D(w, h, TextureFormat.RGBA32, false);
        Color[] pixels = new Color[w * h];

        for (int y = 0; y < h; y++)
        {
            float v = (float)y / (h - 1);
            Color grad = Color.Lerp(botColor, topColor, v);

            for (int x = 0; x < w; x++)
            {
                float dist = CornerDistance(x, y, w, h, radius);
                if (dist > radius)
                {
                    pixels[y * w + x] = Color.clear;
                }
                else if (dist > radius - border)
                {
                    pixels[y * w + x] = borderColor;
                }
                else
                {
                    pixels[y * w + x] = grad;
                }
            }
        }

        tex.SetPixels(pixels);
        tex.Apply();

        byte[] png = tex.EncodeToPNG();
        File.WriteAllBytes(path, png);
        Object.DestroyImmediate(tex);

        AssetDatabase.ImportAsset(path);
        TextureImporter ti = AssetImporter.GetAtPath(path) as TextureImporter;
        if (ti != null)
        {
            ti.textureType = TextureImporterType.Sprite;
            ti.spriteImportMode = SpriteImportMode.Single;
            ti.spriteBorder = new Vector4(radius + 2, radius + 2, radius + 2, radius + 2);
            ti.mipmapEnabled = false;
            ti.SaveAndReimport();
        }
    }

    static float CornerDistance(int x, int y, int w, int h, int r)
    {
        int cx = x < r ? r : (x >= w - r ? w - 1 - r : x);
        int cy = y < r ? r : (y >= h - r ? h - 1 - r : y);
        int dx = x - cx;
        int dy = y - cy;
        return Mathf.Sqrt(dx * dx + dy * dy);
    }

    static Sprite LoadUISprite(string filename)
        => AssetDatabase.LoadAssetAtPath<Sprite>($"{UIFolder}/{filename}");

    // ═══════════════════════════════════════════════════════════════════════
    //  PREFAB INSTANTIATION HELPER
    // ═══════════════════════════════════════════════════════════════════════
    static GameObject SpawnOfficePrefab(GameObject parent, string relativePath, Vector3 pos, Quaternion rot, Vector3 scale)
    {
        string fullPath = "Assets/VNB - Office Set 2/Prefabs/" + relativePath;
        GameObject prefab = AssetDatabase.LoadAssetAtPath<GameObject>(fullPath);
        if (!prefab) return null;

        GameObject inst = (GameObject)PrefabUtility.InstantiatePrefab(prefab);
        inst.transform.SetParent(parent.transform, false);
        inst.transform.position = pos;
        inst.transform.rotation = rot;
        inst.transform.localScale = scale;

        var cols = inst.GetComponentsInChildren<Collider>();
        if (cols.Length == 0)
        {
            var rends = inst.GetComponentsInChildren<Renderer>();
            if (rends.Length > 0)
            {
                Bounds b = rends[0].bounds;
                foreach (var r in rends) b.Encapsulate(r.bounds);
                BoxCollider box = inst.AddComponent<BoxCollider>();
                box.center = inst.transform.InverseTransformPoint(b.center);
                Vector3 s = inst.transform.lossyScale;
                box.size = new Vector3(
                    Mathf.Abs(b.size.x / (s.x != 0 ? s.x : 1)),
                    Mathf.Abs(b.size.y / (s.y != 0 ? s.y : 1)),
                    Mathf.Abs(b.size.z / (s.z != 0 ? s.z : 1))
                );
            }
        }
        return inst;
    }

    static void ApplyCinematicBackground(string texturePath)
    {
        TextureImporter ti = AssetImporter.GetAtPath(texturePath) as TextureImporter;
        if (ti != null && ti.textureType != TextureImporterType.Sprite)
        {
            ti.textureType = TextureImporterType.Sprite;
            ti.spriteImportMode = SpriteImportMode.Single;
            ti.mipmapEnabled = false;
            ti.SaveAndReimport();
        }
        Sprite sp = AssetDatabase.LoadAssetAtPath<Sprite>(texturePath);
        if (!sp) return;

        Canvas canvas = Object.FindFirstObjectByType<Canvas>();
        Image bg = Object.FindObjectsByType<Image>(FindObjectsSortMode.None)
            .FirstOrDefault(i => i.name.ToLowerInvariant().Contains("background"));

        if (!bg && canvas != null)
        {
            GameObject bgObj = new GameObject("BackgroundImage", typeof(RectTransform), typeof(CanvasRenderer), typeof(Image));
            bgObj.transform.SetParent(canvas.transform, false);
            bgObj.transform.SetAsFirstSibling();
            RectTransform rt = bgObj.GetComponent<RectTransform>();
            rt.anchorMin = Vector2.zero;
            rt.anchorMax = Vector2.one;
            rt.sizeDelta = Vector2.zero;
            bg = bgObj.GetComponent<Image>();
        }

        if (bg)
        {
            bg.sprite = sp;
            bg.color = Color.white;
            bg.type = Image.Type.Simple;
            bg.preserveAspect = false;
            bg.raycastTarget = false;
        }
    }

    // ═══════════════════════════════════════════════════════════════════════
    //  JUDICIAL PROPS (GAVEL, SCALES, FLAG, MARKERS)
    // ═══════════════════════════════════════════════════════════════════════
    static void BuildGavel(GameObject root, Vector3 pos)
    {
        Material richWood = LoadMat("Wood_Dark");
        Material gold     = LoadMat("Accent_Gold");

        GameObject gavel = new GameObject("JudgeGavel");
        gavel.transform.SetParent(root.transform);
        gavel.transform.position = pos;

        AddCylinder(gavel, "BaseBlock", pos + new Vector3(0, 0.04f, 0), new Vector3(0.35f, 0.05f, 0.35f), richWood);
        AddCylinder(gavel, "BlockTrim", pos + new Vector3(0, 0.05f, 0), new Vector3(0.37f, 0.015f, 0.37f), gold);

        AddCylinder(gavel, "GavelHandle", pos + new Vector3(0, 0.10f, 0), new Vector3(0.03f, 0.30f, 0.03f), richWood);
        AddCylinder(gavel, "GavelHead",   pos + new Vector3(0, 0.10f, 0.14f), new Vector3(0.07f, 0.16f, 0.07f), richWood);
    }

    static void BuildScalesOfJustice(GameObject root, Vector3 pos, float scale)
    {
        Material gold = LoadMat("Accent_Gold");
        GameObject sc = new GameObject("ScalesOfJustice");
        sc.transform.SetParent(root.transform);
        sc.transform.position = pos;
        sc.transform.localScale = Vector3.one * scale;

        AddCylinder(sc, "Base", pos + new Vector3(0, 0.05f*scale, 0), new Vector3(0.45f, 0.05f, 0.45f)*scale, gold);
        AddCylinder(sc, "Pillar", pos + new Vector3(0, 0.75f*scale, 0), new Vector3(0.05f, 0.75f, 0.05f)*scale, gold);
        AddCube(sc, "Beam", pos + new Vector3(0, 1.50f*scale, 0), new Vector3(1.10f, 0.035f, 0.035f)*scale, gold);

        AddCylinder(sc, "Pan_L", pos + new Vector3(-0.50f*scale, 1.10f*scale, 0), new Vector3(0.25f, 0.02f, 0.25f)*scale, gold);
        AddCylinder(sc, "Pan_R", pos + new Vector3( 0.50f*scale, 1.10f*scale, 0), new Vector3(0.25f, 0.02f, 0.25f)*scale, gold);
    }

    static void BuildIndianFlag(GameObject root, string name, Vector3 pos)
    {
        GameObject flag = new GameObject(name);
        flag.transform.SetParent(root.transform);
        flag.transform.position = pos;

        AddCylinder(flag, "Pole", pos + new Vector3(-0.02f, 0f, 0), new Vector3(0.04f, 2.2f, 0.04f), LoadMat("Accent_Gold"));
        AddSphere(flag, "Finial", pos + new Vector3(-0.02f, 1.15f, 0), Vector3.one * 0.10f, LoadMat("Accent_Gold"));

        AddCube(flag, "Saffron", pos + new Vector3(0.75f, 0.60f, 0), new Vector3(1.5f, 0.35f, 0.02f), LoadMat("Flag_Orange"));
        AddCube(flag, "White",   pos + new Vector3(0.75f, 0.25f, 0), new Vector3(1.5f, 0.35f, 0.02f), LoadMat("White_Mat"));
        AddCube(flag, "Green",   pos + new Vector3(0.75f, -0.10f, 0), new Vector3(1.5f, 0.35f, 0.02f), LoadMat("Flag_Green"));

        AddCylinder(flag, "Chakra", pos + new Vector3(0.75f, 0.25f, -0.015f), new Vector3(0.18f, 0.01f, 0.18f), LoadMat("Flag_Blue"));
    }

    static void AddEvidenceMarker(GameObject parent, string name, Vector3 pos, string number)
    {
        GameObject marker = new GameObject(name);
        marker.transform.SetParent(parent.transform);
        marker.transform.position = pos;

        Material yellow = LoadMat("Marker_Yellow");
        AddCube(marker, "Tent_L", pos + new Vector3(-0.04f, 0.06f, 0), new Vector3(0.02f, 0.14f, 0.12f), yellow);
        AddCube(marker, "Tent_R", pos + new Vector3( 0.04f, 0.06f, 0), new Vector3(0.02f, 0.14f, 0.12f), yellow);
        AddWallText(marker, "Num", number, pos + new Vector3(0, 0.06f, 0.07f), Color.black, 1.2f);
    }

    // ═══════════════════════════════════════════════════════════════════════
    //  MATERIALS & SHADERS (LOW SMOOTHNESS - ZERO SHINY PLASTIC!)
    // ═══════════════════════════════════════════════════════════════════════
    static void BuildMaterials()
    {
        // Flooring with low smoothness (0.12 - 0.18) so there is NO mirror plastic reflection!
        CreateMat("Floor_DarkWood",    new Color(0.32f,0.22f,0.16f),  0.88f, 0.05f);
        CreateMat("Floor_Marble",      new Color(0.28f,0.28f,0.30f),  0.82f, 0.05f);
        CreateMat("Floor_CyberTile",   new Color(0.12f,0.15f,0.20f),  0.85f, 0.08f);
        CreateMat("Floor_Concrete",    new Color(0.24f,0.23f,0.22f),  0.90f, 0.02f);
        CreateMat("Ceiling_Dark",      new Color(0.15f,0.15f,0.17f),  0.95f, 0.00f);
        CreateMat("Ceiling_Mid",       new Color(0.25f,0.25f,0.27f),  0.90f, 0.00f);
        CreateMat("Ceiling_Court",     new Color(0.52f,0.49f,0.44f),  0.90f, 0.00f);

        // Drywall and wood walls (matte, zero glare)
        CreateMat("Wall_Charcoal",     new Color(0.20f,0.22f,0.25f),  0.90f, 0.02f);
        CreateMat("Wall_LightGrey",    new Color(0.50f,0.52f,0.54f),  0.90f, 0.02f);
        CreateMat("Wall_Archive",      new Color(0.24f,0.21f,0.18f),  0.92f, 0.02f);
        CreateMat("Wall_CourtWood",    new Color(0.36f,0.24f,0.18f),  0.80f, 0.05f);
        CreateMat("Wall_CyberDark",    new Color(0.12f,0.14f,0.18f),  0.88f, 0.05f);

        CreateMat("Wood_Walnut",       new Color(0.30f,0.18f,0.12f),  0.78f, 0.05f);
        CreateMat("Wood_Dark",         new Color(0.32f,0.20f,0.14f),  0.75f, 0.05f);
        CreateMat("Metal_Dark",        new Color(0.22f,0.25f,0.28f),  0.45f, 0.80f);
        CreateMat("Metal_Gold",        new Color(0.85f,0.68f,0.22f),  0.35f, 0.85f);
        CreateMat("Trim_Black",        new Color(0.08f,0.08f,0.09f),  0.80f, 0.10f);
        CreateMat("Accent_Gold",       new Color(0.85f,0.68f,0.22f),  0.35f, 0.85f);
        CreateMat("Frame_Dark",        new Color(0.12f,0.10f,0.08f),  0.80f, 0.10f);

        CreateEmissiveMat("Light_Emissive_Warm", new Color(1.0f, 0.82f, 0.55f), 2.0f);
        CreateEmissiveMat("Light_Emissive_Blue", new Color(0.25f,0.65f,0.95f),  2.2f);
        CreateEmissiveMat("Screen_Cyan",        new Color(0.05f,0.60f,0.85f),  1.8f);

        CreateMat("Server_Dark",       new Color(0.10f,0.12f,0.14f),  0.80f, 0.20f);
        CreateMat("Cork_Board",        new Color(0.52f,0.38f,0.22f),  0.95f, 0.00f);
        CreateMat("Paper_Warm",        new Color(0.88f,0.85f,0.76f),  0.95f, 0.00f);
        CreateMat("Evidence_Red",      new Color(0.68f,0.10f,0.12f),  0.75f, 0.05f);
        CreateMat("Archive_Box",       new Color(0.52f,0.38f,0.22f),  0.90f, 0.00f);
        CreateMat("Marker_Yellow",     new Color(0.92f,0.82f,0.10f),  0.60f, 0.05f);
        CreateMat("Leather_Dark",      new Color(0.14f,0.08f,0.05f),  0.75f, 0.05f);
        CreateMat("Rug_Dark",          new Color(0.35f,0.08f,0.10f),  0.98f, 0.00f);
        CreateMat("Folder_Red",        new Color(0.65f,0.10f,0.12f),  0.75f, 0.05f);
        CreateMat("White_Mat",         new Color(0.90f,0.90f,0.90f),  0.85f, 0.02f);

        CreateMat("Flag_Orange",       new Color(1.0f, 0.42f, 0.00f), 0.85f, 0.00f);
        CreateMat("Flag_Green",        new Color(0.05f,0.50f,0.15f),  0.85f, 0.00f);
        CreateMat("Flag_Blue",         new Color(0.04f,0.14f,0.55f),  0.65f, 0.05f);
    }

    static void CreateMat(string name, Color baseColor, float roughness, float metallic)
    {
        string path = $"{MatFolder}/{name}.mat";
        Material m = AssetDatabase.LoadAssetAtPath<Material>(path);
        if (!m)
        {
            Shader s = Shader.Find("Universal Render Pipeline/Lit") ?? Shader.Find("Standard");
            m = new Material(s);
            AssetDatabase.CreateAsset(m, path);
        }
        if (m.HasProperty("_BaseColor"))    m.SetColor("_BaseColor", baseColor);
        if (m.HasProperty("_Color"))        m.SetColor("_Color",     baseColor);
        if (m.HasProperty("_Smoothness"))   m.SetFloat("_Smoothness", 1f - roughness);
        if (m.HasProperty("_Glossiness"))   m.SetFloat("_Glossiness",1f - roughness);
        if (m.HasProperty("_Metallic"))     m.SetFloat("_Metallic",   metallic);
        EditorUtility.SetDirty(m);
    }

    static void CreateEmissiveMat(string name, Color emissiveColor, float intensity)
    {
        string path = $"{MatFolder}/{name}.mat";
        Material m = AssetDatabase.LoadAssetAtPath<Material>(path);
        if (!m)
        {
            Shader s = Shader.Find("Universal Render Pipeline/Lit") ?? Shader.Find("Standard");
            m = new Material(s);
            AssetDatabase.CreateAsset(m, path);
        }
        Color boosted = emissiveColor * intensity;
        if (m.HasProperty("_BaseColor"))       m.SetColor("_BaseColor",     emissiveColor);
        if (m.HasProperty("_Color"))           m.SetColor("_Color",         emissiveColor);
        if (m.HasProperty("_EmissionColor"))   m.SetColor("_EmissionColor", boosted);
        m.EnableKeyword("_EMISSION");
        if (m.HasProperty("_Smoothness")) m.SetFloat("_Smoothness", 0.5f);
        if (m.HasProperty("_Metallic"))   m.SetFloat("_Metallic",   0.0f);
        EditorUtility.SetDirty(m);
    }

    // ═══════════════════════════════════════════════════════════════════════
    //  BASIC HELPERS
    // ═══════════════════════════════════════════════════════════════════════
    static void AddPhysicalCube(GameObject parent, string name, Vector3 pos, Vector3 size, Material mat)
    {
        GameObject g = GameObject.CreatePrimitive(PrimitiveType.Cube);
        g.name = name;
        g.transform.SetParent(parent.transform);
        g.transform.position = pos;
        g.transform.localScale = size;
        var r = g.GetComponent<Renderer>();
        if (r && mat) { r.sharedMaterial = mat; r.shadowCastingMode = UnityEngine.Rendering.ShadowCastingMode.Off; r.receiveShadows = false; }
    }

    static void AddCube(GameObject parent, string name, Vector3 pos, Vector3 size, Material mat)
    {
        GameObject g = GameObject.CreatePrimitive(PrimitiveType.Cube);
        g.name = name;
        g.transform.SetParent(parent.transform);
        g.transform.position = pos;
        g.transform.localScale = size;
        var col = g.GetComponent<Collider>();
        if (col) Object.DestroyImmediate(col);
        var r = g.GetComponent<Renderer>();
        if (r && mat) { r.sharedMaterial = mat; r.shadowCastingMode = UnityEngine.Rendering.ShadowCastingMode.Off; r.receiveShadows = false; }
    }

    static void AddCylinder(GameObject parent, string name, Vector3 pos, Vector3 size, Material mat)
    {
        GameObject g = GameObject.CreatePrimitive(PrimitiveType.Cylinder);
        g.name = name;
        g.transform.SetParent(parent.transform);
        g.transform.position = pos;
        g.transform.localScale = size;
        var col = g.GetComponent<Collider>();
        if (col) Object.DestroyImmediate(col);
        var r = g.GetComponent<Renderer>();
        if (r && mat) { r.sharedMaterial = mat; r.shadowCastingMode = UnityEngine.Rendering.ShadowCastingMode.Off; r.receiveShadows = false; }
    }

    static void AddSphere(GameObject parent, string name, Vector3 pos, Vector3 size, Material mat)
    {
        GameObject g = GameObject.CreatePrimitive(PrimitiveType.Sphere);
        g.name = name;
        g.transform.SetParent(parent.transform);
        g.transform.position = pos;
        g.transform.localScale = size;
        var col = g.GetComponent<Collider>();
        if (col) Object.DestroyImmediate(col);
        var r = g.GetComponent<Renderer>();
        if (r && mat) { r.sharedMaterial = mat; r.shadowCastingMode = UnityEngine.Rendering.ShadowCastingMode.Off; r.receiveShadows = false; }
    }

    static void AddPointLight(GameObject parent, string name, Vector3 pos, Color color, float intensity, float range)
    {
        GameObject g = new GameObject(name);
        g.transform.SetParent(parent.transform);
        g.transform.position = pos;
        Light l = g.AddComponent<Light>();
        l.type = LightType.Point;
        l.color = color;
        l.intensity = intensity;
        l.range = range;
        l.shadows = LightShadows.None;
    }

    static void AddWallText(GameObject parent, string name, string text, Vector3 pos, Color color, float scale = 3.0f)
    {
        GameObject g = new GameObject(name);
        g.transform.SetParent(parent.transform);
        g.transform.position = pos;
        g.transform.localScale = Vector3.one * 0.05f;

        var tmp = g.AddComponent<TextMeshPro>();
        tmp.text = text;
        tmp.color = color;
        tmp.fontSize = scale * 10f;
        tmp.alignment = TextAlignmentOptions.Center;
        tmp.fontStyle = FontStyles.Bold;
        tmp.GetComponent<RectTransform>().sizeDelta = new Vector2(240, 50);
    }

    static void SetAmbient(Color c)
    {
        RenderSettings.ambientMode = UnityEngine.Rendering.AmbientMode.Flat;
        RenderSettings.ambientLight = c;
        RenderSettings.fog = false;
    }

    static Material LoadMat(string name)
        => AssetDatabase.LoadAssetAtPath<Material>($"{MatFolder}/{name}.mat");

    static void EnsureFolder(string path)
    {
        if (AssetDatabase.IsValidFolder(path)) return;
        string parent = Path.GetDirectoryName(path).Replace("\\", "/");
        string name   = Path.GetFileName(path);
        if (!AssetDatabase.IsValidFolder(parent)) EnsureFolder(parent);
        AssetDatabase.CreateFolder(parent, name);
    }
}
#endif
