using UnityEngine;
using UnityEngine.SceneManagement;

public class FinalLevelExit : MonoBehaviour
{
    [Header("Completion Scene")]
    public string completionScene = "GameComplete";

    private bool triggered = false;

    private void OnTriggerEnter(Collider other)
    {
        if (triggered) return;

        if (other.CompareTag("Player") || other.transform.root.CompareTag("Player"))
        {
            var puzzle = Object.FindFirstObjectByType<Level6VerdictPuzzle>();
            if (puzzle != null && !puzzle.IsSolved)
            {
                PopupFeedback.Show("COURT IS IN SESSION - DELIVER FINAL VERDICT FIRST!", false, 2.2f);
                return;
            }

            triggered = true;
            Debug.Log("[CipherCourt] FINAL LEVEL COMPLETED! Loading " + completionScene + "...");

            // Ensure cursor is free before transition
            Cursor.lockState = CursorLockMode.None;
            Cursor.visible = true;

            string targetScene = string.IsNullOrEmpty(completionScene) ? "GameComplete" : completionScene;
            SceneManager.LoadScene(targetScene);
        }
    }
}