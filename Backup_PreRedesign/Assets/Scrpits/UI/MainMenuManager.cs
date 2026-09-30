using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class MainMenuManager : MonoBehaviour
{
    [Header("Instructions")]
    public GameObject instructionsPanel;

    void Awake()
    {
        // Self-healing menu references so the Instructions Close button works even if an Inspector event was lost.
        if (instructionsPanel == null)
        {
            var all = Resources.FindObjectsOfTypeAll<GameObject>();
            foreach (var go in all)
                if (go.scene.IsValid() && go.name.ToLowerInvariant().Contains("instruction") && go.name.ToLowerInvariant().Contains("panel"))
                { instructionsPanel = go; break; }
        }

        foreach (var b in Resources.FindObjectsOfTypeAll<Button>())
        {
            if (!b.gameObject.scene.IsValid()) continue;
            string n = b.name.ToLowerInvariant();
            if (n.Contains("close") && b.transform.IsChildOf(instructionsPanel != null ? instructionsPanel.transform : transform))
            {
                b.onClick.RemoveListener(CloseInstructions);
                b.onClick.AddListener(CloseInstructions);
            }
        }
    }

    public void StartGame() => SceneManager.LoadScene("Level1_Investigation");
    public void OpenInstructions() { if (instructionsPanel != null) instructionsPanel.SetActive(true); }
    public void CloseInstructions() { if (instructionsPanel != null) instructionsPanel.SetActive(false); }
    public void QuitGame() { Debug.Log("Quit Game"); Application.Quit(); }
}
