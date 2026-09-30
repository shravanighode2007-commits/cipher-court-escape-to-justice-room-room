using UnityEngine;
using UnityEngine.SceneManagement;

public class LevelExit : MonoBehaviour
{
    [SerializeField] private string nextScene;

    private void OnTriggerEnter(Collider other)
    {
        if (!other.CompareTag("Player") && !other.transform.root.CompareTag("Player"))
            return;

        if (!IsCurrentLevelSolved())
        {
            PopupFeedback.Show("DOOR LOCKED! SOLVE THE PUZZLE FIRST", false, 2.2f);
            return;
        }

        if (string.IsNullOrEmpty(nextScene))
        {
            Debug.LogWarning("Next Scene is not assigned.");
            return;
        }

        SceneManager.LoadScene(nextScene);
    }

    private bool IsCurrentLevelSolved()
    {
        string sceneName = SceneManager.GetActiveScene().name;

        if (sceneName == "Level1_Investigation")
        {
            var p = FindFirstObjectByType<CipherPuzzle>();
            return p != null && p.IsSolved;
        }
        else if (sceneName == "Level2_Computer")
        {
            var p = FindFirstObjectByType<PasswordPuzzle>();
            return p != null && p.IsSolved;
        }
        else if (sceneName == "Level3_Evidence")
        {
            var p = FindFirstObjectByType<EvidencePuzzle>();
            return p != null && p.IsSolved;
        }
        else if (sceneName == "Level4_Archive")
        {
            var p = FindFirstObjectByType<Level4ArchivePuzzle>();
            return p != null && p.IsSolved;
        }
        else if (sceneName == "Level5_CaseFiles")
        {
            var p = FindFirstObjectByType<Level5CasePuzzle>();
            return p != null && p.IsSolved;
        }
        else if (sceneName == "Level6_FinalVerdict")
        {
            var p = FindFirstObjectByType<Level6VerdictPuzzle>();
            return p != null && p.IsSolved;
        }

        return true;
    }
}