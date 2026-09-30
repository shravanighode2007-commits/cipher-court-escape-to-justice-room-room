using UnityEngine;
using UnityEngine.SceneManagement;

public class FinalLevelExit : MonoBehaviour
{
    [Header("Completion Scene")]
    public string completionScene = "GameComplete";

    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player") ||
            other.transform.root.CompareTag("Player"))
        {
            Debug.Log("FINAL LEVEL COMPLETED!");

            SceneManager.LoadScene(completionScene);
        }
    }
}