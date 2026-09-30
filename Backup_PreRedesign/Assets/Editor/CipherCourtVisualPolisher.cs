#if UNITY_EDITOR
using UnityEngine;
using UnityEngine.UI;
using UnityEditor;
using UnityEditor.SceneManagement;
using UnityEngine.SceneManagement;
using TMPro;
using System.IO;
using System.Linq;
using System.Collections.Generic;

[InitializeOnLoad]
public static class CipherCourtVisualPolisher
{
    const string RootName    = "_VISUAL_POLISH_V14_";
    const string FlagPath    = "Assets/CipherCourtPolish/POLISH_V14_CLEAN_APPLIED.txt";
    const string MatFolder   = "Assets/CipherCourtPolish/Materials";

    // ── Color Palette ─────────────────────────────────────────────────────────
    static readonly Color WarmWhite   = new Color(0.92f, 0.90f, 0.84f, 1f);
    static readonly Color Gold        = new Color(0.95f, 0.82f, 0.45f, 1f);
    static readonly Color Cyan        = new Color(0.08f, 0.65f, 0.86f, 1f);
    static readonly Color CrimsonRed  = new Color(0.68f, 0.10f, 0.12f, 0.98f);
    static readonly Color AzureBlue   = new Color(0.08f, 0.45f, 0.78f, 0.98f);
    static readonly Color PanelDark   = new Color(0.04f, 0.06f, 0.10f, 0.94f);
    static readonly Color BtnDark     = new Color(0.12f, 0.16f, 0.22f, 0.95f);

    static CipherCourtVisualPolisher() { EditorApplication.delayCall += AutoPolish; }

    [MenuItem("Cipher Court/Apply V14 Clean Polish")]
    public static void ApplyFromMenu() => ApplyAll(true);

    static void AutoPolish()
    {
        if (EditorApplication.isPlayingOrWillChangePlaymode || EditorApplication.isCompiling) return;
        if (File.Exists(FlagPath)) return;
        ApplyAll(false);
    }

    static void ApplyAll(bool force)
    {
        if (!force && File.Exists(FlagPath)) return;
        EnsureFolder("Assets/CipherCourtPolish");
        EnsureFolder(MatFolder);
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

        File.WriteAllText(FlagPath, "Cipher Court V14 Clean Build applied.\n");
        AssetDatabase.ImportAsset(FlagPath);
        AssetDatabase.SaveAssets();
        AssetDatabase.Refresh();

        if (!string.IsNullOrEmpty(previous) && File.Exists(previous))
            EditorSceneManager.OpenScene(previous, OpenSceneMode.Single);
        else if (File.Exists("Assets/Scenes/MainMenu.unity"))
            EditorSceneManager.OpenScene("Assets/Scenes/MainMenu.unity", OpenSceneMode.Single);

        Debug.Log("Cipher Court V14: Game Complete background, visible level 1 & 2 clues, level 4 keypad, unobstructed level 6 door & 3D exit corridor complete!");
    }

    // ═══════════════════════════════════════════════════════════════════════
    //  SCENE POLISH & PURGE
    // ═══════════════════════════════════════════════════════════════════════
    static void PolishScene(Scene scene)
    {
        PurgeLegacyObjects(scene);

        GameObject root = new GameObject(RootName);
        SceneManager.MoveGameObjectToScene(root, scene);

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

        AddSceneBackdrop(root, scene.name);
        PositionInteractiveObjects(scene, root);
        PolishUI(scene);
    }

    static void PurgeLegacyObjects(Scene scene)
    {
        string[] badRoots = {
            "_VISUAL_POLISH_ONLY", "_CIPHER_MASTER_BUILD_", "_VISUAL_POLISH_V13_", "_VISUAL_POLISH_V14_",
            "FinishedSpaceBehindDoor", "ReferenceSceneBackdrop"
        };

        foreach (var go in scene.GetRootGameObjects())
        {
            if (badRoots.Contains(go.name))
            {
                Object.DestroyImmediate(go);
                continue;
            }

            string n = go.name.ToLowerInvariant();
            if (n.StartsWith("doorjamb") || n.StartsWith("passage") || n.StartsWith("exitheader") ||
                n.StartsWith("sign") || n.StartsWith("cork") || n.StartsWith("evidsign") ||
                n.StartsWith("archivsign") || n.StartsWith("cybersign") || n.StartsWith("truthsign") ||
                n.StartsWith("promptlabel") || n.StartsWith("l1_clueglow") || n.StartsWith("l2_terminalglow") ||
                n.StartsWith("l3_tableglow") || n.StartsWith("l4_clueglow") || n.StartsWith("l4_keypadglow") ||
                n.StartsWith("l5_tableglow") || n.StartsWith("l6_verdictglow") || n.StartsWith("cluebeacon"))
            {
                Object.DestroyImmediate(go);
            }
        }
    }

    // ═══════════════════════════════════════════════════════════════════════
    //  PHOTOREALISTIC HD BACKDROP
    // ═══════════════════════════════════════════════════════════════════════
    static void AddSceneBackdrop(GameObject root, string sceneName)
    {
        string matName = null;
        switch (sceneName)
        {
            case "Level1_Investigation": matName = "Mat_BG_Level1"; break;
            case "Level2_Computer":      matName = "Mat_BG_Level2"; break;
            case "Level3_Evidence":      matName = "Mat_BG_Level3"; break;
            case "Level4_Archive":       matName = "Mat_BG_Level4"; break;
            case "Level5_CaseFiles":     matName = "Mat_BG_Level5"; break;
            case "Level6_FinalVerdict":  matName = "Mat_BG_Level6"; break;
            case "GameComplete":        matName = "Mat_BG_GameComplete"; break;
            case "MainMenu":            matName = "Mat_BG_MainMenu"; break;
        }
        if (string.IsNullOrEmpty(matName)) return;
        Material m = LoadMat(matName);
        if (!m) return;

        GameObject quad = GameObject.CreatePrimitive(PrimitiveType.Quad);
        quad.name = "ReferenceSceneBackdrop";
        quad.transform.SetParent(root.transform);
        quad.transform.position = new Vector3(0f, 2.50f, 7.95f);
        quad.transform.localScale = new Vector3(16.0f, 5.2f, 1f);
        quad.transform.rotation = Quaternion.identity;
        var col = quad.GetComponent<Collider>();
        if (col) Object.DestroyImmediate(col);
        var rend = quad.GetComponent<Renderer>();
        if (rend) { rend.sharedMaterial = m; rend.shadowCastingMode = UnityEngine.Rendering.ShadowCastingMode.Off; rend.receiveShadows = false; }
    }

    // ═══════════════════════════════════════════════════════════════════════
    //  3D ROOM DESIGNS & ENCLOSED SOLID COLLIDERS
    // ═══════════════════════════════════════════════════════════════════════
    static void BuildRoomShell(GameObject root, Material floorMat, Material wallMat, Material ceilingMat)
    {
        AddPhysicalCube(root, "Floor",      new Vector3(0, -0.10f, 0),  new Vector3(18f, 0.20f, 18f), floorMat);
        AddPhysicalCube(root, "Ceiling",    new Vector3(0,  5.20f, 0),  new Vector3(18f, 0.20f, 18f), ceilingMat);
        AddPhysicalCube(root, "Wall_Back",  new Vector3(0,  2.50f, 8.5f), new Vector3(18f, 5.40f, 0.50f), wallMat);
        AddPhysicalCube(root, "Wall_Front", new Vector3(0,  2.50f,-8.5f), new Vector3(18f, 5.40f, 0.50f), wallMat);
        AddPhysicalCube(root, "Wall_Left",  new Vector3(-8.5f, 2.50f, 0), new Vector3(0.50f, 5.40f, 18f), wallMat);
        AddPhysicalCube(root, "Wall_Right", new Vector3( 8.5f, 2.50f, 0), new Vector3(0.50f, 5.40f, 18f), wallMat);
    }

