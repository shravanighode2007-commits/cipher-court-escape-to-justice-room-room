using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class MainMenuManager : MonoBehaviour
{
    [Header("Instructions")]
    public GameObject instructionsPanel;

    private void Awake()
    {
        // Ensure cursor is free, unlocked, and visible in menus
        Cursor.lockState = CursorLockMode.None;
        Cursor.visible = true;
    }

    private void Start()
    {
        Cursor.lockState = CursorLockMode.None;
        Cursor.visible = true;

        // Auto-heal instructions panel reference if missing
        if (instructionsPanel == null)
        {
            var all = Resources.FindObjectsOfTypeAll<GameObject>();
            foreach (var go in all)
            {
                if (go.scene.IsValid() && go.name.ToLowerInvariant().Contains("instruction") && go.name.ToLowerInvariant().Contains("panel"))
                {
                    instructionsPanel = go;
                    break;
                }
            }
        }

        // Auto-wire all buttons
        foreach (var b in FindObjectsByType<Button>(FindObjectsSortMode.None))
        {
            string n = b.name.ToLowerInvariant();
            if (n.Contains("start") || n.Contains("play"))
            {
                b.onClick.RemoveAllListeners();
                b.onClick.AddListener(StartGame);
            }
            else if (n.Contains("instruction"))
            {
                b.onClick.RemoveAllListeners();
                b.onClick.AddListener(OpenInstructions);
            }
            else if (n.Contains("close") || n.Contains("back"))
            {
                b.onClick.RemoveAllListeners();
                b.onClick.AddListener(CloseInstructions);
            }
            else if (n.Contains("quit") || n.Contains("exit"))
            {
                b.onClick.RemoveAllListeners();
                b.onClick.AddListener(QuitGame);
            }
        }

        // Disable raycast target on non-button static graphics so they don't block button clicks
        foreach (var graphic in FindObjectsByType<Graphic>(FindObjectsSortMode.None))
        {
            if (graphic.GetComponent<Button>() == null && graphic.transform.parent?.GetComponent<Button>() == null)
            {
                if (instructionsPanel == null || (graphic.gameObject != instructionsPanel && !graphic.transform.IsChildOf(instructionsPanel.transform)))
                {
                    graphic.raycastTarget = false;
                }
            }
        }
    }

    private void Update()
    {
        if (Cursor.lockState != CursorLockMode.None || !Cursor.visible)
        {
            Cursor.lockState = CursorLockMode.None;
            Cursor.visible = true;
        }
    }

    public void StartGame()
    {
        Debug.Log("[CipherCourt] Start Game clicked -> Loading Level1_Investigation");
        SceneManager.LoadScene("Level1_Investigation");
    }

    public void OpenInstructions()
    {
        if (instructionsPanel != null) instructionsPanel.SetActive(true);
    }

    public void CloseInstructions()
    {
        if (instructionsPanel != null) instructionsPanel.SetActive(false);
    }

    public void QuitGame()
    {
        Debug.Log("[CipherCourt] Quit Game clicked");
#if UNITY_EDITOR
        UnityEditor.EditorApplication.isPlaying = false;
#else
        Application.Quit();
#endif
    }
}
