using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class GameCompleteManager : MonoBehaviour
{
    [SerializeField] private Button mainMenuButton;
    [SerializeField] private Button quitButton;

    private void Awake()
    {
        // Ensure cursor is completely free, unlocked, and visible for clicking UI buttons
        Cursor.lockState = CursorLockMode.None;
        Cursor.visible = true;
    }

    private void Start()
    {
        Cursor.lockState = CursorLockMode.None;
        Cursor.visible = true;

        // Auto-discover buttons if not assigned in Inspector
        Button[] allButtons = FindObjectsByType<Button>(FindObjectsSortMode.None);
        foreach (var b in allButtons)
        {
            string n = b.name.ToLowerInvariant();
            if (n.Contains("menu") || n.Contains("main"))
            {
                mainMenuButton = b;
            }
            else if (n.Contains("quit") || n.Contains("exit"))
            {
                quitButton = b;
            }
        }

        // Wire up MainMenu button
        if (mainMenuButton != null)
        {
            mainMenuButton.onClick.RemoveAllListeners();
            mainMenuButton.onClick.AddListener(MainMenu);
        }

        // Wire up Quit button
        if (quitButton != null)
        {
            quitButton.onClick.RemoveAllListeners();
            quitButton.onClick.AddListener(QuitGame);
        }

        // Ensure background image and static texts do NOT intercept button clicks
        foreach (var graphic in FindObjectsByType<Graphic>(FindObjectsSortMode.None))
        {
            if (graphic.GetComponent<Button>() == null && graphic.transform.parent?.GetComponent<Button>() == null)
            {
                graphic.raycastTarget = false;
            }
        }
    }

    private void Update()
    {
        // Maintain unlocked and visible cursor in GameComplete
        if (Cursor.lockState != CursorLockMode.None || !Cursor.visible)
        {
            Cursor.lockState = CursorLockMode.None;
            Cursor.visible = true;
        }
    }

    public void MainMenu()
    {
        Debug.Log("[CipherCourt] Main Menu Button clicked -> Loading MainMenu");
        SceneManager.LoadScene("MainMenu");
    }

    public void QuitGame()
    {
        Debug.Log("[CipherCourt] Quit Button clicked -> Navigating to Main Menu");
        SceneManager.LoadScene("MainMenu");
    }
}