    static void BuildInvestigationRoom(GameObject root)
    {
        SetAmbient(new Color(0.12f, 0.10f, 0.08f));
        Material floor    = LoadMat("Floor_DarkWood");
        Material wallChar = LoadMat("Wall_Charcoal");
        Material wallWood = LoadMat("Wood_Walnut");
        Material ceiling  = LoadMat("Ceiling_Dark");
        Material trim     = LoadMat("Trim_Black");
        Material gold     = LoadMat("Accent_Gold");
        Material emissive = LoadMat("Light_Emissive");
        Material corkMat  = LoadMat("Cork_Board");
        Material paperMat = LoadMat("Paper_Warm");
        Material frameMat = LoadMat("Frame_Dark");
        Material plantMat = LoadMat("Plant_Green");
        Material potMat   = LoadMat("Pot_Terracotta");
        Material monMat   = LoadMat("Screen_Cyan");

        BuildRoomShell(root, floor, wallChar, ceiling);

        AddCube(root,"Wainscot_Back", new Vector3(0,0.85f,7.88f), new Vector3(15.8f,1.70f,0.08f), wallWood);
        AddCube(root,"Wainscot_Left", new Vector3(-7.88f,0.85f,0),new Vector3(0.08f,1.70f,15.8f), wallWood);
        AddCube(root,"Wainscot_Right",new Vector3( 7.88f,0.85f,0),new Vector3(0.08f,1.70f,15.8f), wallWood);

        AddCube(root,"Rail_Back", new Vector3(0,1.72f,7.85f), new Vector3(15.8f,0.06f,0.10f), gold);
        AddCube(root,"Rail_Left", new Vector3(-7.85f,1.72f,0),new Vector3(0.10f,0.06f,15.8f), gold);
        AddCube(root,"Rail_Right",new Vector3( 7.85f,1.72f,0),new Vector3(0.10f,0.06f,15.8f), gold);
        AddCube(root,"Skirting_Back", new Vector3(0,0.12f,7.90f), new Vector3(15.8f,0.24f,0.10f), trim);

        for (int i = -2; i <= 2; i += 2)
        {
            AddCube(root,"CeilStrip_"+i, new Vector3(i*2.5f,4.93f,0), new Vector3(1.8f,0.06f,0.28f), emissive);
            AddPointLight(root,"CeilLight_"+i, new Vector3(i*2.5f,4.5f,0), new Color(1f,0.93f,0.82f), 3.5f, 9f);
        }

        // Wall Pictures & Certificates
        AddWallPicture(root, "Art_L1", new Vector3(-7.82f, 3.2f, -2.5f), new Vector3(0.08f, 1.4f, 2.0f), LoadMat("Wood_Walnut"), "CASE EVIDENCE ANALYSIS", Gold);
        AddWallPicture(root, "Art_R1", new Vector3(7.82f, 3.2f, -2.5f), new Vector3(0.08f, 1.4f, 2.0f), LoadMat("Cork_Board"), "FORENSIC SURVEY #101", WarmWhite);
        AddWallPicture(root, "Art_BackL", new Vector3(-6.2f, 3.2f, 7.82f), new Vector3(2.0f, 1.3f, 0.08f), LoadMat("Paper_Warm"), "CHIEF DETECTIVE CREST", Gold);

        AddCube(root,"SignFrame",   new Vector3(-4.0f,3.2f,7.82f), new Vector3(3.6f,1.4f,0.08f), frameMat);
        AddCube(root,"SignBg",      new Vector3(-4.0f,3.2f,7.79f), new Vector3(3.3f,1.1f,0.06f), paperMat);
        AddWallText(root,"SignText_L1","INVESTIGATION", new Vector3(-4.0f,3.45f,7.74f), new Color(0.10f,0.10f,0.10f), 3.2f);
        AddWallText(root,"SignText_L1b","BUILDS JUSTICE", new Vector3(-4.0f,3.10f,7.74f), new Color(0.10f,0.10f,0.10f), 2.6f);

        AddCube(root,"CertFrame_1", new Vector3(-7.82f,3.2f,3.0f), new Vector3(0.08f,1.2f,0.9f), frameMat);
        AddCube(root,"CertPaper_1", new Vector3(-7.79f,3.2f,3.0f), new Vector3(0.06f,1.0f,0.75f), paperMat);
        AddWallText(root,"CertText_1","ACADEMY DIPLOMA", new Vector3(-7.74f,3.2f,3.0f), new Color(0.1f,0.1f,0.1f), 1.8f);

        AddCube(root,"CertFrame_2", new Vector3(7.82f,3.2f,3.0f), new Vector3(0.08f,1.2f,0.9f), frameMat);
        AddCube(root,"CertPaper_2", new Vector3(7.79f,3.2f,3.0f), new Vector3(0.06f,1.0f,0.75f), paperMat);
        AddWallText(root,"CertText_2","HONOR & JUSTICE", new Vector3(7.74f,3.2f,3.0f), new Color(0.1f,0.1f,0.1f), 1.8f);

        AddCube(root,"Sconce_L", new Vector3(-7.8f, 2.8f, 0f), new Vector3(0.12f, 0.25f, 0.12f), gold);
        AddPointLight(root,"SconceLight_L", new Vector3(-7.4f, 2.8f, 0f), new Color(1f, 0.85f, 0.60f), 2.0f, 6f);
        AddCube(root,"Sconce_R", new Vector3( 7.8f, 2.8f, 0f), new Vector3(0.12f, 0.25f, 0.12f), gold);
        AddPointLight(root,"SconceLight_R", new Vector3( 7.4f, 2.8f, 0f), new Color(1f, 0.85f, 0.60f), 2.0f, 6f);

        AddCube(root,"CorkBoard",  new Vector3(4.5f,2.7f,7.82f), new Vector3(3.6f,2.2f,0.10f), corkMat);
        AddCube(root,"CorkBorder", new Vector3(4.5f,2.7f,7.79f), new Vector3(3.8f,2.4f,0.06f), frameMat);
        AddCube(root,"CorkPaper_A",new Vector3(3.9f,3.1f,7.75f),new Vector3(0.75f,0.55f,0.03f),paperMat);
        AddCube(root,"CorkPaper_B",new Vector3(4.8f,3.3f,7.75f),new Vector3(0.55f,0.40f,0.03f),LoadMat("Evidence_Red"));
        AddCube(root,"CorkPaper_C",new Vector3(5.2f,2.8f,7.75f),new Vector3(0.65f,0.45f,0.03f),paperMat);
        AddPointLight(root,"CorkLight", new Vector3(4.5f,4.0f,6.5f), new Color(1f,0.88f,0.65f), 2.4f, 6f);

        AddPhysicalCube(root,"Desk_Top",   new Vector3(3.2f,0.80f,4.5f), new Vector3(3.5f,0.10f,1.6f), wallWood);
        AddPhysicalCube(root,"Desk_Leg_A", new Vector3(2.2f,0.40f,4.5f), new Vector3(0.12f,0.80f,1.4f), wallWood);
        AddPhysicalCube(root,"Desk_Leg_B", new Vector3(4.2f,0.40f,4.5f), new Vector3(0.12f,0.80f,1.4f), wallWood);
        AddCube(root,"Monitor_Screen",new Vector3(3.2f,1.40f,4.3f),new Vector3(1.4f,0.90f,0.08f), monMat);
        AddCube(root,"Keyboard",   new Vector3(3.2f,0.87f,4.0f), new Vector3(0.85f,0.05f,0.28f), trim);
        AddCube(root,"DeskLamp_Head",  new Vector3(4.4f,1.55f,4.65f),new Vector3(0.28f,0.12f,0.28f),gold);
        AddPointLight(root,"DeskLampGlow",new Vector3(4.4f,1.35f,4.5f),new Color(1f,0.88f,0.66f),2.5f,4f);
        AddChair(root,"DeskChair", new Vector3(3.2f,0f,3.3f), Quaternion.identity);

        AddPlant(root,"Plant_L", new Vector3(-7.0f,0f,6.5f), plantMat, potMat);
        AddPlant(root,"Plant_R", new Vector3( 7.0f,0f,6.5f), plantMat, potMat);
    }

    static void BuildCyberRoom(GameObject root)
    {
        SetAmbient(new Color(0.06f, 0.08f, 0.14f));
        Material floor   = LoadMat("Floor_CyberTile");
        Material wall    = LoadMat("Wall_CyberDark");
        Material ceiling = LoadMat("Ceiling_Dark");
        Material trim    = LoadMat("Trim_Cyan");
        Material server  = LoadMat("Server_Dark");
        Material monMat  = LoadMat("Screen_Cyan");
        Material frameMat= LoadMat("Frame_Dark");

        BuildRoomShell(root, floor, wall, ceiling);

        AddCube(root,"LED_Strip_Back_Top", new Vector3(0, 4.2f, 7.88f), new Vector3(15.8f, 0.08f, 0.06f), LoadMat("Light_Emissive_Blue"));
        AddCube(root,"LED_Strip_Back_Bot", new Vector3(0, 1.2f, 7.88f), new Vector3(15.8f, 0.08f, 0.06f), LoadMat("Light_Emissive_Blue"));
        AddCube(root,"LED_Strip_Left",     new Vector3(-7.88f, 2.5f, 0), new Vector3(0.06f, 0.08f, 15.8f), LoadMat("Light_Emissive_Blue"));
        AddCube(root,"LED_Strip_Right",    new Vector3( 7.88f, 2.5f, 0), new Vector3(0.06f, 0.08f, 15.8f), LoadMat("Light_Emissive_Blue"));

        // Cyber Wall Pictures & Schematics
        AddWallPicture(root, "CyberArt_L", new Vector3(-7.82f, 3.2f, -2.0f), new Vector3(0.08f, 1.5f, 2.2f), LoadMat("Screen_Cyan"), "NETWORK DIAGRAM v4.2", Cyan);
        AddWallPicture(root, "CyberArt_R", new Vector3(7.82f, 3.2f, -2.0f), new Vector3(0.08f, 1.5f, 2.2f), LoadMat("Trim_Cyan"), "DATA BREACH ANALYSIS", Cyan);
        AddWallPicture(root, "CyberArt_BackL", new Vector3(-5.2f, 3.4f, 7.82f), new Vector3(2.4f, 1.3f, 0.08f), LoadMat("Server_Dark"), "MAIN SERVER FIREWALL", WarmWhite);

        AddCube(root,"DiagScreen_L_Frame", new Vector3(-7.82f,3.2f,4.0f), new Vector3(0.08f,1.4f,2.2f), frameMat);
        AddCube(root,"DiagScreen_L_Disp",  new Vector3(-7.78f,3.2f,4.0f), new Vector3(0.06f,1.2f,2.0f), monMat);
        AddWallText(root,"DiagText_L","SYSTEM OK // ENCRYPTED", new Vector3(-7.72f,3.2f,4.0f), Cyan, 1.8f);

        AddCube(root,"DiagScreen_R_Frame", new Vector3(7.82f,3.2f,4.0f), new Vector3(0.08f,1.4f,2.2f), frameMat);
        AddCube(root,"DiagScreen_R_Disp",  new Vector3(7.78f,3.2f,4.0f), new Vector3(0.06f,1.2f,2.0f), monMat);
        AddWallText(root,"DiagText_R","CYBER LAB STATUS 100%", new Vector3(7.72f,3.2f,4.0f), Cyan, 1.8f);

        for (int i = -3; i <= 3; i++) AddCube(root,"CeilGrid_X_"+i, new Vector3(i*2.2f,4.94f,0), new Vector3(0.06f,0.05f,16f), trim);
        for (int i = -3; i <= 3; i++) AddCube(root,"CeilGrid_Z_"+i, new Vector3(0,4.94f,i*2.2f), new Vector3(16f,0.05f,0.06f), trim);

        AddCube(root,"SignBacking", new Vector3(0,3.6f,7.82f), new Vector3(6.0f,1.6f,0.10f), LoadMat("Trim_Black"));
        AddWallText(root,"CyberSignL1","CYBER", new Vector3(0,4.10f,7.76f), Cyan, 5.0f);
        AddWallText(root,"CyberSignL2","INVESTIGATION UNIT", new Vector3(0,3.45f,7.76f), WarmWhite, 3.2f);
        AddPointLight(root,"SignGlow", new Vector3(0,3.5f,7.0f), Cyan, 2.5f, 6f);

        for (int i = -1; i <= 1; i++) BuildWorkstation(root, "WS_Back_"+i, new Vector3(i*3.5f,0f,4.5f), false);

        for (int z = -2; z <= 2; z += 2)
        {
            AddPhysicalCube(root,"SR_L_"+z, new Vector3(-7.6f,2.0f,z), new Vector3(0.8f,3.6f,1.4f), server);
            AddPhysicalCube(root,"SR_R_"+z, new Vector3(7.6f,2.0f,z), new Vector3(0.8f,3.6f,1.4f), server);
            AddPointLight(root,"SRL_Light_"+z, new Vector3(-7f,2f,z), Cyan, 1.5f, 4f);
            AddPointLight(root,"SRR_Light_"+z, new Vector3(7f,2f,z), Cyan, 1.5f, 4f);
        }

        AddPointLight(root,"CyberAmbient_A", new Vector3(-3f,0.5f,-2f), new Color(0.05f,0.4f,0.8f), 2.5f, 10f);
        AddPointLight(root,"CyberAmbient_B", new Vector3( 3f,0.5f,-2f), new Color(0.05f,0.4f,0.8f), 2.5f, 10f);
    }

