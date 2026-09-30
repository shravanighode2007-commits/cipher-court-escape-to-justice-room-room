using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Text;
using TMPro;
using UnityEngine;
using UnityEngine.InputSystem;
using UnityEngine.Networking;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class CipherCourtDatabase : MonoBehaviour
{
    private static CipherCourtDatabase instance;

    [SerializeField] private string apiBaseUrl = "http://127.0.0.1:8000";

    [System.Serializable]
    public class GameEventRecord
    {
        public int id;
        public string session_id;
        public string scene;
        public string event_type;
        public string result;
        public string details;
        public string created_at;
    }

    [System.Serializable]
    public class DatabaseContainer
    {
        public List<GameEventRecord> records = new List<GameEventRecord>();
        public int totalCluesCollected = 0;
        public int totalPuzzlesSolved = 0;
    }

    private DatabaseContainer dbData = new DatabaseContainer();
    private string dbFilePath;

    // In-game UI Overlay
    private Canvas dbCanvas;
    private GameObject dbPanel;
    private TMP_Text dbLogText;
    private bool uiVisible = false;

    public static CipherCourtDatabase Instance
    {
        get
        {
            if (instance == null) Bootstrap();
            return instance;
        }
    }

    [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.AfterSceneLoad)]
    private static void Bootstrap()
    {
        if (instance != null) return;
        GameObject go = new GameObject("CipherCourtDatabaseSystem");
        instance = go.AddComponent<CipherCourtDatabase>();
        DontDestroyOnLoad(go);
        instance.InitDatabase();
        LogEvent("game_session", "started", "Cipher Court session started");
    }

    private void InitDatabase()
    {
        dbFilePath = Path.Combine(Application.persistentDataPath, "cipher_court_database.json");
        LoadLocalDatabase();
        BuildUI();
    }

    private void Update()
    {
        bool f1Pressed = false;
        try { if (Input.GetKeyDown(KeyCode.F1)) f1Pressed = true; } catch {}
        try { if (Keyboard.current != null && Keyboard.current.f1Key.wasPressedThisFrame) f1Pressed = true; } catch {}

        if (f1Pressed)
        {
            ToggleDatabaseUI();
        }
    }

    public static void LogEvent(string eventType, string result, string details = "")
    {
        if (instance == null) Bootstrap();
        if (instance == null) return;
        instance.RecordEvent(eventType, result, details);
    }

    private void RecordEvent(string eventType, string result, string details)
    {
        GameEventRecord rec = new GameEventRecord
        {
            id = dbData.records.Count + 1,
            session_id = SystemInfo.deviceUniqueIdentifier,
            scene = SceneManager.GetActiveScene().name,
            event_type = eventType,
            result = result,
            details = details,
            created_at = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
        };

        dbData.records.Add(rec);
        if (eventType == "clue_collected") dbData.totalCluesCollected++;
        if (eventType == "puzzle_answer" && result == "correct") dbData.totalPuzzlesSolved++;

        SaveLocalDatabase();
        RefreshUI();

        StartCoroutine(SendEventToBackend(rec));
    }

    private void SaveLocalDatabase()
    {
        try
        {
            string json = JsonUtility.ToJson(dbData, true);
            File.WriteAllText(dbFilePath, json);
        }
        catch (Exception ex)
        {
            Debug.LogWarning("Failed to save local database: " + ex.Message);
        }
    }

    private void LoadLocalDatabase()
    {
        try
        {
            if (File.Exists(dbFilePath))
            {
                string json = File.ReadAllText(dbFilePath);
                dbData = JsonUtility.FromJson<DatabaseContainer>(json);
                if (dbData == null) dbData = new DatabaseContainer();
            }
        }
        catch (Exception ex)
        {
            Debug.LogWarning("Failed to load local database: " + ex.Message);
            dbData = new DatabaseContainer();
        }
    }

    private IEnumerator SendEventToBackend(GameEventRecord rec)
    {
        string json = JsonUtility.ToJson(rec);
        using (UnityWebRequest req = new UnityWebRequest(apiBaseUrl.TrimEnd('/') + "/game-events", "POST"))
        {
            req.uploadHandler = new UploadHandlerRaw(Encoding.UTF8.GetBytes(json));
            req.downloadHandler = new DownloadHandlerBuffer();
            req.SetRequestHeader("Content-Type", "application/json");
            req.timeout = 2;
            yield return req.SendWebRequest();
        }
    }

    // ── In-Game Database Viewer UI (Press F1) ─────────────────────────
    private void BuildUI()
    {
        GameObject canvasGO = new GameObject("DatabaseViewerCanvas");
        canvasGO.transform.SetParent(transform, false);
        dbCanvas = canvasGO.AddComponent<Canvas>();
        dbCanvas.renderMode = RenderMode.ScreenSpaceOverlay;
        dbCanvas.sortingOrder = 9000;
        canvasGO.AddComponent<CanvasScaler>();
        canvasGO.AddComponent<GraphicRaycaster>();

        dbPanel = new GameObject("DatabasePanel");
        dbPanel.transform.SetParent(canvasGO.transform, false);
        Image img = dbPanel.AddComponent<Image>();
        img.color = new Color(0.04f, 0.06f, 0.10f, 0.96f);

        RectTransform pr = dbPanel.GetComponent<RectTransform>();
        pr.anchorMin = new Vector2(0.08f, 0.08f);
        pr.anchorMax = new Vector2(0.92f, 0.92f);
        pr.offsetMin = Vector2.zero;
        pr.offsetMax = Vector2.zero;

        // Title Header
        GameObject headerGO = new GameObject("HeaderTitle");
        headerGO.transform.SetParent(dbPanel.transform, false);
        TMP_Text headerText = headerGO.AddComponent<TextMeshProUGUI>();
        headerText.text = "CIPHER COURT // INTEGRATED DATABASE SYSTEM [F1]";
        headerText.fontSize = 24f;
        headerText.fontStyle = FontStyles.Bold;
        headerText.color = new Color(0.95f, 0.82f, 0.45f);
        headerText.alignment = TextAlignmentOptions.Center;
        RectTransform hr = headerText.rectTransform;
        hr.anchorMin = new Vector2(0f, 0.90f);
        hr.anchorMax = new Vector2(1f, 1f);
        hr.offsetMin = new Vector2(20, 0);
        hr.offsetMax = new Vector2(-20, -10);

        // Close Button
        GameObject closeBtnGO = new GameObject("CloseButton");
        closeBtnGO.transform.SetParent(dbPanel.transform, false);
        Image btnImg = closeBtnGO.AddComponent<Image>();
        btnImg.color = new Color(0.68f, 0.10f, 0.12f);
        Button closeBtn = closeBtnGO.AddComponent<Button>();
        closeBtn.onClick.AddListener(ToggleDatabaseUI);
        RectTransform br = closeBtnGO.GetComponent<RectTransform>();
        br.anchorMin = new Vector2(0.92f, 0.91f);
        br.anchorMax = new Vector2(0.98f, 0.98f);
        br.offsetMin = Vector2.zero;
        br.offsetMax = Vector2.zero;

        GameObject closeTxtGO = new GameObject("Text");
        closeTxtGO.transform.SetParent(closeBtnGO.transform, false);
        TMP_Text closeTxt = closeTxtGO.AddComponent<TextMeshProUGUI>();
        closeTxt.text = "X";
        closeTxt.fontSize = 20f;
        closeTxt.alignment = TextAlignmentOptions.Center;
        closeTxt.color = Color.white;
        RectTransform ctr = closeTxt.rectTransform;
        ctr.anchorMin = Vector2.zero;
        ctr.anchorMax = Vector2.one;

        // Scrollable Log Text Area
        GameObject scrollGO = new GameObject("LogText");
        scrollGO.transform.SetParent(dbPanel.transform, false);
        dbLogText = scrollGO.AddComponent<TextMeshProUGUI>();
        dbLogText.fontSize = 16f;
        dbLogText.color = new Color(0.90f, 0.92f, 0.95f);
        dbLogText.alignment = TextAlignmentOptions.TopLeft;
#pragma warning disable 0618
        dbLogText.enableWordWrapping = true;
#pragma warning restore 0618
        RectTransform lr = dbLogText.rectTransform;
        lr.anchorMin = new Vector2(0.04f, 0.04f);
        lr.anchorMax = new Vector2(0.96f, 0.88f);
        lr.offsetMin = Vector2.zero;
        lr.offsetMax = Vector2.zero;

        dbPanel.SetActive(false);
    }

    public void ToggleDatabaseUI()
    {
        uiVisible = !uiVisible;
        if (dbPanel != null)
        {
            dbPanel.SetActive(uiVisible);
            if (uiVisible) RefreshUI();
        }
    }

    private void RefreshUI()
    {
        if (dbLogText == null || dbData == null) return;

        StringBuilder sb = new StringBuilder();
        sb.AppendLine($"<color=#FFD700>TOTAL CLUES: {dbData.totalCluesCollected}  |  PUZZLES SOLVED: {dbData.totalPuzzlesSolved}  |  TOTAL EVENTS LOGGED: {dbData.records.Count}</color>");
        sb.AppendLine($"<color=#708090>Persistent Path: {dbFilePath}</color>\n");
        sb.AppendLine("<color=#00E5FF>#ID | TIME                | SCENE             | EVENT TYPE       | RESULT   | DETAILS</color>");
        sb.AppendLine("<color=#444444>-----------------------------------------------------------------------------------------</color>");

        int count = dbData.records.Count;
        int start = Mathf.Max(0, count - 15);
        for (int i = count - 1; i >= start; i--)
        {
            var r = dbData.records[i];
            string color = r.result == "correct" || r.result == "started" ? "#00FF7F" : (r.result == "incorrect" || r.result == "failed" ? "#FF4500" : "#E0E0E0");
            sb.AppendLine($"<color={color}>#{r.id:D3} | {r.created_at} | {r.scene,-17} | {r.event_type,-16} | {r.result,-8} | {r.details}</color>");
        }

        dbLogText.text = sb.ToString();
    }
}