    static void BuildEvidenceRoom(GameObject root)
    {
        SetAmbient(new Color(0.14f, 0.13f, 0.12f));
        Material floor   = LoadMat("Floor_DarkWood");
        Material wall    = LoadMat("Wall_LightGrey");
        Material ceiling = LoadMat("Ceiling_Mid");
        Material wood    = LoadMat("Wood_Walnut");
        Material metal   = LoadMat("Metal_Dark");
        Material plantMat= LoadMat("Plant_Green");
        Material potMat  = LoadMat("Pot_Terracotta");
        Material emissive= LoadMat("Light_Emissive");
        Material paperMat= LoadMat("Paper_Warm");
        Material frameMat= LoadMat("Frame_Dark");

        BuildRoomShell(root, floor, wall, ceiling);

        AddCube(root,"EvidWainscot_Back", new Vector3(0,0.85f,7.88f), new Vector3(15.8f,1.70f,0.08f), LoadMat("Trim_Cyan"));
        AddCube(root,"EvidRail_Back",     new Vector3(0,1.72f,7.85f), new Vector3(15.8f,0.06f,0.10f), LoadMat("Marker_Yellow"));

        for (int i = -2; i <= 2; i += 2)
        {
            AddCube(root,"CeilPanel_"+i, new Vector3(i*2.8f,4.93f,0), new Vector3(2.4f,0.06f,0.8f), emissive);
            AddPointLight(root,"CeilPanelLight_"+i, new Vector3(i*2.8f,4.5f,0), new Color(1f,0.96f,0.90f), 4.5f, 11f);
        }

        // Evidence Wall Pictures & Framed Documents
        AddWallPicture(root, "EvidArt_L", new Vector3(-7.82f, 3.2f, 0.0f), new Vector3(0.08f, 1.6f, 2.2f), LoadMat("Evidence_Red"), "FORENSIC LAB REPORT", CrimsonRed);
        AddWallPicture(root, "EvidArt_R", new Vector3(7.82f, 3.2f, 0.0f), new Vector3(0.08f, 1.6f, 2.2f), LoadMat("Paper_Warm"), "CHAIN OF CUSTODY SEAL", Gold);
        AddWallPicture(root, "EvidArt_BackR", new Vector3(4.8f, 3.2f, 7.82f), new Vector3(2.4f, 1.4f, 0.08f), LoadMat("Wood_Walnut"), "SECURITY VAULT PROTOCOL", Gold);

        AddCube(root,"EvidSignBack",new Vector3(0,3.2f,7.82f),new Vector3(5.5f,1.6f,0.10f), frameMat);
        AddCube(root,"EvidSignPaper",new Vector3(0,3.2f,7.79f),new Vector3(5.0f,1.25f,0.06f),paperMat);
        AddWallText(root,"EvidSign1","EVERY EVIDENCE", new Vector3(0,3.5f,7.74f), new Color(0.08f,0.08f,0.08f), 3.2f);
        AddWallText(root,"EvidSign2","TELLS A STORY",  new Vector3(0,3.1f,7.74f), new Color(0.08f,0.08f,0.08f), 3.2f);

        AddCube(root,"CaseBoard_Frame", new Vector3(-4.5f, 3.0f, 7.82f), new Vector3(3.4f, 2.0f, 0.08f), frameMat);
        AddCube(root,"CaseBoard_Bg",    new Vector3(-4.5f, 3.0f, 7.79f), new Vector3(3.1f, 1.7f, 0.06f), paperMat);
        AddWallText(root,"CaseBoard_Title", "CRIME SCENE #402", new Vector3(-4.5f, 3.6f, 7.74f), CrimsonRed, 2.2f);

        AddPhysicalCube(root,"EvidTable_Top", new Vector3(0,0.80f,2.0f), new Vector3(5.0f,0.12f,2.2f), wood);
        AddPhysicalCube(root,"EvidTable_Leg1",new Vector3(-2.3f,0.38f,2.0f),new Vector3(0.12f,0.76f,1.9f),wood);
        AddPhysicalCube(root,"EvidTable_Leg2",new Vector3( 2.3f,0.38f,2.0f),new Vector3(0.12f,0.76f,1.9f),wood);

        AddEvidenceMarker(root,"EvMark_1", new Vector3(-1.2f,0.92f,1.8f), "1");
        AddEvidenceMarker(root,"EvMark_2", new Vector3( 0.2f,0.92f,2.2f), "2");
        AddEvidenceMarker(root,"EvMark_3", new Vector3( 1.5f,0.92f,1.7f), "3");

        AddCube(root,"CaseFolder",  new Vector3(-0.5f,0.87f,2.5f),new Vector3(0.65f,0.04f,0.90f),LoadMat("Folder_Red"));
        AddCube(root,"Flashlight",  new Vector3(0.8f,0.88f,2.6f), new Vector3(0.12f,0.08f,0.45f),metal);

        BuildMetalShelf(root,"Shelf_L1", new Vector3(-7.2f,0f,3.5f));
        BuildMetalShelf(root,"Shelf_R1", new Vector3( 7.2f,0f,3.5f));

        AddPlant(root,"Plant_BL",new Vector3(-7.0f,0f,6.8f),plantMat,potMat);
        AddPlant(root,"Plant_BR",new Vector3( 7.0f,0f,6.8f),plantMat,potMat);
    }

    static void BuildArchiveRoom(GameObject root)
    {
        SetAmbient(new Color(0.08f, 0.07f, 0.05f));
        Material floor   = LoadMat("Floor_Concrete");
        Material wall    = LoadMat("Wall_Archive");
        Material ceiling = LoadMat("Ceiling_Dark");
        Material metal   = LoadMat("Metal_Dark");
        Material wood    = LoadMat("Wood_Walnut");
        Material boxMat  = LoadMat("Archive_Box");

        BuildRoomShell(root, floor, wall, ceiling);

        // Archive Wall Pictures
        AddWallPicture(root, "ArchiveArt_L", new Vector3(-7.82f, 3.2f, 1.5f), new Vector3(0.08f, 1.6f, 2.0f), LoadMat("Paper_Warm"), "CASE CATALOGUE #1894", Gold);
        AddWallPicture(root, "ArchiveArt_R", new Vector3(7.82f, 3.2f, 1.5f), new Vector3(0.08f, 1.6f, 2.0f), LoadMat("Wood_Walnut"), "HISTORICAL JUDICIAL RECORDS", WarmWhite);
        AddWallPicture(root, "ArchiveArt_BackL", new Vector3(-5.5f, 3.4f, 7.82f), new Vector3(2.2f, 1.3f, 0.08f), LoadMat("Frame_Dark"), "ARCHIVE DEPOSITORY CHARTER", Gold);

        for (int z = -4; z <= 6; z += 5)
        {
            AddPhysicalCube(root, "BrickPillar_L_"+z, new Vector3(-7.75f, 2.5f, z), new Vector3(0.35f, 5.0f, 0.6f), wall);
            AddPhysicalCube(root, "BrickPillar_R_"+z, new Vector3( 7.75f, 2.5f, z), new Vector3(0.35f, 5.0f, 0.6f), wall);
            AddPointLight(root, "Lantern_L_"+z, new Vector3(-7.2f, 3.2f, z), new Color(1f, 0.72f, 0.35f), 2.2f, 6f);
            AddPointLight(root, "Lantern_R_"+z, new Vector3( 7.2f, 3.2f, z), new Color(1f, 0.72f, 0.35f), 2.2f, 6f);
        }

        AddCube(root,"ArchivPlaque_Frame", new Vector3(-4.5f, 3.2f, 7.82f), new Vector3(2.8f, 1.4f, 0.08f), LoadMat("Metal_Gold"));
        AddCube(root,"ArchivPlaque_Bg",    new Vector3(-4.5f, 3.2f, 7.79f), new Vector3(2.5f, 1.1f, 0.06f), wall);
        AddWallText(root,"ArchivPlaque_Text", "RECORDS DIVISION\nEST. 1924", new Vector3(-4.5f, 3.2f, 7.74f), Gold, 2.0f);

        AddCube(root,"ArchivSignBack",new Vector3(0,3.8f,7.82f),new Vector3(5.0f,1.4f,0.12f),metal);
        AddWallText(root,"ArchivSign1","ARCHIVE",          new Vector3(0,4.20f,7.76f), Gold, 4.5f);
        AddWallText(root,"ArchivSign2","RESTRICTED ACCESS",new Vector3(0,3.65f,7.76f), WarmWhite, 2.8f);

        float[] zPositions = { 4.5f, 1.5f, -1.5f };
        foreach (float zp in zPositions)
        {
            BuildTallArchiveShelf(root,"ShelfL_"+zp, new Vector3(-3.8f,0f,zp), metal, boxMat, wood);
            BuildTallArchiveShelf(root,"ShelfR_"+zp, new Vector3( 3.8f,0f,zp), metal, boxMat, wood);
        }

        AddCube(root,"WarnTape_A",new Vector3(-3.8f,0.01f,2f),new Vector3(0.20f,0.02f,6f),LoadMat("Evidence_Red"));
        AddCube(root,"WarnTape_B",new Vector3( 3.8f,0.01f,2f),new Vector3(0.20f,0.02f,6f),LoadMat("Evidence_Red"));
    }

    static void BuildStatementsRoom(GameObject root)
    {
        SetAmbient(new Color(0.11f, 0.09f, 0.07f));
        Material floor   = LoadMat("Floor_DarkWood");
        Material wall    = LoadMat("Wall_WoodPanel");
        Material ceiling = LoadMat("Ceiling_Dark");
        Material wood    = LoadMat("Wood_Walnut");

        BuildRoomShell(root, floor, wall, ceiling);

        // Statements Wall Pictures & Oaths
        AddWallPicture(root, "StmtArt_L", new Vector3(-7.82f, 3.2f, 0.0f), new Vector3(0.08f, 1.7f, 2.4f), LoadMat("Wood_Dark"), "JUDICIAL WITNESS CHARTER", Gold);
        AddWallPicture(root, "StmtArt_R", new Vector3(7.82f, 3.2f, 0.0f), new Vector3(0.08f, 1.7f, 2.4f), LoadMat("Paper_Warm"), "TESTIMONY VERIFICATION OATH", Gold);
        AddWallPicture(root, "StmtArt_BackL", new Vector3(-5.2f, 3.4f, 7.82f), new Vector3(2.4f, 1.4f, 0.08f), LoadMat("Folder_Red"), "HIGH COURT CASE DOSSIER", CrimsonRed);

        for (int i = -7; i <= 7; i++)
        {
            Material sm = (i % 2 == 0) ? LoadMat("WoodSlat_Dark") : LoadMat("WoodSlat_Light");
            AddCube(root,"Slat_Back_"+i, new Vector3(i*1.05f,2.5f,7.88f), new Vector3(0.08f,4.8f,0.06f), sm);
        }

        AddCube(root,"TestimonyPlaque", new Vector3(0, 3.7f, 7.82f), new Vector3(6.2f, 1.2f, 0.10f), LoadMat("Wood_Dark"));
        AddWallText(root,"TestimonyText1", "STATEMENTS & TESTIMONY", new Vector3(0, 3.95f, 7.76f), Gold, 3.6f);
        AddWallText(root,"TestimonyText2", "TRUTH UNDER OATH", new Vector3(0, 3.50f, 7.76f), WarmWhite, 2.4f);

        AddCube(root,"Chandelier_Body",new Vector3(0,4.0f,1.5f),new Vector3(1.8f,0.20f,1.8f),LoadMat("Accent_Gold"));
        AddPointLight(root,"ChandelierGlow",new Vector3(0,3.6f,1.5f),new Color(1f,0.82f,0.55f),5.0f,11f);

        AddPhysicalCube(root,"ConfTable",    new Vector3(0,0.80f,1.5f), new Vector3(6.0f,0.14f,2.8f), wood);
        AddPhysicalCube(root,"ConfTableLeg1",new Vector3(-2.7f,0.38f,1.5f),new Vector3(0.14f,0.76f,2.6f),wood);
        AddPhysicalCube(root,"ConfTableLeg2",new Vector3( 2.7f,0.38f,1.5f),new Vector3(0.14f,0.76f,2.6f),wood);

        AddCube(root,"Folder_Ruby",    new Vector3(-1.8f,0.88f,1.6f), new Vector3(0.55f,0.04f,0.75f), LoadMat("Folder_Red"));
        AddCube(root,"Folder_Emerald", new Vector3( 0.0f,0.88f,1.4f), new Vector3(0.55f,0.04f,0.75f), LoadMat("Flag_Green"));
        AddCube(root,"Folder_Sapphire",new Vector3( 1.8f,0.88f,1.6f), new Vector3(0.55f,0.04f,0.75f), LoadMat("Flag_Blue"));

        AddChair(root,"Chair_L1",new Vector3(-3.5f,0f,0.5f),Quaternion.Euler(0,90,0));
        AddChair(root,"Chair_L2",new Vector3(-3.5f,0f,2.5f),Quaternion.Euler(0,90,0));
        AddChair(root,"Chair_R1",new Vector3( 3.5f,0f,0.5f),Quaternion.Euler(0,-90,0));
        AddChair(root,"Chair_R2",new Vector3( 3.5f,0f,2.5f),Quaternion.Euler(0,-90,0));
    }

    static void BuildCourtroom(GameObject root)
    {
        SetAmbient(new Color(0.14f, 0.12f, 0.10f));
        Material floor   = LoadMat("Floor_Marble");
        Material wall    = LoadMat("Wall_CourtWood");
        Material ceiling = LoadMat("Ceiling_Court");
        Material wood    = LoadMat("Wood_Walnut");
        Material richWood= LoadMat("Wood_Dark");
        Material gold    = LoadMat("Accent_Gold");
        Material carpet  = LoadMat("Rug_Dark");

        BuildRoomShell(root, floor, wall, ceiling);

        // Courtroom Pictures & Wall Charters
        AddWallPicture(root, "CourtArt_L1", new Vector3(-7.82f, 3.2f, 3.0f), new Vector3(0.08f, 1.8f, 2.6f), LoadMat("Wood_Dark"), "PORTRAIT OF JUSTICES", Gold);
        AddWallPicture(root, "CourtArt_L2", new Vector3(-7.82f, 3.2f, -2.5f), new Vector3(0.08f, 1.8f, 2.6f), LoadMat("Paper_Warm"), "CONSTITUTION OF INDIA CHARTER", Gold);
        AddWallPicture(root, "CourtArt_R1", new Vector3(7.82f, 3.2f, 3.0f), new Vector3(0.08f, 1.8f, 2.6f), LoadMat("Wood_Dark"), "THE SCALES OF JUSTICE", Gold);
        AddWallPicture(root, "CourtArt_R2", new Vector3(7.82f, 3.2f, -2.5f), new Vector3(0.08f, 1.8f, 2.6f), LoadMat("Accent_Gold"), "HIGH COURT SEAL OF HONOR", Gold);

        AddCube(root, "CourtCarpet", new Vector3(0, 0.01f, 0), new Vector3(4.0f, 0.02f, 15.0f), carpet);

        AddCube(root, "CrownMolding_Back", new Vector3(0, 4.9f, 7.85f), new Vector3(15.8f, 0.18f, 0.15f), gold);
        AddCube(root, "CrownMolding_Left", new Vector3(-7.85f, 4.9f, 0), new Vector3(0.15f, 0.18f, 15.8f), gold);
        AddCube(root, "CrownMolding_Right",new Vector3( 7.85f, 4.9f, 0), new Vector3(0.15f, 0.18f, 15.8f), gold);

        AddPhysicalCube(root, "JudgePlatform",    new Vector3(0, 0.35f, 6.2f), new Vector3(9.5f, 0.70f, 3.2f), richWood);
        AddPhysicalCube(root, "JudgeBench_Front", new Vector3(0, 1.35f, 5.2f), new Vector3(8.5f, 2.00f, 0.25f), richWood);
        AddPhysicalCube(root, "JudgeBench_Top",   new Vector3(0, 2.38f, 6.0f), new Vector3(8.8f, 0.15f, 2.8f), richWood);
        AddChair(root, "JudgeChair", new Vector3(0, 0.70f, 6.6f), Quaternion.identity);

        AddCylinder(root, "JusticeEmblem_Ring", new Vector3(0, 4.8f, 7.80f), new Vector3(1.8f, 0.06f, 1.8f), gold);
        AddWallText(root, "EmblemText", "SATYAMEVA JAYATE", new Vector3(0, 4.8f, 7.74f), Gold, 2.6f);
        AddWallText(root, "TruthSign", "TRUTH ALWAYS PREVAILS", new Vector3(0, 4.1f, 7.74f), WarmWhite, 3.0f);

        BuildIndianFlag(root, "Flag_Left",  new Vector3(-3.8f, 4.0f, 7.75f));
        BuildIndianFlag(root, "Flag_Right", new Vector3( 3.8f, 4.0f, 7.75f));

        AddPhysicalCube(root, "WitnessBox_Base",  new Vector3(-5.8f, 0.25f, 4.8f), new Vector3(2.2f, 0.50f, 2.2f), richWood);
        AddPhysicalCube(root, "WitnessBox_Front", new Vector3(-5.8f, 0.90f, 3.8f), new Vector3(2.2f, 1.10f, 0.12f), richWood);
        AddPhysicalCube(root, "WitnessBox_Side",  new Vector3(-4.8f, 0.90f, 4.8f), new Vector3(0.12f, 1.10f, 2.2f), richWood);
        AddChair(root, "WitnessChair", new Vector3(-5.8f, 0.50f, 5.0f), Quaternion.identity);

        AddPhysicalCube(root, "JuryPlatform", new Vector3(5.8f, 0.25f, 4.8f), new Vector3(3.2f, 0.50f, 4.0f), richWood);
        AddPhysicalCube(root, "JuryFront",    new Vector3(4.3f, 0.90f, 4.8f), new Vector3(0.15f, 1.10f, 4.0f), richWood);
        for (int jz = 0; jz < 2; jz++)
        {
            AddChair(root, "JuryChair_A_"+jz, new Vector3(5.2f, 0.50f, 3.8f + jz*1.8f), Quaternion.Euler(0, -90, 0));
            AddChair(root, "JuryChair_B_"+jz, new Vector3(6.4f, 0.50f, 3.8f + jz*1.8f), Quaternion.Euler(0, -90, 0));
        }

        AddPhysicalCube(root, "DefTable_Top",   new Vector3(-3.5f, 0.80f, 1.8f), new Vector3(3.6f, 0.12f, 1.6f), wood);
        AddPhysicalCube(root, "DefTable_LegL",  new Vector3(-5.1f, 0.38f, 1.8f), new Vector3(0.12f, 0.76f, 1.4f), wood);
        AddPhysicalCube(root, "DefTable_LegR",  new Vector3(-1.9f, 0.38f, 1.8f), new Vector3(0.12f, 0.76f, 1.4f), wood);
        AddChair(root, "DefChair_1", new Vector3(-4.2f, 0.0f, 0.8f), Quaternion.identity);
        AddChair(root, "DefChair_2", new Vector3(-2.8f, 0.0f, 0.8f), Quaternion.identity);

        AddPhysicalCube(root, "ProsTable_Top",  new Vector3( 3.5f, 0.80f, 1.8f), new Vector3(3.6f, 0.12f, 1.6f), wood);
        AddPhysicalCube(root, "ProsTable_LegL", new Vector3( 1.9f, 0.38f, 1.8f), new Vector3(0.12f, 0.76f, 1.4f), wood);
        AddPhysicalCube(root, "ProsTable_LegR", new Vector3( 5.1f, 0.38f, 1.8f), new Vector3(0.12f, 0.76f, 1.4f), wood);
        AddChair(root, "ProsChair_1", new Vector3( 2.8f, 0.0f, 0.8f), Quaternion.identity);
        AddChair(root, "ProsChair_2", new Vector3( 4.2f, 0.0f, 0.8f), Quaternion.identity);

        AddPhysicalCube(root, "GalleryDivider_L", new Vector3(-4.2f, 0.60f, -1.5f), new Vector3(6.5f, 1.20f, 0.18f), richWood);
        AddPhysicalCube(root, "GalleryDivider_R", new Vector3( 4.2f, 0.60f, -1.5f), new Vector3(6.5f, 1.20f, 0.18f), richWood);

        AddCube(root, "CourtChandelier_1", new Vector3(0, 4.4f, 3.5f), new Vector3(2.2f, 0.25f, 2.2f), gold);
        AddPointLight(root, "CourtChandelierLight_1", new Vector3(0, 3.8f, 3.5f), new Color(1f, 0.90f, 0.72f), 5.5f, 12f);

        AddCube(root, "CourtChandelier_2", new Vector3(0, 4.4f, -2.5f), new Vector3(2.2f, 0.25f, 2.2f), gold);
        AddPointLight(root, "CourtChandelierLight_2", new Vector3(0, 3.8f, -2.5f), new Color(1f, 0.90f, 0.72f), 5.5f, 12f);
    }

    static void BuildMainMenuRoom(GameObject root)
    {
        SetAmbient(new Color(0.04f, 0.04f, 0.06f));
        Material floor = LoadMat("Floor_Marble");
        Material wall  = LoadMat("Wall_MenuDark");

        BuildRoomShell(root, floor, wall, wall);

        BuildScalesOfJustice(root, new Vector3(4.5f, 0f, 5f), 1.5f);
        BuildGavel(root, new Vector3(-4.5f, 0f, 5f));

        AddWallText(root,"MenuTitle1","CIPHER COURT", new Vector3(0,4.9f,7.78f), Gold, 6.0f);
        AddWallText(root,"MenuTitle2","ESCAPE TO JUSTICE ROOM",new Vector3(0,4.35f,7.78f),WarmWhite,3.0f);
        AddPointLight(root,"MenuSpot_A",new Vector3(0,5.5f,4f),new Color(1f,0.88f,0.70f),5.5f,14f);

        ApplyCinematicBackground("Assets/CipherCourtPolish/Backgrounds/Menu_Legal_Cinematic.png");
        StyleMainMenuUI();
    }

    static void BuildGameCompleteRoom(GameObject root)
    {
        SetAmbient(new Color(0.06f, 0.06f, 0.08f));
        Material floor = LoadMat("Floor_Marble");
        Material wall  = LoadMat("Wall_CourtWood");

        BuildRoomShell(root, floor, wall, wall);

        BuildScalesOfJustice(root, new Vector3(0,0f,4f), 2.0f);
        AddWallText(root,"CompTitle","CASE SOLVED",    new Vector3(0,4.8f,7.78f),WarmWhite,6.0f);
        AddWallText(root,"CompSub",  "JUSTICE SERVED", new Vector3(0,4.2f,7.78f),new Color(0.85f,0.18f,0.18f),3.5f);
        AddPointLight(root,"WinLight_A",new Vector3(0,5f,4f),Gold,6.0f,14f);

        ApplyCinematicBackground("Assets/CipherCourtPolish/Backgrounds/Complete_Legal_Cinematic.png");
        StyleGameCompleteUI();
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
        }
    }

    // ═══════════════════════════════════════════════════════════════════════
    //  ALIGN INTERACTIVE GAMEPLAY OBJECTS & HIGHLY VISIBLE CLUE BEACONS
    // ═══════════════════════════════════════════════════════════════════════
    static void PositionInteractiveObjects(Scene scene, GameObject root)
    {
        GameObject door = Object.FindObjectsByType<GameObject>(FindObjectsSortMode.None)
            .FirstOrDefault(g => g.name == "Door" || g.name.ToLowerInvariant().Contains("exitdoor") || g.name == "LevelExit");
        if (door)
        {
            Vector3 doorPos = scene.name == "Level6_FinalVerdict" ? new Vector3(6.2f, 1.5f, 7.3f) : new Vector3(0f, 1.5f, 7.3f);
            door.transform.position = doorPos;
            AddDoorReveal(root, door);
        }

        switch (scene.name)
        {
            case "Level1_Investigation":
                var collectables = Object.FindObjectsByType<CollectibleItem>(FindObjectsSortMode.None).ToList();
                GameObject clue1 = collectables.FirstOrDefault(c => c.name.ToLowerInvariant().Contains("clue") || c.name.ToLowerInvariant().Contains("evidence"))?.gameObject;
                GameObject key1 = collectables.FirstOrDefault(c => c.name.ToLowerInvariant().Contains("key") || (clue1 != null && c.gameObject != clue1))?.gameObject;

                if (!clue1)
                {
                    clue1 = new GameObject("InvestigationClue_Item");
                    clue1.AddComponent<CollectibleItem>();
                }
                clue1.transform.position = new Vector3(2.0f, 0.95f, 4.2f);
                HighlightClue(root, clue1, "EVIDENCE CLUE", Gold, LoadMat("Folder_Red"));

                if (!key1)
                {
                    key1 = new GameObject("SecurityKey_Item");
                    var keyComp = key1.AddComponent<CollectibleItem>();
                    var typeField = typeof(CollectibleItem).GetField("itemType", System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Instance);
                    if (typeField != null) typeField.SetValue(keyComp, CollectibleItem.ItemType.Key);
                }
                key1.transform.position = new Vector3(4.4f, 0.95f, 4.2f);
                HighlightClue(root, key1, "SECURITY KEY", Gold, LoadMat("Metal_Gold"));
                break;

            case "Level2_Computer":
                var passClueComp = Object.FindFirstObjectByType<PasswordClue>();
                GameObject clue2 = passClueComp ? passClueComp.gameObject : null;
                if (!clue2)
                {
                    clue2 = new GameObject("PasswordClue_Item");
                    clue2.AddComponent<PasswordClue>();
                }
                clue2.transform.position = new Vector3(-3.2f, 0.95f, 4.2f);
                HighlightClue(root, clue2, "PASSWORD CLUE", Cyan, LoadMat("Screen_Cyan"));

                var term2 = Object.FindObjectsByType<GameObject>(FindObjectsSortMode.None)
                    .FirstOrDefault(g => g.name.ToLowerInvariant().Contains("computer") || g.name.ToLowerInvariant().Contains("terminal"));
                if (term2)
                {
                    term2.transform.position = new Vector3(0f, 0.95f, 2.0f);
                    HighlightClue(root, term2, "LOGIN TERMINAL", Cyan, LoadMat("Screen_Cyan"));
                }
                break;

            case "Level3_Evidence":
                var files3 = Object.FindObjectsByType<GameObject>(FindObjectsSortMode.None)
                    .Where(g => g.name.ToLowerInvariant().Contains("file") || g.name.ToLowerInvariant().Contains("evidence"))
                    .ToList();
                Vector3[] slots3 = { new Vector3(-1.2f, 0.95f, 2.0f), new Vector3(0.0f, 0.95f, 2.4f), new Vector3(1.2f, 0.95f, 2.0f) };
                int idx3 = 0;
                foreach (var f in files3)
                {
                    if (f.transform.parent != null && f.transform.parent.name == RootName) continue;
                    if (idx3 < slots3.Length)
                    {
                        f.transform.position = slots3[idx3];
                        HighlightClue(root, f, "EVIDENCE #" + (idx3 + 1), Gold, LoadMat("Marker_Yellow"));
                        idx3++;
                    }
                }
                break;

            case "Level4_Archive":
                var clues4 = Object.FindObjectsByType<GameObject>(FindObjectsSortMode.None)
                    .Where(g => g.name.ToLowerInvariant().Contains("clue") && g.transform.parent?.name != RootName)
                    .ToList();
                Vector3[] slots4 = { new Vector3(-3.8f, 1.45f, 3.5f), new Vector3(3.8f, 1.45f, 0.5f), new Vector3(-3.8f, 1.45f, -1.5f) };
                for (int i = 0; i < clues4.Count && i < slots4.Length; i++)
                {
                    clues4[i].transform.position = slots4[i];
                    HighlightClue(root, clues4[i], "ARCHIVE CLUE #" + (i + 1), Gold, LoadMat("Archive_Box"));
                }

                var archiveKeypadComp = Object.FindFirstObjectByType<ArchiveKeypad>();
                GameObject keypad4 = archiveKeypadComp ? archiveKeypadComp.gameObject :
                    Object.FindObjectsByType<GameObject>(FindObjectsSortMode.None)
                        .FirstOrDefault(g => g.name.ToLowerInvariant().Contains("keypad") && g.transform.parent?.name != RootName);

                if (!keypad4)
                {
                    keypad4 = new GameObject("ArchiveKeypad_Terminal");
                    keypad4.AddComponent<ArchiveKeypad>();
                }

                keypad4.transform.position = new Vector3(1.8f, 1.25f, 6.8f);
                BuildKeypadConsoleVisual(root, keypad4);
                HighlightClue(root, keypad4, "ARCHIVE KEYPAD", Gold, LoadMat("Metal_Gold"));

                var l4Puzzle = Object.FindFirstObjectByType<Level4ArchivePuzzle>();
                var akScript = keypad4.GetComponent<ArchiveKeypad>();
                if (akScript && l4Puzzle) akScript.puzzle = l4Puzzle;
                break;

            case "Level5_CaseFiles":
                var files5 = Object.FindObjectsByType<GameObject>(FindObjectsSortMode.None)
                    .Where(g => g.name.ToLowerInvariant().Contains("file") || g.name.ToLowerInvariant().Contains("statement"))
                    .ToList();
                Vector3[] slots5 = { new Vector3(-1.8f, 0.95f, 1.6f), new Vector3(0.0f, 0.95f, 1.4f), new Vector3(1.8f, 0.95f, 1.6f) };
                for (int i = 0; i < files5.Count && i < slots5.Length; i++)
                {
                    if (files5[i].transform.parent != null && files5[i].transform.parent.name == RootName) continue;
                    files5[i].transform.position = slots5[i];
                    HighlightClue(root, files5[i], "STATEMENT #" + (i + 1), Gold, LoadMat("Folder_Red"));
                }
                break;

            case "Level6_FinalVerdict":
                var statements6 = Object.FindObjectsByType<GameObject>(FindObjectsSortMode.None)
                    .Where(g => g.name.ToLowerInvariant().Contains("statement") || g.name.ToLowerInvariant().Contains("clue"))
                    .ToList();
                Vector3[] slots6 = { new Vector3(-3.5f, 0.95f, 1.8f), new Vector3(3.5f, 0.95f, 1.8f), new Vector3(-5.8f, 0.95f, 4.8f) };
                for (int i = 0; i < statements6.Count && i < slots6.Length; i++)
                {
                    if (statements6[i].transform.parent != null && statements6[i].transform.parent.name == RootName) continue;
                    statements6[i].transform.position = slots6[i];
                    HighlightClue(root, statements6[i], "LEGAL EVIDENCE #" + (i + 1), Gold, LoadMat("Folder_Red"));
                }
                var term6 = Object.FindObjectsByType<GameObject>(FindObjectsSortMode.None)
                    .FirstOrDefault(g => g.name.ToLowerInvariant().Contains("terminal") || g.name.ToLowerInvariant().Contains("verdict"));
                if (term6)
                {
                    term6.transform.position = new Vector3(0.0f, 0.95f, 4.2f);
                    HighlightClue(root, term6, "VERDICT CONSOLE", CrimsonRed, LoadMat("Metal_Gold"));
                }
                break;
        }
    }

    static void BuildKeypadConsoleVisual(GameObject root, GameObject keypadObj)
    {
        if (!keypadObj) return;

        Material metal = LoadMat("Metal_Dark");
        Material gold = LoadMat("Accent_Gold");
        Material screen = LoadMat("Screen_Cyan");

        GameObject visual = new GameObject("KeypadConsoleVisual");
        visual.transform.SetParent(keypadObj.transform, false);
        visual.transform.localPosition = Vector3.zero;

        AddCube(visual, "PedestalBase", new Vector3(0, -0.6f, 0), new Vector3(0.6f, 0.1f, 0.6f), metal);
        AddCube(visual, "PedestalPole", new Vector3(0, -0.1f, 0), new Vector3(0.15f, 1.0f, 0.15f), metal);
        AddCube(visual, "TerminalBox",  new Vector3(0, 0.4f, 0),  new Vector3(0.7f, 0.9f, 0.25f), metal);
        AddCube(visual, "ScreenDisplay",new Vector3(0, 0.55f, -0.10f), new Vector3(0.55f, 0.45f, 0.08f), screen);
        AddCube(visual, "KeyPadGrid",   new Vector3(0, 0.18f, -0.10f), new Vector3(0.50f, 0.25f, 0.08f), gold);

        AddPointLight(visual, "TerminalGlow", new Vector3(0, 0.55f, -0.3f), Cyan, 2.5f, 4f);
    }

    static void HighlightClue(GameObject root, GameObject target, string label, Color beaconColor, Material visualMat)
    {
        if (!target) return;

        // Ensure visible 3D Mesh Renderer if target is missing a renderer
        var rends = target.GetComponentsInChildren<Renderer>(true);
        if (rends == null || rends.Length == 0)
        {
            GameObject meshVisual = GameObject.CreatePrimitive(PrimitiveType.Cube);
            meshVisual.name = "ClueVisualModel";
            meshVisual.transform.SetParent(target.transform, false);
            meshVisual.transform.localPosition = new Vector3(0, 0.15f, 0);
            meshVisual.transform.localScale = new Vector3(0.60f, 0.35f, 0.70f);
            var col = meshVisual.GetComponent<Collider>();
            if (col) Object.DestroyImmediate(col);
            var r = meshVisual.GetComponent<Renderer>();
            if (r && visualMat) r.sharedMaterial = visualMat;
        }
        else
        {
            foreach (var r in rends)
            {
                r.enabled = true;
                if (visualMat && (r.sharedMaterial == null || r.sharedMaterial.name.Contains("Default")))
                    r.sharedMaterial = visualMat;
            }
        }

        // Add Pulsing Spotlight Beacon parented DIRECTLY to target (so it disappears when clue is collected!)
        GameObject beacon = new GameObject("ClueBeacon_" + label);
        beacon.transform.SetParent(target.transform, false);
        beacon.transform.localPosition = Vector3.up * 0.75f;

        Light l = beacon.AddComponent<Light>();
        l.type = LightType.Point;
        l.color = beaconColor;
        l.intensity = 4.5f;
        l.range = 5.0f;
        l.shadows = LightShadows.None;

        // Glowing indicator sphere floating above clue
        GameObject markerPin = GameObject.CreatePrimitive(PrimitiveType.Sphere);
        markerPin.name = "BeaconPin";
        markerPin.transform.SetParent(beacon.transform, false);
        markerPin.transform.localPosition = Vector3.zero;
        markerPin.transform.localScale = Vector3.one * 0.22f;
        var mCol = markerPin.GetComponent<Collider>();
        if (mCol) Object.DestroyImmediate(mCol);
        var mRend = markerPin.GetComponent<Renderer>();
        if (mRend) mRend.sharedMaterial = LoadMat("Light_Emissive_Warm");

        // Floating 3D Interaction Label
        AddWallText(beacon, "CluePromptText", "[E] " + label.ToUpper(), Vector3.up * 0.40f, Gold, 2.2f);
    }

    static void AddDoorReveal(GameObject root, GameObject door)
    {
        Vector3 c = door.transform.position;
        Material frameMat = LoadMat("Trim_Black");

        float doorW = 2.5f;
        float doorH = 3.2f;

        // Door Jambs on sides ONLY (completely clear center passage)
        AddCube(root, "DoorJamb_L", c + new Vector3(-doorW*0.5f - 0.2f, 0, 0), new Vector3(0.18f, doorH, 0.20f), frameMat);
        AddCube(root, "DoorJamb_R", c + new Vector3( doorW*0.5f + 0.2f, 0, 0), new Vector3(0.18f, doorH, 0.20f), frameMat);
        AddCube(root, "DoorJamb_T", c + new Vector3(0, doorH*0.5f + 0.15f, 0),  new Vector3(doorW + 0.5f, 0.18f, 0.20f), frameMat);
        AddWallText(root, "ExitHeader", "SECURE EXIT", c + new Vector3(0, doorH*0.5f + 0.40f, -0.1f), Gold, 2.4f);

        // Recessed 3D Illuminated Exit Corridor behind door
        AddDoorPassageBacking(root, c);
    }

    static void AddDoorPassageBacking(GameObject root, Vector3 doorPos)
    {
        Material wallDark = LoadMat("Wall_Charcoal");
        Material floorWood = LoadMat("Floor_DarkWood");

        float pw = 2.8f;
        float ph = 3.4f;
        float pd = 2.5f;
        Vector3 pc = doorPos + new Vector3(0, 0, pd * 0.5f + 0.1f);

        AddCube(root, "Passage_Floor", pc + new Vector3(0, -0.05f, 0), new Vector3(pw, 0.10f, pd), floorWood);
        AddCube(root, "Passage_WallL", pc + new Vector3(-pw*0.5f, ph*0.5f, 0), new Vector3(0.10f, ph, pd), wallDark);
        AddCube(root, "Passage_WallR", pc + new Vector3( pw*0.5f, ph*0.5f, 0), new Vector3(0.10f, ph, pd), wallDark);
        AddCube(root, "Passage_Ceil",  pc + new Vector3(0, ph, 0), new Vector3(pw, 0.10f, pd), wallDark);
        AddCube(root, "Passage_Back",  pc + new Vector3(0, ph*0.5f, pd*0.5f), new Vector3(pw, ph, 0.10f), wallDark);

        AddPointLight(root, "PassageGlow", pc + new Vector3(0, ph*0.75f, 0), new Color(0.2f, 0.9f, 0.4f), 4.0f, 6.0f);
        AddWallText(root, "PassageText", "NEXT LEVEL PASSAGE", pc + new Vector3(0, ph*0.60f, pd*0.48f), Gold, 2.8f);
    }

    // ═══════════════════════════════════════════════════════════════════════
    //  UI STYLING & SELF-HEALING BUTTON WIRING
    // ═══════════════════════════════════════════════════════════════════════
    static void PolishUI(Scene scene)
    {
        foreach (TMP_Text t in Object.FindObjectsByType<TMP_Text>(FindObjectsSortMode.None))
        {
            if (!t) continue;
            string tn = t.name.ToLowerInvariant();
            t.enableWordWrapping = true;
            t.extraPadding = true;

            if (tn.Contains("title"))
            {
                t.color = Gold;
                t.fontSize = scene.name == "MainMenu" || scene.name == "GameComplete" ? 54f : 42f;
                t.fontStyle = FontStyles.Bold;
            }
            else if (tn.Contains("subtitle"))
            {
                t.color = WarmWhite;
                t.fontSize = 26f;
                t.fontStyle = FontStyles.Bold;
            }
            else if (tn.Contains("timer"))
            {
                t.color = new Color(0.85f, 0.93f, 1.0f);
                t.fontSize = 24f;
                t.fontStyle = FontStyles.Bold;
                if (!t.text.StartsWith("Time:", System.StringComparison.OrdinalIgnoreCase) && (t.text.Contains(":") || t.text.Contains(".")))
                    t.text = "Time: " + t.text.Replace("Time ", "").Trim();
            }
            else if (tn.Contains("attempt"))
            {
                t.color = new Color(1f, 0.72f, 0.35f);
                t.fontSize = 22f;
                t.fontStyle = FontStyles.Bold;
                if (!t.text.StartsWith("Attempts:", System.StringComparison.OrdinalIgnoreCase))
                {
                    bool noTrack = scene.name == "Level1_Investigation" || scene.name == "Level5_CaseFiles";
                    t.text = "Attempts: " + (noTrack ? "-" : "3");
                }
            }
            else if (tn.Contains("interaction") || tn.Contains("prompt"))
            {
                t.color = Color.white;
                t.fontSize = 24f;
                t.fontStyle = FontStyles.Bold;
                if (!t.text.Contains("[E]") && !t.text.Contains("Present"))
                    t.text = "[E] Press E to interact";
            }
            else if (tn.Contains("failed") || tn.Contains("error"))
            {
                t.color = new Color(1f, 0.32f, 0.30f);
                t.fontSize = 22f;
                t.fontStyle = FontStyles.Bold;
            }
            else
            {
                t.color = WarmWhite;
                if (t.fontSize < 16f) t.fontSize = 18f;
            }
        }

        foreach (Button b in Object.FindObjectsByType<Button>(FindObjectsSortMode.None))
        {
            Image img = b.GetComponent<Image>();
            string bn = b.name.ToLowerInvariant();
            var txt   = b.GetComponentInChildren<TMP_Text>();

            Color btnColor = BtnDark;
            if (bn.Contains("start") || bn.Contains("play"))
                btnColor = CrimsonRed;
            else if (bn.Contains("submit") || bn.Contains("login"))
                btnColor = AzureBlue;
            else if ((bn.Contains("quit") || bn.Contains("exit")) && (scene.name == "MainMenu" || scene.name == "GameComplete"))
                btnColor = CrimsonRed;
            else if (bn == "c" || bn.Contains("cancel") || bn.Contains("clear"))
                btnColor = new Color(0.72f, 0.12f, 0.12f, 0.98f);

            if (img) img.color = btnColor;
            ColorBlock cb = b.colors;
            cb.normalColor = Color.white;
            cb.highlightedColor = new Color(0.78f, 0.93f, 1.0f);
            cb.pressedColor     = new Color(0.60f, 0.80f, 0.92f);
            cb.selectedColor    = cb.highlightedColor;
            b.colors = cb;

            if (txt)
            {
                txt.color = Color.white;
                txt.fontSize = 20f;
                txt.fontStyle = FontStyles.Bold;
                txt.enableAutoSizing = false;
            }
        }

        foreach (Image img in Object.FindObjectsByType<Image>(FindObjectsSortMode.None))
        {
            if (!img || img.GetComponent<Button>()) continue;
            string n = img.name.ToLowerInvariant();
            if (n.Contains("panel") && img.sprite == null)
                img.color = PanelDark;
        }

        WireSceneButtons(scene);
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
                    if (bn.Contains("start") || bn.Contains("play"))
                    {
                        b.onClick.RemoveAllListeners();
                        b.onClick.AddListener(menuMgr.StartGame);
                    }
                    else if (bn.Contains("instruction"))
                    {
                        b.onClick.RemoveAllListeners();
                        b.onClick.AddListener(menuMgr.OpenInstructions);
                    }
                    else if (bn.Contains("close") || bn.Contains("back"))
                    {
                        b.onClick.RemoveAllListeners();
                        b.onClick.AddListener(menuMgr.CloseInstructions);
                    }
                    else if (bn.Contains("quit") || bn.Contains("exit"))
                    {
                        b.onClick.RemoveAllListeners();
                        b.onClick.AddListener(menuMgr.QuitGame);
                    }
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
                    if (bn.Contains("menu"))
                    {
                        b.onClick.RemoveAllListeners();
                        b.onClick.AddListener(compMgr.MainMenu);
                    }
                    else if (bn.Contains("quit") || bn.Contains("exit"))
                    {
                        b.onClick.RemoveAllListeners();
                        b.onClick.AddListener(compMgr.QuitGame);
                    }
                }
            }
        }
    }

    static void StyleMainMenuUI()
    {
        var title = Object.FindObjectsByType<TMP_Text>(FindObjectsSortMode.None)
            .FirstOrDefault(t => t.name.ToLowerInvariant().Contains("title"));
        if (title) { title.text = "CIPHER COURT"; title.color = Gold; title.fontSize = 56f; title.fontStyle = FontStyles.Bold; }

        foreach (Button b in Object.FindObjectsByType<Button>(FindObjectsSortMode.None))
        {
            string bn = b.name.ToLowerInvariant();
            var img   = b.GetComponent<Image>();
            var txt   = b.GetComponentInChildren<TMP_Text>();
            if (bn.Contains("start") || bn.Contains("play"))
            {
                if (img) img.color = CrimsonRed;
                if (txt) { txt.text = "START GAME"; txt.color = Color.white; txt.fontSize = 22f; txt.fontStyle = FontStyles.Bold; }
            }
            else if (bn.Contains("instruction"))
            {
                if (img) img.color = BtnDark;
                if (txt) { txt.text = "INSTRUCTIONS"; txt.color = WarmWhite; txt.fontSize = 20f; }
            }
            else if (bn.Contains("quit") || bn.Contains("exit"))
            {
                if (img) img.color = BtnDark;
                if (txt) { txt.text = "QUIT"; txt.color = WarmWhite; txt.fontSize = 20f; }
            }
        }
    }

    static void StyleGameCompleteUI()
    {
        foreach (Button b in Object.FindObjectsByType<Button>(FindObjectsSortMode.None))
        {
            string bn = b.name.ToLowerInvariant();
            var img   = b.GetComponent<Image>();
            var txt   = b.GetComponentInChildren<TMP_Text>();
            if (bn.Contains("menu"))
            {
                if (img) img.color = BtnDark;
                if (txt) { txt.text = "MAIN MENU"; txt.color = WarmWhite; txt.fontSize = 20f; }
            }
            else if (bn.Contains("quit") || bn.Contains("exit"))
            {
                if (img) img.color = CrimsonRed;
                if (txt) { txt.text = "QUIT"; txt.color = Color.white; txt.fontSize = 22f; txt.fontStyle = FontStyles.Bold; }
            }
        }
    }

    // ═══════════════════════════════════════════════════════════════════════
    //  PROPS & BUILDERS
    // ═══════════════════════════════════════════════════════════════════════
    static void BuildWorkstation(GameObject root, string name, Vector3 origin, bool facing)
    {
        Material wood = LoadMat("Wood_Walnut");
        Material mon  = LoadMat("Screen_Cyan");
        Material blk  = LoadMat("Trim_Black");

        GameObject ws = new GameObject(name);
        ws.transform.SetParent(root.transform);

        AddPhysicalCube(ws,"Desk",   origin+new Vector3(0,0.80f,0), new Vector3(2.5f,0.10f,1.2f), wood);
        AddPhysicalCube(ws,"DeskFrnt",origin+new Vector3(0,0.40f,facing?-0.55f:0.55f), new Vector3(2.5f,0.80f,0.08f), wood);
        AddCube(ws,"Monitor1",origin+new Vector3(-0.6f,1.4f,-0.1f),new Vector3(1.1f,0.70f,0.06f),mon);
        AddCube(ws,"Monitor2",origin+new Vector3( 0.6f,1.4f,-0.1f),new Vector3(1.1f,0.70f,0.06f),mon);
        AddCube(ws,"Keyboard",origin+new Vector3(0,0.87f,0.28f),new Vector3(0.80f,0.04f,0.25f),blk);
        AddPointLight(ws,"MonGlow",origin+new Vector3(0,1.4f,-0.5f),Cyan,1.5f,4f);
        AddChair(ws,"Chair",origin+new Vector3(0,0f,1.2f),Quaternion.identity);
    }

    static void BuildMetalShelf(GameObject root, string name, Vector3 origin)
    {
        Material metal = LoadMat("Metal_Dark");
        Material box   = LoadMat("Archive_Box");
        Material paper = LoadMat("Paper_Warm");

        GameObject shelf = new GameObject(name);
        shelf.transform.SetParent(root.transform);

        AddPhysicalCube(shelf,"Post_F",origin+new Vector3(0,2.2f,-0.9f),new Vector3(0.08f,4.4f,0.08f),metal);
        AddPhysicalCube(shelf,"Post_B",origin+new Vector3(0,2.2f, 0.9f),new Vector3(0.08f,4.4f,0.08f),metal);
        AddPhysicalCube(shelf,"Post_L",origin+new Vector3(-0.9f,2.2f,0),new Vector3(0.08f,4.4f,0.08f),metal);
        AddPhysicalCube(shelf,"Post_R",origin+new Vector3( 0.9f,2.2f,0),new Vector3(0.08f,4.4f,0.08f),metal);

        for (int y = 0; y < 5; y++)
        {
            float yy = 0.22f + y*0.82f;
            AddPhysicalCube(shelf,"Board_"+y,origin+new Vector3(0,yy,0),new Vector3(1.8f,0.05f,1.8f),LoadMat("Wood_Walnut"));
            AddCube(shelf,"Box_"+y, origin+new Vector3(-0.35f,yy+0.25f,0), new Vector3(0.55f,0.42f,0.55f),box);
            AddCube(shelf,"File_"+y,origin+new Vector3( 0.4f, yy+0.20f,0), new Vector3(0.45f,0.35f,0.18f),paper);
        }
    }

    static void BuildTallArchiveShelf(GameObject root, string name, Vector3 origin,
                                       Material metal, Material boxMat, Material wood)
    {
        GameObject shelf = new GameObject(name);
        shelf.transform.SetParent(root.transform);

        AddPhysicalCube(shelf,"Panel_L",origin+new Vector3(-0.55f,2.3f,0),new Vector3(0.06f,4.6f,1.4f),metal);
        AddPhysicalCube(shelf,"Panel_R",origin+new Vector3( 0.55f,2.3f,0),new Vector3(0.06f,4.6f,1.4f),metal);
        AddPhysicalCube(shelf,"Back",origin+new Vector3(0,2.3f,0.7f),new Vector3(1.1f,4.6f,0.06f),metal);

        for (int y = 0; y < 6; y++)
        {
            float yy = 0.18f + y*0.72f;
            AddPhysicalCube(shelf,"Shelf_"+y,origin+new Vector3(0,yy,0),new Vector3(1.0f,0.05f,1.4f),wood);
            AddCube(shelf,"BoxA_"+y,origin+new Vector3(-0.18f,yy+0.22f,0.05f),new Vector3(0.44f,0.38f,0.55f),boxMat);
            AddCube(shelf,"BoxB_"+y,origin+new Vector3( 0.22f,yy+0.20f,-0.05f),new Vector3(0.38f,0.32f,0.48f),LoadMat("Paper_Warm"));
        }
    }

    static void AddPlant(GameObject root, string name, Vector3 origin, Material plantMat, Material potMat)
    {
        GameObject plant = new GameObject(name);
        plant.transform.SetParent(root.transform);

        AddCylinder(plant,"Pot",    origin+new Vector3(0,0.25f,0),new Vector3(0.45f,0.50f,0.45f),potMat);
        AddCylinder(plant,"Soil",   origin+new Vector3(0,0.52f,0),new Vector3(0.42f,0.06f,0.42f),LoadMat("Trim_Black"));
        AddCylinder(plant,"Trunk",  origin+new Vector3(0,0.85f,0),new Vector3(0.08f,0.75f,0.08f),LoadMat("Wood_Dark"));
        AddSphere(plant,"Foliage_A",origin+new Vector3(0, 1.45f,0),  new Vector3(0.70f,0.70f,0.70f),plantMat);
        AddSphere(plant,"Foliage_B",origin+new Vector3(0.25f,1.60f,0.15f),new Vector3(0.55f,0.60f,0.55f),plantMat);
        AddSphere(plant,"Foliage_C",origin+new Vector3(-0.2f,1.55f,-0.1f),new Vector3(0.52f,0.58f,0.52f),plantMat);
    }

    static void AddChair(GameObject root, string name, Vector3 origin, Quaternion rot)
    {
        Material leather = LoadMat("Leather_Dark");
        Material blk     = LoadMat("Trim_Black");

        GameObject chair = new GameObject(name);
        chair.transform.SetParent(root.transform);
        chair.transform.rotation = rot;

        AddPhysicalCube(chair,"Seat",   origin+new Vector3(0,0.48f,0),  new Vector3(0.58f,0.10f,0.55f),leather);
        AddPhysicalCube(chair,"Back",   origin+new Vector3(0,0.82f,0.26f),new Vector3(0.58f,0.72f,0.10f),leather);
        AddCube(chair,"Leg_FL", origin+new Vector3(-0.22f,0.23f,-0.22f),new Vector3(0.06f,0.46f,0.06f),blk);
        AddCube(chair,"Leg_FR", origin+new Vector3( 0.22f,0.23f,-0.22f),new Vector3(0.06f,0.46f,0.06f),blk);
        AddCube(chair,"Leg_BL", origin+new Vector3(-0.22f,0.23f, 0.22f),new Vector3(0.06f,0.46f,0.06f),blk);
        AddCube(chair,"Leg_BR", origin+new Vector3( 0.22f,0.23f, 0.22f),new Vector3(0.06f,0.46f,0.06f),blk);
    }

    static void AddEvidenceMarker(GameObject root, string name, Vector3 pos, string number)
    {
        Material yellow = LoadMat("Marker_Yellow");
        Material blk    = LoadMat("Trim_Black");

        GameObject marker = new GameObject(name);
        marker.transform.SetParent(root.transform);

        AddCube(marker,"Card_A",pos,                   new Vector3(0.18f,0.22f,0.04f),yellow);
        AddCube(marker,"Card_B",pos+new Vector3(0.05f,0,0.08f),new Vector3(0.04f,0.22f,0.18f),yellow);
        AddWallText(marker,"Num",number,pos+new Vector3(0,0,-0.05f),blk.color,1.2f);
    }

    static void AddWallPicture(GameObject root, string name, Vector3 pos, Vector3 size, Material pictureMat, string title, Color titleColor)
    {
        Material frameMat = LoadMat("Frame_Dark");
        Material borderGold = LoadMat("Accent_Gold");

        GameObject picGroup = new GameObject("WallPic_" + name);
        picGroup.transform.SetParent(root.transform);

        AddCube(picGroup, "Frame", pos, size, frameMat);
        AddCube(picGroup, "Border", pos + new Vector3(0, 0, -0.01f), new Vector3(size.x * 0.94f, size.y * 0.94f, size.z * 0.8f), borderGold);
        AddCube(picGroup, "Canvas", pos + new Vector3(0, 0, -0.02f), new Vector3(size.x * 0.86f, size.y * 0.86f, size.z * 0.5f), pictureMat);

        Vector3 lightOffset = pos.x < -4f ? new Vector3(0.8f, 0.4f, 0) : (pos.x > 4f ? new Vector3(-0.8f, 0.4f, 0) : new Vector3(0, 0.4f, -0.8f));
        AddPointLight(picGroup, "PicSpot", pos + lightOffset, new Color(1f, 0.92f, 0.75f), 1.8f, 4f);

        if (!string.IsNullOrEmpty(title))
        {
            AddWallText(picGroup, "Title", title, pos + new Vector3(0, -size.y * 0.42f, -0.04f), titleColor, size.y * 1.4f);
        }
    }

    static void BuildScalesOfJustice(GameObject root, Vector3 origin, float scale)
    {
        Material gold = LoadMat("Metal_Gold");
        Material blk  = LoadMat("Trim_Black");
        float s = scale;

        AddCube(root,"Scales_Ped",  origin+new Vector3(0,0.35f*s,0),new Vector3(0.25f*s,0.70f*s,0.25f*s),blk);
        AddCube(root,"Scales_PedB", origin+new Vector3(0,0.02f*s,0),new Vector3(0.55f*s,0.04f*s,0.55f*s),gold);
        AddCylinder(root,"Scales_Pillar",origin+new Vector3(0,0.9f*s,0),new Vector3(0.07f*s,0.9f*s*2,0.07f*s),gold);
        AddCube(root,"Scales_Bar",origin+new Vector3(0,1.88f*s,0),new Vector3(1.80f*s,0.06f*s,0.06f*s),gold);
        AddCube(root,"Scales_ChainL",origin+new Vector3(-0.85f*s,1.55f*s,0),new Vector3(0.04f*s,0.72f*s,0.04f*s),gold);
        AddCube(root,"Scales_ChainR",origin+new Vector3( 0.85f*s,1.55f*s,0),new Vector3(0.04f*s,0.72f*s,0.04f*s),gold);
        AddCylinder(root,"Scales_PanL",origin+new Vector3(-0.85f*s,1.16f*s,0),new Vector3(0.52f*s,0.04f*s,0.52f*s),gold);
        AddCylinder(root,"Scales_PanR",origin+new Vector3( 0.85f*s,1.16f*s,0),new Vector3(0.52f*s,0.04f*s,0.52f*s),gold);
        AddPointLight(root,"ScalesGlow",origin+new Vector3(0,1.5f*s,0),Gold,2.0f*s,6f*s);
    }

    static void BuildGavel(GameObject root, Vector3 origin)
    {
        Material wood = LoadMat("Wood_Dark");

        AddCube(root,"Gavel_Block",origin+new Vector3(0,0.85f,0),new Vector3(0.55f,0.32f,0.22f),wood);
        AddCube(root,"Gavel_Handle",origin+new Vector3(0.6f,0.72f,0),new Vector3(1.40f,0.10f,0.10f),wood);
        AddCube(root,"Gavel_SoundBlock",origin+new Vector3(0,0.55f,0),new Vector3(0.70f,0.08f,0.55f),LoadMat("Wood_Walnut"));
        AddPointLight(root,"GavelGlow",origin+new Vector3(0,1.5f,0),Gold,1.5f,4f);
    }

    static void BuildIndianFlag(GameObject root, string name, Vector3 origin)
    {
        Material saffron = LoadMat("Flag_Orange");
        Material white   = LoadMat("White_Mat");
        Material green   = LoadMat("Flag_Green");
        Material pole    = LoadMat("Metal_Gold");
        Material wheel   = LoadMat("Flag_Blue");

        GameObject flag = new GameObject(name);
        flag.transform.SetParent(root.transform);

        AddCylinder(flag,"Pole",origin-new Vector3(0,0.8f,0),new Vector3(0.04f,1.80f,0.04f),pole);
        Vector3 fp = origin+new Vector3(0.6f,0f,0);
        AddCube(flag,"Saffron",fp+new Vector3(0, 0.25f,0), new Vector3(1.2f,0.28f,0.04f),saffron);
        AddCube(flag,"White",  fp+new Vector3(0, 0.00f,0), new Vector3(1.2f,0.28f,0.04f),white);
        AddCube(flag,"Green",  fp+new Vector3(0,-0.25f,0), new Vector3(1.2f,0.28f,0.04f),green);
        AddCylinder(flag,"Wheel",fp+new Vector3(0,0.00f,-0.025f),new Vector3(0.22f,0.22f,0.02f),wheel);
    }

    // ═══════════════════════════════════════════════════════════════════════
    //  MATERIAL SYSTEM
    // ═══════════════════════════════════════════════════════════════════════
    static void BuildMaterials()
    {
        CreateMat("Floor_DarkWood",    new Color(0.14f,0.08f,0.04f),  0.10f, 0.35f);
        CreateMat("Floor_Marble",      new Color(0.24f,0.22f,0.20f),  0.08f, 0.65f);
        CreateMat("Floor_CyberTile",   new Color(0.06f,0.08f,0.12f),  0.12f, 0.75f);
        CreateMat("Floor_Concrete",    new Color(0.18f,0.16f,0.14f),  0.20f, 0.30f);
        CreateMat("Ceiling_Dark",      new Color(0.04f,0.04f,0.05f),  0.80f, 0.05f);
        CreateMat("Ceiling_Mid",       new Color(0.12f,0.12f,0.12f),  0.50f, 0.10f);
        CreateMat("Ceiling_Court",     new Color(0.10f,0.08f,0.07f),  0.40f, 0.12f);

        CreateMat("Wall_Charcoal",     new Color(0.13f,0.14f,0.16f),  0.65f, 0.08f);
        CreateMat("Wall_LightGrey",    new Color(0.45f,0.44f,0.42f),  0.55f, 0.12f);
        CreateMat("Wall_Archive",      new Color(0.18f,0.14f,0.10f),  0.70f, 0.05f);
        CreateMat("Wall_WoodPanel",    new Color(0.18f,0.10f,0.05f),  0.25f, 0.35f);
        CreateMat("Wall_CourtWood",    new Color(0.20f,0.13f,0.07f),  0.20f, 0.40f);
        CreateMat("Wall_MenuDark",     new Color(0.08f,0.07f,0.09f),  0.55f, 0.10f);
        CreateMat("Wall_CyberDark",    new Color(0.05f,0.06f,0.10f),  0.45f, 0.15f);

        CreateMat("Wood_Walnut",       new Color(0.28f,0.14f,0.06f),  0.12f, 0.45f);
        CreateMat("Wood_Dark",         new Color(0.14f,0.07f,0.03f),  0.10f, 0.50f);
        CreateMat("WoodSlat_Light",    new Color(0.30f,0.18f,0.09f),  0.15f, 0.40f);
        CreateMat("WoodSlat_Dark",     new Color(0.16f,0.08f,0.04f),  0.10f, 0.45f);

        CreateMat("Metal_Dark",        new Color(0.18f,0.20f,0.22f),  0.05f, 0.85f);
        CreateMat("Metal_Gold",        new Color(0.80f,0.58f,0.15f),  0.08f, 0.90f);
        CreateMat("Trim_Black",        new Color(0.06f,0.06f,0.07f),  0.30f, 0.65f);
        CreateMat("Trim_Cyan",         new Color(0.05f,0.35f,0.50f),  0.15f, 0.80f);
        CreateMat("Accent_Gold",       new Color(0.80f,0.58f,0.15f),  0.10f, 0.88f);
        CreateMat("Frame_Dark",        new Color(0.08f,0.06f,0.05f),  0.25f, 0.60f);

        CreateEmissiveMat("Light_Emissive",      new Color(1.0f, 0.92f, 0.82f), 2.5f);
        CreateEmissiveMat("Light_Emissive_Warm", new Color(1.0f, 0.78f, 0.50f), 3.0f);
        CreateEmissiveMat("Light_Emissive_Blue", new Color(0.40f,0.75f,1.00f),  3.5f);

        CreateMat("Screen_Cyan",       new Color(0.05f,0.45f,0.75f),  0.10f, 0.90f);
        CreateMat("Server_Dark",       new Color(0.08f,0.10f,0.12f),  0.10f, 0.75f);
        CreateMat("Cork_Board",        new Color(0.55f,0.40f,0.22f),  0.90f, 0.05f);
        CreateMat("Paper_Warm",        new Color(0.88f,0.84f,0.72f),  0.95f, 0.02f);
        CreateMat("Evidence_Red",      new Color(0.72f,0.10f,0.10f),  0.25f, 0.15f);
        CreateMat("Archive_Box",       new Color(0.55f,0.38f,0.20f),  0.80f, 0.05f);
        CreateMat("Marker_Yellow",     new Color(0.92f,0.82f,0.10f),  0.30f, 0.12f);
        CreateMat("Leather_Dark",      new Color(0.14f,0.08f,0.05f),  0.55f, 0.15f);
        CreateMat("Plant_Green",       new Color(0.12f,0.38f,0.12f),  0.90f, 0.05f);
        CreateMat("Pot_Terracotta",    new Color(0.58f,0.28f,0.14f),  0.70f, 0.08f);
        CreateMat("Rug_Dark",          new Color(0.18f,0.10f,0.18f),  0.95f, 0.02f);
        CreateMat("Folder_Red",        new Color(0.58f,0.10f,0.10f),  0.55f, 0.08f);
        CreateMat("Marble_Dark",       new Color(0.20f,0.18f,0.16f),  0.08f, 0.70f);
        CreateMat("White_Mat",         new Color(0.92f,0.92f,0.92f),  0.80f, 0.10f);

        CreateMat("Flag_Orange",       new Color(1.0f, 0.40f, 0.00f), 0.70f, 0.05f);
        CreateMat("Flag_Green",        new Color(0.05f,0.52f,0.15f),  0.70f, 0.05f);
        CreateMat("Flag_Blue",         new Color(0.04f,0.14f,0.58f),  0.35f, 0.30f);

        CreateTexturedMat("Mat_BG_Level1", "Assets/CipherCourtPolish/Backgrounds/Level1_Investigation_Background.png");
        CreateTexturedMat("Mat_BG_Level2", "Assets/CipherCourtPolish/Backgrounds/Level2_Computer_Background.png");
        CreateTexturedMat("Mat_BG_Level3", "Assets/CipherCourtPolish/Backgrounds/Level3_Evidence_Background.png");
        CreateTexturedMat("Mat_BG_Level4", "Assets/CipherCourtPolish/Backgrounds/Level4_Archive_Background.png");
        CreateTexturedMat("Mat_BG_Level5", "Assets/CipherCourtPolish/Backgrounds/Level5_Statements_Background.png");
        CreateTexturedMat("Mat_BG_Level6", "Assets/CipherCourtPolish/Backgrounds/Level6_Courtroom_Background.png");
        CreateTexturedMat("Mat_BG_GameComplete", "Assets/CipherCourtPolish/Backgrounds/Complete_Legal_Cinematic.png");
        CreateTexturedMat("Mat_BG_MainMenu", "Assets/CipherCourtPolish/Backgrounds/Menu_Legal_Cinematic.png");
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
        if (m.HasProperty("_Smoothness")) m.SetFloat("_Smoothness", 0.9f);
        if (m.HasProperty("_Metallic"))   m.SetFloat("_Metallic",   0.0f);
        EditorUtility.SetDirty(m);
    }

    static void CreateTexturedMat(string name, string texturePath)
    {
        string path = $"{MatFolder}/{name}.mat";
        Material m = AssetDatabase.LoadAssetAtPath<Material>(path);
        if (!m)
        {
            Shader s = Shader.Find("Universal Render Pipeline/Unlit") ??
                       Shader.Find("Universal Render Pipeline/Lit") ??
                       Shader.Find("Unlit/Texture") ??
                       Shader.Find("Standard");
            m = new Material(s);
            AssetDatabase.CreateAsset(m, path);
        }

        Texture2D tex = AssetDatabase.LoadAssetAtPath<Texture2D>(texturePath);
        if (tex != null)
        {
            if (m.HasProperty("_BaseMap")) m.SetTexture("_BaseMap", tex);
            if (m.HasProperty("_MainTex")) m.SetTexture("_MainTex", tex);
        }
        if (m.HasProperty("_Color")) m.SetColor("_Color", Color.white);
        if (m.HasProperty("_BaseColor")) m.SetColor("_BaseColor", Color.white);
        EditorUtility.SetDirty(m);
    }

    // ═══════════════════════════════════════════════════════════════════════
    //  PRIMITIVE HELPERS & PHYSICAL COLLIDERS
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
        l.shadows = LightShadows.Soft;
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
        tmp.GetComponent<RectTransform>().sizeDelta = new Vector2(200, 40);
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
